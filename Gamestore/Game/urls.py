from django.urls import path,include
from Game import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.index),
    path('products/add', views.product_add),
    path('products/show', views.product_show),
    path('products/edit/<rid>', views.product_edit),
    path('products/delete/<rid>', views.product_delete),
    path('register', views.user_register),
    path('login', views.user_login),
    path('logout', views.user_logout),
    path('cart/add/<rid>', views.add_to_cart),
    path('cart', views.show_cart),
    path('cart/remove/<rid>', views.remove_cart),
    path('cart/update/<rid>/<cid>', views.update_cart),
    path('blank',views.blank),
    path('order/add', views.add_to_order),
    path('orders', views.show_order),
    path('review/add/<rid>', views.add_review),
    path('product/detail/<rid>',views.product_details),
    path('sendotp',views.send_otp),
    path('verify_otp',views.verify_otp),
    path('update_password',views.update_password),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
