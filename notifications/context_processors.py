def unread_notifications(request):
    if request.user.notifications:
        unread = request.user.notifications.unread()
    
        return {
            'unread_notifications': unread,
            'unread_notifications_count': unread.count()
        }
    
    return {}