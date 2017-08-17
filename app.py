import os
from sanic import Sanic
from sanic.config import Config
from sanic.response import html, text
from sanic.exceptions import RequestTimeout

from jinja2 import PackageLoader
from sanic_jinja2 import SanicJinja2

from config import DATABASE, THEMES
from cms.models import db, User



app = Sanic(__name__)
app.config.update(DATABASE)
app.config.update(THEMES)

# static files serve
app.static('/static', './cms/static')

# Jinja2 template engine
template_package_loader = PackageLoader(app.name, 'cms/templates')
template = SanicJinja2(app, loader=template_package_loader)


# Add listeners
@app.listener('before_server_start')
async def setup_db(app, loop):
    # database create
    db_lock = 'db.lock'
    if not os.path.exists(db_lock):
        db.create_tables([User])
        open(db_lock, "w+").close()

# Add middleware


@app.exception(RequestTimeout)
def timeout(request, exception):
    if request is not None:
        print('ERROR HANDLE:\t', request, exception)
        return text('RequestTimeout from error_handler.', 408)
    return text('RequestTimeout from error_handler.', 408)


# Add views


async def index(request):
    """Index view"""
    return template.render('index.html', request, greetings='Welcome to Sanic-CMS')

# Add routes
app.add_route(index, '/')
app.add_route(index, '/index.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)
