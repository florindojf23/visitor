from django.contrib import admin
from .models import *

# Register your models here.
class FuncionariuList(admin.ModelAdmin):
	list_display = ('id','naran','sexo','data_moris','municipio','email','diresaun')

admin.site.register(Funcionariu,FuncionariuList)
admin.site.register(Visitor)
admin.site.register(DetailVisitor)
