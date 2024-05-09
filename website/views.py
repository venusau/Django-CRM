from django.shortcuts import render,redirect
#Import the django authentication, login, logout and the messages to flash messages 
from django.contrib.auth import authenticate, login, logout 
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record
def home (request):
    record= Record.objects.all()# grabs Everything from the table 

    
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        user= authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request,"You have been logged in!")
            return redirect('home')
        else:
            messages.error(request, "You entered wrong username or password",extra_tags="danger")
            return redirect('home')
    else:
            if request.user.is_authenticated:
                return render (request, 'home.html', {"records":record})
            else:
                return render (request, 'home.html')

# def login_user(request):
#     pass
def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "You have been registered and logged in!")
                return redirect('home')
        else:
            # If form is invalid, re-render the registration form with errors
            return render(request, 'register.html', {'form': form})
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})

def logout_user(request):
    logout(request)
    messages.success(request,"You have been logged out ...")
    return redirect('home')

def customer_record(request, pk):
    if request.user.is_authenticated:
        customer_record = Record.objects.get(id=pk)
        return render(request,'record.html', {'customer_record':customer_record})
    else:
        messages.success(request, "You have to be logged in to view the record...", extra_tags="danger")
        return redirect('home')
    
def delete_record(request, pk):
    if request.user.is_authenticated:
        record = Record.objects.get(id=pk)
        record.delete()
        messages.success(request, "Record has been deleted...", extra_tags="")
        return redirect('home')
    else:
        messages.success(request, "You have to be logged in to delete the record...", extra_tags="danger")
        return redirect('home')
    
def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method=="POST":
            if form.is_valid():
                add_record=form.save()
                messages.success(request, "Record has been added...", extra_tags="")
                return redirect('home')
        
        return render(request, 'add_record.html', {'form':form})
    else:
        messages.success(request, "You must be logged in to add new record...", extra_tags="danger")
        return redirect('home')

def update(request, pk):
    
    customer_record=Record.objects.get(id=pk)
    form = AddRecordForm(request.POST or None, instance=customer_record)
    if request.user.is_authenticated:
        if request.method=='POST':
            if form.is_valid():
                form.save()
                messages.success(request, "Record has been updated...", extra_tags="")
            return redirect('home')
        return render(request,'update.html',{'form':form})
    messages.success(request, "You must be loggeed in to update any record...", extra_tags="danger")
    return redirect('home')

