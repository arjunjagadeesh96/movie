from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import movieform
from .models import movies
def index(request):
    movie=movies.objects.all()
    context={'movie_name': movie}
    return render(request,"index.html",context)
def detail(request,movie_id):
    movie=movies.objects.get(id=movie_id)
    return render(request,'detail.html',{'movies':movie})
def add_movie(request):
    if request.method=="POST":
        name = request.POST.get('name',)
        desc = request.POST.get('desc',)
        year = request.POST.get('year',)
        img = request.FILES['img']
        movie=movies(name=name,desc=desc,year=year,img=img)
        movie.save()
        return redirect('/')
    return render(request,'add.html')
def update(request,id):
    movie=movies.objects.get(id=id)
    forms=movieform(request.POST or None,request.FILES,instance=movie)
    if forms.is_valid():
        forms.save()
        return redirect('/')
    return render(request,'edit.html' ,{'forms':forms , 'movie': movie})
def delete(request,id):
    if request.method=='POST':
        movie=movies.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,'delete.html')