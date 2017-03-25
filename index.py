import web

render = web.template.render('templates/')

class Index:
    def GET(self):
        name = 'Bob'
        return render.index(name)