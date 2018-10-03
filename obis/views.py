from rest_framework import viewsets, filters, serializers
from rest_framework.renderers import BrowsableAPIRenderer, JSONPRenderer,JSONRenderer,XMLRenderer,YAMLRenderer
from rest_framework_csv.renderers import CSVRenderer
from obis.filters import AcctaxFilter,ComtaxFilter #,SearchViewFilter
from obis.models import Acctax,Comtax,Syntax,Hightax,FedStatus,StStatus,OkSwap,RankChange
from obis.models import Occurrence,Source,Institution,County,CoTrs,IdentificationVerification
from obis.models import *
#SpatialRefSys #, VwSearch, VwSearchmv #SearchView
from serializer import *
from rest_framework import permissions
from rest_framework.parsers import JSONParser,MultiPartParser,FormParser,FileUploadParser


#DB Table ViewSet Class
class obisTableViewSet(viewsets.ModelViewSet):
    renderer_classes = (BrowsableAPIRenderer, JSONRenderer,JSONPRenderer,XMLRenderer,YAMLRenderer)
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter,filters.OrderingFilter)

#DB View ViewSet Class
class obisViewViewSet(viewsets.ReadOnlyModelViewSet):
    renderer_classes = (BrowsableAPIRenderer, JSONRenderer,JSONPRenderer,XMLRenderer,YAMLRenderer,CSVRenderer)
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter,filters.OrderingFilter)

#***************************************** OBIS Tables **********************************************************
class AcctaxViewSet(obisTableViewSet):
    """
    This is the Acctax ViewSet with hyperlinked tables.
    """
    model = Acctax
    queryset = Acctax.objects.all()
    serializer_class = AcctaxSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    renderer_classes = (BrowsableAPIRenderer, JSONRenderer,JSONPRenderer,XMLRenderer,YAMLRenderer)
    filter_class = AcctaxFilter
    search_fields = ("sname","scientificnameauthorship","genus","species","subspecies","variety",
                     "forma","elcode","iucncode","g_rank","s_rank","nativity","source","usda_code",
                     "name","sspscientificnameauthorship","varscientificnameauthorship",
                     "formascientificnameauthorship")
    ordering_fields = ("sname","scientificnameauthorship","family","genus","species","subspecies","variety",
                     "forma","elcode","gelcode","iucncode","g_rank","s_rank","nativity","source","usda_code","tsn",
                     "fed_status","st_status","swap","name","sspscientificnameauthorship","varscientificnameauthorship",
                     "formascientificnameauthorship","tracked")

    #search_fields = ('acode','sname','scientificnameauthorship','phylum','taxclass','taxorder','family','genus',
    #                'species','subspecies','variety','forma','elcode','gelcode','iunccode','g_rank','s_rank',
    #                'nativity','source','comtax__vernacularname')
    #ordering_fields = ('acode','sname','scientificnameauthorship','phylum','taxclass','taxorder','family','genus',
    #                'species','subspecies','variety','forma','elcode','gelcode','iunccode','g_rank','s_rank',
    #                'nativity','source')

class ComtaxViewSet(obisTableViewSet):
    """
    This is the Comtax ViewSet with hyperlinked tables.
    """
    model = Comtax
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    renderer_classes = (BrowsableAPIRenderer, JSONRenderer,JSONPRenderer,XMLRenderer,YAMLRenderer)
    queryset = Comtax.objects.all()
    serializer_class =  ComtaxSerializer
    filter_class = ComtaxFilter
    search_fields = ('acode','vernacularname','primary_name')

