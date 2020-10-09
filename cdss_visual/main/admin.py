from django.contrib import admin
from .models import Patients, CompleteBloodCount, \
                    ClinicalUrineTest, BiochemicalBloodAnalysis, \
                    CoagulogramTest, SputumTest, Document

# Register your models here.

admin.site.register(Patients)
admin.site.register(CompleteBloodCount)
admin.site.register(ClinicalUrineTest)
admin.site.register(BiochemicalBloodAnalysis)
admin.site.register(CoagulogramTest)
admin.site.register(SputumTest)
admin.site.register(Document)
