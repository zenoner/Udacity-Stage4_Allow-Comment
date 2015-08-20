import webapp2

form="""
<form method="post" action="/testform">  #THE METHOD ATTRIBUTE 
	<input name="q">
	<input type="submit">
</form>

"""


class MainPage(webapp2.RequestHandler):
    def get(self):
        #self.response.headers['Content-Type'] = 'text/plain' 
        self.response.write(form)

class TestHandler(webapp2.RequestHandler):
	def post(self)
		q = self.request.get("q")
		self.response.out.write(q)

		#self.response.headers['Content-Type'] = 'text/plain' 
		#self.response.out.write(self.request)

app = webapp2.WSGIApplication([('/', MainPage),], debug=True)
