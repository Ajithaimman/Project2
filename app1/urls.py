from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('', views.home,name='home'),
    path('signup/', views.signup,name='signup'),
    path('signin/', views.signin,name='signin'),
    path('signout/', views.signout,name='signout'),
    path("contact/", views.contact,name='contact'),
    path("about/", views.about,name='about'),
    path("category/<slug:val>",views.CategoryView.as_view(),name='category'), 
    path("category/productdetail/<int:pk>",views.productdetail,name='productdetail'),
    path('changepassword/',views.changepassword,name="changepassword"),
    path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('password_reset_done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('password_reset_complete/',auth_views.PasswordResetCompleteView.as_view(template_name='passwordresetcomplete.html'),name='password_reset_complete'),

    path('addtocart',views.addtocart,name="addtocart"),
    path('cart',views.cart,name="cart"),
    path('updatecart',views.updatecart,name="updatecart"),
    path('deletecartitem',views.deletecartitem,name="deletecartitem"),
    path('wishlist',views.wishlist,name="wishlist"),
    path('addtowishlist',views.addtowishlist,name="addtowishlist"),
    path('deletewishlistitem',views.deletewishlistitem,name="deletewishlistitem"),
    path('checkout',views.checkout,name="checkout"),
    path('placeorder',views.placeorder,name="placeorder")

  
    
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

