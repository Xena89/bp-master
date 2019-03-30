# Aufgabenverwaltung besser machen! 
[![Build Status](https://travis-ci.com/frederikroeper/bp.svg?branch=master)](https://travis-ci.com/frederikroeper/bp)
[![Coverage Status](https://coveralls.io/repos/github/frederikroeper/bp/badge.svg?branch=master)](https://coveralls.io/github/frederikroeper/bp?branch=master)



# Befehle

Um den Server zu starten, innerhalb des /mysite Ordners folgenden Befehl ausführen:
```
python3 manage.py runserver
```

Um die Datenbank zu aktualisieren folgenden zwei Befehl ausführen:
```
python3 manage.py makemigrations
```
```
python3 manage.py migrate
```

Um eine App zustarten folgenden Befehl ausführen (ohne Anführungszeichen):
```
python3 manage.py startapp "appname"
```

# Install crispy forms

Install latest stable version into your python path using pip or easy_install:
```
pip install --upgrade django-crispy-forms
```
# Pytest

```
  py.test
  
```
# Install Selenium 

download the chromedriver computer from this site: http://chromedriver.storage.googleapis.com/index.html?path=2.15/

```
pip install selenium

pip install webdriver-manager


>>>from selenium import webdriver
>>>from webdriver_manager.chrome import ChromeDriverManager
>>>driver = webdriver.Chrome(ChromeDriverManager().install())

```
