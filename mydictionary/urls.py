
from django.urls import path
from mydictionary import views
urlpatterns = [
    path("",views.word_meaning),
    
]
