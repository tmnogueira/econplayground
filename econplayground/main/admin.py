from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportActionModelAdmin
from econplayground.main.models import Graph, Assessment, AssessmentRule


class AssessmentResource(resources.ModelResource):
    class Meta:
        model = Assessment
        fields = ('graph',)


class AssessmentRuleResource(resources.ModelResource):
    class Meta:
        model = AssessmentRule
        fields = ('name', 'value', 'feedback_fulfilled',
                  'feedback_unfulfilled', 'score',)
        export_order = ('name', 'value', 'feedback_fulfilled',
                        'feedback_unfulfilled', 'score',)


class AssessmentAdmin(ImportExportActionModelAdmin):
    resource_class = AssessmentResource


admin.site.register(Graph)
admin.site.register(Assessment, AssessmentAdmin)
