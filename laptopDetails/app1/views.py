from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .forms import laptopModelForm
from .models import Laptop
from django.contrib.auth.decorators import login_required
# Create your views here.



def Homeview(request):
    template_name = "app1/home.html"
    context ={}
    return render(request,template_name,context)

def laptopRegisterView(request):
    form = laptopModelForm()
    if request.method == 'POST':
        form = laptopModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('L-list')
    template_name = "app1/RegisterForm.html"
    context ={'form':form}
    return render(request,template_name,context)

@login_required(login_url='login')
def laptopListView(request):
    template_name = "app1/laptopList.html"
    lap_list =Laptop.objects.all()
    context ={'lap_list':lap_list}
    return render(request,template_name,context)

def updateLpatopDetilas(request,id):
    lap_list = Laptop.objects.get(id=id)
    form = laptopModelForm(instance=lap_list)
    if request.method == 'POST':
        form = laptopModelForm(request.POST, instance=lap_list)
        if form.is_valid():
            form.save()
            return redirect('L-list')
    template_name = "app1/RegisterForm.html"
    context = {'form':form}
    return render(request,template_name,context)

def deleteLaptopDetails(request,id):
    lap_list = Laptop.objects.get(id=id)
    lap_list.delete()
    return redirect('L-list')
