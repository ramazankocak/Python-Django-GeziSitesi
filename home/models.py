from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

#blank=True eklenirse boş bırakılabilir.
from django.forms import ModelForm, TextInput, Textarea


class Setting(models.Model):
    #status , sitenin durumu
    STATUS = (
        ('True','Evet'),
        ('False','Hayır'),
    )
    title = models.CharField(max_length=50)
    keyword=models.CharField(max_length=255)
    description=models.CharField(max_length=255)
    company = models.CharField(max_length=50)
    address = models.TextField(blank=True)
    phone = models.CharField(blank=True,max_length=50)
    fax = models.CharField(blank=True,max_length=50)
    email = models.CharField(blank=True,max_length=50)
    smtpserver = models.CharField(blank=True,max_length=50)
    smtpemail = models.CharField(blank=True,max_length=50)
    smtppassword = models.CharField(blank=True,max_length=50)
    smtpport = models.CharField(blank=True,max_length=50)
    icon = models.ImageField(blank=True,max_length=50)
    facebook = models.CharField(blank=True,max_length=150)
    instagram = models.CharField(blank=True,max_length=100)
    twitter = models.CharField(blank=True,max_length=100)
    abouts = RichTextUploadingField(blank=True)
    contact = RichTextUploadingField(blank=True)
    references = RichTextUploadingField(blank=True)
    status = models.CharField(max_length=10, choices=STATUS)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
class ContactFormMessage(models.Model):
    STATUS = (
        ('New','New'),
        ('Read','Read'),
    )
    name= models.CharField(blank=True,max_length=25)
    email= models.CharField(blank=True,max_length=50)
    subject= models.CharField(blank=True,max_length=50)
    message= models.CharField(blank=True,max_length=1000)
    status= models.CharField(max_length=10,choices=STATUS,default='New')
    ip = models.CharField(blank=True,max_length=20)
    note=models.CharField(blank=True,max_length=255)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

class ContactFormu(ModelForm):
    class Meta:
        model=ContactFormMessage
        fields=['name','email','subject','message']
        widgets={
            'name':TextInput(attrs={'class':'input','placeholder':'Name $ Surname'}),
            'subject': TextInput(attrs={'class':'input','placeholder':'Subject'}),
            'email': TextInput(attrs={'class':'input','placeholder':'Email Address'}),
            'message': Textarea(attrs={'class': 'input','placeholder':'Your Message','rows':'5'}),
        }