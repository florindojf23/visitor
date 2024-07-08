from import_export import resources
from .models import *


class FuncionariuRes(resources.ModelResource):
	class Meta:
		model = Funcionariu

class VisitorRes(resources.ModelResource):
	class Meta:
		model = Visitor

class DetVisitorRes(resources.ModelResource):
	class Meta:
		model = DetailVisitor