class SyntaxViewSet(obisTableViewSet):
    """
    This is the Syntax ViewSet with hyperlinked tables.
    """
    model = Syntax
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    renderer_classes = (BrowsableAPIRenderer, JSONRenderer,JSONPRenderer,XMLRenderer,YAMLRenderer)
    queryset = Syntax.objects.all()
    serializer_class =  SyntaxSerializer
    search_fields = ('acode','scode','sname','scientificnameauthorship',
                    'family','genus','species','subspecies','variety',
                    'name','sspscientificnameauthorship','varscientificnameauthorship',
                    'formascientificnameauthorship')
    ordering_fields = ('s_id','acode','scode','sname','scientificnameauthorship',
                    'family','genus','species','subspecies','variety',
                    'name','sspscientificnameauthorship','varscientificnameauthorship',
                    'formascientificnameauthorship','tsn')

class HightaxViewSet(obisTableViewSet):
    """
    This is the Hightax ViewSet with hyperlinked tables.
    """
    model = Hightax
    queryset = Hightax.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    renderer_classes = (BrowsableAPIRenderer, JSONRenderer,JSONPRenderer,XMLRenderer,YAMLRenderer)
    serializer_class = HightaxSerializer

class FedStatusViewSet(obisTableViewSet):
    """
    This is the Fed Status ViewSet with hyperlinked tables.
    """
    model = FedStatus
    queryset = FedStatus.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    renderer_classes = (BrowsableAPIRenderer, JSONRenderer,JSONPRenderer,XMLRenderer,YAMLRenderer)
    serializer_class = FedStatusSerializer

class StStatusViewSet(obisTableViewSet):
    """
    This is the State Status ViewSet with hyperlinked tables.
    """
    model = StStatus
    queryset = StStatus.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    renderer_classes = (BrowsableAPIRenderer, JSONRenderer,JSONPRenderer,XMLRenderer,YAMLRenderer)
    serializer_class = StStatusSerializer

class OkSwapViewSet(obisTableViewSet):
    """
    This is the Ok Swap  ViewSet with hyperlinked tables.
    """
    model = OkSwap
    queryset = OkSwap.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    renderer_classes = (BrowsableAPIRenderer, JSONRenderer,JSONPRenderer,XMLRenderer,YAMLRenderer)
    serializer_class = OkSwapSerializer

class OccurrenceViewSet(obisTableViewSet):
    """
    This is the Occurrence ViewSet with hyperlinked tables.
    """
    model = Occurrence
    queryset = Occurrence.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    renderer_classes = (BrowsableAPIRenderer, JSONRenderer,JSONPRenderer,XMLRenderer,YAMLRenderer)
    serializer_class = OccurenceSerializer

class SourceViewSet(obisTableViewSet):
    """
    This is the Ok Swap  ViewSet with hyperlinked tables.
    """
    model = Source
    queryset = Source.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    renderer_classes = (BrowsableAPIRenderer, JSONRenderer,JSONPRenderer,XMLRenderer,YAMLRenderer)
    serializer_class = SourceSerializer

class InstitutionViewSet(obisTableViewSet):
    """
    This is the Institution  ViewSet with hyperlinked tables.
    """
    model = Institution
    queryset = Institution.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    renderer_classes = (BrowsableAPIRenderer, JSONRenderer,JSONPRenderer,XMLRenderer,YAMLRenderer)
    serializer_class = InstitutionSerializer

class CountyViewSet(obisTableViewSet):
    """
    This is the County ViewSet with hyperlinked tables.
    """
    model = County
    queryset = County.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    renderer_classes = (BrowsableAPIRenderer, JSONRenderer,JSONPRenderer,XMLRenderer,YAMLRenderer)
    serializer_class = CountySerializer

class CoTrsViewSet(obisTableViewSet):
    """
    This is the CoTrs ViewSet with hyperlinked tables.
    """
    model = CoTrs
    queryset = CoTrs.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    renderer_classes = (BrowsableAPIRenderer, JSONRenderer,JSONPRenderer,XMLRenderer,YAMLRenderer)
    serializer_class = CoTrsSerializer

class IdentificationVerificationViewSet(obisTableViewSet):
    """
    This is the IdentificationVerification ViewSet with hyperlinked tables.
    """
    model = IdentificationVerification
    queryset = IdentificationVerification.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    renderer_classes = (BrowsableAPIRenderer, JSONRenderer,JSONPRenderer,XMLRenderer,YAMLRenderer)
    serializer_class = IdentificationVerificationSerializer

