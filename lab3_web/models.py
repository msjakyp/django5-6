from django.db import models

class Articles(models.Model):
    picture = models.ImageField('image', upload_to='lab3_web/static/images')
    title = models.CharField('Flowers', max_length=50)
    price = models.CharField('Price', max_length=250)

    def __str__(self):
        return self.title