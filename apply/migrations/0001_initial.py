# Generated by Django 4.2.7 on 2024-01-09 08:23

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('priority', models.PositiveIntegerField(choices=[(1, '1순위'), (2, '2순위'), (3, '3순위'), (4, '4순위')])),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Major',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('major_name', models.CharField(max_length=255)),
                ('maximum', models.PositiveIntegerField(null=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='major', to='apply.department')),
            ],
        ),
        migrations.CreateModel(
            name='User_apply_profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('major_choices', models.ManyToManyField(through='apply.Choice', to='apply.major')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Subject_code',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10)),
                ('major', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subject_codes', to='apply.major')),
            ],
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('src_file', models.CharField(default='', max_length=225)),
                ('src_name', models.CharField(default='', max_length=225)),
                ('src_link', models.CharField(default='', max_length=225)),
                ('result_text', models.TextField(default='', max_length=4096)),
                ('status', models.BooleanField(default=False, max_length=10)),
                ('usage_flag', models.CharField(default='', max_length=10)),
                ('create_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grades1', models.DecimalField(decimal_places=5, max_digits=6, null=True)),
                ('grades2', models.DecimalField(decimal_places=5, max_digits=6, null=True)),
                ('course_credits1', models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(3)])),
                ('course_credits2', models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(3)])),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_code', models.CharField(max_length=1000)),
                ('course_name', models.CharField(max_length=255)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='choice',
            name='major',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apply.major'),
        ),
        migrations.AddField(
            model_name='choice',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='choice',
            name='user_apply_profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apply.user_apply_profile'),
        ),
        migrations.CreateModel(
            name='Academic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_number', models.CharField(default='', max_length=20)),
                ('academic_status', models.CharField(default='', max_length=50)),
                ('grade', models.CharField(default='', max_length=20)),
                ('major', models.CharField(default='', max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='choice',
            unique_together={('user', 'priority')},
        ),
    ]
