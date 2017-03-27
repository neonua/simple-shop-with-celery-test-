from django.shortcuts import render, redirect
from django.views.generic.list import ListView, View
from django.views.generic import TemplateView, DetailView, CreateView
from models import Product
from braces.views import JSONResponseMixin, AjaxResponseMixin
from django.views.decorators.http import require_http_methods
from .mixins import SessionGet


class ProductList(SessionGet, ListView):
    model = Product
    template_name = 'index.html'

    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super(ProductList, self).get_context_data()
        return context


class CartList(SessionGet, TemplateView):

    template_name = 'cart.html'

    def get_context_data(self, **kwargs):
        context = super(CartList, self).get_context_data()
        context['cart_list'] = self.cart
        return context


class CartAdd(SessionGet, JSONResponseMixin, AjaxResponseMixin, DetailView):

    model = Product
    pk_url_kwarg = 'id'

    def post_ajax(self, request, *args, **kwargs):
        product = self.get_object()
        product_id = str(product.id)

        if product_id in self.cart:
            self.cart[product_id] += 1
        else:
            self.cart[product_id] = 1
        self.request.session['cart'] = self.cart

        return self.render_json_response(self.cart)

    # @require_http_methods(['POST'])
    # def dispatch(self, request, *args, **kwargs):
    #
    #     return super(CartAdd, self).dispatch(request, *args, **kwargs)
