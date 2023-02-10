from django.db import models

# Create your models here.
class Post(models.Model):
      title = models.CharField(max_length=255)
      content = models.TextField()
      publish_date = models.DateTimeField(auto_now_add=True)
      author = models.ForeignKey('Author', on_delete=models.CASCADE)
      views = models.IntegerField(default=0)
      likes = models.IntegerField(default=0)
      time_to_read = models.IntegerField(default=0)
      tags = models.ManyToManyField('Tag', related_name='post_set', null=True, blank=True)


      def __str__(self):
            return str(self.title)


class Author(models.Model):
      name = models.CharField(max_length=255)
      email = models.EmailField(max_length=100, unique=True)
      dob = models.DateField()
      # profile_pic = models.ImageField()
      # all_posts = models.ManyToManyField('Post', related_name='author_set' null=True, blank=True)
      favorites = models.ManyToManyField('Post', related_name='favorite_of_authors', null=True, blank=True)

      def __str__(self):
            return str(self.name)


class Comment(models.Model):
      author = models.ForeignKey('Author', on_delete=models.CASCADE)
      post = models.ForeignKey('Post', on_delete=models.CASCADE)
      body = models.TextField()
      publish_date = models.DateTimeField(auto_now_add=True)
      parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')

      def __str__(self):
            return str(self.body)


class Tag(models.Model):
      name = models.CharField(max_length=100)

      def __str__(self):
            return str(self.name)
