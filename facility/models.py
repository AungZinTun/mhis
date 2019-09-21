from django.db import models

# Create your models here.
class StateRegion(models.Model):
    sr_pcode=models.CharField(max_length=6, primary_key=True)
    sr_name_eng= models.CharField(max_length=30)
    sr_name_mmr= models.CharField(max_length=30)
    myainfo_sd_id= models.CharField(max_length=20)
    source= models.CharField(max_length=3)
    start_date= models.DateField()
    modified_end_date= models.DateField(blank=True, null=True)
    notification= models.CharField(max_length=50, blank=True, null=True)
    notification_modified= models.CharField(max_length=100, blank=True, null=True)
    sr_status= models.CharField(max_length=8, default='active')
    change_type= models.CharField(max_length=20, blank=True, null=True )
    remark= models.CharField(max_length=200,  blank=True, null=True)
    def __str__(self):
        return self.sr_name_mmr
class District(models.Model):
    sr_pcode= models.ForeignKey(StateRegion, on_delete=models.CASCADE , related_name="districts"  )
    district_pcode= models.CharField(max_length=10, primary_key=True)
    district_name_eng= models.CharField(max_length=50)
    district_name_mmr= models.CharField(max_length=50)
    myainfo_d_id= models.CharField(max_length=13, blank=True, null=True )
    source= models.CharField(max_length=20)
    start_date= models.DateField()
    modified_end_date= models.DateField(blank=True, null=True)
    notification= models.CharField(max_length=50, blank=True, null=True)
    notification_modified= models.CharField(max_length=100, blank=True, null=True)
    district_status= models.CharField(max_length=8, default='active')
    change_type= models.CharField(max_length=20, blank=True, null=True )
    remark= models.CharField(max_length=200,  blank=True, null=True)
    def __str__(self):
        return self.district_name_mmr

class Township(models.Model):
    sr_pcode= models.ForeignKey(StateRegion, on_delete=models.CASCADE , related_name="townships"  )
    district_pcode= models.ForeignKey(District, on_delete=models.CASCADE , related_name="townships"  )
    tsp_pcode= models.CharField(max_length=9, primary_key=True)
    township_name_eng= models.CharField(max_length=50)
    township_name_mmr= models.CharField(max_length=50)
    myainfo_ts_id= models.CharField(max_length=12)
    source= models.CharField(max_length=20)
    start_date= models.DateField()
    modified_end_date= models.DateField(blank=True, null=True)
    notification= models.CharField(max_length=50, blank=True, null=True)
    notification_modified= models.CharField(max_length=100, blank=True, null=True)
    township_status= models.CharField(max_length=8, default='active')
    change_type= models.CharField(max_length=20, blank=True, null=True )
    remark= models.CharField(max_length=200,  blank=True, null=True)
    def __str__(self):
        return self.township_name_mmr

class Facility(models.Model):
    sr_pcode= models.ForeignKey(StateRegion, on_delete=models.CASCADE , related_name="facilities"  )
    district_pcode= models.ForeignKey(District, on_delete=models.CASCADE , related_name="facilities" , null=True)
    tsp_pcode=models.ForeignKey(Township, on_delete=models.CASCADE , related_name="facilities" , null=True )
    facility_name_eng=models.CharField(max_length=50)
    facility_name_mmr=models.CharField(max_length=50)
    def __str__(self):
        return self.facility_name_mmr
