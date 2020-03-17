# Generated by Django 2.2.7 on 2020-03-10 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_yandex_maps', '0005_collections_claster_routes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='claster',
            name='icon_color',
            field=models.CharField(blank=True, choices=[('blue', 'Blue'), ('red', 'Red'), ('darkOrange', 'Dark orange'), ('night', 'Night'), ('darkBlue', 'DarkBlue'), ('pink', 'Pink'), ('gray', 'Gray'), ('brown', 'Brown'), ('darkGreen', 'Dark green'), ('violet', 'Violet'), ('black', 'Black'), ('yellow', 'Yellow'), ('green', 'Green'), ('orange', 'Orange'), ('lightBlue', 'Light blue'), ('olive', 'Olive')], max_length=15, null=True, verbose_name='Marker icon color'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='icon_color',
            field=models.CharField(blank=True, choices=[('blue', 'Blue'), ('red', 'Red'), ('darkOrange', 'Dark orange'), ('night', 'Night'), ('darkBlue', 'DarkBlue'), ('pink', 'Pink'), ('gray', 'Gray'), ('brown', 'Brown'), ('darkGreen', 'Dark green'), ('violet', 'Violet'), ('black', 'Black'), ('yellow', 'Yellow'), ('green', 'Green'), ('orange', 'Orange'), ('lightBlue', 'Light blue'), ('olive', 'Olive')], max_length=15, null=True, verbose_name='Marker icon color'),
        ),
    ]