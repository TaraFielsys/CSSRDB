from django.db import models


class Dinucleotides(models.Model):
    ID = models.IntegerField(db_column='ID', primary_key=True)
    Chromosome = models.CharField(db_column='Chromosome No', max_length=100, blank=True, null=True)
    SSRtype = models.CharField(db_column='SSR type', max_length=100, blank=True, null=True)
    SSRsequence = models.CharField(db_column='SSR sequence', max_length=10000, blank=True, null=True)
    Size = models.IntegerField(db_column='Size', blank=True, null=True)
    Start = models.IntegerField(db_column='Start', blank=True, null=True)
    End = models.IntegerField(db_column='End', blank=True, null=True)

    def __str__(self):
        return self.SSRsequence

class Hexanucleotides(models.Model):
    ID = models.IntegerField(db_column='ID', primary_key=True)
    Chromosome = models.CharField(db_column='Chromosome No', max_length=100, blank=True, null=True)
    SSRtype = models.CharField(db_column='SSR type', max_length=100, blank=True, null=True)
    SSRsequence = models.CharField(db_column='SSR sequence', max_length=10000, blank=True, null=True)
    Size = models.IntegerField(db_column='Size', blank=True, null=True)
    Start = models.IntegerField(db_column='Start', blank=True, null=True)
    End = models.IntegerField(db_column='End', blank=True, null=True)
    
    def __str__(self):
        return self.SSRsequence

class Mononucleotides(models.Model):
    ID = models.IntegerField(db_column='ID', primary_key=True)
    Chromosome = models.CharField(db_column='Chromosome No', max_length=100, blank=True, null=True)
    SSRtype = models.CharField(db_column='SSR type', max_length=100, blank=True, null=True)
    SSRsequence = models.CharField(db_column='SSR sequence', max_length=10000, blank=True, null=True)
    Size = models.IntegerField(db_column='Size', blank=True, null=True)
    Start = models.IntegerField(db_column='Start', blank=True, null=True)
    End = models.IntegerField(db_column='End', blank=True, null=True)
    
    def __str__(self):
        return self.SSRsequence

class Pentanucleotides(models.Model):
    ID = models.IntegerField(db_column='ID', primary_key=True)
    Chromosome = models.CharField(db_column='Chromosome No', max_length=100, blank=True, null=True)
    SSRtype = models.CharField(db_column='SSR type', max_length=100, blank=True, null=True)
    SSRsequence = models.CharField(db_column='SSR sequence', max_length=10000, blank=True, null=True)
    Size = models.IntegerField(db_column='Size', blank=True, null=True)
    Start = models.IntegerField(db_column='Start', blank=True, null=True)
    End = models.IntegerField(db_column='End', blank=True, null=True)
    
    def __str__(self):
        return self.SSRsequence

class Tetranucleotides(models.Model):
    ID = models.IntegerField(db_column='ID', primary_key=True)
    Chromosome = models.CharField(db_column='Chromosome No', max_length=100, blank=True, null=True)
    SSRtype = models.CharField(db_column='SSR type', max_length=100, blank=True, null=True)
    SSRsequence = models.CharField(db_column='SSR sequence', max_length=10000, blank=True, null=True)
    Size = models.IntegerField(db_column='Size', blank=True, null=True)
    Start = models.IntegerField(db_column='Start', blank=True, null=True)
    End = models.IntegerField(db_column='End', blank=True, null=True)
    
    def __str__(self):
        return self.SSRsequence

class Trinucleotides(models.Model):
    ID = models.IntegerField(db_column='ID', primary_key=True)
    Chromosome = models.CharField(db_column='Chromosome No', max_length=100, blank=True, null=True)
    SSRtype = models.CharField(db_column='SSR type', max_length=100, blank=True, null=True)
    SSRsequence = models.CharField(db_column='SSR sequence', max_length=10000, blank=True, null=True)
    Size = models.IntegerField(db_column='Size', blank=True, null=True)
    Start = models.IntegerField(db_column='Start', blank=True, null=True)
    End = models.IntegerField(db_column='End', blank=True, null=True)
    
    def __str__(self):
        return self.SSRsequence
