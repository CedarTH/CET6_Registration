# Generated by Django 4.2.1 on 2023-06-03 12:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Admin",
            fields=[
                (
                    "id_card_no",
                    models.CharField(max_length=18, primary_key=True, serialize=False),
                ),
                ("password", models.CharField(blank=True, max_length=255, null=True)),
                ("name", models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                "db_table": "admin",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="AuthGroup",
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
                ("name", models.CharField(max_length=150, unique=True)),
            ],
            options={
                "db_table": "auth_group",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="AuthGroupPermissions",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                "db_table": "auth_group_permissions",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="AuthPermission",
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
                ("codename", models.CharField(max_length=100)),
            ],
            options={
                "db_table": "auth_permission",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="AuthUser",
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
                ("password", models.CharField(max_length=128)),
                ("last_login", models.DateTimeField(blank=True, null=True)),
                ("is_superuser", models.IntegerField()),
                ("username", models.CharField(max_length=150, unique=True)),
                ("first_name", models.CharField(max_length=150)),
                ("last_name", models.CharField(max_length=150)),
                ("email", models.CharField(max_length=254)),
                ("is_staff", models.IntegerField()),
                ("is_active", models.IntegerField()),
                ("date_joined", models.DateTimeField()),
            ],
            options={
                "db_table": "auth_user",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="AuthUserGroups",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                "db_table": "auth_user_groups",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="AuthUserUserPermissions",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                "db_table": "auth_user_user_permissions",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="DjangoAdminLog",
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
                ("action_time", models.DateTimeField()),
                ("object_id", models.TextField(blank=True, null=True)),
                ("object_repr", models.CharField(max_length=200)),
                ("action_flag", models.PositiveSmallIntegerField()),
                ("change_message", models.TextField()),
            ],
            options={
                "db_table": "django_admin_log",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="DjangoContentType",
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
                ("app_label", models.CharField(max_length=100)),
                ("model", models.CharField(max_length=100)),
            ],
            options={
                "db_table": "django_content_type",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="DjangoMigrations",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("app", models.CharField(max_length=255)),
                ("name", models.CharField(max_length=255)),
                ("applied", models.DateTimeField()),
            ],
            options={
                "db_table": "django_migrations",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="DjangoSession",
            fields=[
                (
                    "session_key",
                    models.CharField(max_length=40, primary_key=True, serialize=False),
                ),
                ("session_data", models.TextField()),
                ("expire_date", models.DateTimeField()),
            ],
            options={
                "db_table": "django_session",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Examinee",
            fields=[
                (
                    "id_card_no",
                    models.CharField(max_length=18, primary_key=True, serialize=False),
                ),
                ("gender", models.CharField(blank=True, max_length=10, null=True)),
                ("password", models.CharField(blank=True, max_length=255, null=True)),
                ("name", models.CharField(blank=True, max_length=20, null=True)),
                (
                    "phone_number",
                    models.CharField(blank=True, max_length=11, null=True),
                ),
            ],
            options={
                "db_table": "examinee",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="ExamInformation",
            fields=[
                ("exam_id", models.IntegerField(primary_key=True, serialize=False)),
                ("exam_name", models.CharField(blank=True, max_length=50, null=True)),
                ("exam_time", models.DateTimeField(blank=True, null=True)),
                ("location", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "fee",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=10, null=True
                    ),
                ),
            ],
            options={
                "db_table": "exam_information",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="ObjectiveQuestion",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("question", models.CharField(blank=True, max_length=1000, null=True)),
                ("option_a", models.CharField(blank=True, max_length=500, null=True)),
                ("option_b", models.CharField(blank=True, max_length=500, null=True)),
                ("option_c", models.CharField(blank=True, max_length=500, null=True)),
                ("option_d", models.CharField(blank=True, max_length=500, null=True)),
                (
                    "answer_option",
                    models.CharField(blank=True, max_length=1, null=True),
                ),
                ("score", models.FloatField(blank=True, null=True)),
                ("create_time", models.DateTimeField(blank=True, null=True)),
            ],
            options={
                "db_table": "objective_questions",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Paper",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("paper_name", models.CharField(blank=True, max_length=100, null=True)),
                ("total_score", models.FloatField()),
                ("create_time", models.DateTimeField(blank=True, null=True)),
            ],
            options={
                "db_table": "papers",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="PaperQuestion",
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
                ("question_type", models.CharField(max_length=10)),
            ],
            options={
                "db_table": "paper_question",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="SubjectiveQuestion",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("question", models.CharField(blank=True, max_length=1000, null=True)),
                ("answer", models.CharField(blank=True, max_length=1000, null=True)),
                ("score", models.FloatField(blank=True, null=True)),
                ("create_time", models.DateTimeField(blank=True, null=True)),
            ],
            options={
                "db_table": "subjective_questions",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Enrollment",
            fields=[
                (
                    "id_card_no",
                    models.OneToOneField(
                        db_column="id_card_no",
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        primary_key=True,
                        serialize=False,
                        to="Paper_Modification.examinee",
                    ),
                ),
                ("enrollment_time", models.DateTimeField(blank=True, null=True)),
                (
                    "payment_status",
                    models.CharField(blank=True, max_length=20, null=True),
                ),
            ],
            options={
                "db_table": "enrollment",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="ExamScore",
            fields=[
                (
                    "id_card_no",
                    models.OneToOneField(
                        db_column="id_card_no",
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        primary_key=True,
                        serialize=False,
                        to="Paper_Modification.examinee",
                    ),
                ),
                ("score", models.FloatField(blank=True, null=True)),
                ("publish_date", models.DateField(blank=True, null=True)),
            ],
            options={
                "db_table": "exam_score",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="ObjectiveAnswer",
            fields=[
                (
                    "examinee",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        primary_key=True,
                        serialize=False,
                        to="Paper_Modification.examinee",
                    ),
                ),
                ("answer", models.CharField(blank=True, max_length=1, null=True)),
                ("score", models.FloatField(blank=True, null=True)),
            ],
            options={
                "db_table": "objective_answers",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Payment",
            fields=[
                (
                    "id_card_no",
                    models.OneToOneField(
                        db_column="id_card_no",
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        primary_key=True,
                        serialize=False,
                        to="Paper_Modification.examinee",
                    ),
                ),
                ("payment_time", models.DateTimeField(blank=True, null=True)),
                (
                    "payment_amount",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=10, null=True
                    ),
                ),
            ],
            options={
                "db_table": "payment",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="SubjectiveAnswer",
            fields=[
                (
                    "examinee",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        primary_key=True,
                        serialize=False,
                        to="Paper_Modification.examinee",
                    ),
                ),
                ("answer", models.CharField(blank=True, max_length=1000, null=True)),
                ("score", models.FloatField(blank=True, null=True)),
            ],
            options={
                "db_table": "subjective_answers",
                "managed": False,
            },
        ),
    ]