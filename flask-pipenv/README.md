# How to use this app

1. Install pipenv `pip install --user pipenv`.
2. Install dependencies with `pipenv install`.
3. Activate the virtual environment with `pipenv shell`
4. Run the application with `python index.py`.
5. To convert Pipfile to requirements.txt for App Service run `pipenv run pip freeze > requirements.txt` or `pipenv lock -r > requirements.txt`