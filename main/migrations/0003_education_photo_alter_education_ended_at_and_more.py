from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_education'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='photo',
            field=models.TextField(blank=True, null=True),
        ),

        migrations.RunSQL(
            """
            ALTER TABLE main_education
            ALTER COLUMN ended_at TYPE integer
            USING EXTRACT(YEAR FROM ended_at)::integer
            """,
            reverse_sql=migrations.RunSQL.noop,
        ),

        migrations.RunSQL(
            """
            ALTER TABLE main_education
            ALTER COLUMN started_at TYPE integer
            USING EXTRACT(YEAR FROM started_at)::integer
            """,
            reverse_sql=migrations.RunSQL.noop,
        ),

        migrations.AlterField(
            model_name='education',
            name='tags',
            field=models.JSONField(default=list),
        ),
    ]