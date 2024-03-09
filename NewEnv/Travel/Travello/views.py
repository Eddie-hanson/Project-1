from django.shortcuts import render

from .models import Destination,bestTrips, Subscription,Available_Trips

# Create your views here.
def home(request):
    # dest1= Destination()
    # dest1.Name= 'Ghana'
    # dest1.img="Ghana.jpeg"
    # dest1.desc= 'The gateway to Africa'
    # dest1.Price=200
    # dest1.offer=False
    
    # dest2= Destination()
    # dest2.Name= "La Cote D'ivoire"
    # dest2.img="ivory coast.jpeg"
    # dest2.desc= ' Come to discover a country with enormous potential tourism beaches, culture, ecotourism and religion'
    # dest2.Price=500
    # dest2.offer=True
     
    # dest3= Destination()
    # dest3.Name= "Togo"
    # dest3.img="Togo.jpg"
    # dest3.desc= ' There is much to discover in this West African country. Did you know that this West African country is known for its palm-lined beaches and hilltop villages.'
    # dest3.Price=150
    # dest3.offer=False
     
    # dest4= Destination()
    # dest4.Name= "Namibia"
    # dest4.img="namibia.jpeg"
    # dest4.desc= "This country is among the prime destinations in Africa and is known for ecotourism which features Namibia's extensive wildlife. "
    # dest4.Price=350
    # dest4.offer=False
    
    # dest5= Destination()
    # dest5.Name= "Tanzania"
    # dest5.img="Tanzania.jpeg"
    # dest5.desc= "This African country is a country with many tourist attractions. Approximately 38 percent of Tanzania's land area is set aside in protected areas for conservation."
    # dest5.Price=500
    # dest5.offer=False
    
    # dest6= Destination()
    # dest6.Name= "Angola"
    # dest6.img="Angola.jpg"
    # dest6.desc= "This African country's tourism industry is based on the country's natural environment, including its rivers, waterfalls and coastline"
    # dest6.Price=1200
    # dest6.offer=False
    
    # dests=[dest1,dest2,dest3,dest4,dest5,dest6]
   
    
    
    #To fetch data from the db
    dests=Destination.objects.all()
    trips=bestTrips.objects.all()
    #Posting data to database
    #subscriber= Subscription.objects.all()
    if request.method=='POST':
        subscriber_Name=request.POST.get('Full-name', '')
        subscriber_Email = request.POST.get('Email', '')
        
        
        subscriber=Subscription.objects.create(Name=subscriber_Name, Email=subscriber_Email)
        
    return render(request,"home.html", {'dests':dests ,'trips':trips})

def about(request):
    return render(request, "about.html")





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
     return render(request, 'contact.html')
 
 

def destinations(request):
     return render(request, 'destinations.html')



def elements(request):
     return render(request, 'elements.html')
 
 

def news(request):
     return render(request, 'news.html')


