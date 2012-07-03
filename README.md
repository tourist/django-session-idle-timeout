django-session-idle-timeout
===========================

A Django middleware application to timeout a logged in user 
session after a specified time period.

Installation instructions
-------------------------

Make sure the following Django apps/middlewares are enabled.

- Authentication (http://docs.djangoproject.com/en/dev/topics/auth/)
- Sessions (http://docs.djangoproject.com/en/dev/topics/http/sessions/)
- Messages framework (http://docs.djangoproject.com/en/dev/ref/contrib/messages/)

Install django-session-idle-timeout

    easy_install django-session-idle-timeout

Update the *MIDDLEWARE_CLASSES* on the *settings.py*. Add the 
`sessions.middleware.SessionIdleTimeout` at the bottom.

    MIDDLEWARE_CLASSES = (
        ...
        'sessions.middleware.SessionIdleTimeout',
        )

Update the *INSTALLED_APPS*. Add 'sessions'.

Add a new entry named 'SESSION_IDLE_TIMEOUT', and specify the idle 
timeout period, in seconds. The default value is 30min.

    SESSION_IDLE_TIMEOUT = 1800

That's it, you will receive a session timeout message using 
the Django message framework in your templates.



Important
---------

This is a for of http://github.com/subhranath/django-session-idle-timeout
