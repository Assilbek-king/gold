from django.db import models

# Create your models here.
#
# class Category(models.Model):
#     title = models.CharField(max_length=300, blank=True)
#
#
#     def __str__(self):
#         return f'{self.title}'

class Tovar(models.Model):
    logo = models.ImageField(upload_to='upload', blank=True)
    title = models.CharField(max_length=300, blank=True)
    description = models.TextField(max_length=500, blank=True)
    # cat = models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True)
    price = models.IntegerField(default=0, blank=True)
    status = models.IntegerField(default=0, blank=True)
    # img1 = models.ImageField(upload_to='upload', blank=True)
    # img2 = models.ImageField(upload_to='upload', blank=True)
    # img3 = models.ImageField(upload_to='upload', blank=True)
    # img4 = models.ImageField(upload_to='upload', blank=True)
    # img5 = models.ImageField(upload_to='upload', blank=True)


    def __str__(self):
        return f'{self.title}'

class Photo(models.Model):
    logo = models.ImageField(upload_to='upload', blank=True)
    # title = models.CharField(max_length=300, blank=True)
    # description = models.TextField(blank=True)

    def __str__(self):
        return f'{self.logo}'


# class Partner(models.Model):
#     logo = models.ImageField(upload_to='upload', blank=True)
#     title = models.CharField(max_length=300, blank=True)
#
#     def __str__(self):
#         return f'{self.logo}'


class Feedback(models.Model):
    name = models.CharField(max_length=300, blank=True)
    phone = models.CharField(max_length=15, blank=True)
    comment = models.TextField(blank=True,null=True)

    def __str__(self):
        return f'{self.name} {self.phone}'

# class Otziv(models.Model):
#     name = models.CharField(max_length=300, blank=True)
#     comment = models.TextField(blank=True,null=True)
#
#     def __str__(self):
#         return f'{self.name}'

# class Service(models.Model):
#     title = models.CharField(max_length=300, blank=True)
#     logo = models.ImageField(upload_to='upload', blank=True)
#     mini_description = models.TextField(max_length=500, blank=True)
#
#     def __str__(self):
#         return f'{self.title} '
