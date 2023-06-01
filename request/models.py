from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.contrib.auth.models import User
import random
from accounts.models import Company


def random_string():
    return str(random.randint(1, 10000))


class ConsultationRequest(models.Model):
    
    Request_Status= {
        ('تحت المراجعة' , 'تحت المراجعة'),
        ('مقبول' , 'مقبول'),
        ('مرفوض ' , 'مرفوض'),
    }
    user               = models.ForeignKey(User,  on_delete=models.CASCADE)
    company            = models.ForeignKey(Company,  on_delete=models.CASCADE)
    name               = models.CharField(_("عنوان الطلب "), max_length=50)
    request_status     = models.CharField(_("حالة الطلب "),choices=Request_Status,default='تحت المراجعة' , max_length=50)
    code               = models.IntegerField(_("رقم الطلب"), default=random_string)
    description        = models.TextField(_("وصف الطلب"))
    create_at          = models.DateTimeField(_("تاريخ الطلب"), default = timezone.now) 

    
    class Meta:
        verbose_name = _("Consultation Request")
        verbose_name_plural = _("Consultation Request")


    
    def __str__(self):
        return str(self.name)


class ConsultationComment(models.Model):
    consultationrequest = models.OneToOneField(ConsultationRequest, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text
    class Meta:
        verbose_name = _("Consultation Comment")
        verbose_name_plural = _("Consultation Comment")
    
    
    
# Start ProjectRequest

class ProjectRequest(models.Model):
    
    Request_Status={
        ('تحت المراجعة' , 'تحت المراجعة'),
        ('مقبول' , 'مقبول'),
        ('مرفوض ' , 'مرفوض'),
    }
    
    work_Type={
        ('بناء' , 'بناء'),
        ('ترميم' , 'ترميم'),
        ('شراء ' , 'شراء'),
    }
    
    user               = models.ForeignKey(User,  on_delete=models.CASCADE)
    company            = models.ForeignKey(Company,  on_delete=models.CASCADE)
    workname           = models.CharField(_("إسم العميل"), max_length=50)
    name               = models.CharField(_("عنوان المشروع"), max_length=50)
    workType           = models.CharField(_("نوع العمل "),choices=work_Type,default='بناء' , max_length=50)
    request_status     = models.CharField(_("حالة الطلب "),choices=Request_Status,default='تحت المراجعة' , max_length=50)
    city               = models.CharField(_("المدينة "), max_length=50)
    code               = models.IntegerField(_("رقم الطلب"), default=random_string)
    description        = models.TextField(_("وصف الطلب"))
    create_at          = models.DateTimeField(_("تاريخ الطلب"), default = timezone.now) 

    
    class Meta:
        verbose_name = _("Project Request")
        verbose_name_plural = _("Project Request")

    def __str__(self):
        return str(self.name)


class ProjectStatus(models.Model):


    Project__Status={
        ('1' , 'مرحلة إختيار الأرض'),
        ('2' , 'استلام الارض'),
        ('3' , 'مرحلة تنظيف الأرض'),
        ('4' , 'مرحلة حفر الأساس'),
        ('5' , 'مرحلة تسليح الأساس'),
        ('6' , 'مرحلة البناء'),
        ('7' , 'مرحلة وضع البنية التحتية'),
        ('8' , 'مرحلة التشطيبات'),
        ('9' , 'الإنتهاء من البناء'),
        ('10' , 'تسليم العمل'),
       
    }
    
    projectrequest      = models.OneToOneField(ProjectRequest,  on_delete=models.CASCADE)
    request_status     = models.CharField(_("حالة المرحلة ") , choices=Project__Status, max_length=150)
    image_status     = models.ImageField(_("صورة للمرحلة"), upload_to=None, height_field=None, width_field=None, max_length=None)
    description        = models.TextField(_("وصف المرحلة"))
    update_at          = models.DateTimeField(auto_now_add=True)
    create_at          = models.DateTimeField(_("تاريخ الطلب"), default = timezone.now) 

    def __str__(self):
        return str(self.projectrequest.name) 
    
    class Meta:
        verbose_name = _("Project Status")
        verbose_name_plural = _("Project Status")
    
    def get_choices_list(self, user_input):
        my_list = []
        for choice in self.Project__Status:
            if user_input == choice[0]:
                my_list.append(choice["1"])
        return my_list



class Contracts_Guarantees(models.Model):
    
    contracts_guarantees  = models.OneToOneField(ProjectRequest,  on_delete=models.CASCADE)
    image_status     = models.ImageField(_("صورة العقد"), upload_to=None, height_field=None, width_field=None, max_length=None)
    materials_used     = models.ImageField(_("المواد المستخدمة"), upload_to=None, height_field=None, width_field=None, max_length=None)
    description        = models.TextField(_("الضمنات"))
    update_at          = models.DateTimeField(_("أخر تحديث للطلب"), default = timezone.now) 
    create_at          = models.DateTimeField(_("تاريخ الطلب"), default = timezone.now) 

    def __str__(self):
        return str(self.contracts_guarantees)
    
    class Meta:
        verbose_name = _("Contracts Guarantees")
        verbose_name_plural = _("Contracts Guarantees")


    
class ProjectMeetings(models.Model):
    
    project_meetings  = models.OneToOneField(ProjectRequest,  on_delete=models.CASCADE)
    name        = models.CharField(_("عنوان الاجتماع"), max_length=50)
    description        = models.TextField(_("موضوع الاجتماع"))
    meetingsLink        = models.URLField(("رابط الاجتماع"), max_length=200)
    update_at          = models.DateTimeField(_("أخر تحديث للطلب"), default = timezone.now) 
    create_at          = models.DateTimeField(_("تاريخ الطلب"), default = timezone.now) 

    def __str__(self):
        return str(self.name)
    
    class Meta:
        verbose_name = _("Project Meetings")
        verbose_name_plural = _("Project Meetings")