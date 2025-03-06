from django.shortcuts import render
from django.http import HttpResponse
from .models import Product,Contact,Orders,OrderUpdate # to get data from database of Product,Contact
import json
# Create your views here.
def index(request):
   products= Product.objects.all()# to acess all products from database.
   all_cat = {products[j].category for j in range(len(products))}# set because in it duplicate category can't occur.
   lis = [0,1,2]
   params={'product': products,'all_cat': all_cat,'lis':lis}
   #print(all_cat)'''
   print(products[0].desc)
   return render(request,"shop/index.html",params)
   # HttpResponse('index')

def searchMatch(query,item):
   if query.lower() in item.desc.lower() or query.lower()==item.product_name.lower() or query.lower()==item.category.lower():
       return item
   

def search(request):
   products= Product.objects.all()# to acess all products from database.
   
   search_prod = request.GET.get("search","")
   searched = []
   for item in products:
        search = searchMatch(search_prod,item)
        searched.append(search)
        if search == None:
            searched.remove(search)
   if searched == []:
       search_msg = "this searched product is not available. You can look for other products at myCart "
   else:
       search_msg = "your searching results are"

   params={'product': products,'search_product':searched,'search_msg':search_msg}
   
   return render(request,"shop/search.html",params)

def contact(request):
    if request.method== "POST":
       name= request.POST.get('name','')
       email = request.POST.get('e-mail','')
       phone = request.POST.get('tel','')
       query = request.POST.get('query','')
       contact = Contact(name=name,email=email,phone=phone,query=query)
       #contact.save()
       
       return render(request,'shop/contact.html')
    return render(request,'shop/contact.html')
   # return HttpResponse('contact')

def productview(request,myid):
# fetch specific product using id.
    productview = Product.objects.filter(id=myid) 
    print(productview[0])#productview is a list with only one item , so we need productview[0] to access that item.
    return render(request,'shop/productview.html',{'product':productview[0]})
    #return HttpResponse('''productview''')

def checkout(request):
    if request.method== "POST":
       items_json = request.POST.get('itemsJSON','')
       name= request.POST.get('name','')
       email = request.POST.get('email','')
       phone = request.POST.get('phone','')
       address = request.POST.get('address','')
       city = request.POST.get('city','') 
       state = request.POST.get('state','')
       pin = request.POST.get('pin','')
       order_details = Orders(items_json=items_json,name=name,email=email,phone=phone,address=address,city=city,state=state,pin_code=pin)
       order_details.save()


       order_update = OrderUpdate(order_id=order_details.order_id,update_desc="product has been placed")
       order_update.save()

    return render(request,'shop/checkout.html')
  #  return HttpResponse('checkout')

def tracker(request):
    if request.method == "POST":
        orderId = request.POST.get('orderId','') # get user entered data.
        email = request.POST.get('email','')
        #print(orderId,email)
       # return HttpResponse(f"{email} and {orderId}")
        try:                           # to match user data from Orders database data to verify user.
            order = Orders.objects.filter(order_id =orderId,email = email)
            if len(order) > 0:
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text':item.update_desc,'time':item.timestamp})
                    response = json.dumps([updates,order[0].items_json],default=str) # dumps convert syntax to js compatible syntax.
                    #print('try-if-------------------------------------')
                return HttpResponse(response)#dumps not work for data datatype,so converted it to str in response. 
            else:
                return HttpResponse('{}')
        except:
            return HttpResponse('{}')
            
    return render(request,'shop/tracker.html')
   # return HttpResponse('tracker')

def about(request):
   return render(request,'shop/about.html')
#   return HttpResponse('about')