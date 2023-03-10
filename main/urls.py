from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('about', views.somepage)
    
]

htmx_urlpatterns = [
    path('update1/',views.update1, name='update1'),
    path('update2/',views.update2, name='update2'),
    path('update3/',views.update3, name='update3'),
    path('update4/',views.update4, name='update4')
]

urlpatterns += htmx_urlpatterns