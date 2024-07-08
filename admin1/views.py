from django.shortcuts import render,redirect,HttpResponse
from django.http import JsonResponse
#model lib
from .models import *
from .forms import FuncionariuForm,VisitorForm,DetailVisitorForm

#login lib
from django.contrib.auth.decorators import login_required
#chart or counting
from django.db.models import Count

#pdf lib
from io import BytesIO
from django.template.loader import get_template
from xhtml2pdf import pisa

#Resources csv lib
from .resources import FuncionariuRes,VisitorRes,DetVisitorRes

#LiveEdit csrf
from django.views.decorators.csrf import csrf_exempt
from user.models import User
# Create your views here.

@login_required
def home(request):
	data = {
	'title':"Varanda",
	'active_varanda':"active"
	}
	return render(request,'index.html',data)

@login_required
def funcionariu(request):
	listafuncionariu = Funcionariu.objects.all().order_by('id')
	data = {
	'title':"Lista Funcionariu",
	'dadus':listafuncionariu,
	'active_funsionariu':"active",
	}
	return render(request, 'funcionariu.html',data)

@login_required
def visitor(request):
	listavisitor = Visitor.objects.all()
	data = {
	'title':"Lista Visitor",
	'active_visitor':"active",
	'dadus':listavisitor
	}
	return render(request,'visitor.html',data)

@login_required
def detailvisitor(request):
	listadetailvisitor = DetailVisitor.objects.all()
	data = {
	'title':"Lista DetailVisitor",
	'dadus':listadetailvisitor
	}
	return render(request,'detailvisitor.html',data)

@login_required
def createFuncionariu(request):
	form = FuncionariuForm()

	if request.method == 'POST':
		form = FuncionariuForm(request.POST)
		if form.is_valid():
			instance = form.save(commit=False)
			user = User.objects.create(username=instance.email)
			user.set_password("password")
			if instance.tipu_user == "recepsionit":
				user.is_recepcionist = True
			else:
				user.is_funsionariu = True
			user.email = instance.email
			user.save()
			instance.user = user
			instance.save()
			return redirect('funcionariu')
	data = {
		'form':form,
		'title':"Formulariu Funcionariu",
	}
	return render(request, 'addfuncionariu.html',data)

@login_required
def createvisitor(request):
	form = VisitorForm()

	if request.method == 'POST':
		form = VisitorForm(request.POST)
		if form.is_valid():
			instance = form.save(commit=False)
			user = User.objects.create(username=instance.email)
			user.set_password("password")
			user.is_visitor = True
			user.email = instance.email
			user.save()
			instance.user = user
			instance.save()
			return redirect('visitor')
	data = {
		'form':form,
		'title':"Formulariu Visitor",
	}
	return render(request, 'addvisitor.html',data)

@login_required
def createdetvisitor(request):
	form = DetailVisitorForm()

	if request.method == 'POST':
		form = DetailVisitorForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('detailvisitor')
	data = {
		'form':form,
		'title':"Formulariu Detail Visitor",
	}
	return render(request, 'adddetailvisitor.html',data)

@login_required
def updateFuncionariu(request, id):
	funsionariu = Funcionariu.objects.get(id=id)
	form = FuncionariuForm(instance=funsionariu)

	if request.method == 'POST':
		form = FuncionariuForm(request.POST, instance=funsionariu)
		if form.is_valid():
			form.save()
			return redirect('funcionariu')
	data = {
		'form':form,
		'title':"Formulariu Update Funcionariu",
	}
	return render(request, 'addfuncionariu.html',data)

@login_required
def updatevisitor(request, id):
	visitor= Visitor.objects.get(id=id)
	form = VisitorForm(instance=visitor)

	if request.method == 'POST':
		form = VisitorForm(request.POST, instance=visitor)
		if form.is_valid():
			form.save()
			return redirect('visitor')
	data = {
		'form':form,
		'title':"Formulariu Update Visitor",
	}
	return render(request, 'addvisitor.html',data)

@login_required
def updatedetvisitor(request, id):
	detvisitor= DetailVisitor.objects.get(id=id)
	form = DetailVisitorForm(instance=detvisitor)

	if request.method == 'POST':
		form = DetailVisitorForm(request.POST, instance=detvisitor)
		if form.is_valid():
			form.save()
			return redirect('detailvisitor')
	data = {
		'form':form,
		'title':"Formulariu Update Detail Visitor",
	}
	return render(request, 'adddetailvisitor.html',data)

@login_required
def deleteFuncionariu(request,pk):
	funsionariu = Funcionariu.objects.get(id=pk)
	funsionariu.delete()
	return redirect('funcionariu')

@login_required
def deleteVisitor(request,pk):
	visitor = Visitor.objects.get(id=pk)
	visitor.delete()
	return redirect('visitor')

