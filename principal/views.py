from django.shortcuts import render

def redes(request):
	return render(request,'login.html')

def aplicacion(request):
	return render(request,'index.html')	
# Create your views here.
