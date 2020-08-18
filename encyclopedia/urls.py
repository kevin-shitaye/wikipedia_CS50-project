from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:title>/", views.entry, name="entry"),
    path("search", views.search, name="search"),
    path("newPage", views.newPage, name="newPage"),
    path("<str:title>/edit/", views.editPage, name="editPage"),
    path("editPage", views.edit, name="edit"),
    path("randomPage", views.randomPage, name="randomPage")
]
