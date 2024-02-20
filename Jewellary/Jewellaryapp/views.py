from django.shortcuts import render , redirect
from .models import *
from .forms import *
from  django.contrib.auth import authenticate, login as log, logout
from django.contrib.auth.models import User, auth
from django.core.mail import send_mail
import json


# Create your views here.

def home(request):
    return render (request,'home.html')

#cart
def cartel(request):
    userid=request.session.get('id')
    try:
        if request.method=='GET':
            print(userid)
            if userid:
                cart=cartetl.objects.filter(userid=userid)
                print(cart)
                return render(request,'cartel.html',{'cart':cart})
    except:
        return render(request,'cartel.html')

def about(request):
    return render(request,'about.html')
def viewproduct(request):
    return render (request,'viewproduct.html')
def lalu(request):
    return render (request,'customer_update.html')
def contacts(request):
    return render (request,'contacts.html')

#customer registeration
def customer_rg(request):
    form =customer_form()
    if request.method =='POST':
        form =customer_form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            
            return redirect('custom_login')
    return render(request,'customer_rg.html',{'form':form})

#customer login
def custom_login(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        cr = customer_registeration.objects.filter(username=username,password=password)
        if cr:
            userdetails =customer_registeration.objects.get(username=username, password=password)
            id = userdetails.id
            username = userdetails.username
            password = userdetails.password
            request.session['id'] = id
            request.session['username']  = username
            request.session['password'] = password
            return redirect('custom_dashboard')
        else:
            error ='invalid credentails'
            return render(request, 'customer_login.html',{'error':error})
    else:
        return render(request,'customer_login.html')
    
#customer dashboard
def custom_dashboard(request):
    id=request.session['id']
    username= request.session['username']
    productsview = customer_registeration.objects.all()
    return render(request,'cust_dashboard.html',{'id':id,'username':username,'productsview':productsview})

#customer detailview
def detailedview(request,pk):
  productsview = customer_registeration.objects.get(id=pk)
  return render(request,"detailedview.html",{'productsview':productsview})

#customer update
def custom_update(request,pk):
    pro = customer_registeration.objects.get(id=pk)
    form =customer_form(instance=pro)
    if request.method =='POST':
        form=customer_form(request.POST,instance=pro)
        if form.is_valid():
            form.save()
            return redirect('custom_dashboard')
    return render(request,'customer_update.html',{'form':form})

#customer logout
def custom_logout(request):
    logout(request)
    return redirect('custom_login')

#staff registeration
def reg_staff(request):
    form =staff_form()
    if request.method =='POST':
        form =staff_form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('staff_login')
    return render(request,'staff_registeration.html',{'form':form})

#staff login
def staff_login(request):
    if request.method =='POST':
        username =request.POST.get('username')
        password =request.POST.get('password')
        stf =staff_regsinfo.objects.filter(username=username,password=password,verfiystatus=True)
        if stf:
            user_details=staff_regsinfo.objects.get(username=username,password=password)
            id= user_details.id
            username= user_details.username
            password=user_details.password
            request.session['id']=id
            request.session['username']=username
            request.session['password']=password
            return redirect('staff_dashboard')
        else:
            error='invalid credentials or not approved by admin yet'
            return render(request, 'staff_login.html', {'error':error})
    else:
        return render(request,'staff_login.html')

#staff dashboard
def staff_dashboard(request):
    id=request.session['id']
    username= request.session['username']
    form = addproduct_form()
    if request.method =="POST":
        form = addproduct_form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    cr = addproduct.objects.all()
    return render(request,'staff_dashbord.html',{'username':username,'id':id,'form':form,'cr':cr})

#staff logout
def staff_logout(request):
    logout(request)
    return redirect('staff_login')

#product update
def product_update(request,pk):
    pro = addproduct.objects.get(id=pk)
    form =addproduct_form(instance=pro)
    if request.method =='POST':
        form=addproduct_form(request.POST, instance=pro)
        if form.is_valid():
            form.save()
            return redirect('staff_dashboard')
    return render(request, 'staff_productupdate.html',{'form':form})

#product delete
def product_delete(request,pk):
    delete = addproduct.objects.get(id=pk)
    delete.delete()
    return redirect('staff_dashboard')

#products view
def viewproduct(request):
    ad= addproduct.objects.all()
  
    return render(request,"viewproduct.html",{'ac':ad})

#adding products
def add_product(request):
    form =addproduct_form()
    if request.method =='POST':
        form =addproduct_form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('viewproduct')
    return render(request,'add_product.html',{'form':form})

#cart adding to data base
def cart(request):
   userid=request.session.get('id')
   if userid:
       if request.method=='POST':
           print(request.body)
           data=json.loads(request.body.decode('utf-8'))
           itemname=data.get('itemname')
           price=data.get('price')
           coverimage=data.get('coverimage')
           cart=cartetl.objects.create(userid=userid,itemname=itemname,price=price,coverimage=coverimage)
           return redirect('cartel')
       
   return redirect('cartel')