from django.urls import path
from . import views

urlpatterns = [
    path("add/", views.add_todo, name="add_todo"),  # create todo
    path("", views.list_all_todo, name="list_all_todo"),  # read all todo
    path("edit/<int:todo_id>/", views.edit_todo, name="edit_todo"),  # update todo
    path("delete/<int:todo_id>/", views.delete_todo, name="delete_todo"),  # delete todo
]
