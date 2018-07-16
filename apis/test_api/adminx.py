import xadmin
from .models import TestApiModel

class TestApiAdmin(object):
   list_display=('id','name','numbers','time')
   list_editable=('name','numbers')


xadmin.site.register(TestApiModel,TestApiAdmin)
