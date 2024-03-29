from django.db import models
from django.utils.safestring import mark_safe
from ckeditor_uploader.fields import RichTextUploadingField
from mptt.models import MPTTModel, TreeForeignKey

class Bölge(MPTTModel):
    STATUS = (
        ('True','Evet'),
        ('False','Hayır'),
    )
    title = models.CharField(max_length=50)
    keyword=models.CharField(max_length=255)
    description=models.CharField(max_length=255)
    status=models.CharField(max_length=10, choices=STATUS)
    slug=models.SlugField()
    parent=TreeForeignKey('self',blank=True,null=True,related_name='children',on_delete=models.CASCADE)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    class MPTTMeta:
        order_insertion_by=['title']

    def __str__(self):
        #return self.title
        full_path=[self.title]
        k=self.parent
        while k is not None:
            full_path.append(k.title)
            k=k.parent
        return '->'.join(full_path[::-1])

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
    detay=RichTextUploadingField()
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    image_tag.short_description='Image'

class Images(models.Model):
    şehirler=models.ForeignKey(Şehirler,on_delete=models.CASCADE)
    title=models.CharField(blank=True,max_length=50)
    image=models.ImageField(blank=True,upload_to='images/')
    def __str__(self):
        return self.title