# Generated by Django 3.2.7 on 2021-10-14 18:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sanalberto', '0013_polls_votes'),
    ]

    operations = [
        migrations.AddField(
            model_name='poll',
            name='winner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='won_polls', to='sanalberto.polldesign', verbose_name='diseño ganador'),
        ),
        migrations.AddField(
            model_name='polldesign',
            name='voting_image',
            field=models.ImageField(blank=True, upload_to='designs-tshirts/', verbose_name='imagen de camiseta'),
        ),
    ]
