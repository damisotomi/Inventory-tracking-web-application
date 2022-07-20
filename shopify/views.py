from email import message
from pyexpat.errors import messages
import re
from django.shortcuts import redirect, render,HttpResponse
from django.urls import reverse_lazy
from django.views import generic
from django.db.models import ProtectedError
from shopify.models import Group, ProductInstance, Warehouse, Product

# Create your views here.


def index(request):
    num_of_visits=request.session.get('num_of_visits',0)
    request.session['num_of_visits']=num_of_visits+1
    return render(request,'index.html',{'num_of_visits':num_of_visits})

class WarehouseListView(generic.ListView):
    model=Warehouse
    template_name='warehouse_list.html'
    context_object_name='warehouses'
    paginate_by=5

class WarehouseDetailView(generic.DetailView):
    model=Warehouse
    template_name='warehouse_detail.html'
    context_object_name='warehouse'

class WarehouseCreateView(generic.CreateView):
    model=Warehouse
    template_name='warehouse_form.html'
    fields=['name','location']

class WarehouseUpdateView(generic.UpdateView):
    model=Warehouse
    template_name='warehouse_update_form.html'
    fields=['name','location']

class WarehouseDeleteView(generic.DeleteView):
    model=Warehouse
    template_name='warehouse_delete_form.html'
    success_url=reverse_lazy('warehouses')
    context_object_name='warehouse'

class ProductListView(generic.ListView):
    model=Product
    template_name='product_list.html'
    context_object_name='products'
    paginate_by=5

class ProductDetailView(generic.DetailView):
    model=Product
    template_name='product_detail.html'
    context_object_name='product'

class ProductCreateView(generic.CreateView):
    model=Product
    template_name='product_form.html'
    fields=['name','description','group']

class ProductUpdateView(generic.UpdateView):
    model=Product
    template_name='product_update_form.html'
    fields=['name','description','group']

class ProductDeleteView(generic.DeleteView):
    model=Product
    template_name='product_delete_form.html'
    success_url=reverse_lazy('products')
    context_object_name='product'

class ProductInstanceListView(generic.ListView):
    model=ProductInstance
    template_name='product_instance_list.html'
    context_object_name='productinstances'
    paginate_by =5

class ProductInstanceDetailView(generic.DetailView):
    model=ProductInstance
    template_name='product_instance_detail.html'
    context_object_name='productinstance'

class ProductInstanceCreateView(generic.CreateView):
    model=ProductInstance
    template_name='product_instance_form.html'
    fields=['product','quantity','warehouse']

class ProductInstanceUpdateView(generic.UpdateView):
    model=ProductInstance
    template_name='product_instance_update_form.html'
    fields=['product','quantity','warehouse']

class ProductInstanceDeleteView(generic.DeleteView):
    model=ProductInstance
    template_name='product_instance_delete_form.html'
    success_url=reverse_lazy('product_instances')
    context_object_name='productinstance'

class GroupCreateView(generic.CreateView):
    model=Group
    template_name='group_form.html'
    fields=['name']
    success_url=reverse_lazy('groups')

class GroupUpdateView(generic.UpdateView):
    model=Group
    template_name='group_update_form.html'
    fields=['name']

class GroupDeleteView(generic.DeleteView):
    model=Group
    template_name='group_delete_form.html'
    success_url =reverse_lazy('groups')

class GroupListView(generic.ListView):
    model=Group
    template_name='group_list.html'
    context_object_name='groups'
    paginate_by =5

class GroupDetailView(generic.DetailView):
    model=Group
    template_name='group_detail.html'
    context_object_name='group'

def overview_manual(request):
    return render(request,'overview_manual.html')

def product_manual(request):
    return render(request,'product_manual.html')

def transaction_manual(request):
    return render(request,'transaction_manual.html')

def warehouse_manual(request):
    return render(request,'warehouse_manual.html')

def group_manual(request):
    return render(request,'group_manual.html')