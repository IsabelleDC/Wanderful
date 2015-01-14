from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, render_to_response, redirect
from wander.forms import EmailUserCreationForm, LocationForm, CategoryForm
from wander.models import Location, Category
# Create your views here.



# def test(request):
#     locations = Location.objects.all()
#     for location in locations :
#         country = location.country
#         city=location.city
#         street=location.street
#         streetnum=location.streetnum
#         address='{}, {}, {}, {}'.format(country, city, street, streetnum)
#
#     return render (request, 'test.html', {'address':address})
def test(request):
    return render(request, 'test.html')


def home(request):
    return render(request, 'home.html')

def profile(request):
    return render(request, 'profile.html')

def register(request):
    if request.method == 'POST':
        form = EmailUserCreationForm(request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password1"]
            user = form.save()
            user.email_user("Welcome!", "Thank you for signing up for our website.")
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect("profile")
    else:
        form = EmailUserCreationForm()

    return render(request, "registration/register.html", {
        'form': form,
    })

@login_required()
def location_new(request):
    if request.method =='POST':
        form = LocationForm(request.POST)
        if form.is_valid():
            if form.save():
                return redirect("/categories")
    else:
        form = LocationForm()

    data = {'form': form}
    return render(request, 'location_new.html', data)

@login_required()
def locations(request, category_id):
    locations = Location.objects.filter(categories__id=category_id)
    return render(request, 'locations.html', {'locations': locations})

@login_required()
def category_new(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            name = request.POST["name"]
            Category.objects.create(user=request.user, name =name)
            return redirect("/categories")
    else:
        form = CategoryForm()

    data = {'form': form}
    return render(request, 'category_new.html', data)

@login_required()
def categories(request):
    categories= Category.objects.filter(user=request.user)
    return render(request, 'categories.html', {'categories':categories})

def map(request, location_id):
    location = Location.objects.filter(id=location_id)
    for place in location:
        country = place.country
        city = place.city
        street = place.street
        streetnum = place.streetnum
        address ='{}, {}, {}, {}'.format(country, city, street, streetnum)

    return render (request, 'map.html', {'address': address})


