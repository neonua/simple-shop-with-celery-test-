from django.conf.urls import include, url
from django.contrib import admin
from shop_app.views import ProductList, CartList, CartAdd

urlpatterns = [

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', ProductList.as_view(), name='index'),
    url(r'^cart/$', CartList.as_view(), name='cart'),
    url(r'cart/add/(?P<id>\S+)', CartAdd.as_view(), name='cart_add')
]
