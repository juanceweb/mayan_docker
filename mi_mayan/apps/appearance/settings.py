from django.utils.translation import ugettext_lazy as _

from mayan.apps.smart_settings.classes import SettingNamespace

from .literals import (
    DEFAULT_AJAX_REDIRECTION_CODE, DEFAULT_MAXIMUM_TITLE_LENGTH,
    DEFAULT_MESSAGE_POSITION, DEFAULT_MENU_POLLING_INTERVAL,
    DEFAULT_THROTTLING_MAXIMUM_REQUESTS, DEFAULT_THROTTLING_TIMEOUT
)

namespace = SettingNamespace(
    label=_('Appearance'), name='appearance'
)

setting_ajax_redirection_code = namespace.add_setting(
    default=DEFAULT_AJAX_REDIRECTION_CODE,
    global_name='APPEARANCE_AJAX_REDIRECTION_CODE', help_text=_(
        'Custom HTTP response code for AJAX redirections.'
    )
)
setting_max_title_length = namespace.add_setting(
    default=DEFAULT_MAXIMUM_TITLE_LENGTH,
    global_name='APPEARANCE_MAXIMUM_TITLE_LENGTH', help_text=_(
        'Maximum number of characters that will be displayed as the view '
        'title.'
    )
)
setting_message_position = namespace.add_setting(
    choices=(
        'top-left', 'top-center', 'top-right', 'bottom-left',
        'bottom-center', 'bottom-right',
    ), default=DEFAULT_MESSAGE_POSITION,
    global_name='APPEARANCE_MESSAGE_POSITION', help_text=_(
        'Position where the system messages will be displayed.'
    )
)
setting_menu_polling_interval = namespace.add_setting(
    default=DEFAULT_MENU_POLLING_INTERVAL,
    global_name='APPEARANCE_MENU_POLLING_INTERVAL', help_text=_(
        'Delay in milliseconds after which the menus will be checked for '
        'updates.'
    )
)
appearance_throttling_maximum_requests = namespace.add_setting(
    default=DEFAULT_THROTTLING_MAXIMUM_REQUESTS,
    global_name='APPEARANCE_THROTTLING_MAXIMUM_REQUESTS', help_text=_(
        'Maximum number of requests that can be made before throttling '
        'is enabled.'
    )
)
appearance_throttling_timeout = namespace.add_setting(
    default=DEFAULT_THROTTLING_TIMEOUT,
    global_name='APPEARANCE_THROTTLING_TIMEOUT', help_text=_(
        'Time in milliseconds after which a throttled request will '
        'clear allowing an additional request to be performed.'
    )
)
