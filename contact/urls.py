from django.urls import path
from contact import views

urlpatterns = [
    path('', views.contact_form_view, name='contact_view')
]
