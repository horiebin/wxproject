import web

render = web.template.render('templates/')

class ReMoney:
    def GET(self):
        return render.remoney()