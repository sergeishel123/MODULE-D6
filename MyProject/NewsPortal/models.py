from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE)
    user_rating = models.IntegerField(default = 1)
    def name(self):
        self.user_rating = 0
        for i in self.post_set.all():
            self.user_rating += i.rating
            for k in i.comment_set.all():
                self.user_rating += k.rating
        for j in self.user.comment_set.all():
            self.user_rating += j.rating
        self.save()



class Category(models.Model):
    name = models.CharField(max_length = 255,unique = True)

array = [('N','News'), ('A','Article')]
class Post(models.Model):
    author_post = models.ForeignKey(Author,on_delete = models.CASCADE)
    type = models.CharField(max_length = 1,choices = array)
    time_in = models.DateTimeField(auto_now_add = True)
    category_post = models.ManyToManyField(Category,through = 'PostCategory')
    heading = models.CharField(max_length = 255)
    text = models.TextField()
    rating = models.IntegerField(default = 0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        return f'{self.text[:124]}...'

    def __str__(self):
        return  f' "{self.text}"'


class PostCategory(models.Model):
    post = models.ForeignKey(Post,on_delete = models.CASCADE)
    category = models.ForeignKey(Category,on_delete = models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete = models.CASCADE)
    user = models.ForeignKey(User,on_delete= models.CASCADE)
    text = models.TextField()
    time_in = models.DateTimeField(auto_now_add = True)
    rating = models.IntegerField(default = 0)

    def like(self):
        self.rating += 1
        self.save()
    def dislike(self):
        self.rating -= 1
        self.save()









# Create your models here.
