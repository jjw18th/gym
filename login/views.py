from django.shortcuts import render
from login.forms import UserLogin,NewTrainer,SearchTrainer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from . import models
from . import forms
def login(request):
    res=render(request,'login/login.html');
    return res;
def loginuser(request):
    res=render(request,'login/login2.html');
    return res;
def create(request):
    res=render(request,'login/createuser.html');
    return res;
def save(request):
    if request.method=='POST':
        user=models.Userdetail();
        user.firstName=request.POST['first']
        user.lastName=request.POST['last']
        user.gender=request.POST['gender']
        user.cweight=request.POST['weight']
        user.dweight=request.POST['desired']
        user.height=request.POST['height']
        user.birthday=request.POST['birthdate']
        user.city=request.POST['city']
        user.pincode=request.POST['postal']
        user.state=request.POST['state']
        user.country=request.POST['country']
        user.email=request.POST['email']
        user.phone=request.POST['phone']
        user.dateofjoining=request.POST['today']
        user.trainer=request.POST['trainer']
        user.gymbefore=request.POST['gym']
        user.membership=request.POST['membership']
        user.save();
        res=render(request,'login/save.html');
        return res;
@login_required(login_url='http://localhost:8000/login')
def usercreate(request):
    data={}
    if request.method=="POST":
     username=request.POST['username']
     password=request.POST['password']
     again=request.POST['again']
     if again==password:
      user=User()
      user.username=username
      user.password=password
      user.save()
      res=render(request,'login/login.html')
      return res;
     else:
         data['error':'Password does not match Re-password']
         res=render(request,'login/save.html',data)
         return res
def loggedin(request):
    data={}
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user:
            login(request)
            request.session['username']=username
            return HttpResponseRedirect('http://localhost:8000/login/success')
        else:
           data['error']="Either Username or Password is incorrect"
           res=render(request,'login/login.html',data)
           return res
    else:
        res=render(request,'login/login.html',data)
        return res
def loginnuser(request):
    data={}
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user:
            login(request)
            request.session['username']=username
            return HttpResponseRedirect('http://localhost:8000/login/successuser')
        else:
           data['error']="Either Username or Password is incorrect"
           res=render(request,'login/login.html',data)
           return res
    else:
        res=render(request,'login/login.html',data)
        return res
def success(request):
    res=render(request,'login/loggedin.html')
    return res
def successuser(request):
    res=render(request,'login/loggedinuser.html')
    return res
def trainer(request):
    trainers=models.Trainer.objects.all()
    res=render(request,'login/trainer.html',{'trainers':trainers})
    return res
def traineruser(request):
    trainers=models.Trainer.objects.all()
    res=render(request,'login/traineruser.html',{'trainers':trainers})
    return res
def packageview(request):
    packages=models.Package.objects.all();
    res=render(request,'login/package.html',{'packages':packages})
    return res;
def newtrainer(request):
    form=forms.NewTrainer();
    res=render(request,'login/newtrainer.html',{'form':form})
    return res

def addtrainer(request):
    if request.method=="POST":
        trainer=models.Trainer();
        trainer.FullName=request.POST['FullName'];
        trainer.Pic=request.FILES.get('Picture');
        trainer.Email=request.POST['Email'];
        trainer.Contact=request.POST['Contact'];
        trainer.JoinDate=request.POST['JoinDate'];
        trainer.BirthDate=request.POST['BirthDate'];
        trainer.Status=request.POST['Status'];
        trainer.save()
        trainers=models.Trainer.objects.all()
        res=render(request,'login/trainer.html',{'trainers':trainers})
        return res;
def addpackage(request):
    if request.method=="POST":
        package=models.Package();
        package.PackageName=request.POST['PackageName'];
        package.Pic=request.FILES.get('Picture');
        package.Price=request.POST['Price'];
        package.Details=request.POST['Details'];
        package.save();
        packages=models.Package.objects.all();
        res=render(request,'login/package.html',{'packages':packages})
        return res;
