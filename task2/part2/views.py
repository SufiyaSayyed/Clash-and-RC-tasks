from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

def profile(request):

	if request.method == 'POST':
		username = request.POST['username']
		email = request.POST['email']
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		password = request.POST['password']
		confirm_password = request.POST['confirm_password']
		#phone_no = request.POST['phone_no']

		if password == confirm_password:
			if User.objects.filter(username=username).exists():
				messages.info(request, 'User already exists. Try again.')
				return redirect('profile')
			else:
				user = User.objects.create_user(username=username, email=email, first_name=first_name, last_name=last_name, password=password)
				user.save()
				#ph = Extend_user(User = user, phone_no=phone_no)
				#ph.save()
				return render(request, 'part2/profile.html',{'message':'successful signin'})
		else:
			messages.info(request, 'Passwords do not match. Try again.')
			return redirect('profile')

	else:
		return render(request, 'part2/profile.html')
	

def login(request):

	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		user = auth.authenticate(username=username, password=password)
			
		if user is not None:
			auth.login(request, user)
			return render(request, 'part2/logout.html')

		else:
			messages.info(request, 'Invalid credentials')
			return redirect('login')

	else:
		return render(request, 'part2/login.html')

def logout(request):
	auth.logout(request)
	return render(request, 'part2/profile.html')