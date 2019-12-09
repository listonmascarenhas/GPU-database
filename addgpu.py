import webapp2
from google.appengine.ext import ndb
import jinja2
import os
from gpufeatures import GpuFeatures
from datetime import datetime

JINJA_ENVIRONMENT = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions = ['jinja2.ext.autoescape'],
    autoescape = True
)

class AddGpu(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        gpu_name = self.request.get('gpu_name')
        gpu_edit = self.request.get('gpu_edit')
        gpu_key = ''
        if gpu_name != '':
            key = ndb.Key('GpuFeatures',gpu_name)
            gpu_key=key.get()

        template_values = {
        'gpu_key' : gpu_key,
        'gpu_edit' : gpu_edit,
            }
        template = JINJA_ENVIRONMENT.get_template('addgpu.html')
        self.response.write(template.render(template_values))

    def post(self):
        self.response.headers['Content-Type'] = 'text/html'
        action = self.request.get('button')
        gpu_edit = self.request.get('gpu_edit')
        gpu_name = self.request.get('gpu_name')

        if action == 'Update':

            gpu_manafacturer = self.request.get('gpu_manafacturer')
            gpu_date_issued = self.request.get('gpu_date_issued')
            gpu_date_issued = datetime.strptime(gpu_date_issued, '%Y-%m-%d')
            geometry_shader = bool(self.request.get('geometry_shader'))
            tesselation_shader = bool(self.request.get('tesselation_shader'))
            shader_int16 = bool(self.request.get('shader_int16'))
            sparse_binding=bool(self.request.get('sparse_binding'))
            texture_compression_etc2=bool(self.request.get('texture_compression_etc2'))
            vertex_pipeline_stores_and_atomics = bool(self.request.get('vertex_pipeline_stores_and_atomics'))

            key = ndb.Key('GpuFeatures',gpu_name)
            gpu_key = key.get()

            if gpu_key == None or gpu_edit == 'yes' :
                gpu_key = GpuFeatures(id=gpu_name,gpu_name=gpu_name, gpu_manafacturer=gpu_manafacturer,gpu_date_issued=gpu_date_issued,geometry_shader=geometry_shader,
                tesselation_shader=tesselation_shader,shader_int16=shader_int16,sparse_binding=sparse_binding,texture_compression_etc2=texture_compression_etc2,
                vertex_pipeline_stores_and_atomics=vertex_pipeline_stores_and_atomics)
                gpu_key.put()
            self.redirect('/')

        elif action =='Back':
            #if gpu_edit=='yes':
            #    self.redirect('/gpuInformation?gpu_name='+gpu_name)
            #else :
            self.redirect('/gpuInformation?gpu_name='+gpu_name)
