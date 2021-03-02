from django.contrib.auth.models import Group
from rest_framework import permissions


def is_in_group(user, group_name):
    """
    Returns `True` if the user is in group.
    """

    try:
        return Group.objects.get(
            name=group_name
        ).user_set.filter(id=user.id).exists()
    except Group.DoesNotExist:
        return None


class HasGroupPermission(permissions.BasePermission):
    """
    Ensure user is in required groups.
    """

    def has_permission(self, request, view):
        # Get a mapping of methods -> required group.
        required_groups_mapping = getattr(view, "required_groups", {})
        # get method what are you used
        required_groups = required_groups_mapping.get(request.method, [])
        return any([is_in_group(request.user, group_name) if
                    group_name != "__all__" else True
                    for group_name in required_groups]) \
               or (request.user
                   and request.user.is_staff)
