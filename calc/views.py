from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#controller of MVC

def home(request):
    #return HttpResponse("<center><h1>Hello World<h1><center>")
    return render(request, 'home.html', {'name': 'Eakshitha'})

def add(request):

    #fetch data using get request
    # val1 = request.GET["num1"]
    # val2 = request.GET["num2"]

    #fetch data using post request
    val1 = request.POST["num1"]
    val2 = request.POST["num2"]
    res = int(val1) + int(val2)

    return render(request, "result.html", {'result': res})

def modulus(request):

    firstNum = int(request.POST["firstNum"])
    secondNum = int(request.POST["secondNum"])
    result = firstNum % secondNum

    return render(request, "result.html", {'result': result})