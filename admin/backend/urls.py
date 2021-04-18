from django.urls import path

from . import views

app_name = 'backend'
urlpatterns = [
    path('vonly/', views.TodoVueOnlyTV.as_view(), name='vonly'),
]
