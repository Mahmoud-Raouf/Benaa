# Generated by Django 3.2 on 2023-05-21 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0030_auto_20230521_1217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consultationrequest',
            name='request_status',
            field=models.CharField(choices=[('مقبول', 'مقبول'), ('تحت المراجعة', 'تحت المراجعة'), ('مرفوض ', 'مرفوض')], default='تحت المراجعة', max_length=50, verbose_name='حالة الطلب '),
        ),
        migrations.AlterField(
            model_name='projectrequest',
            name='request_status',
            field=models.CharField(choices=[('مقبول', 'مقبول'), ('تحت المراجعة', 'تحت المراجعة'), ('مرفوض ', 'مرفوض')], default='تحت المراجعة', max_length=50, verbose_name='حالة الطلب '),
        ),
        migrations.AlterField(
            model_name='projectrequest',
            name='workType',
            field=models.CharField(choices=[('بناء', 'بناء'), ('شراء ', 'شراء'), ('ترميم', 'ترميم')], default='بناء', max_length=50, verbose_name='نوع العمل '),
        ),
        migrations.AlterField(
            model_name='projectstatus',
            name='request_status',
            field=models.CharField(choices=[(7, 'مرحلة وضع البنية التحتية'), (5, 'مرحلة تسليح الأساس'), (1, 'مرحلة إختيار الأرض'), (3, 'مرحلة تنظيف الأرض'), (9, 'الإنتهاء من البناء'), (4, 'مرحلة حفر الأساس'), (2, 'استلام الارض'), (8, 'مرحلة التشطيبات'), (10, 'تسليم العمل'), (6, 'مرحلة البناء')], max_length=150, verbose_name='حالة المرحلة '),
        ),
    ]
