from django.contrib import admin
from txl.models import Collection, Item, Situation


class CollectionInline(admin.TabularInline):
    model = Collection
    fk_name = 'parent'
    extra = 0


class ItemInline(admin.TabularInline):
    model = Item
    fk_name = 'collection'
    extra = 0


class SituationInline(admin.StackedInline):
    model = Situation
    fk_name = 'item'
    extra = 0


class CollectionAdmin(admin.ModelAdmin):
    inlines = [
        CollectionInline,
        ItemInline
    ]
    add_form_template = 'admin/add_without_inlines.html'


class ItemAdmin(admin.ModelAdmin):
    inlines = [
        SituationInline
    ]
    add_form_template = 'admin/add_without_inlines.html'


admin.site.register(Collection, CollectionAdmin)
admin.site.register(Item, ItemAdmin)
