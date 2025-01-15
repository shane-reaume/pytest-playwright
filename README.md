# python-playwright-coding-examples
A collection of short, focused "recipes" or examples to cover fundamentals of Python in Playwright tests.

## Microsofts "Introduction to Python" Project Overview
- https://vscodeedu.com/courses/intro-to-python

This project contains Playwright test examples that align with the Python fundamentals course structure from vscodeedu.com. Each test file corresponds to a specific lesson, allowing learners to see practical applications of Python concepts in test automation. I wrote these tests to help me learn Python and the Python implementation of Playwright, and I hope they can help you too.

## Setup Requirements
- Python 3.8 or higher
- pip (Python package installer)
- Git

## Installation Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/shane-reaume/python-playwright-coding-examples.git
   cd python-playwright-coding-examples
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
```
├── tests/
│   ├── test_unit_1_core_ideas/           # Unit 1 - Core Ideas
│   │   ├── CORE_IDEAS.md                 # Unit documentation
│   │   ├── test_lesson_1_fundamentals.py
│   │   ├── test_lesson_2_user_interaction.py
│   │   ├── test_lesson_3_values.py
│   │   ├── test_lesson_4_math.py
│   │   ├── test_lesson_5_logic.py
│   │   ├── test_lesson_6_interactive_evaluation.py
│   │   ├── test_lesson_7_variables.py
│   │   ├── test_lesson_8_tracing.py
│   │   ├── test_lesson_9_execution_and_order.py
│   │   ├── test_lesson_10_comments.py
│   │   ├── test_lesson_11_importing_modules.py
│   │   ├── test_lesson_12_strings.py
│   │   ├── test_lesson_13_string_operations.py
│   │   └── test_lesson_14_errors.py
│   ├── test_unit_2_functions/            # Unit 2 - Functions
│   │   ├── FUNCTIONS.md                  # Unit documentation
│   │   ├── test_lesson_1_calling_functions.py
│   │   ├── test_lesson_2_built_in_functions.py
│   │   ├── test_lesson_3_defining_functions.py
│   │   ├── test_lesson_4_testing_functions.py
│   │   ├── test_lesson_5_debugging.py
│   │   ├── test_lesson_6_scopes_and_bodies.py
│   │   ├── test_lesson_7_docstrings.py
│   │   └── test_lesson_8_function_data_flow.py
│   ├── test_unit_3_if/                   # Unit 3 - If Statements
│   │   ├── IF_STATEMENTS.md              # Unit documentation
│   │   ├── test_lesson_1_if_statements.py
│   │   ├── test_lesson_2_truthiness.py
│   │   ├── test_lesson_3_nested_if.py
│   │   └── test_lesson_4_if_patterns.py
│   ├── test_unit_4_structures/           # Unit 4 - Data Structures
│   │   ├── STRUCTURES.md                 # Unit documentation
│   │   ├── test_lesson_1_dataclasses.py
│   │   ├── test_lesson_2_dataclass_operations.py
│   │   ├── test_lesson_3_returning_dataclasses.py
│   │   ├── test_lesson_4_lists.py
│   │   ├── test_lesson_5_list_operations.py
│   │   └── test_lesson_6_mutability.py
│   ├── test_unit_5_for/                  # Unit 5 - For Loops
│   │   ├── FOR_LOOPS.md                  # Unit documentation
│   │   ├── test_lesson_1_for_loops.py
│   │   ├── test_lesson_2_loop_patterns.py
│   │   ├── test_lesson_3_more_loop_patterns.py
│   │   └── test_lesson_4_loop_composition.py
│   ├── test_unit_6_sequences/            # Unit 6 - Sequences
│   │   ├── SEQUENCES.md                  # Unit documentation
│   │   ├── test_lesson_1_indexes.py
│   │   ├── test_lesson_2_string_iteration.py
│   │   ├── test_lesson_3_file_systems.py
│   │   └── test_lesson_4_files.py
│   ├── test_unit_7_nesting/              # Unit 7 - Nesting
│   │   ├── NESTING.md                    # Unit documentation
│   │   ├── test_lesson_1_lists_of_dataclasses.py
│   │   ├── test_lesson_2_nesting_dataclasses.py
│   │   ├── test_lesson_3_nesting_lists.py
│   │   └── test_lesson_4_heavily_nested_data.py
│   └── test_unit_8_time/                 # Unit 8 - Time
│       ├── TIME.md                       # Unit documentation
│       ├── test_lesson_1_while_loops.py
│       ├── test_lesson_2_while_loop_patterns.py
│       ├── test_lesson_3_time_complexity.py
│       ├── test_lesson_4_sorting_and_searching.py
│       └── test_lesson_5_recursion_and_trees.py
├── config.example.py                      # Example configuration file
├── config.py                             # Local configuration (gitignored)
├── pytest.ini                            # Pytest configuration
└── requirements.txt                      # Project dependencies
```

## Running Tests
- Run all tests:
  ```bash
  pytest
  ```
- Run tests in headed mode:
  ```bash
  pytest --headed
  ```
- Run tests for a specific unit:
  ```bash
  pytest tests/test_unit_1_core_ideas/
  ```
- Run tests for a specific lesson:
  ```bash
  pytest tests/test_unit_1_core_ideas/test_lesson_1_fundamentals.py
  ```
- Run tests with debug mode:
  ```bash
  pytest --headed --slowmo 1000
  ```

## Course Structure
Each unit contains multiple lessons, and each lesson has its own test file demonstrating the concepts through practical web automation examples. The tests use the Magento demo site (https://magento.softwaretestingboard.com/) to show real-world applications of Python concepts.

### Units Overview
1. Core Ideas - Basic programming concepts
2. Functions - Working with functions and methods
3. If Statements - Control flow and decision making
4. Data Structures - Working with complex data
5. For Loops - Iteration and repetition
6. Sequences - Working with collections
7. Nesting - Complex data structures
8. Time - Performance and optimization

## Contributing
Feel free to contribute by submitting pull requests or creating issues for improvements.

## License
This project is licensed under the MIT License - see the LICENSE file for details. 