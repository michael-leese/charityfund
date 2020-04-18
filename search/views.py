from django.shortcuts import render, redirect, reverse, HttpResponseRedirect
from accounts.models import Org
from appeals.models import Appeal
from taggit.models import Tag

def do_search(request):
    '''
    Search Function
    '''
    previous = request.GET.get('next', '/')
    search = request.GET['search']
    if search is "":
        print("blank search")
        if previous is None:
            return redirect(reverse('index'))
        elif previous is not None:
            return HttpResponseRedirect(previous)
    elif search is not "":
        print(search)
        all_appeals = Appeal.objects.filter(tags__name__icontains=search).distinct()
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