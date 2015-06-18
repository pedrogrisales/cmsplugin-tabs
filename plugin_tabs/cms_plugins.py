from django.contrib.admin import StackedInline

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from models import TabsList, Tab, DEFAULT_TEMPLATE


class TabInline(StackedInline):
    model = Tab
    extra = 1
    #prepopulated_fields = {"contenido": ("titulo",)}


class TabsListPlugin(CMSPluginBase):
    model = TabsList
    module = 'Tabs'
    name = 'Tabs'
    admin_preview = False
    render_template = DEFAULT_TEMPLATE
    inlines = [TabInline]


    def render(self, context, instance, placeholder):
        self.render_template = instance.get_template()
        context.update({
            'tabs_list_id': 'tabs_list_plugin_%s' % instance.pk,
            'tabs': instance.tabs.all(),
            })
        return context

plugin_pool.register_plugin(TabsListPlugin)
