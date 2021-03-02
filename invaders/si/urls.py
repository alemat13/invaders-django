from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('<int:invader_id>/', views.invader_detail, name='invader_detail'),
    path('<int:invader_id>/update/', views.invader_update, name='invader_update'),
    path('city/<int:city_id>/', views.city, name='city'),
    path('city/<int:city_id>/invader/add/', views.add_invader, name='add_invader'),
]

