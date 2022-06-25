from django.contrib.auth.tokens import PasswordResetTokenGenerator
import six


class UserTokenGenerator(PasswordResetTokenGenerator):

    def _make_hash_value(self, User, timestamp):
        return (six.text_type(User.pk)+six.text_type(timestamp)+six.text_type(User.is_email_verified))


generate_user_token = UserTokenGenerator()


class AdminTokenGenerator(PasswordResetTokenGenerator):

    def _make_hash_value(self, User, timestamp):
        return (six.text_type(User.pk)+six.text_type(timestamp)+six.text_type(User.is_active))


generate_admin_token = AdminTokenGenerator()