# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#

from django.db import models

class Citybycountry(models.Model):
    city = models.IntegerField(primary_key=True)
    country = models.IntegerField()
    name = models.CharField(max_length=600)
    lat = models.FloatField(null=True, blank=True)
    lng = models.FloatField(null=True, blank=True)
    state = models.CharField(max_length=192)
    class Meta:
        db_table = u'cityByCountry'

class Countries(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=144)
    code = models.CharField(max_length=6)
    class Meta:
        db_table = u'countries'

class ZipCode(models.Model):
    zip_code = models.IntegerField(primary_key=True)
    lattitude = models.FloatField()
    longitude = models.FloatField()
    city = models.CharField(max_length=75)
    state_prefix = models.CharField(max_length=6)
    zip_class = models.CharField(max_length=60)
    class Meta:
        db_table = u'zip_code'

class Ip4_0(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_0'

class Ip4_1(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_1'

class Ip4_10(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_10'

class Ip4_100(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_100'

class Ip4_101(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_101'

class Ip4_102(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_102'

class Ip4_103(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_103'

class Ip4_104(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_104'

class Ip4_105(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_105'

class Ip4_106(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_106'

class Ip4_107(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_107'

class Ip4_108(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_108'

class Ip4_109(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_109'

class Ip4_11(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_11'

class Ip4_110(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_110'

class Ip4_111(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_111'

class Ip4_112(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_112'

class Ip4_113(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_113'

class Ip4_114(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_114'

class Ip4_115(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_115'

class Ip4_116(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_116'

class Ip4_117(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_117'

class Ip4_118(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_118'

class Ip4_119(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_119'

class Ip4_12(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_12'

class Ip4_120(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_120'

class Ip4_121(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_121'

class Ip4_122(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_122'

class Ip4_123(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_123'

class Ip4_124(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_124'

class Ip4_125(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_125'

class Ip4_126(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_126'

class Ip4_127(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_127'

class Ip4_128(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_128'

class Ip4_129(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_129'

class Ip4_13(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_13'

class Ip4_130(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_130'

class Ip4_131(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_131'

class Ip4_132(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_132'

class Ip4_133(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_133'

class Ip4_134(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_134'

class Ip4_135(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_135'

class Ip4_136(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_136'

class Ip4_137(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_137'

class Ip4_138(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_138'

class Ip4_139(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_139'

class Ip4_14(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_14'

class Ip4_140(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_140'

class Ip4_141(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_141'

class Ip4_142(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_142'

class Ip4_143(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_143'

class Ip4_144(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_144'

class Ip4_145(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_145'

class Ip4_146(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_146'

class Ip4_147(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_147'

class Ip4_148(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_148'

class Ip4_149(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    class Meta:
        db_table = u'ip4_149'

class Ip4_15(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_15'

class Ip4_150(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_150'

class Ip4_151(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_151'

class Ip4_152(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_152'

class Ip4_153(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_153'

class Ip4_154(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_154'

class Ip4_155(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_155'

class Ip4_156(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_156'

class Ip4_157(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_157'

class Ip4_158(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_158'

class Ip4_159(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_159'

class Ip4_16(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_16'

class Ip4_160(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_160'

class Ip4_161(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_161'

class Ip4_162(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_162'

class Ip4_163(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_163'

class Ip4_164(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_164'

class Ip4_165(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_165'

class Ip4_166(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_166'

class Ip4_167(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_167'

class Ip4_168(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_168'

class Ip4_169(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_169'

class Ip4_17(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_17'

class Ip4_170(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_170'

class Ip4_171(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_171'

class Ip4_172(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_172'

class Ip4_173(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_173'

class Ip4_174(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_174'

class Ip4_175(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_175'

class Ip4_176(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_176'

class Ip4_177(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_177'

class Ip4_178(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_178'

class Ip4_179(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_179'

class Ip4_18(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_18'

class Ip4_180(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_180'

class Ip4_181(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_181'

class Ip4_182(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_182'

class Ip4_183(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_183'

class Ip4_184(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_184'

class Ip4_185(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_185'

class Ip4_186(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_186'

class Ip4_187(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_187'

class Ip4_188(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_188'

class Ip4_189(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_189'

class Ip4_19(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_19'

class Ip4_190(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_190'

class Ip4_191(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_191'

class Ip4_192(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_192'

class Ip4_193(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_193'

class Ip4_194(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_194'

class Ip4_195(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_195'

class Ip4_196(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_196'

class Ip4_197(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_197'

class Ip4_198(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_198'

class Ip4_199(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_199'

class Ip4_2(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_2'

class Ip4_20(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_20'

class Ip4_200(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_200'

class Ip4_201(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_201'

class Ip4_202(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_202'

class Ip4_203(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_203'

class Ip4_204(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_204'

class Ip4_205(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_205'

class Ip4_206(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_206'

class Ip4_207(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_207'

class Ip4_208(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_208'

class Ip4_209(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_209'

class Ip4_21(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_21'

class Ip4_210(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_210'

class Ip4_211(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_211'

class Ip4_212(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_212'

class Ip4_213(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_213'

class Ip4_214(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_214'

class Ip4_215(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_215'

class Ip4_216(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_216'

class Ip4_217(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_217'

class Ip4_218(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_218'

class Ip4_219(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_219'

class Ip4_22(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_22'

class Ip4_220(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_220'

class Ip4_221(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_221'

class Ip4_222(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_222'

class Ip4_223(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_223'

class Ip4_224(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_224'

class Ip4_225(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_225'

class Ip4_226(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_226'

class Ip4_227(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_227'

class Ip4_228(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_228'

class Ip4_229(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_229'

class Ip4_23(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_23'

class Ip4_230(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_230'

class Ip4_231(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_231'

class Ip4_232(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_232'

class Ip4_233(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_233'

class Ip4_234(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_234'

class Ip4_235(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_235'

class Ip4_236(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_236'

class Ip4_237(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_237'

class Ip4_238(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_238'

class Ip4_239(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_239'

class Ip4_24(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_24'

class Ip4_240(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_240'

class Ip4_241(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_241'

class Ip4_242(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_242'

class Ip4_243(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_243'

class Ip4_244(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_244'

class Ip4_245(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_245'

class Ip4_246(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_246'

class Ip4_247(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_247'

class Ip4_248(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_248'

class Ip4_249(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_249'

class Ip4_25(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_25'

class Ip4_250(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_250'

class Ip4_251(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_251'

class Ip4_252(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_252'

class Ip4_253(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_253'

class Ip4_254(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_254'

class Ip4_255(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_255'

class Ip4_26(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_26'

class Ip4_27(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_27'

class Ip4_28(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_28'

class Ip4_29(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_29'

class Ip4_3(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_3'

class Ip4_30(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_30'

class Ip4_31(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_31'

class Ip4_32(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_32'

class Ip4_33(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_33'

class Ip4_34(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_34'

class Ip4_35(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_35'

class Ip4_36(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_36'

class Ip4_37(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_37'

class Ip4_38(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_38'

class Ip4_39(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_39'

class Ip4_4(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_4'

class Ip4_40(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_40'

class Ip4_41(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_41'

class Ip4_42(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_42'

class Ip4_43(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_43'

class Ip4_44(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_44'

class Ip4_45(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_45'

class Ip4_46(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_46'

class Ip4_47(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_47'

class Ip4_48(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_48'

class Ip4_49(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_49'

class Ip4_5(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_5'

class Ip4_50(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_50'

class Ip4_51(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_51'

class Ip4_52(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_52'

class Ip4_53(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_53'

class Ip4_54(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_54'

class Ip4_55(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_55'

class Ip4_56(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_56'

class Ip4_57(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_57'

class Ip4_58(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_58'

class Ip4_59(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_59'

class Ip4_6(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_6'

class Ip4_60(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_60'

class Ip4_61(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_61'

class Ip4_62(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_62'

class Ip4_63(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_63'

class Ip4_64(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_64'

class Ip4_65(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_65'

class Ip4_66(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_66'

class Ip4_67(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_67'

class Ip4_68(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_68'

class Ip4_69(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_69'

class Ip4_7(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_7'

class Ip4_70(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_70'

class Ip4_71(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_71'

class Ip4_72(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_72'

class Ip4_73(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_73'

class Ip4_74(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_74'

class Ip4_75(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_75'

class Ip4_76(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_76'

class Ip4_77(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_77'

class Ip4_78(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_78'

class Ip4_79(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_79'

class Ip4_8(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_8'

class Ip4_80(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_80'

class Ip4_81(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_81'

class Ip4_82(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_82'

class Ip4_83(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_83'

class Ip4_84(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_84'

class Ip4_85(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_85'

class Ip4_86(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_86'

class Ip4_87(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_87'

class Ip4_88(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_88'

class Ip4_89(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_89'

class Ip4_9(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_9'

class Ip4_90(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_90'

class Ip4_91(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_91'

class Ip4_92(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_92'

class Ip4_93(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_93'

class Ip4_94(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_94'

class Ip4_95(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_95'

class Ip4_96(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_96'

class Ip4_97(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_97'

class Ip4_98(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_98'

class Ip4_99(models.Model):
    b = models.IntegerField(primary_key=True)
    c = models.IntegerField()
    country = models.IntegerField()
    city = models.IntegerField()
    cron = models.DateTimeField()
    class Meta:
        db_table = u'ip4_99'

