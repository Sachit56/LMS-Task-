# Generated by Django 5.0.1 on 2024-02-01 12:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookdetailsmodel',
            old_name='detailsid',
            new_name='details_id',
        ),
        migrations.RemoveField(
            model_name='bookdetailsmodel',
            name='bookid',
        ),
        migrations.AddField(
            model_name='bookdetailsmodel',
            name='book',
            field=models.OneToOneField(default=True, on_delete=django.db.models.deletion.CASCADE, to='lms.bookmodel'),
        ),
    ]
