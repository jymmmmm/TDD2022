from django.shortcuts import render,redirect
from django.http import HttpResponse
from lists.models import Item, List

# Create your views here.
def home_page(request):
    # item=Item()
    # item.text=request.POST.get('item_text','')
    # item.save()
    #
    # return render(request, 'home.html',{
    #     'new_item_text': item.text
    #     })


    return render(request,'home.html')


def view_list(request, list_id):
    list_=List.objects.get(id=list_id)
    return render(request,'list.html',{'list':list_})

def new_list(request):
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['item_text'],list=list_)
    return redirect(f'/lists/{list_.id}/')

def add_item(request,list_id):
    list_=List.objects.get(id=list_id)
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect(f'/lists/{list_.id}/')