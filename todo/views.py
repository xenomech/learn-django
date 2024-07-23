from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from .models import Todo


# Create
class CreateTodoView(LoginRequiredMixin, CreateView):
    login_url = "auth:login"
    model = Todo
    fields = ["title", "description"]
    template_name = "forms/create_todo_form.html"
    success_url = reverse_lazy("todo:list_all_todo")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


# Read
class TodoListView(LoginRequiredMixin, ListView):
    login_url = "auth:login"
    template_name = "index.html"
    context_object_name = "todos"
    model = Todo

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)


# Update
class EditTodoView(LoginRequiredMixin, UpdateView):
    login_url = "auth:login"
    model = Todo
    fields = ["title", "description"]
    template_name = "forms/edit_form.html"
    success_url = reverse_lazy("todo:list_all_todo")

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)


# Delete
class DeleteTodoView(LoginRequiredMixin, DeleteView):
    login_url = "auth:login"
    model = Todo
    success_url = reverse_lazy("todo:list_all_todo")

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)


class CompleteTodoView(LoginRequiredMixin, UpdateView):

    def post(self, request: HttpRequest, pk) -> HttpResponse:
        todo = Todo.objects.get(pk=pk, user=request.user)
        todo.completed = not todo.completed
        todo.save()
        return redirect("todo:list_all_todo")
