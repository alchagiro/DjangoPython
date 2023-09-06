from django.shortcuts import render

def holamundo(request):
    context={}
    return render(request, 'index.html', context)