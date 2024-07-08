from django import forms
from .models import Funcionariu
from .models import Visitor
from .models import DetailVisitor

class DateInput(forms.DateInput):
	input_type = 'date'

class FuncionariuForm(forms.ModelForm):
	class Meta:
		model = Funcionariu
		fields = ['naran','sexo','data_moris','hela_fatin','municipio','nu_kontaktu','email','diresaun','tipu_user']

class VisitorForm(forms.ModelForm):
	class Meta:
		model = Visitor
		fields = ['naran','seksu','husi_diresaun','hela_fatin','nu_kontaktu','email']

class DetailVisitorForm(forms.ModelForm):
	class Meta:
		model = DetailVisitor
		fields = '__all__'