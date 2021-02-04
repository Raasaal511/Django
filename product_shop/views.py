from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy

from .models import Product, Category
from .forms import ProductForm
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views import generic as gen


def view_products(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    context = {'products': products, 'categories': categories}

    return render(request, 'index.html', context)


def filter_by_category(request, category_id):
    filter_categories = Product.objects.filter(category=category_id)
    categories = Category.objects.all()
    current_categories = Category.objects.get(pk=category_id)
    context = {'filter_categories': filter_categories, 'categories': categories,
               'current_categories': current_categories}

    return render(request, 'filter_by_category.html', context)


class ProductView(gen.DetailView):
    model = Product
    template_name = 'detail_product.html'


class CreateProduct(gen.CreateView):
    template_name = 'create_post.html'
    form_class = ProductForm
    success_url = reverse_lazy('view_products')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_name'] = Category.objects.all()

        return context

    def form_valid(self, form):

        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()

        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, gen.UpdateView):
    model = Product
    template_name = 'create_post.html'
    fields = ['category', 'name', 'image', 'slug', 'description', 'price']

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()

        if self.request.user != kwargs['instance'].author:
            return self.handle_no_permission()

        return kwargs


class ProductDeleteView(LoginRequiredMixin, gen.DeleteView):
    model = Product
    success_url = '/'
    template_name = 'delete_product.html'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()

        if self.request.user != kwargs['instance'].author:
            return self.handle_no_permission()

        success_url = self.get_success_url()
        self.object.delete()

        return HttpResponseRedirect(success_url)