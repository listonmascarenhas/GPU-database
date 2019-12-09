import webapp2
import jinja2
import os
from google.appengine.ext import ndb
from gpufeatures import GpuFeatures

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions = ['jinja2.ext.autoescape'],
    autoescape = True
)

class GpuInformation(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        gpu_name = self.request.get('gpu_name')
        key = ndb.Key('GpuFeatures',gpu_name)
        gpu_key = key.get()

        template_values = {
        'gpu_key' : gpu_key,
        }
        template = JINJA_ENVIRONMENT.get_template('gpuinformation.html')
        self.response.write(template.render(template_values))

    def post(self):
        self.response.headers['Content-Type'] = 'text/html'
        action = self.request.get('button')

        if action == 'Edit':
            gpu_name = self.request.get('gpu_name')
            self.redirect('/addGpu?gpu_name='+gpu_name + '&gpu_edit=' + 'yes')
        elif action == 'Back':
            self.redirect('/')
