# Generated by Django 3.2.5 on 2021-07-13 08:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='university',
            field=models.ForeignKey(default=11, on_delete=django.db.models.deletion.CASCADE, to='Student.university'),
            preserve_default=False,
        ),
    ]