from django.shortcuts import render, HttpResponse, redirect, reverse, get_object_or_404, HttpResponseRedirect
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from accounts.models import User, Org, UserProfile
from appeals.models import Appeal
from payments.models import Order
from taggit.models import Tag
from appeals.forms import AppealForm
from django.utils import timezone
from appeals.serializers import AppealsSerializer
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

#Returns the create appeal page
@login_required
def create_appeal(request):
    """
    Ensures create appeal form is valid and pushes data into
    a new appeal, then redirects to appeals list page
    """
    if request.user.is_authenticated:
        active = "active"
        org = Org.objects.filter(user=request.user)
        userprofile = UserProfile.objects.get(user=request.user)
        if org:
            hasOrg = True
            if request.method == "POST":
                form = AppealForm(request.POST, request.FILES)
                if form.is_valid():
                    appeal = form.save(commit=False)
                    appeal.author = request.user
                    appeal.org = Org.objects.get(user=request.user)
                    appeal.created_date = timezone.now()
                    appeal.save()
                    form.save_m2m()
                    messages.success(request, "Congratulations you have added " + appeal.title)
                    return redirect('showallappeals')
            else:
                form = AppealForm()
                return render(request, 'create_appeal.html', {'form': form,'hasOrg': hasOrg, 'org': org, 'active2': active, 'userprofile': userprofile})
        else:
            hasOrg = False
            messages.success(request, "You must create an organisation before setting up an appeal")
            return render(request, 'index.html', {'hasOrg': hasOrg, 'active1': active, 'userprofile': userprofile})
    else:
        return redirect(reverse('index'))

#returns the edit appeal page
@login_required
def edit_appeal(request):
    """
    Edit an appeal if you are the owner of the appeal
    """
    if request.user.is_authenticated:
        previous = request.GET.get('next', '/')
        instance = get_object_or_404(Appeal, id=request.GET.get('id'))
        org = Org.objects.filter(user=request.user)
        userprofile = UserProfile.objects.get(user=request.user)
        if request.method == "POST":
            form = AppealForm(request.POST, request.FILES)
            if form.is_valid():
                appeal = form.save(commit=False)
                appeal.author = request.user
                appeal.org = Org.objects.get(user=request.user)
                appeal.created_date = timezone.now()
                if appeal.image:
                    if appeal.image != instance.image:
                        instance.image.delete(save=True)
                        appeal.image = request.FILES["image"]
                else:
                    appeal.image = instance.image
                appeal.id = instance.id
                appeal.save(force_update=True)
                form.save_m2m()
                messages.success(request, "Congratulations you have edited appeal called " + instance.title)
                return HttpResponseRedirect(previous + "&next=/accounts/viewmyorgs_appeals/")
            else:
                messages.error(request, "Unable to edit at this time.")
                return render(request, 'edit_appeal.html', {'form': form, 'previous': previous, 'instance': instance, 'userprofile': userprofile})
        else:
            form = AppealForm(instance=instance)
            return render(request, 'edit_appeal.html', {'form': form, 'previous': previous, 'instance': instance, 'userprofile': userprofile})
    else:
        active = "active"
        return render(request, 'index.html', {'active1': active})

#returns the all appeals page
def show_all_appeals(request):
    """
    Gets all the appeals available
    """
    filterType = request.GET.get('filter')
    if filterType is None:
        filterType = '-created_date'
    orders = Order.objects.all().order_by('-created_date') 
    active = "active"
    if request.user.is_authenticated:
        logged_in = True
        userprofile = UserProfile.objects.get(user=request.user)
        appeals = Appeal.objects.all().order_by(filterType)
        page = request.GET.get('page', 1)
        paginator = Paginator(appeals, 6)
        try:
            all_appeals = paginator.page(page)
        except PageNotAnInteger:
            all_appeals = paginator.page(1)
        except EmptyPage:
            all_appeals = paginator.page(paginator.num_pages)
        org = Org.objects.filter(user=request.user)
        if org:
            hasOrg = True
            return render(request, 'all_appeals.html', {'all_appeals': all_appeals, 'orders': orders, 'hasOrg': hasOrg, 
                                                        'active6': active, 'logged_in': logged_in, 'userprofile': userprofile}) 
        else:
            hasOrg = False
            return render(request, 'all_appeals.html', {'all_appeals': all_appeals, 'orders': orders, 'hasOrg': hasOrg, 
                                                        'active6': active, 'logged_in': logged_in, 'userprofile': userprofile})
    else:
        all_appeals = Appeal.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')[:6]
        hasOrg = False
        return render(request, 'all_appeals.html', {'all_appeals': all_appeals, 'orders': orders, 'hasOrg': hasOrg, 'active6': active})

#returns the appeal page
@login_required
def single_appeal(request):
    """
    Gets the single appeal clicked on by a user
    """
    if request.user.is_authenticated:
        previous = request.GET.get('next', '/')
        owner = False
        userprofile = UserProfile.objects.get(user=request.user)
        org = Org.objects.filter(user=request.user)
        appeal = Appeal.objects.get(id=request.GET.get('id'))
        creator = appeal.author.id
        if creator is request.user.id:
            owner = True
        orders = Order.objects.filter(appeal=appeal.id).order_by('-created_date')
        calcPercent = progress_perc(appeal.money_raised, appeal.money_target)
        if org:
            hasOrg = True
            return render(request, 'single_appeal.html', {'appeal': appeal, 'orders': orders, 'hasOrg': hasOrg, 
                                                          'calcPercent': calcPercent, 'owner': owner, 'previous': previous, 
                                                          'userprofile': userprofile}) 
        else:
            hasOrg = False
            return render(request, 'single_appeal.html', {'appeal': appeal, 'orders': orders,  'hasOrg': hasOrg, 
                                                          'calcPercent': calcPercent, 'owner': owner, 'previous': previous, 
                                                          'userprofile': userprofile}) 
    else:
        return redirect(reverse('index'))

#Return the percentage raised of target figure
def progress_perc(raised, target):
    """
    Calculates the percentage of the total
    """
    if raised is None: 
        raised = 0
    if target is None or target == 0:
        return 0
    percentage = int((raised/target)*100)
    return percentage

#Returns a json object for the ajax call
class JSONResponse(HttpResponse):
    """
    returns the json object to the ajax call
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

#Returns all appeal map data
def all_appeal_map_data(request):
    """
    returns all the appeals data for maps api
    """
    if request.method == 'GET':
        all_appeals = Appeal.objects.all()
        serializer = AppealsSerializer(all_appeals, many=True)
        return JSONResponse(serializer.data)

#Returns the map data for the users organisation
def my_appeal_map_data(request):
    """
    returns all the users appeals data for maps api
    """
    if request.method == 'GET':
        all_appeals = Appeal.objects.filter(author=request.user)
        serializer = AppealsSerializer(all_appeals, many=True)
        return JSONResponse(serializer.data)
