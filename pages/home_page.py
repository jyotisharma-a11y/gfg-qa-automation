from utils.constants import BASE_URL

class HomePage:
    URL = f"{BASE_URL}/"

    def __init__(self, page):
        self.page = page
        self.logo = page.get_by_role("link", name="GeeksforGeeks")
        self.search_input = page.locator("input[type='search']").first
        self.nav_courses = page.get_by_role("link", name="Courses")

    def goto(self):
        self.page.goto(self.URL)
        self.page.wait_for_load_state("domcontentloaded")

    def get_title(self):
        return self.page.title()

    def is_logo_visible(self):
        return self.logo.is_visible()

    def search(self, query):
        self.search_input.fill(query)
        self.page.keyboard.press("Enter")
        self.page.wait_for_load_state("networkidle")