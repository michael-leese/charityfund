from django.shortcuts import render
from accounts.models import Org
from appeals.models import Appeal
from taggit.models import Tag

def do_search(request):
    '''
    Search Function
    '''
    all_appeals = Appeal.objects.filter(tags__name__icontains=request.GET['search'])
    active = "active"
    if request.user.is_authenticated:
        org = Org.objects.filter(user=request.user)
        if org:
            hasOrg = True
            return render(request, 'all_appeals.html', {'all_appeals': all_appeals, 'hasOrg': hasOrg, 'active6': active}) 
        else:
            hasOrg = False
            return render(request, 'all_appeals.html', {'all_appeals': all_appeals, 'hasOrg': hasOrg, 'active6': active})
    else:
        hasOrg = False
        return render(request, 'all_appeals.html', {'all_appeals': all_appeals, 'hasOrg': hasOrg, 'active6': active})