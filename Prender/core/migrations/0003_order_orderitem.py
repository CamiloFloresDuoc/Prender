# Generated by Django 3.1.13 on 2022-06-05 02:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_producto_imagen'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('numero_telefono', models.CharField(max_length=20)),
                ('direccion', models.CharField(max_length=100)),
                ('comuna', models.CharField(max_length=100)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('total', models.IntegerField()),
                ('comprador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.comprador')),
                ('vendedor', models.ManyToManyField(related_name='ordenes', to='core.Emprendedor')),
            ],
            options={
                'ordering': ['-fecha'],
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pagado', models.BooleanField(default=False)),
                ('precio', models.IntegerField()),
                ('cantidad', models.IntegerField(default=1)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='core.order')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='core.producto')),
                ('vendedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='core.emprendedor')),
            ],
        ),
    ]