from django.shortcuts import render, redirect
from .models import Writer, Book, Chapter
from .forms import *

# Create your views here.
def create(request):
    if request.method == 'POST':
        form = WriterModelForm(request.POST)
        if form.is_valid(): # 유효성 검사
            form.save()
            return redirect('detail')

    elif request.method == 'GET':
        form = WriterModelForm()

    return render(request, 'new.html', {'form': form})



def update(request, id):
    writer = Writer.objects.get(id=id)

    if request.method == 'POST':
        form = WriterModelForm(request.POST, instance=writer)
        if form.is_valid():
            form.save()
            return redirect('detail')

    elif request.method == 'GET':
        form = WriterModelForm(instance=writer)

    return render(request, 'edit.html', {'form': form})