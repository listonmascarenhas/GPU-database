import webapp2
import jinja2
import os
from google.appengine.ext import ndb

from gpufeatures import GpuFeatures

JINJA_ENVIRONMENT = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions = ['jinja2.ext.autoescape'],
    autoescape = True
)

class GpuCompare(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        all_gpu = GpuFeatures.query().fetch()
        gpu_same= ''
        gpu_same = self.request.get('gpu_same')

        template_values = {
        'all_gpu' : all_gpu,
        'gpu_same': gpu_same
        }
        template = JINJA_ENVIRONMENT.get_template('gpucompare.html')
        self.response.write(template.render(template_values))

    def post(self):
        self.response.headers['Content-Type'] = 'text/html'
        action = self.request.get('button')
        if action == 'Compare':
            gpu1 = self.request.get('gpu1')
            gpu2 = self.request.get('gpu2')
            if gpu1 == gpu2:
                self.redirect('/gpuCompare?gpu_same='+'yes')
            else:
                self.redirect('/gpuCompareResults?gpu1='+ gpu1 + '&gpu2=' +gpu2)
        elif action == 'Back':
            self.redirect('/')
