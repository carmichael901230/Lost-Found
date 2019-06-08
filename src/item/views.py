from django.shortcuts import render, get_object_or_404, redirect
from .models import Item
from .forms import ShowItemForms, RegisterItemForms
from datetime import date, datetime

# Create your views here.
def show_item_view(request, item_id):
    if request.method=="POST":
        item = get_object_or_404(Item, id=item_id)
        pre_retrieved_stat = item.retrieved
        form = ShowItemForms(request.POST, instance=item)
        if form.is_valid():
            new_item = form.save(commit=False)
            if new_item.retrieved and not pre_retrieved_stat:
                new_item.retrieve_user=request.user
                new_item.retrieved_date=date.today()
            new_item.save()
            return redirect('/')        # TODO
    else:
        item = get_object_or_404(Item, id=item_id)
        form = ShowItemForms(instance=item)
        context = {
            'item':item,
            'form':form
        }
        return render(request, 'search_item/show_item.html', context)

def RegisterItemView(request):
    if request.method=="POST":
        form = RegisterItemForms(request.POST)
        if form.is_valid():
            new_item = form.save(commit=False)
            new_item.register_user = request.user
            new_item.save()
            return redirect("/")        # TODO
    else:
        form = RegisterItemForms()
        context = {
            'form': form
        }
        return render(request, 'register_item/register_item.html', context)