from django.shortcuts import render_to_response
from .models import Farmer, Schedulling,Farm
from datetime import datetime


def Todays_Dues(request):
	date_format = "%d/%m/%Y"
	a = datetime.strptime('Farm.objects.filter("sowing_date")', date_format)
	b = datetime.strptime('datetime.datetime.now()', date_format)
	delta = b - a
	today=[]
	for i in datedelta:
		if (i-(Schedulling.objects.filer(days_from_sowing)))==0:
		 	today+=i
	return render_to_response("today.html",{today:'today'})

def Tommorow_Dues(request):
	date_format = "%d/%m/%Y"
	a = datetime.strptime('Farm.objects.filter("sowing_date")', date_format)
	b = datetime.strptime('datetime.datetime.now()', date_format)
	delta = b - a
	tommorow=[]
	for i in datedelta:
		if (i-(Schedulling.objects.filer(days_from_sowing)))==1:
		 	tommorow+=i
	return render_to_response("today.html",{tommorow:'tommorow'})

def Farm(request):
	farmer=Farm.objects.filter('farmer')
	return render_to_response('Farm.html',{farmer:'farmer'})

def Cost(request):
	cost=Schedulling.objects.filter(fertilizer='offset')
	quantity=quantity.objects.all()
	total = 0
	for k in quantity:
    	total += k
	return render_to_response('prices.html',{cost:'total'})

