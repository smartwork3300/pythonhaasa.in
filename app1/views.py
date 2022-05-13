from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def staffing(request):
    return render(request,'staffing.html')
def pharmastaffing(request):
    return render(request,'pharmastaffing.html')
def md(request):
    return render(request,'md.html')
def web(request):
    return render(request,'wd.html')
def digital(request):
    return render(request,'dm.html')  
def arch(request):
    return render(request,'arc.html') 
def careers(request):
    return render(request,'careers.html') 
def contacts(request):
    return render(request,'contact.html')