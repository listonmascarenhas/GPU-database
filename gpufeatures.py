from google.appengine.ext import ndb


class GpuFeatures(ndb.Model):
    gpu_name = ndb.StringProperty()
    gpu_manafacturer = ndb.StringProperty()
    #gpu_date_issued = ndb.StringProperty()
    gpu_date_issued = ndb.DateProperty()
    geometry_shader = ndb.BooleanProperty()
    tesselation_shader = ndb.BooleanProperty()
    shader_int16 = ndb.BooleanProperty()
    sparse_binding = ndb.BooleanProperty()
    texture_compression_etc2 = ndb.BooleanProperty()
    vertex_pipeline_stores_and_atomics = ndb.BooleanProperty()
