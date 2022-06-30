# Generated by Django 4.0.5 on 2022-06-29 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('like', '0002_remove_like_post_id_like_post_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='like',
            name='status',
            field=models.CharField(choices=[(1, 'Liked'), (2, 'Disliked')], default=1, max_length=50),
            preserve_default=False,
        ),
    ]
