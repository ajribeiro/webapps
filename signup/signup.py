import webapp2
import jinja2, os


template_dir = os.path.join(os.path.dirname(__file__))
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)
    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)
    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))


class SignUp(Handler):
  def get(self):
    self.render_str('signup.html')


# class MainPage(webapp2.RequestHandler):
#   def write(self,s):
#     self.response.out.write(s)

#   def writeForm(self,user="",passw="",val="",email="",
#                 uerr="",perr="",verr="",eerr=""):
#     self.write(form % {"user": escapeHtml(user),"pass": escapeHtml(passw),
#                        "val": escapeHtml(val),"email": escapeHtml(email),
#                        "uerr": escapeHtml(uerr),"perr": escapeHtml(perr),
#                        "verr": escapeHtml(verr),"eerr": escapeHtml(eerr)})

#   def get(self):
#     # self.response.headers['Content-Type'] = 'text/plain'
#     self.writeForm()

#   def post(self):

#     user = self.request.get('username')
#     passw = self.request.get('password')
#     val = self.request.get('verify')
#     email = self.request.get('email')

#     u = validateUser(user)
#     p = validatePass(passw)

#     if(passw != val):
#       v = None
#     else:
#       v=1

#     if(email == ''): e = 1
#     else: e = validateEmail(email)

#     if(not u): uerr = 'problem with username'
#     else: uerr=""
#     if(not p): perr = 'problem with password'
#     else: perr=""
#     if(not v): verr = 'problem with verification'
#     else: verr=""
#     if(not e): eerr = 'problem with email'
#     else: eerr=""

#     if(u and v and e and p):
#       self.redirect("/welcome?username=%s" % user)
#     else:
#       self.writeForm(user=user,passw=passw,val=val,email=email,
#                 uerr=uerr,perr=perr,verr=verr,eerr=eerr)

      
      

# import re

# def validateUser(username):
#   return re.compile(r"^[a-zA-Z0-9_-]{3,20}$").match(username)

# def validatePass(username):
#   return re.compile(r"^.{3,20}$" ).match(username)

# def validateEmail(username):
#   return re.compile(r"^[\S]+@[\S]+\.[\S]+$" ).match(username)

# def escapeHtml(s):
#   import cgi
#   return cgi.escape(s,quote=True)

class ThanksHandler(webapp2.RequestHandler):
  def get(self):
    self.response.out.write("Welcome, %s!" % self.request.get('username'))
    
app = webapp2.WSGIApplication([('/signup', SignUp),('/welcome', ThanksHandler)], debug=True)

