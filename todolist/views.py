from django.shortcuts import render,redirect
from .models import TaskList
from .forms import CreateTask
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    context={

    }
    return render(request,'index.html',context)

@login_required
def todolist(request):
    if request.method=="POST":
        form=CreateTask(request.POST or None)
        if form.is_valid():
            form.save(commit=False).owner= request.user
            form.save()
        messages.success(request,("New Task Added!"))

        return redirect('todolist')
    else:
        tasklist=TaskList.objects.filter(owner=request.user)
        paginator=Paginator(tasklist,5)
        page=request.GET.get('page')
        tasklist=paginator.get_page(page)
    context={
        'tasklist':tasklist,
    }
    return render(request,'todolist.html',context)

@login_required
def CompleteTask(request,id):
    task=TaskList.objects.get(pk=id)
    if task.owner==request.user:
        task.done=True
        task.save()
    else:
        messages.error(request,("Access Restrictrd, You Are Not Allowed"))
        
    return redirect('todolist')

@login_required
def PendingTask(request,id):
    task=TaskList.objects.get(pk=id)
    if task.owner==request.user:
        task.done=False
        task.save()
    else:
        messages.error(request,("Access Restrictrd, You Are Not Allowed"))

    return redirect('todolist')

@login_required
def DeleteTask(request,id):
    task=TaskList.objects.get(pk=id)
    if task.owner==request.user:
        task.delete()
        messages.success(request,("Task " +str(name)+" Deleted"))
    else:
        messages.error(request,("Access Restrictrd, You Are Not Allowed"))
    return redirect('todolist')

@login_required
def EditTask(request,id):
    if request.method=="POST":
        task=TaskList.objects.get(pk=id)
        form=CreateTask(request.POST or None,instance=task)
        if form.is_valid():
            form.save()
        messages.success(request,("Task Updated!"))
        return redirect('todolist')
    else:
        task=TaskList.objects.get(pk=id)
        context={
            'task':task
        }
        return render(request,'edittask.html',context)

@login_required
def about(request):
    return render(request,'about.html',{})

def contact(request):
    return render(request,'contact.html')
