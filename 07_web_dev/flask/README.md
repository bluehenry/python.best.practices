#Flask
## install 
```bash
pip install -r requirements.txt
```

## Setup
```bash
export FLASK_APP=app.py
export FLASK_ENV=development
```

## Run
```bash
flask run
```

## Host static files
```bash
http://127.0.0.1:5000/static/ThumbDown.png
```

## Get URL map
```bash
python
import app
app.app.url_map
```

# Model-Template-View pattern
## Jinja templates
(Jinja2)[https://palletsprojects.com/p/jinja/] is a full-featured template engine for Python.
* Componets that displaying data to the user
* Generate text files, like HTML
* Calling templates from view
* Passing data/variables from view to template

## Jinja Variables

## Secruity
* Jinjia will replace "<" and ">" with HTML escape codes to prevent Cross Site Scripting (XSS)
* Use [Flask WTF](https://flask-wtf.readthedocs.io/en/stable/) to prevent Cross Site Request Forgery (CSRF)

## Appy CSS style
* Jinja inheritance

## Deployment
* Dont' use Flask server
* [gunicorn](https://gunicorn.org/)
* User a reverse proxy [ngixn](https://www.nginx.com/)

### install gunicorn
```bash
pip install gunicorn
```

## run gunicorn
```bash
gunicorn app:app
gunicorn -D app:app  # Run as a daemon
```

* gunicorn config file
```bash
  server {
    listen 80;
    server_name example.org;
    access_log  /var/log/nginx/example.log;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
  }
```