# Generated by Django 3.2.6 on 2021-08-15 07:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('villains', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Marvel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='marvels', to=settings.AUTH_USER_MODEL)),
                ('villains', models.ManyToManyField(blank=True, related_name='marvels', to='villains.Villain')),
            ],
        ),
        migrations.CreateModel(
            name='MarvelCover',
            fields=[
                ('marvel', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='marvelcover', serialize=False, to='marvels.marvel')),
                ('image', models.ImageField(upload_to='marvels/marvelcovers/%Y/%m/%d/')),
            ],
        ),
        migrations.CreateModel(
            name='Marvelinfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('track', models.FileField(upload_to='marvels/marvelinfo/%Y/%m/%d/')),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='marvelinfo', to='marvels.marvel')),
            ],
        ),
    ]