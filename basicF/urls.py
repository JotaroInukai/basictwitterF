from django.urls import path
from . import views
app_name="basicF"
urlpatterns = [
    path('templates/', views.basicF_template, name='basicF_template'),
    path('templates/basicF_form_show', views.basicF_form_show, name='basicF_form_show'),
    path('templates/basicF_form', views.basicF_form, name='basicF_form'),
    path('templates/basicF_form_show2', views.basicF_form_show2, name='basicF_form_show2'),
    path('templates/basicF_form2', views.basicF_form2, name='basicF_form2'),
    path('templates/basicF_form_show3', views.basicF_form_show3, name='basicF_form_show3'),
    path('templates/basicF_form_show4', views.basicF_form_show4, name='basicF_form_show4'),
    path('templates/basicF_form4', views.basicF_form4, name='basicF_form4'),
]
