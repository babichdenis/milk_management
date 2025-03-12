from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import RawMaterial
from .forms import RawMaterialForm
from suppliers.models import Supplier  # Import the Supplier model


def raw_material_list(request):
    raw_materials = RawMaterial.objects.all()
    suppliers = Supplier.objects.all()  # Retrieve all suppliers
    # Pass suppliers to the template
    return render(request, 'raw_materials/raw_material_list.html', {'raw_materials': raw_materials, 'suppliers': suppliers})


@csrf_exempt
def raw_material_create(request):
    if request.method == 'POST':
        form = RawMaterialForm(request.POST, request.FILES)
        if form.is_valid():
            raw_material = form.save()
            # Возвращаем данные о новом сырье
            return JsonResponse({'success': True, 'raw_material': {
                'id': raw_material.id,
                'supplier_name': raw_material.supplier.name,
                'quantity': str(raw_material.quantity),
                'fat_content': str(raw_material.fat_content),
                'acidity': str(raw_material.acidity),
                'received_date': str(raw_material.received_date),
                'expiration_date': str(raw_material.expiration_date),
                'document_number': raw_material.document_number
            }})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    return JsonResponse({'success': False, 'error': 'Invalid request'})


@csrf_exempt
def raw_material_update(request, pk):
    raw_material = get_object_or_404(RawMaterial, pk=pk)
    if request.method == 'POST':
        form = RawMaterialForm(
            request.POST, request.FILES, instance=raw_material)
        if form.is_valid():
            raw_material = form.save()
            return JsonResponse({'success': True, 'raw_material': {
                'id': raw_material.id,
                'supplier_name': raw_material.supplier.name,
                'quantity': str(raw_material.quantity),
                'fat_content': str(raw_material.fat_content),
                'acidity': str(raw_material.acidity),
                'received_date': str(raw_material.received_date),
                'expiration_date': str(raw_material.expiration_date),
                'document_number': raw_material.document_number
            }})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})


@csrf_exempt
def raw_material_delete(request, pk):
    raw_material = get_object_or_404(RawMaterial, pk=pk)
    if request.method == 'POST':
        raw_material.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})
