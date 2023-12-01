from django.shortcuts import render, redirect
from .models import Item
from .forms import ItemForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

def index(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'food/food.html', context)


class IndexClassView(ListView): 
    model = Item
    template_name = 'food/food.html'
    context_object_name = 'item_list'


def detail(request, item_slug):
    items = Item.objects.get(slug=item_slug)
    context = {
        'items': items
    }
    return render(request, 'food/detail.html', context)

class DetailItem(DetailView):
    model = Item
    template_name = 'food/detail.html'



def create_item(request):
    form = ItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'food/create_item.html', {'form': form})


class CreateItem(CreateView):
    model = Item
    fields = ['name', 'description', 'price', 'slug', 'image']
    template_name = 'food/create_item.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    

def update_item(request, item_slug):
    items = Item.objects.get(slug=item_slug)
    form = ItemForm(request.POST or None, instance=items)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'food/create_item.html', {'form': form, 'items':items})

def delete_item(request, item_slug):
    items = Item.objects.get(slug=item_slug)
    if request.method == 'POST':
        items.delete()
        return redirect('index')
    return render(request, 'food/delete_item.html', {'items':items})
