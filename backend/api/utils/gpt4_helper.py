import openai
import os

# Load your OpenAI API key from an environment variable
openai.api_key = os.getenv('OPENAI_API_KEY')

def analyze_article_with_gpt4(article_content, model="gpt-4"):
    """
    Analyzes the given article content using a specified version of GPT-4.

    Args:
        article_content (str): The textual content of the news article.
        model (str): The GPT-4 model variant to use (e.g., 'gpt-4', 'gpt-4-1106-preview').

    Returns:
        str: The analysis results.
    """
    try:
        prompt = f"Please analyze this news article for bias and factual accuracy: \n\n{article_content}"
        response = openai.Completion.create(
            engine=model,  # Specify the model variant here
            prompt=prompt,
            max_tokens=1
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"An error occurred: {e}"


