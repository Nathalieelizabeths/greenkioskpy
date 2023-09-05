from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Vendor
from .forms import VendorForm

def vendor_list(request):
    vendors = Vendor.objects.all()
    return render(request, 'vendor/vendor_list.html', {'vendors': vendors})

def vendor_detail(request, id):
    vendor = get_object_or_404(Vendor, id=id)
    return render(request, 'vendor/vendor_detail.html', {'vendor': vendor})

def vendor_create(request):
    if request.method == 'POST':
        form = VendorForm(request.POST)
        if form.is_valid():
            vendor = form.save()
            return redirect('vendor_detail', id=vendor.id)
    else:
        form = VendorForm()
    return render(request, 'vendor/vendor_form.html', {'form': form})

def vendor_edit(request, id):
    vendor = get_object_or_404(Vendor, id=id)
    if request.method == 'POST':
        form = VendorForm(request.POST, instance=vendor)
        if form.is_valid():
            vendor = form.save()
            return redirect('vendor_detail', id=vendor.id)
    else:
        form = VendorForm(instance=vendor)
    return render(request, 'vendor/vendor_form.html', {'form': form})

def vendor_delete(request, id):
    vendor = get_object_or_404(Vendor, id=id)
    if request.method == 'POST':
        vendor.delete()
        return redirect('vendor_list')
    return render(request, 'vendor/vendor_confirm_delete.html', {'vendor': vendor})
