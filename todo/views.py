from django.http import HttpResponse

# Create
def add_todo(request):
    return HttpResponse("Add todo view")

# Read
def list_all_todo(request):
    return HttpResponse("List all todo view")

# Update
def edit_todo(request, todo_id):
    return HttpResponse(f"Edit todo view for {todo_id}")

# Delete
def delete_todo(request, todo_id):
    return HttpResponse(f"Delete todo view for {todo_id}")
