from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.urls import reverse


# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Post(models.Model):
    slug = models.SlugField(unique=True, db_index=True)
    title = models.CharField(max_length=100)
    excerpt = models.CharField(max_length=150)
    date = models.DateField(verbose_name="Date", auto_now=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="posts"
    )
    content = models.TextField(
        max_length=1000,
        validators=[MinLengthValidator(50, message="Should be more than 50 characters.")],
    )
    tags = models.ManyToManyField(Tag)  # add related name

    def save(self) -> None:
        self.slug = slugify(self.title)
        return super().save()

    # def get_absolute_url(self):
    #     return reverse("post-detail", kwargs={"pk": self.pk})
    

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(max_length=100)
    date = models.DateTimeField(auto_now=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comment")
