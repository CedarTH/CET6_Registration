# Generated by Django 4.1 on 2023-06-03 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("take_exam", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ObjectiveAnswers",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("examinee_id", models.CharField(max_length=18)),
                ("paper_id", models.IntegerField()),
                ("question_id", models.IntegerField()),
                ("answer", models.CharField(max_length=1)),
                ("score", models.FloatField()),
            ],
            options={
                "db_table": "objective_answers",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="SubjectiveAnswers",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("examinee_id", models.CharField(max_length=18)),
                ("paper_id", models.IntegerField()),
                ("question_id", models.IntegerField()),
                ("answer", models.CharField(max_length=1000)),
                ("score", models.FloatField()),
            ],
            options={
                "db_table": "subjective_answers",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="ObjectiveQuestions",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("question", models.CharField(blank=True, max_length=1000, null=True)),
                ("option_a", models.CharField(max_length=500)),
                ("option_b", models.CharField(max_length=500)),
                ("option_c", models.CharField(max_length=500)),
                ("option_d", models.CharField(max_length=500)),
                (
                    "answer_option",
                    models.CharField(blank=True, max_length=1, null=True),
                ),
                ("score", models.FloatField()),
            ],
            options={
                "db_table": "objective_questions",
                "managed": True,
            },
        ),
        migrations.CreateModel(
            name="PaperQuestions",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("paper_id", models.IntegerField()),
                ("question_id", models.IntegerField()),
                (
                    "question_type",
                    models.CharField(
                        choices=[
                            ("objective", "Objective"),
                            ("subjective", "Subjective"),
                        ],
                        max_length=20,
                    ),
                ),
            ],
            options={
                "db_table": "paper_question",
                "managed": True,
            },
        ),
        migrations.CreateModel(
            name="SubjectiveQuestions",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("question", models.CharField(blank=True, max_length=1000, null=True)),
                ("answer", models.CharField(blank=True, max_length=1000, null=True)),
                ("score", models.FloatField()),
            ],
            options={
                "db_table": "subjective_questions",
                "managed": True,
            },
        ),
    ]