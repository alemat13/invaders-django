from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name = 'index'),
    path('city/<slug:slug>/detail', views.CityView.as_view(), name='city_detail'),
    path('invader/<slug:slug>/detail', views.InvaderView.as_view(), name='invader_detail'),
    path('city/add/', views.add_city, name='add_city'),
    path('invader/add/<slug:slug>', views.add_invader, name='add_invader'),
    path('invader/<slug:slug>/update/', views.update_invader, name='update_invader'),
]

