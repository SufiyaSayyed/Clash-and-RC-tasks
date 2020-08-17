from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from .models import Extend_user

def sign_up(request):

	if request.method == 'POST':
		username = request.POST['username']
		email = request.POST['email']
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		password = request.POST['password']
		confirm_password = request.POST['confirm_password']
		phone_no = request.POST['phone_no']

		if password == confirm_password:
			if User.objects.filter(username=username).exists():
				return render(request, 'part2/sign_up.html', {'message': 'User already exists. Try again.'})
			else:
				user = User.objects.create_user(username=username, email=email, first_name=first_name, last_name=last_name, password=password)
				extend_user=Extend_user(user=user, phone_no=phone_no)
				extend_user.save()
				user = auth.authenticate(username=username, password=password)
				auth.login(request, user)
				return redirect('result')
		return render(request, 'part2/sign_up.html', {'message': 'Passwords do not match. Try again.'})

	return render(request, 'part2/sign_up.html')
	
def login(request):

	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		user = auth.authenticate(username=username, password=password)
			
		if user is not None:
			auth.login(request, user)
			return redirect('result')

		return render(request,'part2/login.html',{'message': 'Invalid credentials'})
	return render(request, 'part2/login.html')

def logout(request):
	auth.logout(request)
	return render(request, 'part2/sign_up.html')
	
def result(request):
	return render(request, 'part2/result.html')

