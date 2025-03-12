from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import ProductionPlan
from products.models import Product
from .forms import ProductionPlanForm
from django.contrib.auth.decorators import login_required


@login_required
def plan_list(request):
    """
    Отображение списка планов производства.
    """
    plans = ProductionPlan.objects.all()
    products = Product.objects.all()  # Получаем все продукты
    return render(request, 'production_plans/list.html', {'plans': plans, 'products': products})


def add_plan(request):
    """
    Добавление нового плана производства.
    """
    if request.method == 'POST':
        form = ProductionPlanForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = ProductionPlanForm()
    return render(request, 'production_plans/add.html', {'form': form})


def edit_plan(request, plan_id):
    """
    Редактирование существующего плана производства.
    """
    plan = get_object_or_404(ProductionPlan, id=plan_id)
    if request.method == 'POST':
        form = ProductionPlanForm(request.POST, instance=plan)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = ProductionPlanForm(instance=plan)
    return render(request, 'production_plans/edit.html', {'form': form, 'plan': plan})


def delete_plan(request, plan_id):
    """
    Удаление плана производства.
    """
    plan = get_object_or_404(ProductionPlan, id=plan_id)
    if request.method == 'POST':
        plan.delete()
        return JsonResponse({'success': True})
    return render(request, 'production_plans/delete.html', {'plan': plan})
