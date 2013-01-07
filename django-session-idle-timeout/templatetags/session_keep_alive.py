# -*- coding: UTF-8 -*-
from django import template
from django.conf import settings

register = template.Library()

def session_keep_alive(context):
    return context.update({
        'interval': int(getattr(settings, 'SESSION_IDLE_TIMEOUT', 1800)) / 2 * 1000,
    })
register.inclusion_tag('session_keep_alive.html', takes_context=True)(session_keep_alive)
