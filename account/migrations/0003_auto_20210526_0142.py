# Generated by Django 3.2.3 on 2021-05-25 16:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_profile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plr',
            name='lecture',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='plrs', to='account.lecture'),
        ),
        migrations.AlterField(
            model_name='plr',
            name='profile',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='plrs', to='account.profile'),
        ),
    ]
