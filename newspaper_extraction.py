from newspaper import Article

def extract_article_text(url):
    article = Article(url)
    article.download()
    article.parse()
    return article.text
