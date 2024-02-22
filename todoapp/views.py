from django.shortcuts import render,HttpResponse,redirect
from .models import Todo
from .forms import TodoForm,TodoSearchForm
from django.contrib.auth.decorators import login_required

from django.contrib.auth import login,authenticate,logout


def loginPage(request):
    error = None
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('list_todo')
        error = "Username or Password Error"
    context = {
        'error':error,
    }  

    return render(request,'login.html',context)

def logoutPage(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('loginPage') 
    
# Create your views here.
def todo_index(request):
    return HttpResponse("THIS IS TODO INDEX")

def list_todo(request):
    if not request.user.is_authenticated:
        return redirect('loginPage')
    
    todo_search_form = TodoSearchForm()
    keyword = request.GET.get('title')
    if keyword is not None and keyword != "":
        todos = Todo.objects.filter(title__exact = keyword)
    else:
        todos = Todo.objects.all()
    todos = todos.filter(created_by = request.user)
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

# @login_required(login_url="loginPage")
## if reqeust.user.is_authenticated()
def create_todo(request):
    if not request.user.is_authenticated:
        return redirect('loginPage')
    form = TodoForm()
    if request.method == "POST":
        print(request.POST)
        form = TodoForm(request.POST)
        if form.is_valid():
            # from save and create object
            form_object = form.save(commit=False)
            form_object.created_by = request.user
            form_object.save()#creates Todo in the database
            

            return redirect('list_todo')

    context = {
        'form':form

    }
    return render(request,'todoapp/create.html',context)


login_required()
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
