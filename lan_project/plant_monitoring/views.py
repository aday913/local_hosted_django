from django.shortcuts import render

def simple_view(request):
    return render(request, 'lan_project/base.html')
    