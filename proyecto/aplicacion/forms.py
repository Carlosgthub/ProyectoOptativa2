from django import forms
from .models import Carrera, Alumno, Docente, Materia, Grupo

class CarreraForm(forms.ModelForm):
    nombre=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))

    class Meta:
        model=Carrera
        fields='__all__'

class AlumnoForm(forms.ModelForm):
    nombre=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    apellido=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    carrera=forms.ModelChoiceField(
        queryset=Carrera.objects.all(),
        widget=forms.Select(
            attrs={
                "class":"form-control"
    }))

    class Meta:
        model=Alumno
        fields='__all__'

class MateriaForm(forms.ModelForm):
    nombre=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    creditos=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control"}))
    maestro=forms.ModelChoiceField(
        queryset=Docente.objects.all(),
        widget=forms.Select(
            attrs={
                "class":"form-control"
    }))

    class Meta:
        model=Materia
        fields='__all__'

class DocenteForm(forms.ModelForm):
    nombre=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    apellido=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))

    class Meta:
        model=Docente
        fields='__all__'

class GrupoForm(forms.ModelForm):
    materia=forms.ModelChoiceField(
        queryset=Materia.objects.all(),
        widget=forms.Select(
            attrs={
                "class":"form-control"
    }))

    alumno=forms.ModelChoiceField(
        queryset=Alumno.objects.all(),
        widget=forms.Select(
            attrs={
                "class":"form-control"
    }))

    class Meta:
        model=Grupo
        fields='__all__'