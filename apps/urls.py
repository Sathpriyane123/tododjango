from django.urls import path
from . views import *

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('form', form, name = 'form'),
    path('update/<int:id>/', update_student, name='update_student'),
    path('delete/<int:id>/', delete_student, name='delete_student'),]