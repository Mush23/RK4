from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .rk4 import rk4
from .rk4 import rk4Analyse

def home(request):
	print("Hello World",request.method,'Yes')
	if request.method == 'POST':
		f = request.POST['f']
		x0 = float(request.POST['x0'])
		y0 = float(request.POST['y0'])
		xn = float(request.POST['xn'])
		step = int(request.POST['step'])
		origEq = request.POST['origEq']
		if origEq == "":
			lists = rk4(f, x0, y0, xn, step)
			print ("18")
		else:
			lists = rk4Analyse(f, x0, y0, xn, step, origEq)
		# msgs = messages.success(request, 'Your List '+ str(r))
		#print (lists)
		return render(request,'table.html',{'listVal':lists})
	return render(request,'base.html')


