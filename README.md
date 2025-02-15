# Python Code Reviewer

This repository contains a Python program that reviews pasted Python code and provides a bug report, fixes the code, and explains the changes made.

## Features

- **Bug Report**: The program analyzes the pasted Python code and identifies potential bugs and issues.
- **Code Fixes**: It provides fixed code that addresses the identified issues.
- **Explanation**: It offers a detailed explanation of the changes made to fix the code.

## Installation

To install the required dependencies, run the following command:
```bash
pip install -r requirements.txt
```

## Usage

To use the Python Code Reviewer, follow these steps:

1. Clone this repository:
    ```bash
    git clone gh repo clone kvnk1999/GenAI_Python_Reviewer
    ```

2. Navigate to the project directory:
    ```bash
    cd python-code-reviewer
    ```

3. Run the program:
    ```bash
    python main.py
    ```

4. Paste the Python code you want to review when prompted.

## Example

Here is an example of how the program works:

1. Paste the following Python code:
    ```python
    def add_numbers(a, b):
        return a + b
    print(add_number(1, 2))
    ```

2. The program generates the following bug report:
    ```bash
    Bug Report:
    - NameError: name 'add_number' is not defined. Did you mean 'add_numbers'?
    ```

3. The program provides the fixed code:
    ```python
    def add_numbers(a, b):
        return a + b
    print(add_numbers(1, 2))
    ```

4. Explanation of the changes:
    ```bash
    Explanation:
    - The function name 'add_number' was corrected to 'add_numbers'.
    ```
