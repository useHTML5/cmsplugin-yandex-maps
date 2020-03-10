# Generated by Django 2.2.7 on 2020-03-10 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_yandex_maps', '0006_auto_20200310_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yandexmaps',
            name='sizing',
            field=models.CharField(choices=[('aspect', 'Keep aspect'), ('static', 'Static'), ('static_height', 'Min height and full width'), ('auto', 'Auto')], default='aspect', max_length=6, verbose_name='Sizing'),
        ),
    ]
