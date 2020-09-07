from django.shortcuts import render
from .forms import StudentRegistration
from .models import User
# Create your views here.
from django.http import HttpResponseRedirect
def add(request):
    if request.method=="POST":
        fm=StudentRegistration(request.POST)
        if fm.is_valid():
            fm.save()

    fm=StudentRegistration()
    return render(request,'course/add.html',{'forms':fm})
def show(request):
    obj=User.objects.all()
    return render(request,'course/show.html',{'info':obj})
def delete(request,my_id):
    pi=User.objects.get(pk=my_id)
    pi.delete()
    return HttpResponseRedirect('/show/')
def update(request,my_id):

    if request.method == "POST":
        pi=User.objects.get(pk=my_id)
        fm=StudentRegistration(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
            print(fm)
    else:
        pi=User.objects.get(pk=my_id)
        fm=StudentRegistration(instance=pi)
    return render(request,'course/update.html',{'forms':fm})