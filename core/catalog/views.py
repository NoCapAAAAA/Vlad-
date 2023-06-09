from catalog.models import (Product, HistoryOrders)
from cart.models import Cart
from django.views.generic import TemplateView, FormView, ListView, DetailView, UpdateView, View
from django_registration.forms import RegistrationForm
from django.urls import reverse_lazy
from django.shortcuts import HttpResponseRedirect
from django.db.models import Sum
from catalog.filtres import SnippetFiter
from django.db.models import F
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, logout, authenticate, get_user_model
from .forms import RegisterForm, UserEditForm
import datetime
User = get_user_model()

#регстрация пользователя криспи форм кастом юзер
class RegisterView(FormView):
    template_name = 'registration/registration.html'
    form_class = RegisterForm
    success_url = reverse_lazy('snippets:main_page')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return HttpResponseRedirect(self.get_success_url())

#Редактирование данных в профиле пользователя
class UserEditView(LoginRequiredMixin,UpdateView):
    template_name = 'registration/user_edit.html'
    form_class = UserEditForm
    success_url = reverse_lazy('snippets:user_edit')
    
    def get_object(self):
        return self.request.user


#Главная страница, унаследован от ListView
class MainPageView(ListView):
    template_name = "home.html"
    #пагинация
    paginate_by = 9
    model = Product

    #Вывод данных на страницу
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product'] = Product.objects.filter().order_by('-pk')[:3]
        context['filter'] = SnippetFiter(self.request.GET, queryset=self.get_queryset())
        return context

    #Переопределнная функция класса ListView для совместной работы пагинатора и фильтра
    def get_queryset(self, **kwargs):
        search_results = SnippetFiter(self.request.GET, self.queryset)
        self.no_search_result = True if not search_results.qs else False
        return search_results.qs.distinct()
    
#Страница с корзиной, унаследован от TemplateView, используется с миксином - LoginRequiredMixin для перенаправления если пользователь не зарегестрирован
class DetailCartView(LoginRequiredMixin,TemplateView):
    template_name = "cart/detail.html"
    success_url = reverse_lazy('snippets:main_page')

    # Вывод данных на страниц
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart'] = Cart.objects.prefetch_related('post').filter(user = self.request.user)
        #переменная с сложной (сложная так-как используется класс F)агрегатной функцией для подсчета суммы товара
        context['sum'] = Product.objects.filter(cart__user = self.request.user).aggregate(total=Sum(F('price')* F('cart__value')))['total']
        return context
    #Оформление заказа
    def post(self, request):

        names = []
        data = dict(request.POST)
        name = Product.objects.filter(cart__user=self.request.user).values('name')
        value = Cart.objects.filter(user=self.request.user).values('value')
        price = Product.objects.filter(cart__user=self.request.user).aggregate(total=Sum(F('price') * F('cart__value')))
        for i, z in zip(name, value):
            names.append(f"{i['name']} - {z['value']} шт\n")
        #
        create = HistoryOrders.objects.create(
                                            user = self.request.user,
                                            c_companyname=data.get('c_companyname')[0],
                                            c_address=data.get('c_address')[0],
                                            price = price['total'],
                                            c_adressetc=data.get('c_adressetc')[0],
                                            c_order_notes=data.get('c_order_notes')[0],
                                            detail=", \n".join(names)
                                            )
        if create:
            carts = Cart.objects.prefetch_related('post').filter(user = self.request.user)
            carts.delete()
        return HttpResponseRedirect(self.success_url)


class DetailOrderView(DetailView):
    template_name = "profile/orderdetail.html"
    model = HistoryOrders
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['detail'] = HistoryOrders.objects.filter(pk=self.kwargs['pk'])
        print(context)
        return context


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "profile/user_profile.html"
    model = HistoryOrders
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lasthis'] = HistoryOrders.objects.filter().order_by('-pk')[:3]
        return context



#Страница с историей
class HistoryView(LoginRequiredMixin,TemplateView):
    template_name = "profile/history.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['history'] = HistoryOrders.objects.filter(user = self.request.user)
        return context

    
#Страница с историей
class ProfieDetailView(LoginRequiredMixin,TemplateView):
    template_name = "profile/profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profiledetail'] = HistoryOrder.objects.filter(user = self.request.user)
        return context

class ContactPageView(TemplateView):
    template_name = "contacts.html"

class LoginView(TemplateView):
    template_name = "account/login.html"
    success_url = reverse_lazy('snippets:main_page')
    def form_valid(self, form):
        # проверка валидности reCAPTCHA
        if self.request.recaptcha_is_valid:
            return HttpResponseRedirect(self.get_success_url())


class MainProduct(TemplateView):
    template_name = "main.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = Product.objects.filter(slug=self.kwargs['slug'])
        return context
    
class AboutView(TemplateView):
    template_name = "about.html"