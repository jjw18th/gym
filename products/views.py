from django.shortcuts import render
from login.forms import UserLogin,NewTrainer,SearchTrainer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from . import models


# Create your views here.
def product(request):
    products=models.Products.objects.all();
    res=render(request,'products/products.html',{'products':products})
    return res;
def productuser(request):
    products=models.Products.objects.all();
    res=render(request,'products/productsuser.html',{'products':products})
    return res;
def faq(request):
    faqs=models.Faq.objects.all();
    res=render(request,'products/faq.html',{'faqs':faqs})
    return res
def recipe(request):
        recipes=models.Recipe.objects.all();
        res=render(request,'products/recipe.html',{'recipes':recipes})
        return res;
def review(request):
    messages=models.Message.objects.all();
    res=render(request,'products/reviews.html',{'messages':messages})
    return res;
def msgsave(request):
    message=models.Message();
    message.name=request.POST['name'];
    message.msg=request.POST['msg'];
    message.save();
    res=render(request,'gym/contact2.html')
    return res;
def diet(request):
    diets=models.Diet.objects.all();
    res=render(request,'products/diet.html',{'diets':diets})
    return res;
def batches(request):
    batches=models.Batches.objects.all();
    res=render(request,'products/batches.html',{'batches':batches})
    return res;
def batchesuser(request):
    batches=models.Batches.objects.all();
    res=render(request,'products/batchesuser.html',{'batches':batches})
    return res;
def newproduct(request):
    res=render(request,'products/newproduct.html')
    return res;
def newfaq(request):
    res=render(request,'products/newfaq.html')
    return res;
def newrecipe(request):
    res=render(request,'products/newrecipe.html')
    return res;
def newdiet(request):
    res=render(request,'products/newdiet.html')
    return res;
def newbatch(request):
    res=render(request,'products/newbatch.html')
    return res;
def addproduct(request):
    if request.method=="POST":
        product=models.Products();
        product.ProductName=request.POST['ProductName'];
        product.Pic=request.FILES.get('Picture');
        product.Price=request.POST['Price'];
        product.save();
        products=models.Products.objects.all();
        res=render(request,'products/products.html',{'products':products})
        return res;
def addfaq(request):
    if request.method=="POST":
        faq=models.Faq();
        faq.Query=request.POST['Query'];
        faq.Response=request.POST['Response'];
        faq.save();
        faqs=models.Faq.objects.all();
        res=render(request,'products/faq.html',{'faqs':faqs})
        return res;
def addrecipe(request):
    if request.method=="POST":
        recipe=models.Recipe();
        recipe.MealName=request.POST['MealName'];
        recipe.Pic=request.FILES.get('Picture');
        recipe.Recipe=request.POST['Recipe'];
        recipe.save();
        recipes=models.Recipe.objects.all();
        res=render(request,'products/recipe.html',{'recipes':recipes})
        return res;
def addplan(request):
    diet=models.Diet();
    diet.Meal=request.POST['Meal'];
    diet.Time=request.POST['Time'];
    diet.WhatToEat=request.POST['WhatToEat'];
    diet.save();
    diets=models.Diet.objects.all();
    res=render(request,'products/diet.html',{'diets':diets})
    return res;
def addbatch(request):
    batch=models.Batches();
    batch.BatchName=request.POST['BatchName'];
    batch.BatchTiming=request.POST['BatchTiming'];
    batch.save();
    batches=models.Batches.objects.all();
    res=render(request,'products/batches.html',{'batches':batches})
    return res;
def deleteproduct(request):
        productid=request.GET['product-id'];
        product=models.Products.objects.filter(id=productid)
        product.delete();
        return HttpResponseRedirect('http://localhost:8000/products/products');
def deletefaq(request):
        faqid=request.GET['faq-id'];
        faq=models.Faq.objects.filter(id=faqid)
        faq.delete();
        return HttpResponseRedirect('http://localhost:8000/products/faq');
def deleterecipe(request):
        recipeid=request.GET['recipe-id'];
        recipe=models.Recipe.objects.filter(id=recipeid)
        recipe.delete();
        return HttpResponseRedirect('http://localhost:8000/products/recipe');
def deleteplan(request):
    dietid=request.GET['diet-id'];
    diet=models.Diet.objects.filter(id=dietid)
    diet.delete();
    return HttpResponseRedirect('http://localhost:8000/products/diet');
def deletebatch(request):
    batchid=request.GET['batch-id'];
    batch=models.Batches.objects.filter(id=batchid)
    batch.delete();
    return HttpResponseRedirect('http://localhost:8000/products/batches');
def deletemessage(request):
    messageid=request.GET['message-id'];
    message=models.Message.objects.filter(id=messageid)
    message.delete();
    return HttpResponseRedirect('http://localhost:8000/products/reviews');
