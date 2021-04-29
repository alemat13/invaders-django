from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name = 'city-list'),
    path('city/<slug:slug>', views.CityView.as_view(), name='city-detail'),
    path('city/add/', views.add_city, name='city-add'),
    path('invader/add/', views.InvaderCreateView.as_view(), name='invader-add'),
    path('invader/<slug:slug>', views.InvaderView.as_view(), name='invader-detail'),
    path('invader/<slug:slug>/update/', views.InvaderUpdateView.as_view(), name='invader-update'),
    path('invader/<slug:slug>/delete/', views.InvaderDeleteView.as_view(), name='invader-delete'),
]

