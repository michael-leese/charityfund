from django.shortcuts import render
from appeals.models import Appeal
from taggit.models import Tag

def do_search(request):
    '''
    Search Fucntion
    '''
    all_appeals = Appeal.objects.filter(tags__name__icontains=request.GET['search'])
    print(all_appeals)
    return render(request, "all_appeals.html", {"all_appeals": all_appeals})