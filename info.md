vevn 
venv/activate
install django
 django-admin startproject core .
py manage.py startapp store
py manage.py makemigrations
py manage.py migrate

settings - import os, create BASE_DIR for media

urls.py - from django.conf import settings
from django.conf.urls.static import static

admin.py register models

py manage.py createsuperuser

py manage.py runserver
pip install coverage


coverage run manage.py test
coverage run --omit='*/venv/*' manage.py test
coverage report
coveage html

py manage.py test

pip install flake8-isort
flake8
setup.cfg




   <!-- <nav class="navbar navbar-expand-md navbar-light bg-white border-bottom">
            <div class="container-fluid">
                <a class="navbar-brand" href="/">BookStore</a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarCollapse"
                    aria-controls="navbarCollapse" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="navbarCollapse">
                    <ul class="navbar-nav me-auto mb-2 mb-md-0">
                        <li class="nav-item dropdown">
                            <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button"
                                data-bs-toggle="dropdown" aria-expanded="false">
                                Library
                            </a>
                            <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
                                <li><a class="dropdown-item" href="{% url "store:product_all" %}">All</a></li>
                                {% for c in categories %}
                                <li {% if category.slug == c.slug %}class="selected" {% endif %}>
                                    <a class="dropdown-item" href="{{ c.get_absolute_url }}">{{ c.name|title }}</a>
                                </li>
                                {% endfor %}
                            </ul>
                        </li>
                    </ul>
                </div>
            </div>
        </nav> -->