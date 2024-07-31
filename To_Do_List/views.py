# views.py
import json
from django.shortcuts import render, redirect, get_object_or_404
from .models import To_Do_List
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def to_do_list(request):
    if request.method == 'POST':
        task = request.POST.get('task')
        if task:
            To_Do_List.objects.create(task=task)
    
    tasks = To_Do_List.objects.all()
    context = {"tasks": tasks}
    return render(request, 'to_do_list.html', context)


@csrf_exempt
def delete_task(request, task_id):
    if request.method == 'POST':
        task = get_object_or_404(To_Do_List, id=task_id)
        task.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})


def complete_task(request, task_id):
    if request.method == 'POST':
        task = get_object_or_404(To_Do_List, id=task_id)
        task.completed = True
        task.save()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})



def edit_task(request, task_id):
    if request.method == 'POST':
        task = get_object_or_404(To_Do_List, id=task_id)
        data = json.loads(request.body)
        new_task = data.get('task')
        if new_task:
            task.task = new_task
            task.save()
            return JsonResponse({'success': True})
    return JsonResponse({'success': False})