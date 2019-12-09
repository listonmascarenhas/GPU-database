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

class GpuQuery(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        def str_to_bool(s):
            if s== 'True':
                return True
            else :
                return False
        geometry_shader = self.request.get('gs')
        tesselation_shader = self.request.get('ts')
        shader_int16 = self.request.get('si16')
        sparse_binding=self.request.get('sb')
        texture_compression_etc2=self.request.get('tce2')
        vertex_pipeline_stores_and_atomics = self.request.get('vpsaa')
        search = self.request.get('search')
        query_gpu = ''
        query=''
        #queryList=[]
        if search == 'yes':
            query = GpuFeatures.query()
            if(geometry_shader=='True'):
                query = query.filter(GpuFeatures.geometry_shader == str_to_bool(geometry_shader))
        #        query1 = GpuFeatures.query(GpuFeatures.geometry_shader == str_to_bool(geometry_shader)).fetch()
        #        queryList.append(query1)
            if(tesselation_shader=='True'):
                query = query.filter(GpuFeatures.tesselation_shader == str_to_bool(tesselation_shader))
        #        query2 =GpuFeatures.query(GpuFeatures.tesselation_shader == str_to_bool(tesselation_shader)).fetch()
        #        queryList.append(query2)
            if(shader_int16=='True'):
                query = query.filter(GpuFeatures.shader_int16 == str_to_bool(shader_int16))
        #        query3 =GpuFeatures.query(GpuFeatures.shader_int16 == str_to_bool(shader_int16)).fetch()
        #        queryList.append(query3)
            if(sparse_binding=='True'):
                query =query.filter(GpuFeatures.sparse_binding == str_to_bool(sparse_binding))
        #        query4 =GpuFeatures.query(GpuFeatures.sparse_binding == str_to_bool(sparse_binding)).fetch()
        #        queryList.append(query4)
            if(texture_compression_etc2=='True'):
                query = query.filter(GpuFeatures.texture_compression_etc2 == str_to_bool(texture_compression_etc2))
        #        query5 =GpuFeatures.query(GpuFeatures.texture_compression_etc2 == str_to_bool(texture_compression_etc2)).fetch()
        #        queryList.append(query5)
            if(vertex_pipeline_stores_and_atomics=='True'):
                query = query.filter(GpuFeatures.vertex_pipeline_stores_and_atomics == str_to_bool(vertex_pipeline_stores_and_atomics))
        #        query6 =GpuFeatures.query(GpuFeatures.vertex_pipeline_stores_and_atomics == str_to_bool(vertex_pipeline_stores_and_atomics)).fetch()
        #        queryList.append(query6)
                query = query.fetch()
            #query_gpu = GpuFeatures.query(ndb.AND(GpuFeatures.geometry_shader == str_to_bool(geometry_shader),
            #                                GpuFeatures.tesselation_shader == str_to_bool(tesselation_shader),
            #                                GpuFeatures.shader_int16 == str_to_bool(shader_int16),
            #                                GpuFeatures.sparse_binding== str_to_bool(sparse_binding),
            #                                GpuFeatures.texture_compression_etc2== str_to_bool(texture_compression_etc2),
            #                                GpuFeatures.vertex_pipeline_stores_and_atomics== str_to_bool(vertex_pipeline_stores_and_atomics))).fetch()
            #query_gpu=queryList[0]
            #for query in queryList:
            #    query_gpu = query_gpu and query

        template_values = {
        'geometry_shader' : geometry_shader,
        'tesselation_shader' : tesselation_shader,
        'shader_int16' : shader_int16,
        'sparse_binding' : sparse_binding,
        'texture_compression_etc2' : texture_compression_etc2,
        'vertex_pipeline_stores_and_atomics' : vertex_pipeline_stores_and_atomics,
        'query_gpu' : query,

        }

        template = JINJA_ENVIRONMENT.get_template('gpuquery.html')
        self.response.write(template.render(template_values))


    def post(self):
        self.response.headers['Content-Type'] = 'text/plain'
        action = self.request.get('button')
        if action == 'Search':
            geometry_shader = self.request.get('geometry_shader') != ''
            tesselation_shader = self.request.get('tesselation_shader') != ''
            shader_int16 = self.request.get('shader_int16') != ''
            sparse_binding=self.request.get('sparse_binding') != ''
            texture_compression_etc2=self.request.get('texture_compression_etc2') != ''
            vertex_pipeline_stores_and_atomics = self.request.get('vertex_pipeline_stores_and_atomics') != ''
            self.redirect('/gpuQuery?gs='+str(geometry_shader)+'&ts='+str(tesselation_shader)+'&si16='
            +str(shader_int16)+'&sb='+str(sparse_binding)+'&tce2='+str(texture_compression_etc2)+'&vpsaa='
            +str(vertex_pipeline_stores_and_atomics)+'&search='+'yes')
        elif action== 'Back':
            self.redirect('/')
