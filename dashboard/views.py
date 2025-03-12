# dashboard/views.py
from django.http import JsonResponse
from django.shortcuts import render
from suppliers.models import Supplier
from raw_materials.models import RawMaterial
from products.models import Product
from production_plans.models import ProductionPlan
from django.db.models import Sum, Count
from django.utils import timezone
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


def dashboard_view(request):
    # Статистика по поставщикам
    suppliers_stats = {
        'total': Supplier.objects.count(),
        'latest': Supplier.objects.order_by('-id')[:5]
    }

    # Статистика по сырью
    raw_materials_stats = {
        'total_quantity': RawMaterial.objects.aggregate(Sum('quantity'))['quantity__sum'] or 0,
        'expiring_soon': RawMaterial.objects.filter(
            expiration_date__lte=timezone.now() + timezone.timedelta(days=7)
        ).count(),
        'by_supplier': RawMaterial.objects.values('supplier__name').annotate(
            total=Sum('quantity')
        ).order_by('-total')[:5]
    }

    # Статистика по продукции
    products_stats = {
        'total': Product.objects.count(),
        'total_production_cost': Product.objects.aggregate(Sum('production_cost'))['production_cost__sum'] or 0,
        'by_category': Product.objects.values('category').annotate(
            count=Count('id')
        ).order_by('-count')
    }

    # Производственные планы
    production_plans = {
        'current': ProductionPlan.objects.filter(
            planned_date__gte=timezone.now()
        ).order_by('planned_date')[:5],
        'status_distribution': ProductionPlan.objects.values('status').annotate(
            count=Count('id')
        )
    }

    context = {
        'suppliers_stats': suppliers_stats,
        'raw_materials_stats': raw_materials_stats,
        'products_stats': products_stats,
        'production_plans': production_plans
    }

    return render(request, 'dashboard/dashboard.html', context)


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'error': 'Неверные учетные данные'})
    return render(request, 'dashboard/login.html')


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Вход пользователя сразу после регистрации
            return redirect('dashboard')  # Перенаправление на главную страницу
        else:
            # Проверка на существующее имя пользователя
            username = request.POST.get('username', '')
            if User.objects.filter(username=username).exists():
                error = 'Это имя пользователя уже занято'
            else:
                error = form.errors.as_json()
            return render(request, 'dashboard/register.html', {'form': form, 'error': error})
    else:
        form = UserCreationForm()
    return render(request, 'dashboard/register.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('dashboard')
