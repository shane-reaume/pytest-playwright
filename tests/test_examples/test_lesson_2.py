from playwright.sync_api import Page
from conftest import describe, it

@describe("Exercise 2")
class TestExercise2:
    @it("Should validate hello world")
    def test_hello_world(self, capsys, page: Page):
        """
        The goal of this Challenge is to write a short program in Python that 
        prints out the phrase "Hello world!"
        """
        # Execute the actual print statement - this is the code we're testing
        print("Hello World!")
        
        # Get the captured output and verify it
        captured = capsys.readouterr()
        assert captured.out.strip() == "Hello World!"

    @it("Should validate comments")
    def test_comments(self, capsys, page: Page):
        """
        The goal of this Challenge is to write a short program in Python that 
        comments out the print statement that prints "Hello world!"
        """
        # observe comments are # and als""
        # print("Hello World!")
        
        # Get the captured output and verify it
        captured = capsys.readouterr()
        # The output should not contain "Hello World!"
        assert captured.out.strip() != "Hello World!"
      

    @it("Should validate types")
    def test_types(self, capsys, page: Page):
        """
        The goal of this Challenge is to verify Python's basic data types
        """
        # None type
        assert type(None) is None.__class__

        # Boolean types
        assert type(True) is bool
        assert type(False) is bool

        # Numeric types
        assert type(1) is int
        assert type(1.0) is float

        # String types (all variations are str type)
        assert type("Hello") is str
        assert type('Hello') is str
        assert type("""Hello""") is str
        assert type('''Hello''') is str

        # isinstance is a built-in function that checks if an object is an instance of a class
        assert isinstance(None, type(None))
        assert isinstance(True, bool)
        assert isinstance(1, int)
        assert isinstance(1.0, float)
        assert isinstance("Hello", str)

    @it("Should validate playwright page with unit tests")
    def test_playwright_page_with_unit_tests(self, page: Page):
        """
        The goal of this Challenge is to write a short program in Python that 
        takes input from the user and prints it out
        """
        assert isinstance(1, int)
        page.goto("https://www.google.com")
        assert page.title() == "Google"
        assert isinstance("Hello", str)

@describe("Browser app test - per test")
class TestBrowserApp:
    @it("navigates to 'What's New' when logged in fresh each time")
    def test_whats_new(self, luma_test_page):
        luma_test_page.goto("https://magento.softwaretestingboard.com/what-is-new.html")
        assert "What's New" in luma_test_page.title()

    @it("navigates to 'Gear' also with fresh login")
    def test_gear(self, luma_test_page):
        luma_test_page.goto("https://magento.softwaretestingboard.com/gear.html")
        assert "Gear" in luma_test_page.title()

@describe("Browser app test - single login per class")
class TestBrowserAppClassScope:
    @it("navigates to 'What's New' and stays logged in across tests")
    def test_whats_new(self, luma_test_class_page):
        luma_test_class_page.goto("https://magento.softwaretestingboard.com/what-is-new.html")
        assert "What's New" in luma_test_class_page.title()

    @it("navigates to 'Gear' and is still logged in")
    def test_gear(self, luma_test_class_page):
        luma_test_class_page.goto("https://magento.softwaretestingboard.com/gear.html")
        assert "Gear" in luma_test_class_page.title()