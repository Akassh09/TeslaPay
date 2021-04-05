from django.urls import path
from . import views

urlpatterns = [
    path('pay/',views.initiate_payment,name='pay'),
    path('callback/',views.callback,name='callback'),
    path('',views.paypal,name='paypal'),
]