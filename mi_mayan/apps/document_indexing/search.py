from django.utils.translation import ugettext_lazy as _

from mayan.apps.dynamic_search.search_models import SearchModel

from .permissions import permission_index_instance_view

search_model_index_instance_node = SearchModel(
    app_label='document_indexing', model_name='IndexInstanceNodeSearchResult',
    permission=permission_index_instance_view,
    serializer_path='mayan.apps.document_indexing.serializers.IndexInstanceNodeSerializer'
)
search_model_index_instance_node.add_proxy_model(
    app_label='document_indexing', model_name='IndexInstanceNode'
)

search_model_index_instance_node.add_model_field(
    field='value', label=_('Value')
)

search_model_index_instance_node.add_model_field(
    field='documents__document_type__label', label=_('Document type')
)
search_model_index_instance_node.add_model_field(
    field='documents__files__mimetype', label=_('Document MIME type')
)
search_model_index_instance_node.add_model_field(
    field='documents__label', label=_('Document label')
)
search_model_index_instance_node.add_model_field(
    field='documents__description', label=_('Document description')
)
search_model_index_instance_node.add_model_field(
    field='documents__uuid', label=_('Document UUID')
)
search_model_index_instance_node.add_model_field(
    field='documents__files__checksum', label=_('Document checksum')
)
