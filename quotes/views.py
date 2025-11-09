from django.shortcuts import render
from .models import Quote
import random

# fallback static quotes if DB is empty
FALLBACK_QUOTES = [
    ("The best way to predict the future is to create it.", "Peter Drucker"),
    ("Do what you can, with what you have, where you are.", "Theodore Roosevelt"),
    ("The only limit to our realization of tomorrow is our doubts of today.", "Franklin D. Roosevelt"),
    ("Start where you are. Use what you have. Do what you can.", "Arthur Ashe"),
    
]

def index(request):
    qs = list(Quote.objects.all())
    if qs:
        quote = random.choice(qs)
        text, author = quote.text, quote.author
    else:
        text, author = random.choice(FALLBACK_QUOTES)
    return render(request, 'quotes/index.html', {'text': text, 'author': author})