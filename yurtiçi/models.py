from django.db import models
from django.utils.safestring import mark_safe


class Bölge(models.Model):
    STATUS = (
        ('True','Evet'),
        ('False','Hayır'),
    )
    title = models.CharField(max_length=50)
    keyword=models.CharField(max_length=255)
    description=models.CharField(max_length=255)
    image=models.ImageField(blank=True,upload_to='images/')
    status=models.CharField(max_length=10, choices=STATUS)
    slug=models.SlugField()
    parent=models.ForeignKey('self',blank=True,null=True,related_name='children',on_delete=models.CASCADE)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Şehirler(models.Model):
    STATUS = (
        ('True','Evet'),
        ('False','Hayır'),
    )
    bölge=models.ForeignKey(Bölge,on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    keyword=models.CharField(max_length=255)
    description=models.CharField(max_length=255)
    image=models.ImageField(blank=True,upload_to='images/')
    status=models.CharField(max_length=10, choices=STATUS)
    şehir=models.TextField()
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    image_tag.short_description='Image'

class Images(models.Model):
    şehirler=models.ForeignKey(Şehirler,on_delete=models.CASCADE)
    title=models.CharField(max_length=50)
    image=models.ImageField(blank=True,upload_to='images/')
    def __str__(self):
        return self.title