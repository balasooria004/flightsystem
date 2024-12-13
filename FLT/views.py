from django.shortcuts import render, redirect
from .models import FLIGHT
from .forms import *

# Create your views here.
def home(request):
    return render(request, "home.html")
    
def add(request):
    
    if(request.method=='POST'):
        form = AddFlight(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show')
    
    else:
        form = AddFlight()
    
    return render(request, "add.html", {"form": form})
    
    
def show(request):
    data = FLIGHT.objects.all()
    return render(request, "show.html", {"data" : data})
    
def update(request):
    
    if(request.method=='POST'):
        form = GetFlightId(request.POST)
        if form.is_valid():
            flt_id = form.cleaned_data['flt_id']
            return redirect('updateid', id=flt_id)
    else:
        form = GetFlightId()
    
    return render(request, "get_id.html", {"form" : form})
    

def updateid(request, id):
    try:
        flight = FLIGHT.objects.get(pk=id)
    except FLIGHT.DoesNotExist:
        return render(request, "notfound.html", {'id': id})
    
    if(request.method=='POST'):
        form = UpdateFlight(request.POST, instance=flight)
        if form.is_valid():
            form.save()
            return redirect('show')
        
    else:
        form = UpdateFlight(instance=flight)
    
    return render(request, 'update.html', {'form' : form})
    
    
def delete(request):
    
    if(request.method=='POST'):
        form = GetFlightId(request.POST)
        if form.is_valid():
            flt_id = form.cleaned_data['flt_id']
            return redirect('deleteid', id=flt_id)
    else:
        form = GetFlightId()
    
    return render(request, "get_id.html", {"form" : form})
    

def deleteid(request, id):
    try:
        flight = FLIGHT.objects.get(pk=id)
    except FLIGHT.DoesNotExist:
        return render(request, "notfound.html", {'id': id})
    
    if(request.method=='POST'):
        flight.delete()
        return redirect('show')
        
    else:
        return render(request, 'delete.html', {'id' : id})
        

    
def search(request):
    
    if(request.method=='POST'):
        form = GetFlightId(request.POST)
        if form.is_valid():
            flt_id = form.cleaned_data['flt_id']
            return redirect('searchid', id=flt_id)
    else:
        form = GetFlightId()
    
    return render(request, "get_id.html", {"form" : form})
    

def searchid(request, id):
    try:
        flight = FLIGHT.objects.get(pk=id)
    except FLIGHT.DoesNotExist:
        return render(request, "notfound.html", {'id': id})
        
    return render(request, 'search.html', {'flight' : flight})