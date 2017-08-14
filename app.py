from sanic import Sanic
from sanic.response import html
from config import DATABASE, THEMES


app = Sanic(__name__)
app.config.update(DATABASE)
app.config.update(THEMES)


@app.route("/")
async def index(request):
    return html('<html>'
                '   <body>'
                '       <h2>Welcome to Sanic-CMS!</h2><br>'
                '       settings:'
                '       <pre>'
                '           <span>DB_ENGINE: ' + app.config.DB_ENGINE + '</span><br>'
                '           <span>DB_NAME: ' + app.config.DB_NAME + '</span><br>'
                '       </pre>'
                '   </body>'
                '</html>')

app.run(host="0.0.0.0", port=8000, debug=True)