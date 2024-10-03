from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("filmes", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="filme",
            name="data_de_lancamento",
        ),
        migrations.AddField(
            model_name="filme",
            name="ano_de_lancamento",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
