from django.shortcuts import render, redirect
from .models import Transaction
from .form import TransactionForm
 
def listing(request):
    transaction = Transaction.objects.all()
    return render(request, "account/listing.html", { 'transaction' : transaction })

def newTransaction(request):
    form = TransactionForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('url_listing')

    return render(request, "account/form.html", { 'form' : form })

def update(request, pk):
    transaction = Transaction.objects.get(pk=pk)
    form = TransactionForm(request.POST or None, instance=transaction)
 
    if form.is_valid():
        form.save()
        return redirect('url_listing')

    return render(request, "account/form.html", { 'form' : form, 'transaction' : transaction })

def delete(request, pk):
    transaction = Transaction.objects.get(pk=pk)
    transaction.delete()
 
    return redirect('url_listing')