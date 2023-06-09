# Generated by Django 3.2 on 2023-05-21 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0028_auto_20230521_1216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consultationrequest',
            name='request_status',
            field=models.CharField(choices=[('مرفوض ', 'مرفوض'), ('تحت المراجعة', 'تحت المراجعة'), ('مقبول', 'مقبول')], default='تحت المراجعة', max_length=50, verbose_name='حالة الطلب '),
        ),
        migrations.AlterField(
            model_name='projectrequest',
            name='request_status',
            field=models.CharField(choices=[('مرفوض ', 'مرفوض'), ('تحت المراجعة', 'تحت المراجعة'), ('مقبول', 'مقبول')], default='تحت المراجعة', max_length=50, verbose_name='حالة الطلب '),
        ),
        migrations.AlterField(
            model_name='projectrequest',
            name='workType',
            field=models.CharField(choices=[('ترميم', 'ترميم'), ('بناء', 'بناء'), ('شراء ', 'شراء')], default='بناء', max_length=50, verbose_name='نوع العمل '),
        ),
        migrations.AlterField(
            model_name='projectstatus',
            name='request_status',
            field=models.CharField(choices=[(4, 'مرحلة حفر الأساس'), (10, 'تسليم العمل'), (7, 'مرحلة وضع البنية التحتية'), (8, 'مرحلة التشطيبات'), (6, 'مرحلة البناء'), (9, 'الإنتهاء من البناء'), (3, 'مرحلة تنظيف الأرض'), (5, 'مرحلة تسليح الأساس'), (2, 'استلام الارض'), (1, 'مرحلة إختيار الأرض')], max_length=150, verbose_name='حالة المرحلة '),
        ),
    ]
