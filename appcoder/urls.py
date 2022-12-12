from django.urls import path
from appcoder import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", views.inicio, name="coder-inicio"),

    path("estudiantes/", views.estudiantes, name="coder-estudiantes"),
    
    path("profesores/", views.profesores, name="coder-profesores"),

    path("profesores/crear/", views.creacion_profesores, name="coder-profesores-crear"),
    
    path("cursos/", views.cursos,name="coder-cursos"),

    path("cursos/crear/", views.creacion_curso, name="coder-cursos-crear"),

    path("cursos/buscar/", views.busqueda_curso, name="coder-cursos-buscar"),

    path("cursos/borrar/<id>/", views.eliminar_curso, name="coder-cursos-borrar"),

    path("cursos/editar/<id>", views.editar_curso, name="coder-cursos-editar"),

    path("cursos/buscar/resultados", views.resultado_busqueda_cursos, name="coder-cursos-resultado-busqueda"),
    
    path("entregables/", views.entregables, name="coder-entregables"),
    
    path("login/", views.iniciar_sesion, name="auth-login"),

    path("register/", views.registrar_usuario, name ="reg-user"),

    path("logout/", LogoutView.as_view(template_name='appcoder/logout.html'), name = "auth-logout"),

    path("perfil/editar/", views.editar_perfil, name="auth-editar-perfil"),
    
    path("perfil/avatar/", views.agregar_avatar, name="auth-avatar"),
]