from django.shortcuts import render, get_object_or_404
from .models import Item
from .forms import ShowItemForms

# Create your views here.
def show_item_view(request, item_id):
    if request.method=="POST":
        pass
    else:
        item = get_object_or_404(Item, pk=item_id)
        form = ShowItemForms(instance=item)
        context = {
            'item':item,
            'form':form
        }
        return render(request, 'item/search_item/show_item.html', context)