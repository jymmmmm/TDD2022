from django.shortcuts import render,redirect
from django.http import HttpResponse
from lists.models import Item

# Create your views here.
def home_page(request):
    # item=Item()
    # item.text=request.POST.get('item_text','')
    # item.save()
    #
    # return render(request, 'home.html',{
    #     'new_item_text': item.text
    #     })

    if request.method =='POST':
        new_item_text=request.POST['item_text']
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/')

    items=Item.objects.all()

    return render(request,'home.html',{'items':items})
