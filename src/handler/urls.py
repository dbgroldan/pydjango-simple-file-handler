from django.urls import path
from . import views

urlpatterns = [
    path('handler', views.FileCSVHandlerView.as_view(), name='file_upload'),
    path('clients', views.ClientView.as_view(), name='clients'),
    path('clients/<str:pk>', views.ClientDetailView.as_view(), name='client_profile')
]
