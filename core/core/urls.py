from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from catalog.views import RegisterView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('catalog.urls', namespace = 'snippets')),
    path('', include('cart.urls', namespace = 'category')),
    path('accounts/register/', RegisterView.as_view(), name='django_registration'),
    path('accounts/', include('django_registration.backends.activation.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


