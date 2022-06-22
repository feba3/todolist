from django.shortcuts import render,redirect
# from django.http import HttpResponse
from todoapp.form import ToDoForm
from todoapp.models import ToDo

def myfun(request):
  # return render(request,'home.html')
  form=ToDoForm()
  # all values kittan
  todos=ToDo.objects.all()
  # databasil value kodukkan
  if request.method=='POST':
    form=ToDoForm(request.POST)
    if form.is_valid():
       form.save()
  return render(request,'home.html',{'form':form,'todo':todos})

def update(request,todo_id):
  todo=ToDo.objects.get(id=todo_id)
  form=ToDoForm(instance=todo)

  if request.method=='POST':
    form=ToDoForm(request.POST,instance=todo)

    if form.is_valid():
       form.save()
       return redirect('/')
  return render(request,'update.html',{'form':form})



def deletePage(request,todo_id):
  data = ToDo.objects.get(id=todo_id)
  data.delete()

  return redirect('home')
    
   
  
  

