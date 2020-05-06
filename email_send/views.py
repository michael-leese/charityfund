from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from accounts.models import User, Org, UserProfile
from appeals.models import Appeal

@login_required
def emailOrg(request):
    '''
    This emails an organisation from a user about an appeal
    '''
    previous = request.GET.get('next', '/')
    if request.user.is_authenticated:
        appeal = Appeal.objects.get(id=request.GET.get('id'))
        org = Org.objects.get(id=appeal.id)
        user = User.objects.get(user=request.user)
        userprofile = UserProfile.objects.get(user=request.user)
        ownerOrg = Org.objects.filter(user=request.user)
        creator = appeal.author.id
        owner = False
        if creator is request.user.id:
            owner = True
            return render(request, 'email.html', {'appeal': appeal, 'org': org, 'owner': owner, 'userprofile': userprofile})
        return render(request, 'email.html', {'appeal': appeal, 'org': org, 'user':user, 'owner': owner, 'userprofile': userprofile})
    else:
        return HttpResponseRedirect(previous)