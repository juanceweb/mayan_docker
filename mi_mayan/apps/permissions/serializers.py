from django.contrib.auth.models import Group
from django.utils.translation import ugettext_lazy as _

from mayan.apps.rest_api import serializers
from mayan.apps.rest_api.relations import FilteredPrimaryKeyRelatedField
from mayan.apps.user_management.permissions import permission_group_edit

from .classes import Permission
from .models import Role, StoredPermission


class PermissionSerializer(serializers.Serializer):
    namespace = serializers.CharField(
        label=_('Namespace'), read_only=True
    )
    pk = serializers.CharField(
        label=_('Primary key'), read_only=True
    )
    label = serializers.CharField(
        label=_('Label'), read_only=True
    )

    def to_representation(self, instance):
        if isinstance(instance, StoredPermission):
            return super().to_representation(
                instance.volatile_permission
            )
        else:
            return super().to_representation(
                instance
            )


class RoleGroupAddSerializer(serializers.Serializer):
    group = FilteredPrimaryKeyRelatedField(
        help_text=_('Primary key of the group to add to the role.'),
        label=_('Group ID'), source_queryset=Group.objects.all(),
        source_permission=permission_group_edit
    )


class RoleGroupRemoveSerializer(serializers.Serializer):
    group = FilteredPrimaryKeyRelatedField(
        help_text=_('Primary key of the group to remove from the role.'),
        label=_('Group ID'), source_queryset=Group.objects.all(),
        source_permission=permission_group_edit
    )


class RolePermissionAddSerializer(serializers.Serializer):
    permission = FilteredPrimaryKeyRelatedField(
        help_text=_('Primary key of the permission to add to the role.'),
        label=_('Permission ID'), source_queryset=Permission.all()
    )


class RolePermissionRemoveSerializer(serializers.Serializer):
    permission = FilteredPrimaryKeyRelatedField(
        help_text=_(
            'Primary key of the permission to remove from the role.'
        ), label=_('Permission ID'), source_queryset=Permission.all()
    )


class RoleSerializer(serializers.HyperlinkedModelSerializer):
    groups_url = serializers.HyperlinkedIdentityField(
        label=_('Groups URL'), lookup_url_kwarg='role_id',
        view_name='rest_api:role-group-list'
    )
    groups_add_url = serializers.HyperlinkedIdentityField(
        label=_('Groups add URL'), lookup_url_kwarg='role_id',
        view_name='rest_api:role-group-add'
    )
    groups_remove_url = serializers.HyperlinkedIdentityField(
        label=_('Groups remove URL'), lookup_url_kwarg='role_id',
        view_name='rest_api:role-group-remove'
    )
    permissions_url = serializers.HyperlinkedIdentityField(
        label=_('Permissions URL'), lookup_url_kwarg='role_id',
        view_name='rest_api:role-permission-list'
    )
    permissions_add_url = serializers.HyperlinkedIdentityField(
        label=_('Permissions add URL'), lookup_url_kwarg='role_id',
        view_name='rest_api:role-permission-add'
    )
    permissions_remove_url = serializers.HyperlinkedIdentityField(
        label=_('Permissions remove URL'), lookup_url_kwarg='role_id',
        view_name='rest_api:role-permission-remove'
    )

    class Meta:
        extra_kwargs = {
            'url': {
                'label': _('URL'),
                'lookup_url_kwarg': 'role_id',
                'view_name': 'rest_api:role-detail'
            }
        }
        fields = (
            'groups_add_url', 'groups_remove_url', 'groups_url', 'id',
            'label', 'permissions_add_url', 'permissions_url',
            'permissions_remove_url', 'url'
        )
        model = Role
