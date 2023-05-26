from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.utils.text import slugify
from django.db.models.signals import post_save

import random


def random_string():
    return str(random.randint(1, 10000))
        
        
class Company(models.Model):
    user               = models.OneToOneField(User,  on_delete=models.CASCADE)
    name                    = models.CharField(_("إسم الشركة"),max_length=150)
    Company_image              = models.ImageField(_("صورة الشركة"), upload_to='Company_image',blank=True, null=True)
    code                      = models.IntegerField(_("كود الشركة"), default=random_string)
    phone1                    = models.CharField(_("هاتف الشركة "),max_length=50)
    phone2                    = models.CharField(_("إضافة رقم هاتف ثانى"),max_length=50)
    description          = models.TextField(_("وصف الشركة"))
    address                 = models.CharField(_("العنوان"),max_length=150)
    founding_date            = models.CharField(_("تاريخ التأسيس"),max_length=150)
    number_projects            = models.CharField(_("عدد المشاريع"),max_length=150)
    create_at             = models.DateTimeField(_("تاريخ الإضافة"), default = timezone.now) 
    company_request = models.BooleanField(_("موافقه على طلب شركة") ,default = False)

    def __str__(self):
        return self.name



class Profile(models.Model):
    
    userType = {
        ('شركة' , 'شركة'),
        ('عميل' , 'عميل'),
    }

    user = models.OneToOneField(User , verbose_name=("user_profile"), on_delete=models.CASCADE)
    image = models.ImageField(("الصوره"), upload_to='user-image')
    name = models.CharField(("الإسم ثلاثي"), max_length=50)
    phone = models.CharField(_("رقم الهاتف"),max_length=50)
    userType = models.CharField(choices=userType , default='عميل',max_length=50, blank=True, null=True)
    country = models.CharField(("الدولة"), max_length=50, blank=True, null=True)
    address = models.CharField(("المنطقة"), max_length=50, blank=True, null=True)
    slug = models.SlugField(("Slug :"),blank=True, null=True)

    def __str__(self):
        return '%s' %(self.user.username)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.user.username)
        super(Profile, self).save(*args, **kwargs)



def create_profile(sender , **kwrag):
    if kwrag['created']:
        Profile.objects.create(user=kwrag['instance'])

post_save.connect(create_profile , sender=User)
