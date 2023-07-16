# UI_API_Automation_Challenge
This is a sample project with two python files containing UI and API automation scripts for completing a QA challenge.

## Description
This project demonstrates UI testing using Python and Selenium for automating the Google search functionality. It allows you to perform a basic search on the Google website using Selenium WebDriver. The project utilizes pipenv for virtual environment management and environment variables for configuring the URL and search term. 
It also contains a file for API testing the petsStore api using Python, requests and unittest library.

## Prerequisites

- Python 3.x
- Pipenv
- Google Chrome browser

## Installation

1. Clone the repository: git clone https://github.com/your-username/your-project.git
2. Change to the project directory: ``` cd to-the-path-you-cloned-the-project```
3. Install project dependencies using Pipenv: ```pipenv install```
4. Set the environment variables:
- `URL`: The URL of the Google website. (e.g., `https://www.google.com/`)
- `SEARCH_TERM`: The term to search on Google.
- `URL_API`= `https://petstore3.swagger.io/api/v3`
- `API_KEY`= You will need to authorize an API Key to access the API and complete the tests.
- `ENDPOINT`= `/pet`

## Usage

1. Open a Terminal in the project's path

2. Activate the project's virtual environment:
```pipenv shell```

3. Run the UI test script:
```python test_search.py```

4. Run the API test scripts:
```python api_test.py```

## Configuration

- Update the `test_search.py` and/or `api_test.py` scripts to modify the tests scenarios or add additional test cases as required.
- Adjust the environment variables based on your desired Google URL and search terms.

## Considerations
The approach taken to create these automation scripts was a simple one taking into consideration the time and nature of this challenge. However, using test frameworks like pytest or unittest 
(The one briefly used in the api test script) is the best approach on a real project, when the complexity and the different types of test scenarios may arise.
