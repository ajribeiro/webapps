import webapp2

form="""
<form method="post">
  Enter some text to ROT13:
  <br>
  <textarea name="text">%(txt)s</textarea>
  <br>
  <input type="submit">
</form>
"""


class MainPage(webapp2.RequestHandler):

  def writeForm(self,t=""):

    self.response.out.write(form % {"txt": escapeHtml(t)})

  def get(self):
    self.writeForm()

  def post(self):
    userText = self.request.get('text')

    alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m', \
          'n','o','p','q','r','s','t','u','v','w','x','y','z']

    y=list(userText)

    for j in range(len(y)):
      l = y[j]
      if l.isalpha():
        i=alpha.index(l.lower())
        i= (i+13)%26
        

        if(l.islower()):
          y[j] = alpha[i]
        else:
          y[j] = alpha[i].upper()

    userText = "".join(y)

    # self.response.headers['Content-Type'] = 'text/plain'
    self.writeForm(t=userText)
      


def escapeHtml(s):
  import cgi
  return cgi.escape(s,quote=True)

    
app = webapp2.WSGIApplication([('/', MainPage)], debug=True)

