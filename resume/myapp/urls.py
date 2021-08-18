from django.urls import path
from . import views

# app_name = "main"

urlpatterns = [
    path("", views.index, name="index"),
    path("index", views.index, name="index"),
    path("contact", views.contact, name="contact"),
    path("education", views.education, name="education"),
    path("project", views.project, name="project"),
    path("skill", views.skill, name="skill")
]