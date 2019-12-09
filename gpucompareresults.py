import webapp2
from google.appengine.ext import ndb
import jinja2
import os

JINJA_ENVIRONMENT = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions = ['jinja2.ext.autoescape'],
    autoescape = True
)

class GpuCompareResults(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        gpu1 = self.request.get('gpu1')
        gpu2 = self.request.get('gpu2')

        key = ndb.Key('GpuFeatures',gpu1)
        gpu1_key=key.get()

        key = ndb.Key('GpuFeatures',gpu2)
        gpu2_key=key.get()

        template_values = {
        'gpu1_key' : gpu1_key,
        'gpu2_key' : gpu2_key
        }

        template = JINJA_ENVIRONMENT.get_template('gpucompareresults.html')
        self.response.write(template.render(template_values))

    def post(self):
        self.response.headers['Content-Type'] = 'text/html'
        action = self.request.get('button')
        if action == 'Back':
            self.redirect('/gpuCompare')
