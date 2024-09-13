from django.contrib import admin
from .models import Mononucleotides, Dinucleotides, Trinucleotides, Tetranucleotides, Pentanucleotides, Hexanucleotides

class MononucleotidesAdmin(admin.ModelAdmin):
    list_display = ('ID', 'Chromosome', 'SSRtype', 'SSRsequence', 'Size', 'Start', 'End')
    search_fields = ('Chromosome', 'SSRtype', 'Start', 'End')

class DinucleotidesAdmin(admin.ModelAdmin):
    list_display = ('ID', 'Chromosome', 'SSRtype', 'SSRsequence', 'Size', 'Start', 'End')
    search_fields = ('Chromosome', 'SSRtype', 'Start', 'End')

class TrinucleotidesAdmin(admin.ModelAdmin):
    list_display = ('ID', 'Chromosome', 'SSRtype', 'SSRsequence', 'Size', 'Start', 'End')
    search_fields = ('Chromosome', 'SSRtype', 'Start', 'End')

class TetranucleotidesAdmin(admin.ModelAdmin):
    list_display = ('ID', 'Chromosome', 'SSRtype', 'SSRsequence', 'Size', 'Start', 'End')
    search_fields = ('Chromosome', 'SSRtype', 'Start', 'End')

class PentanucleotidesAdmin(admin.ModelAdmin):
    list_display = ('ID', 'Chromosome', 'SSRtype', 'SSRsequence', 'Size', 'Start', 'End')
    search_fields = ('Chromosome', 'SSRtype', 'Start', 'End')
    
class HexanucleotidesAdmin(admin.ModelAdmin):
    list_display = ('ID', 'Chromosome', 'SSRtype', 'SSRsequence', 'Size', 'Start', 'End')
    search_fields = ('Chromosome', 'SSRtype', 'Start', 'End')

admin.site.register(Mononucleotides, MononucleotidesAdmin)
admin.site.register(Dinucleotides, DinucleotidesAdmin)
admin.site.register(Trinucleotides, TrinucleotidesAdmin)
admin.site.register(Tetranucleotides, TetranucleotidesAdmin)
admin.site.register(Pentanucleotides, PentanucleotidesAdmin)
admin.site.register(Hexanucleotides, HexanucleotidesAdmin)
