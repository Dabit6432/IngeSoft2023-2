from django.shortcuts import render, HttpResponse
from .models import* #Importamos todos los modelos

# Create your views here.
def index(request):

    grupo1 = Estudiante.objects.filter(grupo=1) #Consulta que nos da la inf de los estudiantes con grupo 1
    grupo4 = Estudiante.objects.filter(grupo=4) #Consulta que nos da la inf de los estudiantes con grupo 4
    edadEq = Estudiante.objects.filter(edad=20)
    edadEq1 = Estudiante.objects.filter(edad=21)
    edadEq2 = Estudiante.objects.filter(edad=22)
    edadEq3 = Estudiante.objects.filter(edad=23)
    edadEq4 = Estudiante.objects.filter(edad=24)
    edadEq5 = Estudiante.objects.filter(edad=25)
    apellidosEq = Estudiante.objects.filter(apellidos="Mendoza")
    apellidosEq1 = Estudiante.objects.filter(apellidos="Landaverde")
    apellidosEq2 = Estudiante.objects.filter(apellidos="Garces")
    apellidosEq3 = Estudiante.objects.filter(apellidos="Gómez")
    todos = Estudiante.objects.all()
    grupo3Edad = Estudiante.objects.filter(grupo=3,edad=22)

    
    #return HttpResponse('Hola mundo :)')
    return render(request, 'index.html', {'grupo1':grupo1, 'grupo4':grupo4, 'apellidosEq':apellidosEq, 'apellidosEq1':apellidosEq1, 'apellidosEq2':apellidosEq2, 'apellidosEq3':apellidosEq3, 'edadEq':edadEq, 'edadEq1':edadEq1, 'edadEq2':edadEq2, 'edadEq3':edadEq3, 'edadEq4':edadEq4, 'edadEq5':edadEq5,'grupo3Edad':grupo3Edad, 'todos':todos})
