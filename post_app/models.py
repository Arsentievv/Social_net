from django.db import models
from profile_app.models import Profile
from django.core.validators import FileExtensionValidator


class Post(models.Model):
    content = models.TextField()
    image = models.ImageField(
        upload_to='posts', validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])], blank=True
    )
    liked = models.ManyToManyField(Profile, related_name='likes', blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Profile, related_name='posts', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.content[:20])

    def num_likes(self):
        return self.liked.all().count()

    def num_comments(self):
        return self.comments_post.all().count()

    class Meta:
        ordering = ('-created', )


class Comment(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='comments_user')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments_post')
    body = models.TextField(max_length=300)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.pk)

LIKE_CHOICES = (
    ('Like', 'Like'),
    ('Unlike', 'Unlike')
)

class Like(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='likes_user')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes_post')
    value = models.CharField(max_length=8, choices=LIKE_CHOICES)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} - {self.post} - {self.value}'

