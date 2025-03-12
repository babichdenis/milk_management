from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Supplier
from .forms import SupplierForm


def supplier_list(request):
    suppliers = Supplier.objects.all()
    return render(request, 'suppliers/supplier_list.html', {'suppliers': suppliers})


@csrf_exempt
def supplier_create(request):
    if request.method == 'POST':
        form = SupplierForm(request.POST)
        if form.is_valid():
            supplier = form.save()
            return JsonResponse({'success': True, 'supplier': {'id': supplier.id, 'name': supplier.name, 'contact_person': supplier.contact_person, 'phone': supplier.phone, 'email': supplier.email}})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    return JsonResponse({'success': False, 'error': 'Invalid request'})


@csrf_exempt
def supplier_update(request, pk):
    supplier = get_object_or_404(Supplier, pk=pk)
    if request.method == 'POST':
        form = SupplierForm(request.POST, instance=supplier)
        if form.is_valid():
            supplier = form.save()
            return JsonResponse({'success': True, 'supplier': {'id': supplier.id, 'name': supplier.name, 'contact_person': supplier.contact_person, 'phone': supplier.phone, 'email': supplier.email}})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    return JsonResponse({'success': False, 'error': 'Invalid request'})


@csrf_exempt
def supplier_delete(request, pk):
    supplier = get_object_or_404(Supplier, pk=pk)
    if request.method == 'POST':
        supplier.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})
