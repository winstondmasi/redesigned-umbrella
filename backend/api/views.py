from django.http import JsonResponse
from rest_framework.decorators import api_view
from .utils.gpt4_helper import analyze_article_with_gpt4
import requests
from bs4 import BeautifulSoup
from django.shortcuts import render

def home(request):
    # Logic to render the home page
    return render(request, 'index.html')


@api_view(['POST'])
def analyze_article(request):
    # Extract the URL from the POST request
    article_url = request.data.get('url')
    
    article_content = fetch_article_content(article_url)

    # Analyze the article content using GPT-4
    analysis_results = analyze_article_with_gpt4(article_content)

    # Return the analysis results as JSON
    return JsonResponse({'analysis': analysis_results})

def fetch_article_content(url):
    try:
        # Send a request to the URL
        response = requests.get(url)

        # If the request was successful, process the response
        if response.status_code == 200:
            # Parse the HTML content of the page
            soup = BeautifulSoup(response.content, 'html.parser')

            # Extract the main content of the article
            # This part highly depends on the structure of the news website
            # and might require custom logic for different sites
            article_content = soup.find('div', class_='article-content').get_text(strip=True)

            return article_content
        else:
            return "Error: Unable to fetch the article."
    except Exception as e:
        return f"An error occurred: {e}"