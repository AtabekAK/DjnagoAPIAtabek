from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from import_export.admin import ExportMixin
from .models import Category, Product, Order


class ProductInline(admin.TabularInline):
    model = Product
    extra = 1
    fields = ('name', 'price', 'stock')
    readonly_fields = ('name',)


@admin.register(Category)
class CategoryAdmin(ExportMixin, SimpleHistoryAdmin):
    list_display = ('id', 'name', 'description', 'products_count')
    search_fields = ('name',)
    list_filter = ('name',)
    fieldsets = (
        ('Общая информация', {
            'fields': ('name', 'description')
        }),
    )
    inlines = [ProductInline]

    def products_count(self, obj):
        """Количество продуктов в категории."""
        return obj.products.count()
    products_count.short_description = 'Количество продуктов'


@admin.register(Product)
class ProductAdmin(ExportMixin, SimpleHistoryAdmin):
    """Настройки админки для модели Product."""
    list_display = ('id', 'name', 'price', 'stock', 'category', 'in_stock')
    search_fields = ('name', 'description')
    list_filter = ('price', 'category')
    fieldsets = (
        ('Основные параметры', {
            'fields': ('name', 'description', 'price', 'stock', 'category'),
        }),
    )
    readonly_fields = ('in_stock',)

    def in_stock(self, obj):
        """Проверяет, есть ли товар на складе."""
        return obj.stock > 0
    in_stock.boolean = True
    in_stock.short_description = 'В наличии'


@admin.register(Order)
class OrderAdmin(ExportMixin, SimpleHistoryAdmin):
    """Настройки админки для модели Order."""
    list_display = ('id', 'user', 'product', 'quantity', 'total_price')
    search_fields = ('user__username', 'product__name')
    list_filter = ('user',)
    fieldsets = (
        ('Детали заказа', {
            'fields': ('user', 'product', 'quantity', 'total_price')
        }),
    )
    readonly_fields = ('total_price',)
