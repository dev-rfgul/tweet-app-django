# Django Tweet App

A Twitter-like application built with Django that allows users to create, view and interact with tweets.

## Table of Contents
- [Setup and Installation](#setup-and-installation)
- [Configuration](#configuration)
- [Creating an App](#creating-an-app)
- [Setting Up Templates](#setting-up-templates)
- [URL Configuration](#url-configuration)
- [Static and Media Files](#static-and-media-files)
- [Creating Models](#creating-models)
- [Setting Up Forms](#setting-up-forms)
- [Creating Views](#creating-views)

## Setup and Installation

1. Initialize your Django project


Run the Followind command in your  `terminal`:

```bash
$ mkdir djangotutorial
```
After creating a folder named `djangotutorial` run this command in terminal to create a project.
```bash
$ django-admin startproject mysite djangotutorial
```
2. Follow the configuration steps below to set up your project properly

## Configuration

### Media Files Configuration


Add the following to your `settings.py`:
we are doing this to include media files , eg imgs, videos etc in our web pages.

```python
import os

# Media files configuration
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

### Static Files Configuration
we are doing this to include static files like , html , css and jquery to our web pages.

Add the following to your `settings.py`:

```python
# Static files configuration
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
```

### Update URLs Configuration

Modify your main `urls.py` to serve media files:
urls.py file handles the routing in our django application

```python
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # Your other URL patterns
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

## Creating an App

1. Create a new Django app:
   ```bash
   python manage.py startapp tweet
   ```

2. Create a `urls.py` file in your app directory with the following content:
   ```python
   from django.urls import path
   from . import views

   urlpatterns = [
       # Your app URL patterns
   ]
   ```

3. Register your app in `settings.py`:
   ```python
   INSTALLED_APPS = [
       # Default Django apps
       'django.contrib.admin',
       'django.contrib.auth',
       'django.contrib.contenttypes',
       'django.contrib.sessions',
       'django.contrib.messages',
       'django.contrib.staticfiles',
       
       # Your apps
       'tweet',
   ]
   ```

## Setting Up Templates

1. Configure the templates directory in `settings.py`:
   ```python
   TEMPLATES = [
       {
           'BACKEND': 'django.template.backends.django.DjangoTemplates',
           'DIRS': [os.path.join(BASE_DIR, 'templates')],
           'APP_DIRS': True,
           'OPTIONS': {
               'context_processors': [
                   'django.template.context_processors.debug',
                   'django.template.context_processors.request',
                   'django.contrib.auth.context_processors.auth',
                   'django.contrib.messages.context_processors.messages',
               ],
           },
       },
   ]
   ```

2. Create a `templates` folder in your app directory for app-specific templates
3. Create a `templates` folder in your main project directory for base templates

## URL Configuration

Update your main `urls.py` to include your app's URLs:

```python
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tweet/', include('tweet.urls')),
    # You can customize the path prefix as needed
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

## Static and Media Files

1. Create a `static` folder in your main project directory for static files (CSS, JS, images)
2. Create a `media` folder for user-uploaded content

## Creating Models

Define your models in the app's `models.py`:

```python
from django.db import models
from django.contrib.auth.models import User

class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=240)
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.user.username}-{self.text[:20]}'
```

Register your models in `admin.py`:

```python
from django.contrib import admin
from .models import Tweet

admin.site.register(Tweet)
```

Apply migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

## Setting Up Forms

Create a `forms.py` file in your app directory:

```python
from django import forms
from .models import Tweet

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['text', 'photo']
```

## Creating Views

Update your app's `views.py`:

```python
from django.shortcuts import render, get_object_or_404
from .models import Tweet
from .forms import TweetForm

def home(request):
    tweets = Tweet.objects.all().order_by('-created_at')
    return render(request, 'tweet/index.html', {'tweets': tweets})

# Add more views as needed
```

## Running the Server

Start the development server:

```bash
python manage.py runserver 8000
```

Visit http://localhost:8000/ to view your app.

## License

[Your License]

## Acknowledgements

This project was created by following a YouTube tutorial.