# Generated by Django 2.1 on 2018-08-15 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searchapp', '0003_auto_20180813_1345'),
    ]

    operations = [
        migrations.AddField(
            model_name='questions',
            name='chapter_number',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
