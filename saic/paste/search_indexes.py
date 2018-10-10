import datetime
from haystack.indexes import *
from haystack import indexes
from models import Paste, Commit


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
