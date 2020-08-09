from django.shortcuts import render
from django.http import HttpResponse

def num(request):
	l=[]
	for i in range(1,21):
		l.append(i)
	context={'list_num': l}
	return render(request, 'part1/num.html', context)

def printn(request):
	l=[]
	str=""
	val1 = int(request.GET['start'])
	val2 = int(request.GET['end'])
	if(val1<val2):
		for i in range(val1,val2+1):
			l.append(i)
	else:
		str="error: starting point is greater than ending point"
	context={'result1': l,'result2': str}
	return render(request, 'part1/result.html',context)
