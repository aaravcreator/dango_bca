from django.shortcuts import render,HttpResponse,redirect
from .models import Todo
from .forms import TodoForm,TodoSearchForm
# Create your views here.
def todo_index(request):
    return HttpResponse("THIS IS TODO INDEX")

def list_todo(request):
    todo_search_form = TodoSearchForm()
    keyword = request.GET.get('title')
    if keyword is not None and keyword != "":
        todos = Todo.objects.filter(title__exact = keyword)
    else:
        todos = Todo.objects.all()
    completed_todos_count = Todo.objects.filter(completed_status=True).count()
    incomplete_todos_count = Todo.objects.filter(completed_status=False).count()
    print(todos)
    context = {
        'todo_search_form':todo_search_form,
        'todo_list':todos,
        'completed_todos_count':completed_todos_count,
        'incomplete_todos_count':incomplete_todos_count
    }
    return render(request,'todoapp/list.html',context)


def create_todo(request):
    form = TodoForm()
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            # from save and create object
            form.save() # creates Todo in the database
            return redirect('list_todo')

    context = {
        'form':form

    }
    return render(request,'todoapp/create.html',context)

def edit_todo(request,id):
    todo = Todo.objects.get(id=id)
    
    form = TodoForm(instance=todo)
    if request.method == 'POST':
        form = TodoForm(request.POST,instance=todo)
        if form.is_valid():
            form.save()
            return redirect('list_todo')
    context = {
        'todo':todo,
        'form':form,

    }
    return render(request,'todoapp/edit.html',context)


def delete_todo(request,id):
    try:
         todo = Todo.objects.get(id=id)
    except Todo.DoesNotExist:
        return HttpResponse("NOT FOUND")
   
    if request.method == 'POST':
        todo.delete()
        return redirect('list_todo')
    context = {
    'todo':todo
    }
    return render(request,'todoapp/delete.html',context)
