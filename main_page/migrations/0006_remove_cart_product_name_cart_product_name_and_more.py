# Generated by Django 4.0.5 on 2022-06-16 16:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0005_cart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='product_name',
        ),
        migrations.AddField(
            model_name='cart',
            name='product_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main_page.products'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='user_id',
            field=models.IntegerField(),
        ),
    ]
