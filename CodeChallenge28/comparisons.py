def sort_by_year(movies):
    return sorted(movies, key=lambda movie: movie['year'], reverse=True)

def sort_by_title(movies):
    return sorted(movies, key=lambda movie: remove_articles(movie['title']))

def remove_articles(title):
    for article in ["A ", "An ", "The "]:
        if title.startswith(article): return title[len(article):]
    return title
