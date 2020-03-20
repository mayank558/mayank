from django.shortcuts import render

# Create your views here.
from . models import Destination


def index(request):

    tag='Top Destinations across India'
    # dest1 = Destination()
    # dest1.name = 'Mumbai'
    # dest1.price = 700
    # dest1.image = 'destination_1.jpg'
    # dest1.desc = 'The place that never sleeps'
    # dest1.offer = True
    # dest2 = Destination()
    # dest2.name = 'Rajasthan'
    # dest2.price = 600
    # dest2.image = 'destination_2.jpg'
    # dest2.desc = 'Aao padharo maarhe desh'
    # dest3 = Destination()
    # dest3.name = 'Delhi'
    # dest3.price = 650
    # dest3.image = 'destination_3.jpg'
    # dest3.desc = 'The Capital'
    # dest4 = Destination()
    # dest4.name = 'Bangalore'
    # dest4.price = 650
    # dest4.image = 'destination_4.jpg'
    # dest4.desc = 'Indias Silicon valley'
    # dest5 = Destination()
    # dest5.name = 'Kolkata'
    # dest5.price = 450
    # dest5.image = 'destination_5.jpg'
    # dest5.desc = 'Ami tumha ke bhalo bhasi'
    # dest6 = Destination()
    # dest6.name = 'Gujrat'
    # dest6.price = 500
    # dest6.image = 'destination_6.jpg'
    # dest6.desc = 'Kabhi to padhariye humare Gujrat mai'
    # dest2.offer = False
    # dest3.offer = False
    # dest4.offer = False
    # dest5.offer = False
    # # dest6.offer = False

    dests=Destination.objects.all()
    return render(request, 'index.html', {'dests': dests,'tag':tag})
