from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('about', views.somepage)
    
]

htmx_urlpatterns = [
    path('update/',views.update, name='update')
]

urlpatterns += htmx_urlpatterns