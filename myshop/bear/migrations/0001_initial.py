# Generated by Django 4.2.5 on 2023-09-15 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200)),
                ('image', models.ImageField(blank=True, upload_to='products/%Y/%m/%d')),
                ('description', models.TextField(blank=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('available', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['name'],
                'indexes': [models.Index(fields=['id', 'slug'], name='bear_produc_id_1d16bd_idx'), models.Index(fields=['name'], name='bear_produc_name_044cf6_idx')],
            },
        ),
    ]
