from django.shortcuts import render
from .forms import CarDetailsForm

def index(request):
    context = {}
    context['form'] = CarDetailsForm()
    if request.GET:
        make = request.GET['car_make']
        model = request.GET['car_model']
        year = request.GET['car_year']

        #API data fetch
        url = "http://localhost:8080/" + "carbonfootprint?car_make=" + make + "&car_model=" + model + "&car_year=" + year
        print(url)

        print(f"Make: {make}\nMode: {model}\nYear: {year}")
    return render(request, 'cf_app/index.html', context)