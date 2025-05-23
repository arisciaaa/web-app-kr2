# Generated by Django 4.1.7 on 2025-05-15 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("site_pages", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="sitepage",
            options={
                "ordering": ["order"],
                "verbose_name": "Страница",
                "verbose_name_plural": "Страницы",
            },
        ),
        migrations.AddField(
            model_name="sitepage",
            name="image",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to="page_images/",
                verbose_name="Изображение",
            ),
        ),
        migrations.AddField(
            model_name="sitepage",
            name="order",
            field=models.PositiveIntegerField(
                default=0, verbose_name="Порядок отображения"
            ),
        ),
    ]
