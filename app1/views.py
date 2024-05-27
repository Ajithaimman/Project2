from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.models import auth,User
from .models import Product,Cart,Wishlist,Order,OrderItem
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.http import JsonResponse
from .forms import CreateUserForm,LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm

# login_url='/signin/'   must given otherwise not working
@login_required(login_url='/signin/')
def home(request):
    # current_user=request.user
    if 'search' in request.GET:
        search=request.GET['search']
        data=Product.objects.filter(name__icontains=search)
    else:
        data=Product.objects.all()
    return render(request,'app/home.html',{'data':data})


def signup(request):
    form=CreateUserForm()

    if request.method=="POST":
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    context={'form':form}
    return render(request,'app/signup.html',context)


def signin(request):

    form=LoginForm()

    if request.method=="POST":
        form=LoginForm(request,data=request.POST)

        if form.is_valid():
            username=request.POST.get('username')
            password=request.POST.get('password')

            user=authenticate(request,username=username,password=password)

            if user is not None:
                auth.login(request,user)
                return redirect("home")
    context={'form':form}        

    return render(request,'app/signin.html',context)


def signout(request):
    auth.logout(request)
    return redirect("signin")

def changepassword(request):
    if request.method=="POST":
        form=PasswordChangeForm(user=request.user,data=request.POST)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            # messages.success(request,"Your password changed successfully")
            return redirect('signin')

    else:
        form=PasswordChangeForm(request.user)

    return render(request,'app/changepassword.html',{'form':form})

def about(request):
    return render(request,"app/about.html")

def contact(request):
    return render(request,"app/contact.html")
 
class CategoryView(View):
    def get(self,request,val):
        products=Product.objects.filter(category=val)
        titles=Product.objects.filter(category=val).values('title')
        return render(request,"app/category.html",locals())
    
def productdetail(request,pk):
    product=Product.objects.get(pk=pk)
    return render(request,"app/productdetail.html",{'product':product})


def addtocart(request):
    if request.method=="POST":
        if request.user.is_authenticated:
            product_id=int(request.POST.get("product_id"))
            product_check=Product.objects.get(id=product_id)

            if product_check:
                if(Cart.objects.filter(user=request.user.id,product_id=product_id)):
                    return JsonResponse({'status':"Product already in cart"})
                else:
                    product_qty=int(request.POST.get("product_qty"))

                    if product_check.quantity >= product_qty:
                        Cart.objects.create(user=request.user,product_id=product_id,product_qty=product_qty)
                        return JsonResponse({'status':"Product added successfully"})
                    else:
                        return JsonResponse({'status':"Only "+str(product_check.quantity+ " quantity available")})
            else:
                return JsonResponse({'status':"No such product found"})
        else:
            return JsonResponse({'status':"Login to continue"})
    return redirect('/')

@login_required(login_url='/signin/')    
def cart(request):
    cartitem=Cart.objects.filter(user=request.user)
    context={'cart':cartitem}
    return render(request,"app/cart.html",context)

@login_required(login_url='/signin/')
def updatecart(request):
    if request.method=="POST":
        product_id=int(request.POST.get('product_id'))
        if(Cart.objects.filter(user=request.user,product_id=product_id)):
            product_qty=int(request.POST.get('product_id'))
            cart=Cart.objects.get(product_id=product_id,user=request.user)
            cart.product_qty=product_qty
            cart.save()
            return JsonResponse({'status':'updated successfully'})
    return redirect('/')


@login_required(login_url='/signin/')
def deletecartitem(request):
    if request.method=="POST":
        product_id=int(request.POST.get('product_id'))

        if(Cart.objects.filter(user=request.user,product_id=product_id)):
            cartitem=Cart.objects.get(product_id=product_id,user=request.user)
            cartitem.delete()
            return JsonResponse({'status':'deleted successfully'})
    return redirect('/')

@login_required(login_url='/signin/')
def wishlist(request):
    wishlistitems = Wishlist.objects.filter(user=request.user)
    context={'wishlist':wishlistitems}

    return render(request,'app/wishlist.html',context)



def addtowishlist(request):
    if request.method=="POST":
        if request.user.is_authenticated:
            product_id=int(request.POST.get("product_id"))
            product_check=Product.objects.get(id=product_id)

            if product_check:
                if(Wishlist.objects.filter(user=request.user.id,product_id=product_id)):
                    return JsonResponse({'status':"Product already in Wishlist"})
                else:
                    Wishlist.objects.create(user=request.user,product_id=product_id)
                    return JsonResponse({'status':"Product added to Wishlist"})
    
            else:
                return JsonResponse({'status':"No such product found"})
        else:
            return JsonResponse({'status':"Login to continue"})
    return redirect('/')

def deletewishlistitem(request):
    if request.method=="POST":
        product_id=int(request.POST.get('product_id'))

        if(Wishlist.objects.filter(user=request.user,product_id=product_id)):
            wishlistitem=Wishlist.objects.get(product_id=product_id,user=request.user)
            wishlistitem.delete()
            return JsonResponse({'status':'deleted successfully'})
        else:
            return JsonResponse({'status':"No such product found"})
    return redirect('/')


def checkout(request):
    rawcart=Cart.objects.filter(user=request.user)
    for item in rawcart:
        if item.product_qty > item.product.quantity:
            Cart.objects.delete(id=item.id)
        
    cartitems=Cart.objects.filter(user=request.user)
    total_price=0
    for item in cartitems:
        total_price += item.product.selling_price * item.product_qty

    context={'cartitems':cartitems,'total_price':total_price}
    return render(request,'app/checkout.html',context)


def placeorder(request):
    if request.method=="POST":
        neworder=Order()
        neworder.user=request.user
        neworder.fname=request.POST.get('fname')
        neworder.lname=request.POST.get('lname')
        neworder.email=request.POST.get('email')
        neworder.phone=request.POST.get('phone')
        neworder.address=request.POST.get('address')
        neworder.city=request.POST.get('city')
        neworder.state=request.POST.get('state')
        neworder.country=request.POST.get('country')
        neworder.pincode=request.POST.get('pincode')

        cart=Cart.objects.filter(user=request.user)
        cart_total_price=0
        for item in cart:
            cart_total_price += item.product.selling_price * item.product_qty

        neworder.total_price=cart_total_price
        neworder.save()

        neworderitems=Cart.objects.filter(user=request.user)
        for item in neworderitems:
            OrderItem.objects.create(
                order=neworder,
                product=item.product,
                price=item.product.selling_price,
                quantity=item.product_qty
            )

            orderproduct=Product.objects.filter(id=item.product_id).first()
            orderproduct.quantity -= item.product_qty
            orderproduct.save()

            Cart.objects.filter(user=request.user).delete() 
            return JsonResponse({'status':"Order has been placed successfully"})
            




        



        
