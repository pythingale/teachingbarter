from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_extensions.db.models import TimeStampedModel

from wall.models import UserWall

User = get_user_model()


class CommentBox(TimeStampedModel):
    wall = models.OneToOneField(
        UserWall, on_delete=models.CASCADE, related_name="comment_box"
    )
    comments_number = models.PositiveIntegerField(default=0)

    @receiver(post_save, sender=UserWall)
    def create_comment_box(sender, instance, created, **kwargs):
        if created:
            CommentBox.objects.create(wall=instance)

    def __str__(self):
        return self.wall.user.username


class Comment(TimeStampedModel):
    comment_box = models.ForeignKey(
        CommentBox, on_delete=models.CASCADE, related_name="comment"
    )
    sender = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="comment_sender",
    )
    comment = models.CharField(max_length=300)
    likes = models.IntegerField(default=0)
    likers = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.comment


@receiver(post_save, sender=Comment)
def update_comment_numbers(sender, instance=None, **kwargs):

    comment_box = CommentBox.objects.get(id=instance.comment_box.id)
    comment_box.comments_number = Comment.objects.filter(
        comment_box=comment_box
    ).count()
    comment_box.save()


class Reply(TimeStampedModel):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    sender = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="reply_sender"
    )
    reply = models.CharField(max_length=300)

    def __str__(self):
        return self.reply
