from django.urls import path
from . import views

urlpatterns = (
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('homies/', views.homies_index, name='index'),
    path('homies/new/', views.new_homie, name='new_homie'),
    path('homies/<int:homie_id>/', views.homies_detail, name='detail'),
    path('homies/<int:homie_id>/edit/', views.homies_update, name='homies_update'),
    path('homies/<int:homie_id>/delete/', views.homies_delete, name='homies_delete'),
    path('homies/<int:homie_id>/', views.add_saw, name='add_saw'),
    #locations paths
    path('locations/', views.location_index, name='locations_index'),
    path('locations/<int:pk>/', views.LocationDetail.as_view(), name='locations_detail'),
    path('locations/create/', views.LocationCreate.as_view(), name='locations_create'),
    path('locations/<int:pk>/update/', views.LocationUpdate.as_view(), name='locations_update'),
    path('locations/<int:pk>/delete/', views.LocationDelete.as_view(), name='locations_delete'),
)