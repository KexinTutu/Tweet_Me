from django.contrib.auth.models import User
from django.db import models


class Friendship(models.Model):
    from_user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name='followings'
    )
    to_user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name='followers'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (('from_user_id', 'to_user'),) #is from_user ok?
        index_together = (
            # to get all my followings, when from_user is me
            ('from_user_id', 'created_at'),
            # to get all my followers, when to_user is me
            ('to_user_id', 'created_at'),
        )

    def __str__(self):
        return f'{self.from_user_id} followed {self.to_user_id}'

