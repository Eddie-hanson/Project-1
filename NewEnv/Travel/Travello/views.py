from django.shortcuts import render
from .models import Destination
# Create your views here.
def index(request):
    dest1= Destination()
    dest1.Name= 'Ghana'
    dest1.img="Ghana.jpeg"
    dest1.desc= 'The gateway to Africa'
    dest1.Price=200
    
    dest2= Destination()
    dest2.Name= "La Cote D'ivoire"
    dest2.img="ivory coast.jpeg"
    dest2.desc= ' Come to discover a country with enormous potential tourism beaches, culture, ecotourism and religion'
    dest2.Price=500
    
    dest3= Destination()
    dest3.Name= "Togo"
    dest3.img="Togo.jpg"
    dest3.desc= ' There is much to discover in this West African country. Did you know that this West African country is known for its palm-lined beaches and hilltop villages.'
    dest3.Price=150
    
    dest4= Destination()
    dest4.Name= "Namibia"
    dest4.img="namibia.jpeg"
    dest4.desc= "This country is among the prime destinations in Africa and is known for ecotourism which features Namibia's extensive wildlife. "
    dest4.Price=350
    
    dest5= Destination()
    dest5.Name= "Tanzania"
    dest5.img="Tanzania.jpeg"
    dest5.desc= "This African country is a country with many tourist attractions. Approximately 38 percent of Tanzania's land area is set aside in protected areas for conservation."
    dest5.Price=500
    
    dest6= Destination()
    dest6.Name= "Angola"
    dest6.img="Angola.jpg"
    dest6.desc= "This African country's tourism industry is based on the country's natural environment, including its rivers, waterfalls and coastline"
    dest6.Price=1200
    dests=[dest1,dest2,dest3,dest4,dest5,dest6]
    return render(request,"index.html", {'dests':dests})