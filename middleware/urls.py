from django.contrib import admin
from django.urls import path
from mdlware import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home),
]
