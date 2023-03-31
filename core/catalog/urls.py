from django.contrib import admin
from django.urls import path, include
from catalog.views import (MainPageView, 
                            ContactPageView, RegisterView, ProfileView, DetailCartView, ProductView, 
                            ProductDetailView, HistoryOrders, HistoryView, ProfieDetailView, UserEditView,
                            TireStoreLandingPageView, HowGetOrderView, MainProduct,
                            UserTire, AboutView)
from . import views as v 

app_name = 'snippets'

urlpatterns = [
    path('', MainPageView.as_view(), name='main_page'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('catalog/<slug:slug>/', MainProduct.as_view(), name='main'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('cart/', DetailCartView.as_view(), name='cart_detail'),
    path('<int:pk>/', ProductDetailView.as_view(), name='detail'),
    path('history/', HistoryView.as_view(), name='history'),
    path('profiledetail/', ProfieDetailView.as_view(), name='profiledetail'),
    path('user_edit/', UserEditView.as_view(), name='user_edit'),
    path('orderSubmit/', TireStoreLandingPageView.as_view(), name='orderSubmit'),
    path('howget/', HowGetOrderView.as_view(), name='howget'),
    path('usertire/', UserTire.as_view(), name='usertire'),
    path('about/', AboutView.as_view(), name='about'),
]