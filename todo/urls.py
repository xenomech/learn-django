from django.urls import path
from .views import CreateTodoView, TodoListView, EditTodoView, DeleteTodoView, CompleteTodoView

app_name = "todo"
urlpatterns = [
    path("", TodoListView.as_view(), name="list_all_todo"),  # read all todo
    path("create/", CreateTodoView.as_view(), name="create_todo"),  # create todo
    path("edit/<int:pk>/", EditTodoView.as_view(), name="edit_todo"),  # update todo
    path(
        "delete/<int:pk>/", DeleteTodoView.as_view(), name="delete_todo"
    ),  # delete todo
    path("complete/<int:pk>/", CompleteTodoView.as_view(), name="complete_todo"), 
]
