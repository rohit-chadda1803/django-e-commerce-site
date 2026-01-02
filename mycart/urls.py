"""mycart URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include # NOTE:include to attach shop folder.
 # if we add /shop/ to site url, it will redirect it to shop.urls to handle further.
from django.conf import settings
from django.conf.urls.static import static
from . import views

from shop.views import create_admin #`to create superuser on browser`

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shop/', include('shop.urls')),
    path('blog/', include('blog.urls')),
    path('',views.index,name='index') , 
    path("createsuperuser/", create_admin), # to create superuser on browser
    
 ]  +  static(settings.MEDIA_URL,document_root= settings.MEDIA_ROOT)


# STEPS IN CREATING THIS PROJECT : NOTE :- we created shop and blog app to it.
# 1.) CREATE (mycart) in site2e-commerce.
# 2.) USE (djang-admin startapp) to create (blog & shop) in mycart as  in showen oder.
# 3.) create (urls.py file) in shop & add path in it.
# 4.) ADD index in views.py in shop.
# 5.) add line 24 {include('shop.urls')} in current file .
# 6.) Repeat steps(3,4,5) for (blog) also like shop.
# 7.) create(templates folder)in blog and shop,then make new folder shop in template of shop and blog in temp.of blog.
# 8.) add ('blog','shop') in (INSTALLED APPS) IN settings.py of mycart.
# 9.) add html fies in temlates and (return render(request,'blog/index.html')) in views.py of blog&in shop similarly.
#10. create blog->static->blog & same in(shop) to store static files.
#11. link static files in index.html by ({% load static %} and in next line :
#    --->NOTE:<a href="{%static 'blog/blogstatic.txt' %}">read my static file</a> <--to join static file.-->.
#12. created pipelines(path('',--,name="--")) in shop.url and corresponding func. in shop.view .

#13.NOTE:(python manage.py migrate) to inform django ,we are changing  migrations in models {i.e way of storing 
#        data in database} and add models in models.py of shop .

#14.NOTE: Replace 'shop' with 'shop.apps.Shopconfig' in apps in mycart->settings.py , Shopcfig is name of class in
#         shop -> apps.py

#15.NOTE: to store (it will'nt apply) migrations-->( python manage.py makemigrations)& then to apply stored
# migrations --->( python manage.py migrate) . NOTE: it will create 001_initial.py in shop-->mogrations.

#16. NOTE:(python manage.py createsuperuser) to create superuser account and then enter name(Rohit_CHADDA,Rohit_Chadda),e-mail,
#       pass.(1803) and superuser can acess database.

#17. NOTE: (http://127.0.0.1:8000/admin) to login to django administration page with name,pass.

#18. register (Product)in admin.py by lines(4,5) & it will display on django administration page and now add product
#    here with details as written in models.py

#19.NOTE: edit shop-->index.html to make homepage & carousel(i.e slideshoe of objects) with cards in it. 
#20.NOTE:adding images and adding more models(price,category,image).STEPS:-
#   a.) (pip install Pillow)  to store image in database.
#   b.)add ln(132,133 i.e{MEDIA_ROOT,MEDIA_URL}) in settings.py after ( Managing Media at bottom)&
#   c.) ln(19,20,26{static(--)}) in current file.

#21.NOTE: Way to add product using (python manage.py shell) in terminal {just for information & not used further}-->
#a.) from shop.models import Product
# b.)newprod=Product(detail_name = "",---,---,--)& newprod.save() & to show all products --> Product.objects.all() 

#22.NOTE:template inheritance(using same basic.html template in every file without writing whole code).FOR IT:-
# NOTE:create{% block property %}{% endblock %}in basic.html& in about.html({% block property %}property{% endblock %}) &
# it will replace {% block property %}{% endblock %} with property in code of basic.html use it as code of about.html

#23.NOTE:fetching products from django database.FOR IT:- add (products= Product.objects.all(),params)in shop/views.py
#NOTE:use (django for loop) in index.html(ln92-109) to show products acc. to no. of products in django database.

#24.NOTE:added for loop(all_cat) to show no. of slides acc. all categories using(all_cat) in views.py
# & NOTE:{% if i.category == cat %} to put specific item in specific category slide.

#23.NOTE:add js script tag in index.html to get of user activity at index page when it click&moves to 'add to cart'.

#24.NOTE:add popover in navbar & js to activate in js script &{document.getElementById("popcart").setAttribute('data-
#   bs-content','<h5>--content--</h5>');}for popver content & add(data-bs-html='true') to use html in cont. attribute.
#  &  add span with id="cart" to get total no. of product added to cart .

#25.NOTE:add quickview button in card,in shop->urls.py change(productview to productview/<"int:myid">)& add myid in 
#   shop-views->def productview(req-,myid) and productview=Product.objects.filter(id=myid) to this function
#   to acess that  productview page for every product with unique id. & create(productview.html) for it.

#26.NOTE:add form in contact.html & edit (def contact in shop->views.py) and make Contact database from models.py and 
#  admin.py & add(contact = Contact(na-,--),contact.save()) to save contact page user data in database,automatically.

#27.NOTE:create & edit productview page

#28.NOTE: We updated code in if-else of '$('.cart').click(function(){}' to get item name and quantity also instead
#   of quantity only.For it added(name,qty & card[idstr]=[qty,name])

#29.NOTE: We have linked index file with basic.html & removed useless code.

#30.NOTE: jquery link in basic page to acess jquery in all pages.        

#31.NOTE: added some js(if{-}else{-}for(--){-}) in checkout.html to get cart items detail from 'cart' of index page
#         & show their {name,quantity} using bootstrap ul (remove default li  & add new by js for items).

#32.NOTE:a.)created Orders database & b.)showing thanks alert on clicking {"Place Order"} button.
#        c.) $('#itemsJSON').val(JSON.stringify(cart)) in js of checkout.html to store cart details
#            in {items_json} of Orders database.

#33.NOTE:created a page for(http://127.0.0.1:8000/) which was showing error.For it :-
#    a.)add {templates->index.html} in {mycart->mycart} & edit {index.html} & add {'DIRS':['mycart/templates'],} in
#    {TEMPLATES in settings.py of mycart->mycart} in place of {'DIRS':[],}

#   b.)create views.py in {mycart->mycart} & add ln(21,26) in {current filr i.e mycart->mycart-urls.py} to path it 
#   with index function of that views.py

#34.NOTE:{Tracking the order}-a.) create OrderUpdate database & edit tracker.html
#                            b.)create&save {order_details} in views.py{checkout function}
#                          c.)edit func tracker to get user data{on trcker form} & match it to Orders database data.
#                        d.)in tracker func,add {if-(for---)else} to get&give updates of order.
#                      e.)add some js in tracker.html to get & display data of updates.

#35.NOTE: added price in cart to display item price and total price in checkout page.

#35.NOTE:display order details on clicking 'track order'. -----
#.      a.)in shop->views.py->tracker change {JSON.dumps(updates,default=str)} to {JSON.dumps([updates,
#          order[0].items_json],default=str)} to get order item details stored in items_json in Orders database.

#       b.)in tracker.html change({updates = JSON.parse(data)}to{data =JSON.parse(data)  updates=data[1]})& to 
#          display items add {cart=JSON.parse(data[1]) for(item in cart){--}}.Here,old updates = new updates,so
#          no need to modify rest code.  

#36.NOTE : {window.location = "/shop"} to rediredct {http://127.0.0.1:8000} to {http://127.0.0.1:8000/shop/} in 
#          mycart->mycart->templates->index.html {in head tag's script tag}

#37.) styled navbar of both{blog & index} & edit bolg->{index.html,basic.html}

#38.NOTE: created database{Blogpost} in blogs& edited blog->index.html & displayed all content card from database by
#         taking {blogs = Blogpost.objects.all(),blogposted = {'blogs':blogs}} in index func of blog->views.py.

#39.NOTE:like productview in (25.),created dynamic blogpost for each blog in database{Blogpost} with specific id.
#        a.)in blog->views.py, change {path('blogpost/',--,name="-")} to {path('blogpost/<int:myid>',--,name="--")}.
#        b.) def blogpost(request): to {---(myid,request):} & in it ,add(blog=---.filter(post_id=myid) & blogposted).

#40.NOTE:created next blog & prev blog button in blogspot page.


# production now : 

# 1. pip install gunicorn whitenoise psycopg2-binary
#  2 . MIDDLEWARE = [
#     'django.middleware.security.SecurityMiddleware',
#     'whitenoise.middleware.WhiteNoiseMiddleware',
#     ...
# ]

# 3. STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'  in settings.py

# 4. creae render.yml file for render.com deployment

# content :

# services:
#   - type: web
#     name: mycart
#     env: python
#     buildCommand: "pip install -r requirements.txt"
#     startCommand: "gunicorn mycart.wsgi:application"


# 5. Create Procfile for  deployment  //Now your Django app knows how to start on the server 🚀

'''
Procfile tells the server how to start your Django website.

When your project is deployed, the hosting platform does not know:

“Which file should I run to start this app?”

So the Procfile answers that question.


web:	This is a web server
gunicorn:	production web server
mycart.wsgi:application	: Django entry point
'''

#6 . gitignore ---> these files will not on github ,as they may give problems in deployment.
# db.sqlite3
# __pycache__/
# *.pyc
# media/
# staticfiles/
# .env

# 7 . 
# 2️⃣ Tell Git to stop tracking old files

# Run:

# git rm --cached db.sqlite3
# git rm -r --cached media
# git rm -r --cached mycart/__pycache__


# (These files will stay on your PC.)


# 8 . 
# ALLOWED_HOSTS = [
#     'mycart-shop-blog.onrender.com',
#     'localhost',
#     '127.0.0.1',
# ]
