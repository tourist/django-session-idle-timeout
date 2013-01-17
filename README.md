# django-session-idle-timeout

A Django middleware application to timeout a logged in user
session after a specified time period.
A django message will be issued if the session gets timed out.

## Requirements

Make sure the following Django apps and middlewares are enabled:
* Authentication (http://docs.djangoproject.com/en/dev/topics/auth/)
* Sessions (http://docs.djangoproject.com/en/dev/topics/http/sessions/)
* Messages framework (http://docs.djangoproject.com/en/dev/ref/contrib/messages/)

```python
INSTALLED_APPS += (
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.messages',
)
```

```python
MIDDLEWARE_CLASSES += (
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)
```

## Installation instructions

Install django-session-idle-timeout
```bash
easy_install django-session-idle-timeout
```

or

```bash
pip install django-session-idle-timeout
```

### Installed apps

```python
INSTALLED_APPS += (
    'django-session-idle-timeout',
)
```

### Middleware

```python
MIDDLEWARE_CLASSES += (
    'django-session-idle-timeout.middleware.SessionIdleTimeout',
)
```

### Settings

SESSION_IDLE_TIMEOUT defines the period after which the session gets timed out in seconds.
The default value is 30min.

```python
SESSION_IDLE_TIMEOUT = 1800
```

## Keepalive Ping

Keeps the session alive as long as the browser window is opened using a javascript ping.

### Urls

Add to your urls.py e.g.:
```python
urlpatterns += (
    url(r'^django-session-idle-timeout/', include('django-session-idle-timeout.urls')),
)
```

### Template

Load the keepalive template tag to start the javascript polling:
```django
{% session_keep_alive %}
{% load session_keep_alive %}
```

## Important
This is a fork of http://github.com/subhranath/django-session-idle-timeout
