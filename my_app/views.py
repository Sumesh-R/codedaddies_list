from django.shortcuts import render

# Create your views here.
def home(request):
    context = {
        
    }
    return render(request, 'base.html', context)

def new_search(request):
    search = request.POST['search']
    context = {
        "search":search,
    }
    return render(request, 'my_app/new_search.html',context)