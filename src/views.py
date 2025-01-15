from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from .models import MenuItem, Sale
from .forms import SaleForm, MenuItemForm

from django.contrib.auth.decorators import login_required

def home(request):
    menu_items = MenuItem.objects.all()
    can_change_menuitem = request.user.has_perm('change_menuitem') if request.user.is_authenticated else False
    return render(request, 'core/home.html', {
        'menu_items': menu_items,
        'can_change_menuitem': can_change_menuitem,
    })


@login_required
def record_sale(request):
    if request.method == "POST":
        form = SaleForm(request.POST)
        if form.is_valid():
            sale = form.save(commit=False)
            sale.sold_by = request.user
            sale.total_price = sale.item.price * sale.quantity
            sale.save()
            messages.success(request, "Sale recorded successfully!")
            return redirect('home')
    else:
        form = SaleForm()
    return render(request, 'core/record_sale.html', {'form': form})

@permission_required('core.change_menuitem', raise_exception=True)
def set_pricing(request):
    if request.method == "POST":
        form = MenuItemForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Menu item updated successfully!")
            return redirect('home')
    else:
        form = MenuItemForm()
    return render(request, 'core/set_pricing.html', {'form': form})

from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'core/signup.html', {'form': form})
