# Generated by Django 3.1.3 on 2020-11-14 23:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recipes', '0002_auto_20201114_2246'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='accounts.account'),
            preserve_default=False,
        ),
    ]