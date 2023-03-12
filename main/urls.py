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
    path('update4/',views.update4, name='update4'),
    path('light11/',views.light11, name='light11'),
    path('light12/',views.light12, name='light12'),
    path('light21/',views.light21, name='light21'),
    path('light22/',views.light22, name='light22'),
    path('light31/',views.light31, name='light31'),
    path('light32/',views.light32, name='light32'),
    path('light41/',views.light41, name='light41'),
    path('light42/',views.light42, name='light42')

    
]

urlpatterns += htmx_urlpatterns