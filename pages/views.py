from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request):
      my_context = {
            "my_thing":"kindly enter the title",
            "yours":"This is our description",
            "my_number":123,
            "my_list":["abc",23,21,0,"GET",11,25,4, 105]

      }
      return render(request, "home.html", my_context)
def contact_view(request):
      return render(request, "contact.html")
def about_view(request):
      return render(request, "about.html")
      
