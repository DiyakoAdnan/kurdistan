from django.shortcuts import render
# About Page
def about(request):
    context = {
        "title": "About Kurdistan Tourism",
        "description": "Kurdistan is a region rich in history, culture, and natural beauty. It offers a unique blend of ancient traditions and modern attractions, making it a must-visit destination."
    }
    return render(request, 'about.html', context)
# Homepage - Kurdistan Tourism Overview
def home(request):
    context = {
        "title": "Explore Kurdistan",
        "highlights": [
            "Rich cultural heritage",
            "Stunning mountain landscapes",
            "Ancient historical sites",
        ],
    }
    return render(request, 'index.html', context)

# Sulaymaniyah Touristic Sites
def sulaymaniyah(request):
    attractions = [
        {
            "name": "Ahmed Awa Waterfall",
            "image": "ahmed_awa.jpg",
            "desc": "A breathtaking waterfall in the mountains near Sulaymaniyah."
        },
        {
            "name": "Azmar Mountain",
            "image": "azmar_mountain.jpg",
            "desc": "Perfect for hiking with panoramic views of the city."
        },
    ]
    return render(request, 'sulaymaniyah.html', {'attractions': attractions})

# Hawler (Erbil) Touristic Sites
def hawler(request):
    attractions = [
        {
            "name": "Erbil Citadel",
            "image": "erbil_citadel.jpg",
            "desc": "A UNESCO World Heritage Site with 6,000 years of history."
        },
        {
            "name": "Sami Abdulrahman Park",
            "image": "sami_park.jpg",
            "desc": "A vast green space ideal for picnics and relaxation."
        },
    ]
    return render(request, 'hawler.html', {'attractions': attractions})




# Contact Page (Bonus)
def contact(request):
    return render(request, 'contact.html')