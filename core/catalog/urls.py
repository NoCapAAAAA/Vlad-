from django.contrib import admin
from django.urls import path, include
from catalog.views import (MainPageView, 
                            ContactPageView, RegisterView, ProfileView, DetailCartView,
                         HistoryOrders, HistoryView, ProfieDetailView, UserEditView, MainProduct,
                         AboutView, DetailOrderView)
from . import views as v 

app_name = 'snippets'

urlpatterns = [
    path('', MainPageView.as_view(), name='main_page'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('catalog/<slug:slug>/', MainProduct.as_view(), name='main'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('cart/', DetailCartView.as_view(), name='cart_detail'),
    path('history/', HistoryView.as_view(), name='history'),
    path('profiledetail/', ProfieDetailView.as_view(), name='profiledetail'),
    path('user_edit/', UserEditView.as_view(), name='user_edit'),
    path('about/', AboutView.as_view(), name='about'),
    path('history/<int:pk>/', DetailOrderView.as_view(), name='detailord'),
]