# Generated by Django 4.1 on 2024-10-28 02:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('search_app', '0002_rename_searched_at_searchhistory_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='search_app.category'),
        ),
    ]
