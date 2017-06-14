# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-14 13:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Acceso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Modulo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255, verbose_name='Nombre del Ítem de menú')),
                ('nombre_completo', models.CharField(max_length=1000)),
                ('padre', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='permisos.Modulo', verbose_name='Ítem de nivel superior')),
            ],
            options={
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('acceso_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='permisos.Acceso')),
                ('nombre', models.CharField(max_length=255, verbose_name='Nombre del grupo de usuarios')),
            ],
            bases=('permisos.acceso',),
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('acceso_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='permisos.Acceso')),
                ('nombre', models.CharField(max_length=255, verbose_name='Nombre del usuario')),
                ('grupo_usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='grupo_usuario', to='permisos.Grupo', verbose_name='Grupo de usuarios')),
            ],
            bases=('permisos.acceso',),
        ),
        migrations.AddField(
            model_name='acceso',
            name='permiso',
            field=models.ManyToManyField(related_name='permiso_acceso', to='permisos.Modulo', verbose_name='Modulos permitidos'),
        ),
    ]