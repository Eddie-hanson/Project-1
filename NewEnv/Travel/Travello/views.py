from django.shortcuts import render,redirect
from .forms import SubscriptionForm, UserFeedbackForm

from .models import Destination,News, Subscription,Available_Trips,Contact,AllDestinations, UserFeedback

# Create your views here.
def home(request):

    
    #To fetch data from the db
    dests=Destination.objects.all()
    news=News.objects.all()
    #Posting data to database
    #subscriber= Subscription.objects.all()
    form = SubscriptionForm()
   
    if request.method=='POST':  
        form=SubscriptionForm(request.POST) 
        if form.is_valid():
            form.save()
            return redirect('/')
    context= {'dests':dests ,'news':news, 'form':form}    
    return render(request,"home.html",context)

def about(request):
    form = SubscriptionForm()
    if request.method=='POST':  
        form=SubscriptionForm(request.POST) 
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form}    
    return render(request, "about.html",context)

def Search(request):
    if request.method=='GET':
        query = request.GET.get('query')
        if query:
            available_Trips=Available_Trips.objects.filter(Name__icontain='query')
            return render(request, "Search.html" ,{"available_Trips":available_Trips})
        else:
            print ('No destinations available')
            return render(request,"Search.html",{})
               
def contact(request):
        
    form = SubscriptionForm()
    if request.method=='POST':  
        form=SubscriptionForm(request.POST) 
        if form.is_valid():
            form.save()
            return redirect('/')
        
    form_2=UserFeedbackForm()
    if request.method=='POST':
        form_2=UserFeedbackForm(request.POST)
        if form_2.is_valid():
            form_2.save()
            return redirect('/')   
    context={'form':form,'form_2':form_2}     
    return render(request, 'contact.html', context)    
 
def destinations(request):
    destinations=AllDestinations.objects.all()
    form = SubscriptionForm()
    if request.method=='POST':
       form=SubscriptionForm(request.POST)
       if form.is_valid():
        form.save()
        return redirect('/')
    context= {'destinations':destinations, 'form':form} 
        
    return render(request, 'destinations.html',context)

def elements(request):
   
        # form=SubscriptionForm(request.POST)
        
    form=SubscriptionForm(request.POST)
    if request.method=='POST':
       form=SubscriptionForm(request.POST)
       if form.is_valid():
        form.save()
        return redirect('/')
    context= {'form':form}      
    return render(request, 'elements.html',context)
 
def news(request):
    form = SubscriptionForm()
    if request.method=='POST':
       form=SubscriptionForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('/')
    context={'form':form}
    return render(request, 'news.html', context)


