from django.db import models
from django.utils import timezone
from django.urls import reverse
# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete = models.CASCADE)
    # This mean with each SuperUser
    # we create. We crete a user wo
    # an author of this Post object
    title = models.CharField(max_length =200) #?
    text = models.TextField()
    created_date = models.DateTimeField(default = timezone.now())
    # this save the information of date created with timezone module
    # This timezone is effected by settings.py TIME_ZONE variable.
    # So don't forget to change the timezone there.
    published_date = models.DateTimeField(blank = True, null = True)
    # blank = True as some time we haven't wanted the post to be published
    # yet. So the blank help it stay in Daft. The null = True will
    # This will make more sense later when we run the blog.
    def publish(self):
        self.published_date = timezone.now()
        self.save()
        # I don't remember much about this save.
        # Which are savable and which are not ?
        # Which need commit = False ? And why commit = False?

    def approve_comments(self):
        return self.comments.filter(approved_comment = True)
        # this let only the approved comments to appear

    def get_absolute_url(self):
        return reverse('blog:post_detail', kwargs={'pk':self.pk})

    def __str__(self):
        return self.text
        # Hey, what is this name ? We haven't created This
        # Is it a auth.User's attribute ?

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name = 'comments', on_delete = models.CASCADE)
    # So this mean we now have 2 way to call a ForeignKey:
    # 1/ use exact the name of models we imported.
    # 2/ Neme 'the_app_it_belong.name_of_the_modle'
    author = models.CharField(max_length = 200)
    text = models.TextField()
    create_date = models.DateTimeField(default = timezone.now())
    approved_comment = models.BooleanField(default = False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
        return reverse('blog:post_list')

    def __str__(self):
        return self.text
