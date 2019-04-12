from django.urls import path
from . import views

urlpatterns=[
    path('', views.inicio, name="inicio"),

    path('alumnos/', views.ListaAlumnos.as_view(), name="alumnos"),
    path('alumnoNuevo/', views.RegistrarAlumno.as_view(), name="RegistrarAlumno"),
    path('alumnosDetalle/<int:pk>', views.AlumnoDetalle.as_view(), name="AlumnoDetalle"),
    path('alumnosModificar/<int:pk>', views.ModificarAlumno.as_view(), name="ModificarAlumno"),
    path('alumnosEliminar/<int:pk>', views.EliminarAlumno.as_view(), name="EliminarAlumno"),

    path('Carreras/', views.ListaCarreras.as_view(), name="carreras"),
    path('CarreraNueva/', views.RegistrarCarrera.as_view(), name="RegistrarCarrera"),
    path('CarrerasModificar/<int:pk>', views.ModificarCarrera.as_view(), name="ModificarCarrera"),
    path('CarrerasEliminar/<int:pk>', views.EliminarCarrera.as_view(), name="EliminarCarrera"),

    path('Materias/', views.ListaMaterias.as_view(), name="Materias"),
    path('MateriaNueva/', views.RegistrarMateria.as_view(), name="RegistrarMateria"),
    path('MateriasModificar/<int:pk>', views.ModificarMateria.as_view(), name="ModificarMateria"),
    path('MateriasEliminar/<int:pk>', views.EliminarMateria.as_view(), name="EliminarMateria"),

    path('Docentes/', views.ListaDocentes.as_view(), name="Docentes"),
    path('DocenteNuevo/', views.RegistrarDocente.as_view(), name="RegistrarDocente"),
    path('DocentesDetalle/<int:pk>', views.DocenteDetalle.as_view(), name="DocenteDetalle"),
    path('DocentesModificar/<int:pk>', views.ModificarDocente.as_view(), name="ModificarDocente"),
    path('DocentesEliminar/<int:pk>', views.EliminarDocente.as_view(), name="EliminarDocente"),

    path('Grupos/', views.ListaGrupos, name="Grupos"),
    path('GrupoNuevo/', views.RegistrarAlumnoAMateria.as_view(), name="RegistrarGrupo"),
    path('AlumnosDelGrupo/<int:materia>', views.AlumnosDelGrupo, name="GrupoDetalle"),
    path('borrarAlumnoDelGrupo/<int:id><int:materia>', views.BorrarAlumnoDelGrupo, name="borrarAlumnoGrupo"),
]
