# Generated by Django 3.2 on 2023-06-01 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0032_auto_20230521_1229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consultationrequest',
            name='request_status',
            field=models.CharField(choices=[('تحت المراجعة', 'تحت المراجعة'), ('مقبول', 'مقبول'), ('مرفوض ', 'مرفوض')], default='تحت المراجعة', max_length=50, verbose_name='حالة الطلب '),
        ),
        migrations.AlterField(
            model_name='projectrequest',
            name='request_status',
            field=models.CharField(choices=[('تحت المراجعة', 'تحت المراجعة'), ('مقبول', 'مقبول'), ('مرفوض ', 'مرفوض')], default='تحت المراجعة', max_length=50, verbose_name='حالة الطلب '),
        ),
        migrations.AlterField(
            model_name='projectstatus',
            name='request_status',
            field=models.CharField(choices=[('9', 'الإنتهاء من البناء'), ('3', 'مرحلة تنظيف الأرض'), ('2', 'استلام الارض'), ('1', 'مرحلة إختيار الأرض'), ('4', 'مرحلة حفر الأساس'), ('8', 'مرحلة التشطيبات'), ('5', 'مرحلة تسليح الأساس'), ('6', 'مرحلة البناء'), ('7', 'مرحلة وضع البنية التحتية'), ('10', 'تسليم العمل')], max_length=150, verbose_name='حالة المرحلة '),
        ),
    ]
