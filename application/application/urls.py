
from django.contrib import admin
from django.urls import path,re_path
from app import views
from django.conf import settings
from django.conf.urls.static import static
# from django.conf.urls import url
from django.views.static import serve


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.vaccancy),
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
