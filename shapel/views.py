from django.shortcuts import render

def home_view(request):
    return render(request,"index.html")

def about_view(request):
    return render(request,"about.html")

def blog_view(request):
    return render(request,"blog.html")

def gallary_view(request):
    return render(request,"gallery.html")