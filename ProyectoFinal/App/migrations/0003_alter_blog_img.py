# Generated by Django 4.1 on 2022-10-03 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_alter_blog_fecha_pub_alter_comentario_fecha_pub'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='avatares'),
        ),
    ]