from django.db import models
from user.models import User
# Create your models here.
class Funcionariu(models.Model):
	SEXO = (
			('Mane', 'Mane'),
			('Feto', 'Feto'),
			)

	TIPU_USER = (
			('Funsionariu', 'Funsionariu'),
			('recepsionit', 'recepsionit'),
			)

	MUNICIPIO = (
			('Aileu', 'Aileu'),
			('Ainaru', 'Ainaru'),
			('Baucau', 'Baucau'),
			('Bobonaru', 'Bobonaru'),
			('Covalima', 'Covalima'),
			('Dili', 'Dili'),
			('Ermera', 'Ermera'),
			('Likisa', 'Likisa'),
			('Lautem', 'Lautem'),
			('Manatuto', 'Manatuto'),
			('Manufahi', 'Manufahi'),
			('Oecusse', 'Oecusse'),
			('Viqueque', 'Viqueque'),
			)

	naran = models.CharField(max_length=200,null=True)
	sexo = models.CharField(max_length=200,null=True,choices=SEXO)
	data_moris = models.DateField(auto_now=False,auto_now_add=False,null=True)
	hela_fatin = models.CharField(max_length=200,null=True)
	municipio = models.CharField(max_length=200,null=True,choices=MUNICIPIO)
	nu_kontaktu = models.CharField(max_length=200,null=True)
	email = models.EmailField(max_length=200,null=True)
	diresaun = models.CharField(max_length=200,null=True)
	tipu_user = models.CharField(max_length=200,null=True,choices=TIPU_USER)
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

	def __str__(self):
		return self.naran


class Visitor(models.Model):
	SEKSU = (
			('Mane', 'Mane'),
			('Feto', 'Feto'),
			)

	naran = models.CharField(max_length=200,null=True)
	seksu = models.CharField(max_length=200,null=True,choices=SEKSU)
	husi_diresaun = models.CharField(max_length=200,null=True)
	hela_fatin = models.CharField(max_length=200,null=True)
	nu_kontaktu = models.CharField(max_length=200,null=True)
	email = models.EmailField(max_length=200,null=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	

	def __str__(self):
		return self.naran	

class DetailVisitor(models.Model):
	naranvisitor = models.ForeignKey(Visitor,on_delete=models.CASCADE)
	hasorufuncionariu = models.ForeignKey(Funcionariu,on_delete=models.CASCADE)
	asuntu = models.CharField(max_length=200,null=True)
	data = models.DateField(null=True)
	orashahu = models.TimeField(auto_now_add=True)
	orastermina = models.TimeField(auto_now_add=False)
	fatinhasoru = models.CharField(max_length=200,null=True)
	
	def __str__(self):
		return self.asuntu	

		