import logging
from django.http import JsonResponse
from django.shortcuts import redirect

from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView

from mayan.apps.acls.models import AccessControlList
from mayan.apps.rest_api import generics

from ..classes import DocumentFileAction
from ..models.document_models import Document
from ..models.document_type_models import DocumentType
from ..permissions import (
    permission_document_change_type, permission_document_create,
    permission_document_properties_edit, permission_document_trash,
    permission_document_view
)
from ..serializers.document_serializers import (
    DocumentFileActionSerializer, DocumentSerializer,
    DocumentChangeTypeSerializer, DocumentUploadSerializer,
)



from .document_api_functions import cargar_modelo_extra, update_modelo_extra, obtener_form


logger = logging.getLogger(name=__name__)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
##################################################################################
# Controlador API /document_form/document_type_id
##################################################################################
class APIFormView(APIView):

    def get(self, request,format=None, *args, **kwargs):

        document_type_id = kwargs['document_type_id']

        form = obtener_form(document_type_id, initial= {'document_type_id': document_type_id } )

        form = form.as_p()
        
        return JsonResponse( {'form': form } )
    
    def post(self, request, format=None, *args, **kwargs):

        document_type_id = kwargs['document_type_id']

        form = obtener_form(document_type_id, request.POST, request.FILES)

        if form.is_valid():
            return JsonResponse({ 'success': True })
        
        else:
            form = form.as_p()
            return JsonResponse({'success': False, 'form': form })
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

##################################################################################
# Controlador API /documents/id
##################################################################################
class APIDocumentDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Returns the selected document details.
    delete: Move the selected document to the thrash.
    get: Return the details of the selected document.
    patch: Edit the properties of the selected document.
    put: Edit the properties of the selected document.
    """
    lookup_url_kwarg = 'document_id'
    mayan_object_permissions = {
        'GET': (permission_document_view,),
        'PUT': (permission_document_properties_edit,),
        'PATCH': (permission_document_properties_edit,),
        'DELETE': (permission_document_trash,)
    }
    serializer_class = DocumentSerializer
    source_queryset = Document.valid.all()
    
    def get_instance_extra_data(self):
        return {
            '_event_actor': self.request.user,
    }
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    def put(self, request, *args, **kwargs):
        doc_id = kwargs['document_id']
        document = Document.objects.get(id = doc_id)

        update_modelo_extra(document, request.data)

        return self.update(request, *args, **kwargs)
    #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        



class APIDocumentFileActionListView(generics.ListAPIView):
    """
    get: Returns a list of the available document file actions.
    """
    serializer_class = DocumentFileActionSerializer

    def get_serializer_context(self):
        return {
            'format': self.format_kwarg,
            'request': self.request,
            'view': self
        }

    def get_source_queryset(self):
        return DocumentFileAction.get_all()

##################################################################################
# Controlador API /documents
##################################################################################
class APIDocumentListView(generics.ListCreateAPIView):
    """
    get: Returns a list of all the documents.
    post: Create a new document.
    """
    mayan_object_permissions = {
        'GET': (permission_document_view,),
    }
    ordering_fields = ('datetime_created', 'document_type', 'id', 'label')
    serializer_class = DocumentSerializer
    source_queryset = Document.valid.all()

    def perform_create(self, serializer):
        queryset = DocumentType.objects.all()

        queryset = AccessControlList.objects.restrict_queryset(
            permission=permission_document_create, queryset=queryset,
            user=self.request.user
        )

        serializer.validated_data['document_type'] = get_object_or_404(
            pk=serializer.validated_data['document_type_id'],
            queryset=queryset
        )

        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        if hasattr(self, 'get_instance_extra_data'):
            serializer.validated_data['_instance_extra_data'] = self.get_instance_extra_data()
        
        cargar_modelo_extra(serializer.validated_data['document_type_id'], serializer)     
        #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

        super().perform_create(serializer=serializer)

    def get_instance_extra_data(self):
        return {
            '_event_actor': self.request.user,
            #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            'extras': self.request.data
            #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        }


class APIDocumentChangeTypeView(generics.ObjectActionAPIView):
    """
    post: Change the type of the selected document.
    """
    lookup_url_kwarg = 'document_id'
    mayan_object_permissions = {
        'POST': (permission_document_change_type,)
    }
    serializer_class = DocumentChangeTypeSerializer
    source_queryset = Document.valid.all()

    def object_action(self, obj, request, serializer):
        document_type_id = serializer.validated_data['document_type_id']
        obj.document_type_change(
            document_type=document_type_id, user=self.request.user
        )

##################################################################################
# Controlador API /documents/id/upload
##################################################################################
class APIDocumentUploadView(generics.CreateAPIView):
    """
    post: Create a new document and a new document file.
    """
    serializer_class = DocumentUploadSerializer

    def perform_create(self, serializer):
        queryset = DocumentType.objects.all()

        queryset = AccessControlList.objects.restrict_queryset(
            permission=permission_document_create, queryset=queryset,
            user=self.request.user
        )

        serializer.validated_data['document_type'] = get_object_or_404(
            pk=serializer.validated_data['document_type_id'],
            queryset=queryset
        )

        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        if hasattr(self, 'get_instance_extra_data'):
            serializer.validated_data['_instance_extra_data'] = self.get_instance_extra_data()
        
        cargar_modelo_extra(serializer.validated_data['document_type_id'], serializer)     
        #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

        super().perform_create(serializer=serializer)

    def get_instance_extra_data(self):

        return {
            '_event_actor': self.request.user,
            #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            'extras': self.request.data
            #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<    
        }
