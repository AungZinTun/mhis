from django.contrib import admin
from .models import District, StateRegion, Township, Facility
from import_export import resources
from import_export.admin import ImportExportActionModelAdmin
# Register your models here.

class DistrictResource(resources.ModelResource):
    class Meta:
        model = District
        fields=("sr_pcode",
                "sr_name_eng",
                "district_pcode",
                "district_name_eng",
                "district_name_mmr",
                "myainfo_d_id",
                "source",
                "start_date",
                "modified_end_date",
                "notification",
                "notification_modified",
                "district_status",
                "change_type",
                "remark")
class DistrictAdmin(ImportExportActionModelAdmin):
    resource_class=DistrictResource

admin.site.register(StateRegion)
admin.site.register(District, DistrictAdmin)
admin.site.register(Township)
admin.site.register(Facility)
