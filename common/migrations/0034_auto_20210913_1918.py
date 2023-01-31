# Generated by Django 3.2 on 2021-09-13 13:48

import django.db.models.deletion
import phonenumber_field.modelfields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("common", "0033_alter_user_alternate_email"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="comment",
            name="user",
        ),
        migrations.RemoveField(
            model_name="google",
            name="user",
        ),
        migrations.RemoveField(
            model_name="user",
            name="address",
        ),
        migrations.RemoveField(
            model_name="user",
            name="alternate_phone",
        ),
        migrations.RemoveField(
            model_name="user",
            name="has_marketing_access",
        ),
        migrations.RemoveField(
            model_name="user",
            name="has_sales_access",
        ),
        migrations.RemoveField(
            model_name="user",
            name="is_admin",
        ),
        migrations.RemoveField(
            model_name="user",
            name="phone",
        ),
        migrations.RemoveField(
            model_name="user",
            name="role",
        ),
        migrations.AddField(
            model_name="apisettings",
            name="company",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="common.company",
            ),
        ),
        migrations.AddField(
            model_name="comment",
            name="profile",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="user_comments",
                to="common.profile",
            ),
        ),
        migrations.AddField(
            model_name="document",
            name="company",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="common.company",
            ),
        ),
        migrations.AddField(
            model_name="google",
            name="profile",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="google",
                to="common.profile",
            ),
        ),
        migrations.AddField(
            model_name="profile",
            name="address",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="adress_users",
                to="common.address",
            ),
        ),
        migrations.AddField(
            model_name="profile",
            name="alternate_phone",
            field=phonenumber_field.modelfields.PhoneNumberField(
                max_length=128, null=True, region=None
            ),
        ),
        migrations.AddField(
            model_name="profile",
            name="company",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="common.company",
            ),
        ),
        migrations.AddField(
            model_name="profile",
            name="date_of_joining",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="profile",
            name="has_marketing_access",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="profile",
            name="has_sales_access",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="profile",
            name="is_active",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="profile",
            name="is_organization_admin",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="profile",
            name="phone",
            field=phonenumber_field.modelfields.PhoneNumberField(
                max_length=128, null=True, region=None, unique=True
            ),
        ),
        migrations.AddField(
            model_name="profile",
            name="role",
            field=models.CharField(
                choices=[("ADMIN", "ADMIN"), ("USER", "USER")],
                default="USER",
                max_length=50,
            ),
        ),
        migrations.AlterField(
            model_name="apisettings",
            name="created_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="settings_created_by",
                to="common.profile",
            ),
        ),
        migrations.AlterField(
            model_name="apisettings",
            name="lead_assigned_to",
            field=models.ManyToManyField(
                related_name="lead_assignee_users", to="common.Profile"
            ),
        ),
        migrations.AlterField(
            model_name="attachments",
            name="created_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="attachment_created_by",
                to="common.profile",
            ),
        ),
        migrations.AlterField(
            model_name="comment",
            name="commented_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="common.profile",
            ),
        ),
        migrations.AlterField(
            model_name="company",
            name="sub_domain",
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name="document",
            name="created_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="document_uploaded",
                to="common.profile",
            ),
        ),
        migrations.AlterField(
            model_name="document",
            name="shared_to",
            field=models.ManyToManyField(
                related_name="document_shared_to", to="common.Profile"
            ),
        ),
        migrations.AlterField(
            model_name="profile",
            name="activation_key",
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name="profile",
            name="key_expires",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="profile",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="username",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterUniqueTogether(
            name="profile",
            unique_together={("user", "company")},
        ),
    ]
