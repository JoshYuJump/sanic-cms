from sanic import Sanic
from sanic.response import html
from jinja2 import PackageLoader
from sanic_jinja2 import SanicJinja2
from config import DATABASE, THEMES


app = Sanic(__name__)
app.config.update(DATABASE)
app.config.update(THEMES)

# static files serve
app.static('/static', './cms/static')

# Jinja2 template engine
template_package_loader = PackageLoader(app.name, 'cms/templates')
template = SanicJinja2(app, loader=template_package_loader)


@app.route("/")
async def index(request):
    """Index view"""
    return template.render('index.html', request, greetings='Welcome to Sanic-CMS')

app.run(host="0.0.0.0", port=8000, debug=True)