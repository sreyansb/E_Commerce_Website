from django.shortcuts import render
from django.http import HttpResponse
from .models import Products,Contact,Orders,OrderUpdate
from math import ceil

import json#used in tracker to send response to tracker.html

# Create your views here
def index(request):
    allproducts=Products.objects.all()
    numberofslides=int(ceil(len(allproducts)/4))
    #params={'products':allproducts,'no_of_slides':numberofslides,'range':range(1,numberofslides)}#because of 0 based indexing range from 1 to numberofslides-1
    #to print for multiple categories
    #all categories
    points=Products.objects.values('category')
    categories_set={i['category'] for i in points}
    allProds=[]
    for i in categories_set:
        catproducts=Products.objects.filter(category=i)
        numberofslides=int(ceil(len(catproducts)/4))
        allProds.append([catproducts,range(1,numberofslides),numberofslides])
    params={'allProds':allProds}
    return render(request,"shop/index.html",params)#very important to specify shop/ in shop/index.html otherwise wont work

def searchmatch(query,item):
    query=query.lower()
    if query in item.desc.lower() or query in item.product_name.lower() or query in item.category.lower() or query in item.subcategory.lower():
        return True
    return False

def search(request):
    #search using a word which is present in the description,name,category,subcategory of the product
    query=request.GET.get('query',"")
    points=Products.objects.values('category')
    categories_set={i['category'] for i in points}
    allProds=[]
    for i in categories_set:
        catproducts=Products.objects.filter(category=i)
        catproducts=[i for i in catproducts if searchmatch(query,i)]
        numberofslides=int(ceil(len(catproducts)/4))
        if len(catproducts)!=0:
            allProds.append([catproducts,range(1,numberofslides),numberofslides])
    if len(allProds)==0:
        params={'msg':0}
        return render(request,"shop/search.html",params)
    params={'allProds':allProds,'msg':1}
    return render(request,"shop/search.html",params)

def about(request):
    return render(request,"shop/about.html")

def contact(request):
    if request.method=="POST":
        name=request.POST.get('name','')
        phone=request.POST.get('phone','')
        email=request.POST.get('email','')
        desc=request.POST.get('desc','')
        contact=Contact(name=name,desc=desc,phone=phone,email=email)
        contact.save()
        return render(request,"shop/contact.html",{'done':True})
    return render(request,"shop/contact.html")

def tracker(request):
    
    if request.method=="POST":
        order_ID=request.POST.get("order_ID","")
        email=request.POST.get("email","")
        try:
            order=Orders.objects.filter(order_ID=int(order_ID),email=email)
            # print(order)
            if len(order)>0:
                update=OrderUpdate.objects.filter(order_id=int(order_ID))#to get all updates
                updates=[]
                for item in update:
                    updates.append({'time':item.timestamp,'Description':item.update_desc})
                res=json.dumps([updates,order[0].items_json],default=str)
                return HttpResponse(res)
            else:
                return HttpResponse("{}")
        except Exception as e:
            print(e)
            return HttpResponse("{}")
    return render(request,"shop/tracker.html")


def productView(request,id):
    #to make a product ka page
    product=Products.objects.get(id=id)
    return render(request,"shop/ProdView.html",{'product':product})

def checkout(request):
    if request.method=="POST":
        items_json=request.POST.get("items_json","")
        name=request.POST.get("name","")
        amount=request.POST.get("amount","")
        email=request.POST.get("email","")
        phone=request.POST.get("phone","")
        city=request.POST.get("city","")
        state=request.POST.get("state","")
        zip_code=request.POST.get("zip_code","")
        address1=request.POST.get("address1","")
        address2=request.POST.get("address2","")
        orders=Orders(amount=amount,items_json=items_json,name=name,phone=phone,email=email,address=address1+" "+address2,city=city,state=state,zip_code=zip_code)
        orders.save()
        #order_id available after save
        order_update=OrderUpdate(order_id=orders.order_ID,update_desc="Order Placed")
        order_update.save()
        # to clear local storage if a person checks out
        return render(request,'shop/CheckOut.html',{'thank':True,'id':orders.order_ID})
    return render(request,"shop/CheckOut.html")