import xadmin
from .models import VerifyCode

class VerifyCodeAdmin(object):
   list_display=('email','code','add_time')

xadmin.site.register(VerifyCode,VerifyCodeAdmin)
