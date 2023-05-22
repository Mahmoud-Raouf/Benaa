# Generated by Django 3.2 on 2023-05-21 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0021_auto_20230521_1139'),
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
            model_name='projectrequest',
            name='workType',
            field=models.CharField(choices=[('شراء ', 'شراء'), ('ترميم', 'ترميم'), ('بناء', 'بناء')], default='بناء', max_length=50, verbose_name='نوع العمل '),
        ),
        migrations.AlterField(
            model_name='projectstatus',
            name='request_status',
            field=models.CharField(choices=[(1, 'مرحلة إختيار الأرض'), ('مرحلة البناء', 'مرحلة البناء'), ('الإنتهاء من البناء', 'الإنتهاء من البناء'), ('مرحلة تنظيف الأرض', 'مرحلة تنظيف الأرض'), ('مرحلة تسليح الأساس', 'مرحلة تسليح الأساس'), ('مرحلة التشطيبات', 'مرحلة التشطيبات'), ('مرحلة حفر الأساس', 'مرحلة حفر الأساس'), ('تسليم العمل', 'تسليم العمل'), ('مرحلة وضع البنية التحتية', 'مرحلة وضع البنية التحتية'), ('استلام الارض', 'استلام الارض')], max_length=150, verbose_name='حالة المرحلة '),
        ),
    ]
