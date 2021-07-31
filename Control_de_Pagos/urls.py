"""Control_de_Pagos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from profiles.urls import profiles_patterns
#from core import views as core_views
from django.conf.urls.static import static

urlpatterns = [
    
    #path('', core_views.home, name="home"),
    path('', include('pagos.urls')),
    #path('registro', core_views.registro, name="registro"),
    #path('registro_alumno', core_views.registro_alumno, name="registro_alumno"),
    path('alumnos/', include('alumnos.urls')),
    path('admin/', admin.site.urls),
    path('carrera/', include('grados_carreras.urls')),
    path('reporte/', include('reportes.urls')),
    path('tipoPago/', include('tipo_pago.urls')),

    #path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('registration.urls')),
    path('profiles/', include(profiles_patterns)),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
