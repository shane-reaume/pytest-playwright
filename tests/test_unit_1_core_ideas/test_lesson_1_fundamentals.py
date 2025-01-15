"""
Lesson 1 - Fundamentals
Objectives:
Upon completion of this lesson, you'll be able to:

Define the terms Computer Science, programs, and programming.
Explain abilities and limitations of programs.
Recognize synonyms for programs and execution.
Justify the use of Python compared to other language options.
"""

from playwright.sync_api import Page

class TestLesson1Fundamentals:
    def test_hello_world(self, page: Page, capsys):
        """
        The goal of this Challenge is to write a short program in Python that 
        prints out the phrase "Hello world!"
        """
        # Execute the actual print statement - this is the code we're testing
        print("Hello World!")
        
        # Get the captured output and verify it
        captured = capsys.readouterr()
        assert captured.out.strip() == "Hello World!"

    def test_comments(self, page: Page, capsys):
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