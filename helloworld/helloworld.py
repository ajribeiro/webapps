import webapp2

form="""
<form method="post">
  What is your birthday?
  <br>

  <label>Month <input type="text" name="month" value="%(month)s"></label>

  <label>Day <input type="text" name="day" value="%(day)s"></label>

  <label>Year <input type="text" name="year" value="%(year)s"> </label>

  <div style="color: red">%(error)s</div>

  <br><br>
  <input type="submit">
</form>
"""


class MainPage(webapp2.RequestHandler):
  def writeForm(self,error="",month="",day="",year=""):
    self.response.out.write(form % {"error": escapeHtml(error),
                                    "month": escapeHtml(month),
                                    "day": escapeHtml(day),
                                    "year": escapeHtml(year)})

  def get(self):
    # self.response.headers['Content-Type'] = 'text/plain'
    self.writeForm()

  def post(self):

    userMonth = self.request.get('month')
    userDay = self.request.get('day')
    userYear = self.request.get('year')

    month = validMonth(userMonth)
    day = validDay(userDay)
    year = validYear(userYear)

    if not(month and day and year):
      self.writeForm("problem with you input",userMonth,userDay,userYear)
    else:
      self.redirect("/thanks")
      

def validMonth(month):
  if month.isdigit():
    month = int(month)
    if(0 < month < 13):
      return str(month)

def validDay(month):
  if month.isdigit():
    month = int(month)
    if(0 < month < 32):
      return str(month)

def validYear(month):
  if month.isdigit():
    month = int(month)
    if(1900 < month < 2020):
      return str(month)

def escapeHtml(s):
  import cgi
  return cgi.escape(s,quote=True)

class ThanksHandler(webapp2.RequestHandler):
  
  def get(self):
    self.response.out.write("Thanks, that's a totally valid day!")
    
app = webapp2.WSGIApplication([('/', MainPage),('/thanks', ThanksHandler)], debug=True)

