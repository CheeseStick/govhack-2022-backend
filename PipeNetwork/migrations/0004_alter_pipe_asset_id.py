# Generated by Django 4.1 on 2022-08-20 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PipeNetwork', '0003_pipe_shape_length'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pipe',
            name='asset_id',
            field=models.CharField(db_index=True, max_length=24),
        ),
    ]