class RankChangeViewSet(obisTableViewSet):
    """
    This is the Rank Change ViewSet with hyperlinked tables.
    """
    model = RankChange
    queryset = RankChange.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    renderer_classes = (BrowsableAPIRenderer, JSONRenderer,JSONPRenderer,XMLRenderer,YAMLRenderer)
    serializer_class = RankChangeSerializer

class SpatialRefSysViewSet(obisTableViewSet):
    """
    This is the Spatial-Ref-Sys  ViewSet with hyperlinked tables.
    """
    model = SpatialRefSys
    queryset = SpatialRefSys.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    renderer_classes = (BrowsableAPIRenderer, JSONRenderer,JSONPRenderer,XMLRenderer,YAMLRenderer)
    serializer_class = SpatialRefSysSerializer

#***************************************** OBIS DB Views ********************************************************
"""
class VwSearchViewSet(obisViewViewSet):
    ""
    This is the Search ViewSet with hyperlinked tables.
    ""
    model = VwSearch
    queryset = VwSearch.objects.all()
    search_fields = ('acode', 'elcode', 'family', 'fed_status_id', 'forma', 'formascientificnameauthorship',
    'g_rank', 'gelcode', 'genus', 'itis_code', 'iucncode', 'name', 'nativity', 'pkey', 'primary_name', 's_rank', 'scientificnameauthorship',
    'sname', 'source', 'species', 'sspscientificnameauthorship', 'st_status_id', 'subspecies', 'swap_id', 'tracked',
    'usda_code', 'variety', 'varscientificnameauthorship', 'vernacularname','kingdom','phylum','taxclass','taxorder')
    ordering_fields = ('acode', 'elcode', 'family', 'fed_status_id', 'forma', 'formascientificnameauthorship',
    'g_rank', 'gelcode', 'genus', 'itis_code', 'iucncode', 'name', 'nativity', 'pkey', 'primary_name', 's_rank', 'scientificnameauthorship',
    'sname', 'source', 'species', 'sspscientificnameauthorship', 'st_status_id', 'subspecies', 'swap_id', 'tracked',
    'usda_code', 'variety', 'varscientificnameauthorship', 'vernacularname','kingdom','phylum','taxclass','taxorder')

class VwSearchmvViewSet(obisViewViewSet):
    ""
    This is the Material View Search ViewSet with hyperlinked tables.
    Database: When data updated must run to update view: 'REFRESH MATERIALIZED VIEW vm_search_mv;'
    ""
    model = VwSearchmv
    queryset = VwSearchmv.objects.all()
    search_fields = ('acode', 'elcode', 'family', 'fed_status_id', 'forma', 'formascientificnameauthorship',
    'g_rank', 'gelcode', 'genus', 'itis_code', 'iucncode', 'name', 'nativity', 'pkey', 'primary_name', 's_rank', 'scientificnameauthorship',
    'sname', 'source', 'species', 'sspscientificnameauthorship', 'st_status_id', 'subspecies', 'swap_id', 'tracked',
    'usda_code', 'variety', 'varscientificnameauthorship', 'vernacularname','kingdom','phylum','taxclass','taxorder')
    ordering_fields = ('acode', 'elcode', 'family', 'fed_status_id', 'forma', 'formascientificnameauthorship',
    'g_rank', 'gelcode', 'genus', 'itis_code', 'iucncode', 'name', 'nativity', 'pkey', 'primary_name', 's_rank', 'scientificnameauthorship',
    'sname', 'source', 'species', 'sspscientificnameauthorship', 'st_status_id', 'subspecies', 'swap_id', 'tracked',
    'usda_code', 'variety', 'varscientificnameauthorship', 'vernacularname','kingdom','phylum','taxclass','taxorder')
"""
