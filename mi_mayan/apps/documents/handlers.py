from django.apps import apps

from .literals import (
    DEFAULT_DOCUMENT_TYPE_LABEL, STORAGE_NAME_DOCUMENT_FILE_PAGE_IMAGE_CACHE,
    STORAGE_NAME_DOCUMENT_VERSION_PAGE_IMAGE_CACHE
)
from .settings import (
    setting_document_file_page_image_cache_maximum_size,
    setting_document_version_page_image_cache_maximum_size
)
from .signals import signal_post_initial_document_type


def handler_create_default_document_type(sender, **kwargs):
    DocumentType = apps.get_model(
        app_label='documents', model_name='DocumentType'
    )

    if not DocumentType.objects.count():
        document_type = DocumentType.objects.create(
            label=DEFAULT_DOCUMENT_TYPE_LABEL
        )
        signal_post_initial_document_type.send(
            sender=DocumentType, instance=document_type
        )


def handler_create_document_file_page_image_cache(sender, **kwargs):
    Cache = apps.get_model(app_label='file_caching', model_name='Cache')
    Cache.objects.update_or_create(
        defaults={
            'maximum_size': setting_document_file_page_image_cache_maximum_size.value,
        }, defined_storage_name=STORAGE_NAME_DOCUMENT_FILE_PAGE_IMAGE_CACHE
    )


def handler_create_document_version_page_image_cache(sender, **kwargs):
    Cache = apps.get_model(app_label='file_caching', model_name='Cache')
    Cache.objects.update_or_create(
        defaults={
            'maximum_size': setting_document_version_page_image_cache_maximum_size.value,
        },
        defined_storage_name=STORAGE_NAME_DOCUMENT_VERSION_PAGE_IMAGE_CACHE
    )
