# Generated by Django 3.2 on 2024-11-02 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCESFAM', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='libro',
            name='categorias',
            field=models.ManyToManyField(related_name='libros', to='AppCESFAM.Categoria'),
        ),
    ]
