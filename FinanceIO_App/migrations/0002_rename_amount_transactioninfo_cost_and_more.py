# Generated by Django 4.1.4 on 2022-12-25 12:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("FinanceIO_App", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="transactioninfo",
            old_name="amount",
            new_name="cost",
        ),
        migrations.RenameField(
            model_name="transactioninfo",
            old_name="user",
            new_name="user_expense",
        ),
    ]