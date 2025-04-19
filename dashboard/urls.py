from django.urls import path
from .views import *

urlpatterns = [
    path('', main_dashboard, name='main_dashboard'),
    path('login/', login_page, name="login_page"),
    path('logout/', logout_page, name="logout_page"),

    path('gallery/create/', gallery_create, name='gallery_create'),
    path('gallery/<int:pk>/edit/', gallery_edit, name='gallery_edit'),
    path('gallery/<int:pk>/delete/', gallery_delete, name='gallery_delete'),
    path('gallery/list/', gallery_list, name='gallery_list'),

    path('education/create/', education_create, name='education_create'),
    path('education/<int:pk>/edit/', education_edit, name='education_edit'),
    path('education/<int:pk>/delete/', education_delete, name='education_delete'),
    path('education/list/', education_list, name='education_list'),

    path('activity/create/', activity_create, name='activity_create'),
    path('activity/<int:pk>/edit/', activity_edit, name='activity_edit'),
    path('activity/<int:pk>/delete/', activity_delete, name='activity_delete'),
    path('activity/list/', activity_list, name="activity_list"),

    path('rest_area/create/', rest_area_create, name='rest_area_create'),
    path('rest_area/<int:pk>/edit/', rest_area_edit, name='rest_area_edit'),
    path('rest_area/<int:pk>/delete/', rest_area_delete, name='rest_area_delete'),
    path('rest_area/list/', rest_area_list, name="rest_area_list"),
]
