import os
from sanic import Sanic
from sanic.config import Config
from sanic.response import html, text
from sanic.exceptions import RequestTimeout

from jinja2 import PackageLoader
from sanic_jinja2 import SanicJinja2

from config import DATABASE, THEMES
from cms.models import db, User, create_tables

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
    # database table create
    create_tables()


@app.listener('before_server_start')
async def setup_static_files_serve(app, loop):
    '''support old website'''
    if os.path.isdir('/admin'):
        app.static('/admin', '/admin')
        print('support /admin sucessful')
    if os.path.isdir('/home'):
        app.static('/home', '/home')
        print('support /home sucessful')


# Add exception handler
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
