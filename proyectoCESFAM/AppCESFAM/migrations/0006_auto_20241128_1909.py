# Generated by Django 3.2 on 2024-11-28 22:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AppCESFAM', '0005_auto_20241128_0534'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asignacion',
            fields=[
                ('id_asignacion', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_asignacion', models.DateField()),
                ('estado', models.CharField(max_length=50)),
                ('nota', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('id_documento', models.AutoField(primary_key=True, serialize=False)),
                ('motivo', models.TextField()),
                ('fecha_ingreso', models.DateField()),
                ('fecha_documento', models.DateField()),
                ('valor_monetario', models.DecimalField(decimal_places=2, max_digits=12)),
            ],
        ),
        migrations.CreateModel(
            name='Institucion',
            fields=[
                ('id_institucion', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=255)),
                ('rut', models.CharField(max_length=12, unique=True)),
                ('tipo', models.CharField(max_length=50)),
                ('direccion', models.TextField()),
                ('contacto', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='TipoDocumento',
            fields=[
                ('id_tipodoc', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='usuario',
        ),
        migrations.RemoveField(
            model_name='libro',
            name='categorias',
        ),
        migrations.RemoveField(
            model_name='libro',
            name='usuario',
        ),
        migrations.RemoveField(
            model_name='prestamo',
            name='categoria',
        ),
        migrations.RemoveField(
            model_name='prestamo',
            name='cliente',
        ),
        migrations.RemoveField(
            model_name='prestamo',
            name='libro',
        ),
        migrations.RemoveField(
            model_name='prestamo',
            name='usuario',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='contrasena',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='id',
        ),
        migrations.AddField(
            model_name='usuario',
            name='correo',
            field=models.EmailField(default=None, max_length=254, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usuario',
            name='id_usuario',
            field=models.AutoField(default=None, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usuario',
            name='nombre',
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usuario',
            name='password',
            field=models.CharField(default=None, max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usuario',
            name='telefono',
            field=models.CharField(default=None, max_length=15),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='usuario',
            name='rut',
            field=models.CharField(max_length=12, unique=True),
        ),
        migrations.DeleteModel(
            name='Categoria',
        ),
        migrations.DeleteModel(
            name='Cliente',
        ),
        migrations.DeleteModel(
            name='Libro',
        ),
        migrations.DeleteModel(
            name='Prestamo',
        ),
        migrations.AddField(
            model_name='documento',
            name='id_institucion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppCESFAM.institucion'),
        ),
        migrations.AddField(
            model_name='documento',
            name='id_tipodoc',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppCESFAM.tipodocumento'),
        ),
        migrations.AddField(
            model_name='asignacion',
            name='id_documento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppCESFAM.documento'),
        ),
        migrations.AddField(
            model_name='asignacion',
            name='id_usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppCESFAM.usuario'),
        ),
    ]
