from django.shortcuts import render
from django.views import View
from cart.models import Cart
from catalog.models import Product
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin

#Добавить в коризну 
class Likes(LoginRequiredMixin, View):
    def post(self, *args, **kwargs):
        blog_post_id = int(self.request.POST.get('blog_post_id'))
        try:
            value = int(self.request.POST.get('value'))
        except:
            value = 1
        user_id = int(self.request.POST.get('user_id'))
        url_from = self.request.POST.get("url_from")
        user_inst = get_user_model().objects.get(id=int(user_id))
        blog_post_inst = Product.objects.get(id=blog_post_id)
        try:
            blog_like_inst = Cart.objects.get(post = blog_post_inst, user = user_inst)
        except:
            block_like = Cart(post=blog_post_inst, \
                                user=user_inst, \
                                value = value
            )
            block_like.save()
        return redirect(url_from)


#Удалить из коризны 
class RemoveLike(LoginRequiredMixin, View):
    def post(self, *args, **kwargs):
        #берем из likes_blog.py
        user_id = int(self.request.POST.get('user_id'))
        blog_post_id = int(self.request.POST.get('blog_post_id'))
        url_from = self.request.POST.get('url_from')
        blog_like = Cart.objects.get(post_id = blog_post_id, user = user_id)
        blog_like.delete()
        return redirect(url_from)

#Добавить кол-во к товару
class AddValue(LoginRequiredMixin, View):
    def post(self, *args, **kwargs):
        #берем из likes_blog.py
        user_id = int(self.request.POST.get('user_id'))
        blog_post_id = int(self.request.POST.get('blog_post_id'))
        url_from = self.request.POST.get('url_from')
        blog_like = Cart.objects.get(post_id = blog_post_id, user = user_id)
        blog_like.value += 1
        blog_like.save()
        return redirect(url_from)

#Удалить кол-во к товару
class RemoveValue(LoginRequiredMixin, View):
    def post(self, *args, **kwargs):
        #берем из likes_blog.py
        user_id = int(self.request.POST.get('user_id'))
        blog_post_id = int(self.request.POST.get('blog_post_id'))
        url_from = self.request.POST.get('url_from')
        blog_like = Cart.objects.get(post_id = blog_post_id, user = user_id)
        blog_like.value -= 1
        if blog_like.value == 0:
            Cart.objects.get(post_id = blog_post_id, user = user_id).delete()
        else:
            blog_like.save()
        return redirect(url_from)
