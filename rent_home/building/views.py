from django.http import HttpRequest
from django.shortcuts import redirect, render, get_object_or_404, get_list_or_404
from .models import Address, Building
from .forms import AddressForm, BuildingForm, FilterForm
from django.contrib.messages import success
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET
# Create your views here.

@login_required
def add_new_building(request:HttpRequest):
    if request.method == 'POST':
        ad_form = AddressForm(request.POST)
        bu_form = BuildingForm(data=request.POST, files=request.FILES)

        if ad_form.is_valid() and bu_form.is_valid():
            address:Address = ad_form.save(commit=True)

            building:Building = bu_form.save(commit=False)
            building.user = request.user
            building.address = address
            building.save()

            success(request, 'The building added successfully. Please wait to verify your building', 'alert alert-success my-3', False)
            return redirect('account:dashboard')
    else:
        ad_form = AddressForm()
        bu_form = BuildingForm()

    context = {'ad_form':ad_form, 'bu_form':bu_form}
    return render(request, 'building/add_new_building.html', context)

def the_buildings(request:HttpRequest):
    if request.method == 'POST':
        form = FilterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data  
            
            cards = Building.objects.filter(
                address__city=cd['city'], 
                address__state=cd['state'],
                address__street=cd['street'],
                building_type=cd['building_type'],
                price__gt=cd['price']
            )
            print(cards)
            context = {'cards':cards, 'form':form}
            return render(request, 'building/the_buildings.html', context)


    form = FilterForm()
    cards = Building.objects.filter(status=True).all()

    context = {'cards':cards, 'form':form}
    return render(request, 'building/the_buildings.html', context)

@require_GET
def the_buildings_(request:HttpRequest):
    if request.method == 'GET':
        form = FilterForm(request.GET)
        print(request.GET)
    else:
        form = FilterForm()
    context = {'form':form}
    return render(request, 'building/the_buildings.html')


def detail(request:HttpRequest, pk):
    building = get_object_or_404(Building, pk=pk)
    context = {'building': building}
    return render(request, 'building/detail.html', context)