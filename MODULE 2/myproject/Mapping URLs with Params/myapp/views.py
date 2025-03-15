from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def drinks(request, drink_name):
    # Step 3: Create a dictionary of drinks with their descriptions
    drinks_dict = {
        'mocha': 'type of coffee',
        'tea': 'type of beverage',
        'lemonade': 'type of refreshment',
        'coffee': 'type of hot drink',  # New entry
    }
    
    # Step 4: Fetch the description based on the drink_name from the dictionary
    choice_of_drink = drinks_dict.get(drink_name, "This drink is not available.")
    
    # Step 5: Return an HttpResponse with dynamic content
    return HttpResponse(f"<h2>{drink_name}</h2> {choice_of_drink}")

