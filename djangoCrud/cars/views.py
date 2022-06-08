from django.shortcuts import render, redirect
from .models import Car
from .forms import Create
from django.http import HttpResponse


def index(request):
    stock = Car.objects.all()
    return render(request, 'show.html', {'stock': stock})

def upload(request):
    upload = Create()
    if request.method == 'POST':
        upload = Create(request.POST)
        if upload.is_valid():
            upload.save()
            return redirect('index')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'index'}}">reload</a>""")
    else:
        return render(request, 'upload_form.html', {'upload_form':upload})

def update_Car(request, Car_id):
    Car_id = int(Car_id)
    try:
        Car_sel = Car.objects.get(id = Car_id)
    except Car.DoesNotExist:
        return redirect('index')
    Car_form = Create(request.POST or None, instance = Car_sel)
    if Car_form.is_valid():
       Car_form.save()
       return redirect('index')
    return render(request, 'upload_form.html', {'upload_form':Car_form})

def delete_Car(request, Car_id):
    Car_id = int(Car_id)
    try:
        Car_sel = Car.objects.get(id = Car_id)
    except Car.DoesNotExist:
        return redirect('index')
    Car_sel.delete()
    return redirect('index')