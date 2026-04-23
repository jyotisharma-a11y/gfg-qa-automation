import json

def test_hello_world():
    assert 1 + 1 == 2

def test_home_page_title():
    # Load the pages.json file
    with open('/home/gfg0931@gfg.geeksforgeeks.org/Documents/gfg-qa-automation/test_data/pages.json', 'r') as file:
        pages = json.load(file)

    # Get the title for the home page
    home_page = pages.get("home", {})
    expected_title = home_page.get("title", "")

    # Simulate opening the home page and getting the title
    # Replace this with actual code to open the page and fetch the title
    actual_title = "Home Page Title"  # Example placeholder

    # Verify the title matches
    assert actual_title == expected_title, f"Expected '{expected_title}', but got '{actual_title}'"