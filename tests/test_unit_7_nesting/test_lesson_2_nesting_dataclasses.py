"""
Lesson 2 - Nesting Dataclasses
Objectives:
- Describe how dataclasses can be nested as attributes of other dataclasses
- Describe how lists can be nested as attributes of dataclasses
- Create instances of dataclasses that have dataclasses inside
- Use attribute access to access data nested in multiple layers of dataclasses
- Use attribute access and list indexing to access data nested in lists inside of dataclasses
- Use temporary variables to organize nested attribute access
- Predict the behavior of updating nested attribute access, regular attribute access, and variables for values on the heap
- Interpret a stack/heap diagram that shows nested dataclasses
- Identify the order in which nested dataclasses should be defined
- Justify a particular level of nesting when designing dataclasses
"""

from playwright.sync_api import Page, expect

class TestLesson2NestingDataclasses:
    def test_nesting_dataclasses(page: Page):
        """
        Setup tests and outside methods to demonstrate requirements of this lesson.
        """
        pass
