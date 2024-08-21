from django.shortcuts import render, redirect
from .models import Persona
from .form import PersonaForm

# Create your views here.

def Registrar(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Listar')
    else: 
        form = PersonaForm()
    return render(request,'registrar.html',{'form':form})

def Listar(request):
    personas = Persona.objects.all()
    return render(request,'listar.html',{'personas':personas})