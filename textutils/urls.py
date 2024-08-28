from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('analyze', views.analyze, name='analyze'),
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
