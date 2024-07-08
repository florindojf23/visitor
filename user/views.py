from django.shortcuts import render,redirect,HttpResponse
from django.template.loader import get_template
from .models import *
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def userlist(request):
	user = User.objects.all()
	context = {
		"userlist":user,
	}
	return render(request,"userlist.html",context)