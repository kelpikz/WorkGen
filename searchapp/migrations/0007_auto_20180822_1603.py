# Generated by Django 2.1 on 2018-08-22 16:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('searchapp', '0006_auto_20180822_0923'),
    ]

    operations = [
        migrations.CreateModel(
            name='GeneratedQuestionPaper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=100)),
                ('file_path', models.CharField(default=None, max_length=200)),
                ('is_ready', models.BooleanField(default=False)),
                ('mentor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='subject',
            name='subject_name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
