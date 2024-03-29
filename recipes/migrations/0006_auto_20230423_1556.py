# Generated by Django 3.2.16 on 2023-04-23 15:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recipes', '0005_recipes_excerpt'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recipes',
            options={'ordering': ['-created_on']},
        ),
        migrations.AddField(
            model_name='recipes',
            name='image_alt',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='recipes',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipe_owner', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='recipes',
            name='description',
            field=models.CharField(max_length=500),
        ),
    ]
