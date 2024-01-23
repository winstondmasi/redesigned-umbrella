from django.db import models

'''
stores basic information about the news articles, 
such as the URL and when it was submitted. 
The URL field is marked as unique to avoid duplicate entries.
'''
class Article(models.Model):
    url = models.URLField(unique=True)  # Store the URL of the news article
    submitted_on = models.DateTimeField(auto_now_add=True)  # Timestamp of when the article was submitted for analysis

    def __str__(self):
        return self.url

'''
stores the results of the analysis. It's linked to the Article model using a ForeignKey,
 which allows multiple analyses for the same article 
 (useful if you want to keep track of how analysis results change over time or with different parameters). 
'''
class ArticleAnalysis(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='analyses')  # Link to the Article model
    analyzed_text = models.TextField()  # Store the text of the article that was analyzed
    bias_score = models.FloatField(null=True, blank=True)  # Store the bias score, if applicable
    accuracy_score = models.FloatField(null=True, blank=True)  # Store the accuracy score, if applicable
    analysis_date = models.DateTimeField(auto_now_add=True)  # Timestamp of when the analysis was performed

    def __str__(self):
        return f"Analysis for {self.article.url} on {self.analysis_date}"

