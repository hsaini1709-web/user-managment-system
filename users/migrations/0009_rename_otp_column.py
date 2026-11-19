from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_rename_otp_blocked_until'),
    ]

    operations = [
        migrations.RunSQL(
            sql="""
                ALTER TABLE users_otpverification
                RENAME COLUMN otp_blocked_untill TO otp_blocked_until;
            """,
            reverse_sql="""
                ALTER TABLE users_otpverification
                RENAME COLUMN otp_blocked_until TO otp_blocked_untill;
            """
        ),
    ]