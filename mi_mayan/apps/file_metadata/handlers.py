from django.apps import apps

from .settings import setting_auto_process


def handler_initialize_new_document_type_file_metadata_settings(
    sender, instance, **kwargs
):
    DocumentTypeSettings = apps.get_model(
        app_label='file_metadata', model_name='DocumentTypeSettings'
    )

    if kwargs['created']:
        DocumentTypeSettings.objects.create(
            auto_process=setting_auto_process.value, document_type=instance
        )


def process_document_file_metadata(sender, instance, **kwargs):
    if instance.document.document_type.file_metadata_settings.auto_process:
        instance.submit_for_file_metadata_processing()
