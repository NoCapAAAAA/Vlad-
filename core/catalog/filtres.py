import django_filters
from catalog.models import Product


# Настройка фильтров
class SnippetFiter(django_filters.FilterSet):
    class Meta:
        model = Product
        paginate_by = 3
        # какие фильтры отображаются
        fields = ('typevan', 'lengthvan', 'servicetype',)
