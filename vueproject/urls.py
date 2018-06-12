from django.contrib import admin
from django.conf.urls import  include, url
from .routers import router
from django.views.generic import TemplateView

urlpatterns = [
    url('admin/', admin.site.urls),
    url('api/', include(router.urls)),
    url('vueapp', TemplateView.as_view(template_name='index.html')),
]
