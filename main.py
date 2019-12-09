import webapp2
import jinja2
import os
from google.appengine.ext import ndb
from google.appengine.api import users

from myuser import MyUser
from addgpu import AddGpu
from gpufeatures import GpuFeatures
from gpuinformation import GpuInformation
from gpuquery import GpuQuery
from gpucompare import GpuCompare
from gpucompareresults import GpuCompareResults

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape= True
)

#Liston Mascarenhas
#Msc.Bda
#2970414

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'

        url = ''
        url_string = ''
        all_gpu_names = ''
        user = users.get_current_user()

        if user:
            url = users.create_logout_url(self.request.uri)
            url_string = 'logout'

            myuser_key = ndb.Key('MyUser', user.user_id())
            myuser = myuser_key.get()

            if myuser == None:
                myuser = MyUser(id=user.user_id(),email_address=user.email())
                myuser.put()

        else :
            url = users.create_login_url(self.request.uri)
            url_string = 'login'



        all_gpu_names = GpuFeatures.query().fetch()
        template_values = {
            'url' : url,
            'url_string' : url_string,
            'all_gpu_names' : all_gpu_names,
            'user' : user,
        }

        template = JINJA_ENVIRONMENT.get_template('main.html')
        self.response.write(template.render(template_values))

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/addGpu', AddGpu),
    ('/gpuInformation',GpuInformation),
    ('/gpuQuery',GpuQuery),
    ('/gpuCompare',GpuCompare),
    ('/gpuCompareResults',GpuCompareResults),
], debug =True)
