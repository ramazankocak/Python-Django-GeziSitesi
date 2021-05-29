from django.db import models

#blank=True eklenirse boş bırakılabilir.
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
    icon = models.ImageField(blank=True,max_length=5)
    facebook = models.CharField(blank=True,max_length=150)
    instagram = models.CharField(blank=True,max_length=100)
    twitter = models.CharField(blank=True,max_length=100)
    abouts = models.TextField(blank=True)
    contact = models.TextField(blank=True)
    references = models.TextField(blank=True)
    status = models.CharField(max_length=10, choices=STATUS)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title