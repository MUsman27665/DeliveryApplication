# Generated by Django 2.2.12 on 2020-10-26 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_contactus'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(default='', max_length=30)),
                ('category_image', models.ImageField(upload_to='iCV_Nation/category')),
            ],
        ),
    ]