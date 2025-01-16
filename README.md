# pytest-playwright

A setup that allows you to write and run Playwright tests using Pytest with these key features:

- Fixtures to launch and close the browser per test or per class
  - `luma_test_page` logs into our Luma demo site every test
  - `luma_test_page_class` logs into our Luma demo site once per class
- Clean use of `describe` and `it` blocks for test organization
  - Similar to Jest, Mocha, and other JS testing frameworks
- Simple command-line interface to run tests with various options

## Setup Requirements
- Python 3.8 or higher
- pip (Python package installer)
- Git

## Installation Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/shane-reaume/pytest-playwright.git
   cd pytest-playwright
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Install the required browsers:
   ```bash
   playwright install
   ```

## Project Structure
```
pytest-playwright/
├── tests/
│   ├── test_examples/
│   │   ├── test_unit_only.py    # Basic unit test examples
│   │   └── test_login_scope.py  # Browser login scope examples
│   └── conftest.py              # Shared test fixtures and configurations
├── scripts.py                   # Test runner script
├── pytest.ini                   # Pytest configuration
└── requirements.txt            # Project dependencies
```

## Running Tests
We provide a simple command-line interface through `scripts.py` to run tests:

### Basic Usage
```bash
python scripts.py run <test_name>
```

### Available Test Commands
- Run all tests:
  ```bash
  python scripts.py run all
  ```
- Run all tests in test_examples directory:
  ```bash
  python scripts.py run test_examples
  ```
- Run specific test files:
  ```bash
  python scripts.py run test_unit_only
  python scripts.py run login_scope
  ```

### Test Options
Add these flags to any test command:
- `--headed`: Run tests in headed mode (visible browser)
  ```bash
  python scripts.py run all --headed
  ```
- `--debug`: Run tests in debug mode (slower execution)
  ```bash
  python scripts.py run all --debug
  ```

### Help
To see all available commands and options:
```bash
python scripts.py help
```

## Test Organization
We use descriptive test organization with:
- `@describe`: Marks a class as a test suite description
- `@it`: Marks a test method with a description of what it tests

Example:
```python
@describe("Browser app test")
class TestBrowserApp:
    @it("navigates to 'What's New' when logged in")
    def test_whats_new(self, luma_test_page):
        # Test code here
```

## Available Fixtures
- `luma_test_page`: Fresh login for each test
- `luma_test_class_page`: Single login shared across test class

## Contributing
Feel free to contribute by submitting pull requests or creating issues for improvements.

## License
This project is licensed under the MIT License - see the LICENSE file for details. 