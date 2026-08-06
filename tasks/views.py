from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm


def index(request):

    search = request.GET.get("search", "")

    tasks = Task.objects.all().order_by("due_date")

    if search:
        tasks = tasks.filter(title__icontains=search)

    total_tasks = tasks.count()
    completed_tasks = tasks.filter(status="Completed").count()
    pending_tasks = tasks.filter(status="Pending").count()

    progress = 0
    if total_tasks > 0:
        progress = int((completed_tasks / total_tasks) * 100)

    context = {
        "tasks": tasks,
        "total_tasks": total_tasks,
        "completed_tasks": completed_tasks,
        "pending_tasks": pending_tasks,
        "progress": progress,
        "search": search,
    }

    return render(request, "tasks/index.html", context)


def add_task(request):

    if request.method == "POST":

        form = TaskForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("index")

        print(form.errors)   # <-- IMPORTANT

    else:
        form = TaskForm()

    return render(request, "tasks/add.html", {
        "form": form
    })


def edit_task(request, id):

    task = get_object_or_404(Task, id=id)

    if request.method == "POST":

        form = TaskForm(request.POST, instance=task)

        if form.is_valid():
            form.save()
            return redirect("index")

        print(form.errors)   # <-- IMPORTANT

    else:
        form = TaskForm(instance=task)

    return render(request, "tasks/edit.html", {
        "form": form
    })


def delete_task(request, id):

    task = get_object_or_404(Task, id=id)
    task.delete()

    return redirect("index")


def complete_task(request, id):

    task = get_object_or_404(Task, id=id)

    if task.status == "Pending":
        task.status = "Completed"
    else:
        task.status = "Pending"

    task.save()

    return redirect("index")