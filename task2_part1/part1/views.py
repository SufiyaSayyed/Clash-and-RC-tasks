from django.shortcuts import render, redirect
from part1.models import Info

def add(request):
	if request.method == 'POST':

		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		email = request.POST['email']
		phone_no = request.POST['phone_no']
		gender = request.POST['gender']

		info = Info(first_name = first_name, last_name = last_name, email = email, phone_no = phone_no, gender = gender)
		info.save()

		return redirect('add')

	else:
		return render(request, 'part1/add.html')

def find(request):
	if request.method == 'POST':
		email = request.POST['Email']
		try:
			info = Info.objects.get(email=email)
			return render(request, 'part1/result.html',{'info': info, 'message': 'Found User'})
		except:
			return render(request, 'part1/result.html',{'message': 'sorry no user found'})
	else:
		return render(request, 'part1/find.html')