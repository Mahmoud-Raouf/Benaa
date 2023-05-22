# Generated by Django 3.2 on 2023-05-21 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0026_alter_projectstatus_request_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consultationrequest',
            name='request_status',
            field=models.CharField(choices=[('تحت المراجعة', 'تحت المراجعة'), ('مرفوض ', 'مرفوض'), ('مقبول', 'مقبول')], default='تحت المراجعة', max_length=50, verbose_name='حالة الطلب '),
        ),
        migrations.AlterField(
            model_name='projectrequest',
            name='request_status',
            field=models.CharField(choices=[('تحت المراجعة', 'تحت المراجعة'), ('مرفوض ', 'مرفوض'), ('مقبول', 'مقبول')], default='تحت المراجعة', max_length=50, verbose_name='حالة الطلب '),
        ),
        migrations.AlterField(
            model_name='projectrequest',
            name='workType',
            field=models.CharField(choices=[('ترميم', 'ترميم'), ('شراء ', 'شراء'), ('بناء', 'بناء')], default='بناء', max_length=50, verbose_name='نوع العمل '),
        ),
        migrations.AlterField(
            model_name='projectstatus',
            name='request_status',
            field=models.CharField(choices=[('10', 'تسليم العمل'), ('2', 'استلام الارض'), ('4', 'مرحلة حفر الأساس'), ('7', 'مرحلة وضع البنية التحتية'), ('3', 'مرحلة تنظيف الأرض'), ('8', 'مرحلة التشطيبات'), ('6', 'مرحلة البناء'), ('1', 'مرحلة إختيار الأرض'), ('9', 'الإنتهاء من البناء'), ('5', 'مرحلة تسليح الأساس')], max_length=150, verbose_name='حالة المرحلة '),
        ),
    ]
