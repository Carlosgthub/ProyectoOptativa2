from django.shortcuts import render, redirect, reverse
from django.views import generic
from django.urls import reverse_lazy

from .models import Carrera, Alumno, Docente, Materia, Grupo
from .forms import AlumnoForm, CarreraForm, MateriaForm, DocenteForm, GrupoForm

from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.http import HttpResponseRedirect


# Create your views here.
@login_required
def inicio(request):
    return render(request, 'inicio.html', {})

class ListaAlumnos(LoginRequiredMixin,generic.ListView):
    model = Alumno
    template_name = "alumnos.html"

class AlumnoDetalle(LoginRequiredMixin,generic.DetailView):
    model = Alumno
    template_name = "alumnodetalle.html"
    success_url=reverse_lazy('alumnos')

class EliminarAlumno(LoginRequiredMixin,SuccessMessageMixin,generic.DeleteView):
    model = Alumno
    template_name = "eliminarAlumno.html"
    success_message = "El alumno %(nombre)s %(apellido)s ha sido borrado"

    def get_context_data(self, **kwargs):
        context_data = super(EliminarAlumno, self).get_context_data(**kwargs)
        pk=self.kwargs.get('pk')
        alumnos=Alumno.objects.get(id=int(pk))
        return context_data

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.warning(self.request, self.success_message % obj.__dict__)
        return super(EliminarAlumno, self).delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('alumnos')

class RegistrarAlumno(LoginRequiredMixin,SuccessMessageMixin,generic.CreateView):
    model = Alumno
    template_name = "registrar.html"
    form_class=AlumnoForm
    success_message = "El alumno %(nombre)s %(apellido)s ha sido registrado"
    success_url=reverse_lazy('alumnos')

class ModificarAlumno(LoginRequiredMixin,SuccessMessageMixin,generic.UpdateView):
    model = Alumno
    template_name = "modificar.html"
    form_class=AlumnoForm
    success_message = "El alumno %(nombre)s %(apellido)s ha sido modificado"
    success_url=reverse_lazy('alumnos')

# ----------------------------------------------------------------

class ListaCarreras(LoginRequiredMixin,generic.ListView):
    model = Carrera
    template_name = "carreras.html"

class EliminarCarrera(LoginRequiredMixin,SuccessMessageMixin,generic.DeleteView):
    model = Carrera
    template_name = "eliminarCarrera.html"
    success_message = "La carrera %(nombre)s ha sido borrada"

    def get_context_data(self, **kwargs):
        context_data = super(EliminarCarrera, self).get_context_data(**kwargs)
        pk=self.kwargs.get('pk')
        carreras=Carrera.objects.get(id=int(pk))
        return context_data

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.warning(self.request, self.success_message % obj.__dict__)
        return super(EliminarCarrera, self).delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('carreras')

class RegistrarCarrera(LoginRequiredMixin,SuccessMessageMixin,generic.CreateView):
    model = Carrera
    template_name = "registrar.html"
    form_class=CarreraForm
    success_message = "La carrera %(nombre)s ha sido agregada"
    success_url=reverse_lazy('carreras')

class ModificarCarrera(LoginRequiredMixin,SuccessMessageMixin,generic.UpdateView):
    model = Carrera
    template_name = "modificar.html"
    form_class=CarreraForm
    success_message = "La carrera %(nombre)s ha sido modificada"
    success_url=reverse_lazy('carreras')

# ----------------------------------------------------------------

class ListaMaterias(LoginRequiredMixin,generic.ListView):
    model = Materia
    template_name = "materias.html"

class EliminarMateria(LoginRequiredMixin,SuccessMessageMixin,generic.DeleteView):
    model = Materia
    template_name = "eliminarMateria.html"
    success_message = "La materia %(nombre)s ha sido borrada"

    def get_context_data(self, **kwargs):
        context_data = super(EliminarMateria, self).get_context_data(**kwargs)
        pk=self.kwargs.get('pk')
        materias=Materia.objects.get(id=int(pk))
        return context_data

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.warning(self.request, self.success_message % obj.__dict__)
        return super(EliminarMateria, self).delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('Materias')

class RegistrarMateria(LoginRequiredMixin,SuccessMessageMixin,generic.CreateView):
    model = Materia
    template_name = "registrar.html"
    form_class=MateriaForm
    success_message = "La materia %(nombre)s ha sido agregada"
    success_url=reverse_lazy('Materias')

class ModificarMateria(LoginRequiredMixin,SuccessMessageMixin,generic.UpdateView):
    model = Materia
    template_name = "modificar.html"
    form_class=MateriaForm
    success_message = "La materia %(nombre)s ha sido modificada"
    success_url=reverse_lazy('Materias')

# ----------------------------------------------------------------

class ListaDocentes(LoginRequiredMixin,generic.ListView):
    model = Docente
    template_name = "docentes.html"

class DocenteDetalle(LoginRequiredMixin,generic.DetailView):
    model = Docente
    template_name = "docentedetalle.html"
    success_url=reverse_lazy('docentes')

