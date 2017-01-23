# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_blog_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='blog_image',
            field=models.ImageField(null=True, upload_to='blog/media'),
        ),
    ]