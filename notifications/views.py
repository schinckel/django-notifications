from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_http_methods as allow

from .utils import slug2id
from .models import Notification

@login_required
@allow(['GET'])
def all(request):
    """
    Index page for authenticated user
    """
    return render(request, 'notifications/list.html', {
        'notifications': request.user.notifications.all()
    })

@login_required
@allow(['GET'])
def unread(request):
    return render(request, 'notifications/list.html', {
        'notifications': request.user.notifications.unread()
    })
    
@login_required
@allow(['POST'])
def mark_all_as_read(request):
    request.user.notifications.mark_all_as_read()
    return unread(request)

@login_required
@allow(['POST'])
def mark_as_read(request, slug=None):
    pk = slug2id(slug)

    notification = get_object_or_404(Notification, recipient=request.user, id=pk)
    notification.mark_as_read()
    
    return unread(request)