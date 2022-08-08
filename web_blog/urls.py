from django.urls import path

from . import views

urlpatterns = [
    path('', views.PostView.as_view()),
    path('post.html', views.PostView.as_view()),
    path('about.html', views.PostAbout.as_view()),
    path('contact.html', views.PostContact.as_view())
]
