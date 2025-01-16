# pytest-playwright
A setup that allows you to write and run Playwright tests using Pytest with these key features:

- fixtures to launch and close the browser per test or per class
  - `luma_test_page` logs into our Luma demo site every test
  - `luma_test_page_class` logs into our Luma demo site once per class
- Clean use of `describe` and `it` blocks for test organization
  - similar to Jest, Mocha, and other JS testing frameworks we are used to

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
5. Configure test credentials:
   ```bash
   cp config.example.py config.py
   ```
   Then edit `config.py` with your actual test credentials (this file is gitignored)

## Project Structure

## Running Tests
- Run all tests:
  ```bash
  pytest
  ```
- Run tests in headed mode:
  ```bash
  pytest --headed
  ```
- Run tests for a specific group:
  ```bash
  pytest tests/examples/
  ```
- Run tests for a specific file:
  ```bash
  pytest tests/examples/test_login_scope.py
  ```
- Run tests with debug mode:
  ```bash
  pytest --headed --slowmo 1000
  ```

## Contributing
Feel free to contribute by submitting pull requests or creating issues for improvements.

## License
This project is licensed under the MIT License - see the LICENSE file for details. 