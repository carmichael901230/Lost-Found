from django.shortcuts import render, get_object_or_404, redirect
from .models import Item
from .forms import ShowItemForms, RegisterItemForms, SearchItemForms
from datetime import date, datetime
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def show_item_view(request, item_id):
    if request.method=="POST":
        item = get_object_or_404(Item, id=item_id)
        pre_retrieved_stat = item.retrieved
        form = ShowItemForms(request.POST, request.FILES, instance=item)
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

@login_required
def register_item_view(request):
    if request.method=="POST":
        form = RegisterItemForms(request.POST, request.FILES)
        if form.is_valid():
            new_item = form.save(commit=False)
            # handle empty 'date' filed
            if new_item.date is None:       
                new_item.date = date.today()
            new_item.register_user = request.user
            new_item.save()
            return redirect("/")        # TODO
    else:
        form = RegisterItemForms()
    context = {
        'form': form
    }
    return render(request, 'register_item/register_item.html', context)

@login_required
def search_item_view(request):
    if request.method=="GET":
        form = SearchItemForms(request.GET, initial={'retrieved': False, 'orderBy':None})
        if len(request.GET) == 0:
            context = {
                'form': form
            }
            return render(request, 'search_item/search_item.html', context)
        else:
            if form.is_valid():
                queryset = form.cleaned_data
                result = Item.objects.filter(category__exact=queryset['category'])
                result = result.filter(retrieved__exact=(True if queryset['retrieved']=='True' else False))
                if queryset['building'] and queryset['building'].pk!=42:
                    result = result.filter(building__exact=queryset['building'])
                if queryset['room']:
                    result = result.filter(room__iexact=queryset['room'])
                if queryset['from_date']:
                    result = result.filter(date__gte=queryset['from_date'])
                if queryset['to_date']:
                    result = result.filter(date__lte=queryset['to_date'])
                if queryset['color']:
                    result = result.filter(color__exact=queryset['color'])
                if queryset['orderBy']:
                    result = result.order_by(queryset['orderBy'])
                print(result)

                context = {
                    'object_list':result,
                    'form':form
                }
                return render(request, 'search_item/search_result.html', context)

