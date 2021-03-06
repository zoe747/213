# Generated by Django 3.2.7 on 2021-09-10 08:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_delete_profile'),
        ('folder', '0006_folder_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='folder',
            name='father_folder',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children_folders', to='folder.folder'),
        ),
        migrations.AlterField(
            model_name='folder',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='folders', to='account.user'),
        ),
    ]
