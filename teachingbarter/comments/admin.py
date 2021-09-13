from django.contrib import admin

from .models import Comment, CommentBox, Reply

admin.site.register(CommentBox)
admin.site.register(Comment)
admin.site.register(Reply)
