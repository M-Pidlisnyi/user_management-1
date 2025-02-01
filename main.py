import django_setup
from users.models import User, Role

# new_role = Role(role_name = "tester")
# new_role.save()

# newer_role = Role.objects.create(role_name = "newcomer")

new_role = Role.objects.get_or_create(role_name = "superadmin")
print(new_role)