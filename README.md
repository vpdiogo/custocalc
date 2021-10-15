# About Project

This project consists of a phone call rate simulator system. The page shows a list comparing the values.

## Install

Create a directorie to the project:

```
mkdir falemais-project
```

Inside 'falemais-project', install a virtual environment and initialize it:

Lunix or Mac
```
python3 -m venv env
source env/bin/activate
```
Windows
```
py -m venv env
.\env\Scripts\activate
```

Download repositorie:

```
git clone https://github.com/vpdiogo/falemais.git
```

Install dependencies:

```
cd falemais
make install
```

Create the file for SECRET KEY:

```
touch .secrets.toml
```
Inside the created file, write:

```
[default]
SECRET_KEY = 'your-secret-key'
```
## Testing

In root of the project:

```
make test
```

## Execute 
For initialize the application, inside directory from app.py:

```
export FLASK_ENV=development
export FLASK_APP=app.py
flask run
```

## Suggestions

If you haven't Git and Python 3 installed, folow the ULR to download them:
- https://www.python.org/
- https://git-scm.com/

If you use Windows, install Windows Subsystem for Linux in:
- https://docs.microsoft.com/en-us/windows/wsl/install 
