# HTML extractor
This repo is containing a Python program, that gets the url, opens it, gets the HTML website content,
and extracts the last element of the unordered list if the HTML document contains one.

## Running the project
In order to run the project:
1. Clone this github repository
2. Make sure to use Python 3.8.5 or higher
3. After cloning the repository on your local machine, enter the project folder and run:
    -   ```
        python -m venv .venv
        ```
    - On Windows machine using Powershell:
        ```
        .\.venv\Scripts\Activate.ps1   
        ```
        For other systems see: https://docs.python.org/3/library/venv.html
4. After activating the virtual environment:
    -   Running the program 
        ```
            python src\main.py
        ```
    - Running the tests:
        - Make sure you have `pytest` installed with
        ```
            python -m pytest tests
        ```