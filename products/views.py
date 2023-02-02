from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

from common.views import TitleMixin

from .models import Basket, Product, ProductCategory

# def index(request):
#     context = {
#         'title': 'Store',
#         'is_promotion': True,
#     }
#     return render(request, 'products/index.html', context=context)


class IndexView(TitleMixin, TemplateView):
    template_name = 'products/index.html'
    title = 'Store'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data()
        context['is_promotion'] = True
        return context


# def products(request, category_id=None, page_number=1):
#     products = Product.objects.filter(category_id=category_id) if category_id else Product.objects.all()
#
#     paginator = Paginator(products, per_page=3)
#     products_paginator = paginator.page(page_number)
#
#     context = {
#         'title': 'Store - Каталог',
#         'categories': ProductCategory.objects.all(),
#         'products': products_paginator,
#     }
#     return render(request, 'products/products.html', context=context)


class ProductsListView(TitleMixin, ListView):
    model = Product
    template_name = 'products/products.html'
    title = 'Store - Каталог'
    paginate_by = 3

    def get_queryset(self):
        queryset = super(ProductsListView, self).get_queryset()
        category_id = self.kwargs.get('category_id')
        return queryset.filter(category_id=category_id) if category_id else queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductsListView, self).get_context_data()
        context['categories'] = ProductCategory.objects.all()
        return context


@login_required
def basket_add(request, product_id):
    Basket.create_or_update(product_id=product_id, user=request.user)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
