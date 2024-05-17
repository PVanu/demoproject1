from django.shortcuts import render

def allcategories(request):
    return render(request,'category.html')
