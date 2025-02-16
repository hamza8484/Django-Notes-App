# Generated by Django 4.2.16 on 2024-10-13 14:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0002_alter_brand_brddesc_alter_brand_brdname_and_more'),
        ('product', '0007_alter_category_catdesc_alter_category_catimg_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='PRDBrand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='settings.brand'),
        ),
        migrations.AddField(
            model_name='product',
            name='PrdCategory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.category'),
        ),
    ]
