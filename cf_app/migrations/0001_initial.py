# Generated by Django 4.0 on 2022-01-02 17:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarMake',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='CarYear',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('make', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cf_app.carmake')),
            ],
        ),
        migrations.AddField(
            model_name='carmake',
            name='year',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cf_app.caryear'),
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fuel_efficiency', models.IntegerField(blank=True, default=0)),
                ('make', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cf_app.carmake')),
                ('model', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cf_app.carmodel')),
                ('year', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cf_app.caryear')),
            ],
        ),
    ]
