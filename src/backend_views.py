from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from django.http import HttpResponseForbidden
from django.shortcuts import render
from .models import Sale
from .decorators import group_required

@login_required
def view_sales(request):
    sales = Sale.objects.filter(sold_by=request.user).select_related('item', 'sold_by')
    return render(request, 'core/view_sales.html', {'sales': sales})


@permission_required('core.can_transfer_money', raise_exception=True)
@group_required("Site Owner")
def transfer_money(request):
    if request.method == "POST":
        # Simulate transfer logic
        messages.success(request, "Money transferred successfully to the bank account!")
        return render(request, 'core/transfer_money.html')
    return render(request, 'core/transfer_money.html')


@login_required
def view_all_sales(request):
    # Check if the user belongs to the "Site Owner" group
    if not request.user.groups.filter(name="Site Owner").exists():
        return HttpResponseForbidden("You do not have permission to view all sales.")

    sales = Sale.objects.all().select_related('item', 'sold_by')
    return render(request, 'core/view_all_sales.html', {'sales': sales})
