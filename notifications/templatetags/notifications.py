# -*- coding: utf-8 -*-
from django.template import Library
from django.template.base import TemplateSyntaxError
from django.template import Node

register = Library()

@register.simple_tag(takes_context=True)
def notifications_unread_count(context):
    if 'user' not in context:
        return ''
    
    user = context['user']
    if user.is_anonymous():
        return ''
    return user.notifications.unread().count()

@register.inclusion_tag('notifications/count.html', takes_context=True)
def notifications_unread_count_badge(context):
    return {
        'unread_count': context['user'].notifications.unread().count()
    }

@register.inclusion_tag('notifications/list.html', takes_context=True)
def all_notifications(context):
    return {
        'notifications': context['user'].notifications.all()
    }

@register.inclusion_tag('notifications/list.html', takes_context=True)
def unread_notifications(context):
    return {
        'notifications': context['user'].notifications.unread()
    }

