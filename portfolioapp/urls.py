from django.urls import path
from.import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about',views.about,name='home'),
    path('resume',views.resume,name='resume'),
    path('project',views.project,name='project'),
    path('contact',views.contact,name='contact'),
]
