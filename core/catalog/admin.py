from django.contrib import admin
from catalog import models as m
 


@admin.register(m.Product)
class Product(admin.ModelAdmin):
    list_display = [field.name for field in m.Product._meta.fields]
    prepopulated_fields = {'slug': ('name',)}
    class Meta:
        model = m.Product


@admin.register(m.SirviceType)
class SirviceType(admin.ModelAdmin):
    list_display = [field.name for field in m.SirviceType._meta.fields]
    class Meta:
        model = m.SirviceType

@admin.register(m.VanType)
class VanType(admin.ModelAdmin):
    list_display = [field.name for field in m.VanType._meta.fields]
    class Meta:
        model = m.VanType


@admin.register(m.VanLength)
class VanLength(admin.ModelAdmin):
    list_display = [field.name for field in m.VanLength._meta.fields]
    class Meta:
        model = m.VanLength


# admin.site.register(m.HistoryOrder)
@admin.register(m.HistoryOrders)
class HistoryOrders(admin.ModelAdmin):
    list_display = [field.name for field in m.HistoryOrders._meta.fields]

    class Meta:
        model = m.HistoryOrders


@admin.register(m.User)
class User(admin.ModelAdmin):
    list_display = [field.name for field in m.User._meta.fields]

    class Meta:
        model = m.User
