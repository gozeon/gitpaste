import datetime
from haystack.indexes import *
from haystack import indexes
from models import Paste, Commit, Set


class PasteIndex(indexes.SearchIndex, indexes.Indexable):
    text = CharField(document=True, use_template=True)
    paste = CharField(model_attr='paste')
    filename = CharField(model_attr='filename')
    language = CharField(model_attr='language')
    commit = CharField(model_attr='revision__commit')

    def get_model(self):
        return Paste

    def index_queryset(self, using=None):
        return Paste.objects.all()


class SetIndex(indexes.SearchIndex, indexes.Indexable):
    text = CharField(document=True, use_template=True)
    description = CharField(model_attr='description')

    def get_model(self):
        return Set

    def index_queryset(self, using=None):
        return Set.objects.all()
