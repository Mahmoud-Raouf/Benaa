# Generated by Django 2.2.7 on 2023-05-09 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0017_auto_20230509_2222'),
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
            field=models.CharField(choices=[('ترميم', 'ترميم'), ('شراء ', 'شراء'), ('بناء', 'بناء')], default='بناء', max_length=50, verbose_name='نوع العمل '),
        ),
        migrations.AlterField(
            model_name='projectstatus',
            name='request_status',
            field=models.CharField(choices=[('مرحلة وضع البنية التحتية', 'مرحلة وضع البنية التحتية'), ('تسليم العمل', 'تسليم العمل'), ('الإنتهاء من البناء', 'الإنتهاء من البناء'), ('مرحلة التشطيبات', 'مرحلة التشطيبات'), ('مرحلة حفر الأساس', 'مرحلة حفر الأساس'), ('مرحلة تنظيف الأرض', 'مرحلة تنظيف الأرض'), ('مرحلة إختيار الأرض', 'مرحلة إختيار الأرض'), ('مرحلة تسليح الأساس', 'مرحلة تسليح الأساس'), ('مرحلة البناء', 'مرحلة البناء')], max_length=150, verbose_name='حالة المرحلة '),
        ),
        migrations.AlterField(
            model_name='projectstatus',
            name='update_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
