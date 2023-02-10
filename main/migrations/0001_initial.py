# Generated by Django 4.1.6 on 2023-02-10 10:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Author",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("email", models.EmailField(max_length=100, unique=True)),
                ("dob", models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name="Tag",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Post",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                ("content", models.TextField()),
                ("publish_date", models.DateTimeField(auto_now_add=True)),
                ("views", models.IntegerField(default=0)),
                ("likes", models.IntegerField(default=0)),
                ("time_to_read", models.IntegerField(default=0)),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="main.author"
                    ),
                ),
                (
                    "tags",
                    models.ManyToManyField(related_name="post_set", to="main.tag"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("body", models.TextField()),
                ("publish_date", models.DateTimeField(auto_now_add=True)),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="main.author"
                    ),
                ),
                (
                    "parent",
                    models.ForeignKey(
                        blank=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="replies",
                        to="main.comment",
                    ),
                ),
                (
                    "post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="main.post"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="author",
            name="favorites",
            field=models.ManyToManyField(
                blank=True, related_name="favorite_of_authors", to="main.post"
            ),
        ),
    ]
