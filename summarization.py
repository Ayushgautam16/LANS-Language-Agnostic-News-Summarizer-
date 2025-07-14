from newspaper_extraction import extract_article_text
from lsa_summarizer import LsaSummarizer
import nltk

from nltk.corpus import stopwords

def summarize_text(text, summary_length=50, language='english'):
    summary=""
    nltk.download("punkt", quiet=True)
    nltk.download("stopwords", quiet=True)

    summarizer = LsaSummarizer()
    stopwords_list = stopwords.words(language)
    summarizer.stop_words = stopwords_list

    summary = summarizer(text, summary_length)

    return str(summary)

def summarize_news_article(url):
    # extracted text
    article_text = extract_article_text(url)
    
    # summarizing
    summarized_text = summarize_text(article_text)
    
    return summarized_text
