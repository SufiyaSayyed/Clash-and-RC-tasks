from django.shortcuts import render
from django.http import HttpResponse
from .models import Info

def get_info(request):
	
	return render(request, 'part1/add_info.html')

def add_info(request):
	if request.method == 'POST':
		info = Info()
		info.first_name = request.POST.get('first_name')
		info.last_name = request.POST.get('last_name')
		info.email = request.POST.get('email')
		info.phone_num = request.POST.get('phone_num')
		info.gender = request.POST.get('gender')
		info.save()

	return render(request, 'part1/add_info.html')

def index(request):
	info = Info.objects.all()
	return render(request, 'part1/index.html',{'users': info})

#def find_user(request):
#	info = Info()
#	if request.POST.get('email') == info.email:
#		return render(request, 'part1/result.html')
#	else:
#		return render(request, 'part1/result.html',context={result="sorry user not found"})