def searchproduct(request):
     res=render(request,'products/searchproduct.html');
     return res;
def searchproductuser(request):
     res=render(request,'products/searchproductuser.html');
     return res;
def searchfaq(request):
    res=render(request,'products/searchfaq.html');
    return res;
def searchrecipe(request):
     res=render(request,'products/searchrecipe.html');
     return res;
def searchplan(request):
      res=render(request,'products/searchplan.html');
      return res;
def searchbatch(request):
      res=render(request,'products/searchbatch.html');
      return res;
def searchbatchuser(request):
      res=render(request,'products/searchbatchuser.html');
      return res;
def search2product(request):
     title=request.POST['ProductName']
     products=models.Products.objects.filter(ProductName=title)
     res=render(request,'products/search2product.html',{'products':products})
     return res;
def search2productuser(request):
     title=request.POST['ProductName']
     products=models.Products.objects.filter(ProductName=title)
     res=render(request,'products/search2productuser.html',{'products':products})
     return res;
def search2faq(request):
     title=request.POST['Query']
     faqs=models.Faq.objects.filter(Query=title)
     res=render(request,'products/search2faq.html',{'faqs':faqs})
     return res;
def search2recipe(request):
     title=request.POST['MealName']
     recipes=models.Recipe.objects.filter(MealName=title)
     res=render(request,'products/search2recipe.html',{'recipes':recipes})
     return res;
def search2batch(request):
     title=request.POST['BatchName']
     batches=models.Batches.objects.filter(BatchName=title)
     res=render(request,'products/search2batch.html',{'batches':batches})
     return res;
def search2batchuser(request):
     title=request.POST['BatchName']
     batches=models.Batches.objects.filter(BatchName=title)
     res=render(request,'products/search2batchuser.html',{'batches':batches})
     return res;
def search2plan(request):
     title=request.POST['Meal']
     diets=models.Diet.objects.filter(Meal=title)
     res=render(request,'products/search2plan.html',{'diets':diets})
     return res;
def edit(request):
    product=models.Products.objects.get(id=request.GET['product-id']);
    res=render(request,'products/editproduct.html',{'product':product});
    return res;
def editfaq(request):
    faq=models.Faq.objects.get(id=request.GET['faq-id']);
    res=render(request,'products/editfaq.html',{'faq':faq});
    return res;
def editrecipe(request):
    recipe=models.Recipe.objects.get(id=request.GET['recipe-id']);
    res=render(request,'products/editrecipe.html',{'recipe':recipe});
    return res;
def editplan(request):
    diet=models.Diet.objects.get(id=request.GET['diet-id']);
    res=render(request,'products/editplan.html',{'diet':diet});
    return res;
def editbatch(request):
    batch=models.Batches.objects.get(id=request.GET['batch-id']);
    res=render(request,'products/editbatch.html',{'batch':batch});
    return res;
def addProduct(request):
    product=models.Products();
    product.id=request.POST['id'];
    product.delete();
    product.ProductName=request.POST['ProductName'];
    product.Pic=request.FILES.get('Picture');
    product.Price=request.POST['Price'];
    product.save();
    products=models.Products.objects.all()
    res=render(request,'products/products.html',{'products':products});
    return res;
def addFaq(request):
    faq=models.Faq();
    faq.id=request.POST['id'];
    faq.delete();
    faq.Query=request.POST['Query'];
    faq.Response=request.POST['Response'];
    faq.save();
    faqs=models.Faq.objects.all()
    res=render(request,'products/faq.html',{'faqs':faqs});
    return res;
def addRecipe(request):
    recipe=models.Recipe();
    recipe.id=request.POST['id'];
    recipe.delete();
    recipe.MealName=request.POST['MealName'];
    recipe.Pic=request.FILES.get('Picture');
    recipe.Recipe=request.POST['Recipe'];
    recipe.save();
    recipes=models.Recipe.objects.all()
    res=render(request,'products/recipe.html',{'recipes':recipes});
    return res;
def addPlan(request):
    diet=models.Diet();
    diet.id=request.POST['id'];
    diet.delete();
    diet.Meal=request.POST['Meal'];
    diet.Time=request.POST['Time'];
    diet.WhatToEat=request.POST['WhatToEat']
    diet.save();
    diets=models.Diet.objects.all()
    res=render(request,'products/diet.html',{'diets':diets});
    return res;
def addBatch(request):
    batch=models.Batches();
    batch.id=request.POST['id'];
    batch.delete();
    batch.BatchName=request.POST['BatchName'];
    batch.BatchTiming=request.POST['BatchTiming']
    batch.save();
    batches=models.Batches.objects.all()
    res=render(request,'products/batches.html',{'batches':batches});
    return res;