def addTrainer(request):
    if request.method=="POST":
        trainer=models.Trainer();
        trainer.id=request.POST['id'];
        trainer.FullName=request.POST['FullName'];
        trainer.Pic=request.FILES.get('Picture');
        trainer.Email=request.POST['Email'];
        trainer.Contact=request.POST['Contact'];
        trainer.JoinDate=request.POST['JoinDate'];
        trainer.BirthDate=request.POST['BirthDate'];
        trainer.Status=request.POST['Status'];
        trainer.save()
        trainers=models.Trainer.objects.all()
        res=render(request,'login/trainer.html',{'trainers':trainers})
        return res;
def AddTrainer(request):
    trainer=models.Trainer();
    trainer.id=request.POST['id'];
    trainer.delete();
    trainer.FullName=request.POST['FullName'];
    trainer.Pic=request.FILES.get('Picture');
    trainer.Email=request.POST['Email'];
    trainer.Contact=request.POST['Contact'];
    trainer.JoinDate=request.POST['JoinDate'];
    trainer.BirthDate=request.POST['BirthDate'];
    trainer.Status=request.POST['Status'];
    trainer.save()
    trainers=models.Trainer.objects.all()
    res=render(request,'login/trainer.html',{'trainers':trainers})
    return res;
def AddPackage(request):
    package=models.Package();
    package.id=request.POST['id'];
    package.delete();
    package.PackageName=request.POST['PackageName'];
    package.Pic=request.FILES.get('Picture');
    package.Price=request.POST['Price'];
    package.Details=request.POST['Details'];
    package.save();
    packages=models.Package.objects.all()
    res=render(request,'login/package.html',{'packages':packages});
    return res;
def delete(request):
    trainerid=request.GET['trainer-id'];
    trainer=models.Trainer.objects.filter(id=trainerid)
    trainer.delete();
    return HttpResponseRedirect('http://localhost:8000/login/view-trainer');
def deletepackage(request):
    packageid=request.GET['package-id'];
    package=models.Package.objects.filter(id=packageid)
    package.delete();
    return HttpResponseRedirect('http://localhost:8000/login/view-package');
def edit(request):
    trainer=models.Trainer.objects.get(id=request.GET['trainer-id']);
    fields={'FullName':trainer.FullName,'Pic':trainer.Pic,'Email':trainer.Email,'Contact':trainer.Contact,'JoinDate':trainer.JoinDate,'BirthDate':trainer.BirthDate,'Status':trainer.Status}
    form=forms.NewTrainer(initial=fields)
    res=render(request,'login/edit3.html',{'trainer':trainer,'form':form})
    return res
def editpackage(request):
    package=models.Package.objects.get(id=request.GET['package-id']);
    res=render(request,'login/editpackage.html',{'package':package});
    return res;
def searchTrainer(request):
    res=render(request,'login/search.html');
    return res;
def searchTraineruser(request):
    res=render(request,'login/searchuser.html');
    return res;
def SearchTrainer(request):
    title=request.POST['FullName']
    trainers=models.Trainer.objects.filter(FullName=title)
    res=render(request,'login/search2.html',{'trainers':trainers})
    return res;
def SearchTraineruser(request):
    title=request.POST['FullName']
    trainers=models.Trainer.objects.filter(FullName=title)
    res=render(request,'login/search2user.html',{'trainers':trainers})
    return res;
def searchPackage(request):
    res=render(request,'login/searchpackage.html')
    return res;
def SearchPackage(request):
    title=request.POST['PackageName']
    packages=models.Package.objects.filter(PackageName=title)
    res=render(request,'login/searchpackage2.html',{'packages':packages})
    return res;
def package(request):
        packages=models.Package.objects.all();
        res=render(request,'login/package.html',{'packages':packages})
        return res;
def newpackage(request):
    res=render(request,'login/newpackage.html');
    return res;
