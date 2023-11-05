from django.shortcuts import render

# Create your views here.
def complete_line(request):
    context = {}
    return render(request, 'account_management/complete_line.html', context)