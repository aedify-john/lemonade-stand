from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from src.models import Sale


class Command(BaseCommand):
    help = "Sets up groups and permissions for the Lemonade Stand project"

    def handle(self, *args, **options):
        # Create the Site Owner group
        group_name = "Site Owner"
        group, group_created = Group.objects.get_or_create(name=group_name)
        if group_created:
            self.stdout.write(f"Group '{group_name}' created successfully.")
        else:
            self.stdout.write(f"Group '{group_name}' already exists.")

        # Ensure the content type for the model exists
        content_type = ContentType.objects.get_for_model(Sale)

        # Create the can_transfer_money permission
        permission_codename = "can_transfer_money"
        permission_name = "Can transfer money to a bank account"
        permission, perm_created = Permission.objects.get_or_create(
            codename=permission_codename,
            name=permission_name,
            content_type=content_type,
        )
        if perm_created:
            self.stdout.write(f"Permission '{permission_name}' created successfully.")
        else:
            self.stdout.write(f"Permission '{permission_name}' already exists.")

        # Assign the permission to the Site Owner group
        if not group.permissions.filter(codename=permission_codename).exists():
            group.permissions.add(permission)
            group.save()
            self.stdout.write(f"Permission '{permission_name}' added to group '{group_name}'.")
        else:
            self.stdout.write(f"Group '{group_name}' already has permission '{permission_name}'.")

        self.stdout.write("Permissions setup completed successfully.")
