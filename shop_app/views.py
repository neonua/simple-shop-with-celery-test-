from django.shortcuts import render, redirect
from django.views.generic.list import ListView, View
from django.views.generic import TemplateView, DetailView, CreateView
from models import Product
from braces.views import JSONResponseMixin, AjaxResponseMixin
from django.http import Http404, HttpResponseRedirect, HttpResponseBadRequest
from django.views.decorators.http import require_http_methods


class ProductList(ListView):
    model = Product
    template_name = 'index.html'

    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super(ProductList, self).get_context_data()
        session = self.request.session.get('cart', {})
        self.request.session['cart'] = session
        return context


class CartList(TemplateView):

    template_name = 'cart.html'

    def get_context_data(self, **kwargs):
        context = super(CartList, self).get_context_data()
        cart = self.request.session['cart']
        context['cart_list'] = cart

        return context


class CheckID(CreateView):
    """
    Mixin for getting id current object
    """
    model = Product
    pk_url_kwarg = 'id'

    def get_object(self, *args, **kwargs):
        try:
            product = super(CheckID, self).get_object(*args, **kwargs)
        except:
            raise Http404()
        else:
            return product

    @require_http_methods(['POST'])
    def dispatch(self, request, *args, **kwargs):

        return super(CheckID, self).dispatch(request, *args, **kwargs)


class CartAdd(JSONResponseMixin, AjaxResponseMixin, CheckID):

    def post_ajax(self, request, *args, **kwargs):
        product = self.get_object()
        product_id = str(product.id)
        cart = self.request.session.get('cart', {})

        if product_id in cart:
            cart[product_id] += 1
        else:
            cart[product_id] = 1
        self.request.session['cart'] = cart

        return self.render_json_response(cart)

