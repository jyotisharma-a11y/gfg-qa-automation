class SearchResultsPage:
    def __init__(self, page):
        self.page = page

    def get_url(self):
        return self.page.url

    def has_results(self):
        return self.page.locator("article, h2, .article-list").count() > 0
