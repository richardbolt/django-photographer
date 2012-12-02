from haystack import indexes, fields
from elephantblog.models import Entry


class EntryIndex(indexes.RealTimeSearchIndex, indexes.Indexable):
    """
    Index for FeinCMS ElephantBlog Entry objects.

    Body is generated using a complex template which includes rendered content
    for many content objects.
    
    """

    url = fields.CharField(model_attr="get_absolute_url")
    title = fields.CharField(model_attr="title")
    text = fields.CharField(document=True, use_template=True)
    pub_date = fields.DateTimeField(model_attr="published_on", null=True)
    mod_date = fields.DateTimeField(model_attr="last_changed", null=True)
    
    def get_model(self):
        return Entry
    
    def should_update(self, instance, **kwargs):
        return True # instance.is_active()

    def index_queryset(self):
        """
        Return a Django QuerySet used for all search-related queries.
        Currently we index all active pages.
        
        """
        return Entry.objects.active()

    def get_updated_field(self):
        return "mod_date"
