from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.contrib.auth import logout
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm

from .models import WarrantyItem
from .forms import WarrantyItemForm

def home(request):
    return render(request, 'home.html')

def is_admin(user):
    # Only username "admin" is admin. If you want all staff, use: return user.is_staff
    return user.is_authenticated and user.username == 'admin'

@login_required
def dashboard(request):
    # NO REDIRECT! Admin can use dashboard like a normal user.
    items = WarrantyItem.objects.filter(user=request.user)
    return render(request, 'dashboard.html', {'items': items})

def force_logout(request):
    logout(request)
    return redirect('/')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful! You can now log in.')
            return redirect('login')
        else:
            print("Form errors:", form.errors)  # Debug
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def upload_warranty(request):
    if request.method == 'POST':
        form = WarrantyItemForm(request.POST, request.FILES)
        if form.is_valid():
            warranty = form.save(commit=False)
            warranty.user = request.user
            warranty.save()
            messages.success(request, "Warranty item uploaded successfully.")
            return redirect('dashboard')
    else:
        form = WarrantyItemForm()
    return render(request, 'upload_warranty_item.html', {'form': form})

# ==== ADMIN PANEL ====

@login_required
@user_passes_test(is_admin)
def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')

@login_required
@user_passes_test(is_admin)
def admin_items(request):
    items = WarrantyItem.objects.all()
    return render(request, 'admin_items.html', {'items': items})

@login_required
@user_passes_test(is_admin)
def admin_delete_item(request, pk):
    item = get_object_or_404(WarrantyItem, pk=pk)
    item.delete()
    messages.success(request, "Item deleted.")
    return redirect('admin_items')

# USER deletes their own item (not admin panel)
@login_required
def delete_warranty(request, item_id):
    item = get_object_or_404(WarrantyItem, id=item_id, user=request.user)
    item.delete()
    messages.success(request, "Warranty item deleted.")
    return redirect('dashboard')
