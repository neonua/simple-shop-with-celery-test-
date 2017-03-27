from django import template
from shop_app.models import Product


register = template.Library()


@register.filter(name='product_name')
def product_name(id):
    name = Product.objects.get(id=id).name
    return name


@register.filter(name='product_sum')
def product_sum(id, count):
    product_price = Product.objects.get(id=id).price
    sum = float(product_price) * count
    return sum
