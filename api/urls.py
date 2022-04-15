from django.urls import path

from . import views

urlpatterns = [
    path('', views.apiOverview, name='api'),

    path('family-child/', views.familyChildList, name='family-child-list'),
    path('family/', views.familyList, name='families'),
    path('child/', views.childList, name='children'),

    path('family/create/', views.createFamily, name='create-family'),
    path('child/create/', views.createChild, name='create-child'),

    path('family/update/', views.warn, name='update-family'),
    path('family/update/<int:pk>/', views.familyUpdate, name='update-familyid'),
    path('child/update/', views.warn, name='update-child'),
    path('child/update/<int:pk>/', views.childUpdate, name='update-childid'),
    path('family/delete/', views.warn, name='family-delete'),

    path('family/delete/', views.warn, name='family-delete'),
    path('family/delete/<int:pk>/', views.familyDelete, name='family-deleteid'),
    path('child/delete/', views.warn, name='child-delete'),
    path('child/delete/<int:pk>/', views.childDelete, name='child-deleteid'),
]