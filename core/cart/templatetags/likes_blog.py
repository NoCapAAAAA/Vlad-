from django import template
from cart.models import Cart

register = template.Library()

#для передачи данных через jinja в функцию post для обработки запроса
@register.simple_tag(takes_context=True)
def is_liked(context, blog_post_id  ):
    request = context['request']
    print(request)
    try:
        blog_likes = Cart.objects.get(post_id = blog_post_id, user=request.user.id).like
    except Exception as err:
        print(err)
        blog_likes = False
        return blog_likes
        
#для передачи данных через jinja в функцию post для обработки запроса
@register.simple_tag(takes_context=True)
def blog_likes_id(context, blog_post_id):
    request = context['request']
    print(request)
    return Cart.objects.get(post_id =blog_post_id, user=request.user.id)