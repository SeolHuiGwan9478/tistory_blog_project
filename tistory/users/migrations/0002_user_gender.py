# Generated by Django 3.1.6 on 2021-02-09 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('남성', '남성'), ('여성', '여성')], default='남성', max_length=2, verbose_name='성별'),
            preserve_default=False,
        ),
    ]