class EliminarDocente(LoginRequiredMixin,SuccessMessageMixin,generic.DeleteView):
    model = Docente
    template_name = "eliminarDocente.html"
    success_message = "El docente %(nombre)s %(apellido)s ha sido borrado"

    def get_context_data(self, **kwargs):
        context_data = super(EliminarDocente, self).get_context_data(**kwargs)
        pk=self.kwargs.get('pk')
        docentes=Docente.objects.get(id=int(pk))
        return context_data

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.warning(self.request, self.success_message % obj.__dict__)
        return super(EliminarDocente, self).delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('Docentes')

class RegistrarDocente(LoginRequiredMixin,SuccessMessageMixin,generic.CreateView):
    model = Docente
    template_name = "registrar.html"
    form_class=DocenteForm
    success_message = "El docente %(nombre)s %(apellido)s ha sido registrado"
    success_url=reverse_lazy('Docentes')

class ModificarDocente(LoginRequiredMixin,SuccessMessageMixin,generic.UpdateView):
    model = Docente
    template_name = "modificar.html"
    form_class=DocenteForm
    success_message = "El docente %(nombre)s %(apellido)s ha sido modificado"
    success_url=reverse_lazy('Docentes')

# ----------------------------------------------------------------
@login_required
def ListaGrupos(request):
    grupos=Grupo.objects.values('materia').distinct()
    
    queryset={
        'grupos':grupos
    }

    return render(request, 'grupos.html', queryset)

class RegistrarAlumnoAMateria(LoginRequiredMixin,SuccessMessageMixin,generic.CreateView):
    model = Grupo
    template_name = "registrar.html"
    form_class=GrupoForm
    success_message = "El alumno sido registrado a la materia de %(materia)s"
    success_url=reverse_lazy('Grupos')

@login_required
def AlumnosDelGrupo(request, materia):
    materia=Materia.objects.get(id=materia)
    grupos=Grupo.objects.filter(materia=materia.id)
    
    queryset={
        'materia':materia,
        'grupos':grupos
    }
    return render(request, 'grupoDetalle.html', queryset)

@login_required
def BorrarAlumnoDelGrupo(request, id, materia):
  Grupo.objects.get(id=id).delete()
  return HttpResponseRedirect(reverse('GrupoDetalle', kwargs={"materia": materia}))

  
# API-REST
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from .serializers import UserSerializer, GroupSerializer, CarreraSerializer, AlumnoSerializer, DocenteSerializer, MateriaSerializer

class UserViewSet(viewsets.ModelViewSet):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


# -----------------------------------------------------------------

@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated, ))
def ListaDeCarrerasAPI(request):
    """
    Lista de alumnos y para crear nuevos alumnos.
    """
    if request.method == 'GET':
        carreras = Carrera.objects.all()
        serializer = CarreraSerializer(carreras, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CarreraSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((IsAuthenticated, ))
def CarreraDetalleAPI(request, pk):
    """
    Consulta, modifica o elimina un alumno.
    """
    try:
        carrera = Carrera.objects.get(pk=pk)
    except Carrera.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CarreraSerializer(carrera)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CarreraSerializer(carrera, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        carrera.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# -----------------------------------------------------------------

@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated, ))
def ListaDeAlumnosAPI(request):
    """
    Lista de alumnos y para crear nuevos alumnos.
    """
    if request.method == 'GET':
        alumnos = Alumno.objects.all()
        serializer = AlumnoSerializer(alumnos, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AlumnoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((IsAuthenticated, ))
def AlumnoDetalleAPI(request, pk):
    """
    Consulta, modifica o elimina un alumno.
    """
    try:
        alumno = Alumno.objects.get(pk=pk)
    except Alumno.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AlumnoSerializer(alumno)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = AlumnoSerializer(alumno, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        alumno.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# -----------------------------------------------------------------

@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated, ))
def ListaDeDocentesAPI(request):
    """
    Lista de Docentes y para crear nuevos Docentes.
    """
    if request.method == 'GET':
        docentes = Docente.objects.all()
        serializer = DocenteSerializer(docentes, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = DocenteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((IsAuthenticated, ))
def DocenteDetalleAPI(request, pk):
    """
    Consulta, modifica o elimina un alumno.
    """
    try:
        docente = Docente.objects.get(pk=pk)
    except Docente.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DocenteSerializer(docente)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = DocenteSerializer(docente, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        docente.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# -----------------------------------------------------------------

@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated, ))
def ListaDeMateriasAPI(request):
    """
    Lista de Materias y para crear nuevos Materias.
    """
    if request.method == 'GET':
        materias = Materia.objects.all()
        serializer = MateriaSerializer(materias, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MateriaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((IsAuthenticated, ))
def MateriaDetalleAPI(request, pk):
    """
    Consulta, modifica o elimina un alumno.
    """
    try:
        materia = Materia.objects.get(pk=pk)
    except Materia.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MateriaSerializer(materia)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = MateriaSerializer(materia, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        materia.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