@login_required
def deletedetvisitor(request,id):
	detvisitor = DetailVisitor.objects.get(id=id)
	detvisitor.delete()
	return redirect('detailvisitor')

	#Pdf

@login_required
def pdf_funcionariu(request):
	funcionariu = Funcionariu.objects.all()
	data = {'dadus':funcionariu,
			'title':"PDF Docs"}
	pdf = render_to_pdf('pdf/pdf_funcionariu.html',data)
	return HttpResponse(pdf,content_type='application/pdf')

def render_to_pdf(template_src,context_dict={}):
	template = get_template(template_src)
	html = template.render(context_dict)
	result = BytesIO()
	pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")),result)
	if not pdf.err:
		return HttpResponse(result.getvalue(),content_type='application/pdf')
	return None

@login_required
def pdf_visitor(request):
	visitor = Visitor.objects.all()
	data = {'dadus':visitor,
			'title':"PDF Docs"}
	pdf = render_to_pdf('pdf/pdf_visitor.html',data)
	return HttpResponse(pdf,content_type='application/pdf')

def render_to_pdf(template_src,context_dict={}):
	template = get_template(template_src)
	html = template.render(context_dict)
	result = BytesIO()
	pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")),result)
	if not pdf.err:
		return HttpResponse(result.getvalue(),content_type='application/pdf')
	return None

@login_required
def pdf_det_visitor(request):
	detvisitor = DetailVisitor.objects.all()
	data = {'dadus':detvisitor,
			'title':"PDF Docs"}
	pdf = render_to_pdf('pdf/pdf_det_visitor.html',data)
	return HttpResponse(pdf,content_type='application/pdf')

def render_to_pdf(template_src,context_dict={}):
	template = get_template(template_src)
	html = template.render(context_dict)
	result = BytesIO()
	pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")),result)
	if not pdf.err:
		return HttpResponse(result.getvalue(),content_type='application/pdf')
	return None

@login_required
def csv_funcionariu(request):
	funcionariuRes = FuncionariuRes()
	dataset = funcionariuRes.export()
	response = HttpResponse(dataset.csv, content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename="funcionariu.csv"'
	return response

@login_required
def csv_visitor(request):
	visitorRes = VisitorRes()
	dataset = visitorRes.export()
	response = HttpResponse(dataset.csv, content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename="visitor.csv"'
	return response

@login_required
def csv_det_visitor(request):
	detvisitorRes = DetVisitorRes()
	dataset = detvisitorRes.export()
	response = HttpResponse(dataset.csv, content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename="Detail_visitor.csv"'
	return response

@login_required
def charts(request):
	data = {
	'title':"Charts"
	}
	return render(request,'charts.html',data)

@login_required
def chart_seksu_visitor(request):
	labels = []
	data = []
	queryset = Visitor.objects.values('seksu').annotate(total_seksu=Count('seksu'))
	for item in queryset:
		labels.append(item['seksu'])
		data.append(item['total_seksu'])
	return JsonResponse(data={
		'labels':labels,
		'data':data,
		})

@login_required
def chart_municipiu_funcionariu(request):
	labels = []
	data = []
	queryset = Funcionariu.objects.values('municipio').annotate(total_municipiu=Count('municipio'))
	for item in queryset:
		labels.append(item['municipio'])
		data.append(item['total_municipiu'])
	return JsonResponse(data={
		'labels':labels,
		'data':data,
		})

@login_required
@csrf_exempt
def liveFunSave(request):
	id = request.POST.get('id','')
	type = request.POST.get('type','')
	value =request.POST.get('value','')
	doc = Funcionariu.objects.get(id=id)

	if type == "naran":
		doc.naran=value
	if type == "sexo":
		doc.sexo=value
	if type == "data_moris":
		doc.data_moris=value
	if type == "hela_fatin":
		doc.hela_fatin=value
	if type == "municipio":
		doc.municipio=value
	if type == "nu_kontaktu":
		doc.nu_kontaktu=value
	if type == "email":
		doc.email=value
	if type == "diresaun":
		doc.diresaun=value

	doc.save()
	return JsonResponse({"success":"Updated"})

@login_required
def liveVisSave(request):
	id = request.POST.get('id','')
	type = request.POST.get('type','')
	value =request.POST.get('value','')
	doc = Funcionariu.objects.get(id=id)

	if type == "naran":
		doc.naran=value
	if type == "seksu":
		doc.seksu=value
	if type == "husi_diresaun":
		doc.husi_diresaun=value
	if type == "hela_fatin":
		doc.hela_fatin=value
	if type == "nu_kontaktu":
		doc.nu_kontaktu=value
	if type == "email":
		doc.email=value

	doc.save()
	return JsonResponse({"success":"Updated"})
