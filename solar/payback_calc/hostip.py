import MySQLdb
import urllib
import string
import models
from urllib import unquote, quote

ip_dict = {
    0:models.Ip4_0,
    1:models.Ip4_1,
    2:models.Ip4_2,
    3:models.Ip4_3,
    4:models.Ip4_4,
    5:models.Ip4_5,
    6:models.Ip4_6,
    7:models.Ip4_7,
    8:models.Ip4_8,
    9:models.Ip4_9,
    10:models.Ip4_10,
    11:models.Ip4_11,
    12:models.Ip4_12,
    13:models.Ip4_13,
    14:models.Ip4_14,
    15:models.Ip4_15,
    16:models.Ip4_16,
    17:models.Ip4_17,
    18:models.Ip4_18,
    19:models.Ip4_19,
    20:models.Ip4_20,
    21:models.Ip4_21,
    22:models.Ip4_22,
    23:models.Ip4_23,
    24:models.Ip4_24,
    25:models.Ip4_25,
    26:models.Ip4_26,
    27:models.Ip4_27,
    28:models.Ip4_28,
    29:models.Ip4_29,
    30:models.Ip4_30,
    31:models.Ip4_31,
    32:models.Ip4_32,
    33:models.Ip4_33,
    34:models.Ip4_34,
    35:models.Ip4_35,
    36:models.Ip4_36,
    37:models.Ip4_37,
    38:models.Ip4_38,
    39:models.Ip4_39,
    40:models.Ip4_40,
    41:models.Ip4_41,
    42:models.Ip4_42,
    43:models.Ip4_43,
    44:models.Ip4_44,
    45:models.Ip4_45,
    46:models.Ip4_46,
    47:models.Ip4_47,
    48:models.Ip4_48,
    49:models.Ip4_49,
    50:models.Ip4_50,
    51:models.Ip4_51,
    52:models.Ip4_52,
    53:models.Ip4_53,
    54:models.Ip4_54,
    55:models.Ip4_55,
    56:models.Ip4_56,
    57:models.Ip4_57,
    58:models.Ip4_58,
    59:models.Ip4_59,
    60:models.Ip4_60,
    61:models.Ip4_61,
    62:models.Ip4_62,
    63:models.Ip4_63,
    64:models.Ip4_64,
    65:models.Ip4_65,
    66:models.Ip4_66,
    67:models.Ip4_67,
    68:models.Ip4_68,
    69:models.Ip4_69,
    70:models.Ip4_70,
    71:models.Ip4_71,
    72:models.Ip4_72,
    73:models.Ip4_73,
    74:models.Ip4_74,
    75:models.Ip4_75,
    76:models.Ip4_76,
    77:models.Ip4_77,
    78:models.Ip4_78,
    79:models.Ip4_79,
    80:models.Ip4_80,
    81:models.Ip4_81,
    82:models.Ip4_82,
    83:models.Ip4_83,
    84:models.Ip4_84,
    85:models.Ip4_85,
    86:models.Ip4_86,
    87:models.Ip4_87,
    88:models.Ip4_88,
    89:models.Ip4_89,
    90:models.Ip4_90,
    91:models.Ip4_91,
    92:models.Ip4_92,
    93:models.Ip4_93,
    94:models.Ip4_94,
    95:models.Ip4_95,
    96:models.Ip4_96,
    97:models.Ip4_97,
    98:models.Ip4_98,
    99:models.Ip4_99,
    100:models.Ip4_100,
    101:models.Ip4_101,
    102:models.Ip4_102,
    103:models.Ip4_103,
    104:models.Ip4_104,
    105:models.Ip4_105,
    106:models.Ip4_106,
    107:models.Ip4_107,
    108:models.Ip4_108,
    109:models.Ip4_109,
    110:models.Ip4_110,
    111:models.Ip4_111,
    112:models.Ip4_112,
    113:models.Ip4_113,
    114:models.Ip4_114,
    115:models.Ip4_115,
    116:models.Ip4_116,
    117:models.Ip4_117,
    118:models.Ip4_118,
    119:models.Ip4_119,
    120:models.Ip4_120,
    121:models.Ip4_121,
    122:models.Ip4_122,
    123:models.Ip4_123,
    124:models.Ip4_124,
    125:models.Ip4_125,
    126:models.Ip4_126,
    127:models.Ip4_127,
    128:models.Ip4_128,
    129:models.Ip4_129,
    130:models.Ip4_130,
    131:models.Ip4_131,
    132:models.Ip4_132,
    133:models.Ip4_133,
    134:models.Ip4_134,
    135:models.Ip4_135,
    136:models.Ip4_136,
    137:models.Ip4_137,
    138:models.Ip4_138,
    139:models.Ip4_139,
    140:models.Ip4_140,
    141:models.Ip4_141,
    142:models.Ip4_142,
    143:models.Ip4_143,
    144:models.Ip4_144,
    145:models.Ip4_145,
    146:models.Ip4_146,
    147:models.Ip4_147,
    148:models.Ip4_148,
    149:models.Ip4_149,
    150:models.Ip4_150,
    151:models.Ip4_151,
    152:models.Ip4_152,
    153:models.Ip4_153,
    154:models.Ip4_154,
    155:models.Ip4_155,
    156:models.Ip4_156,
    157:models.Ip4_157,
    158:models.Ip4_158,
    159:models.Ip4_159,
    160:models.Ip4_160,
    161:models.Ip4_161,
    162:models.Ip4_162,
    163:models.Ip4_163,
    164:models.Ip4_164,
    165:models.Ip4_165,
    166:models.Ip4_166,
    167:models.Ip4_167,
    168:models.Ip4_168,
    169:models.Ip4_169,
    170:models.Ip4_170,
    171:models.Ip4_171,
    172:models.Ip4_172,
    173:models.Ip4_173,
    174:models.Ip4_174,
    175:models.Ip4_175,
    176:models.Ip4_176,
    177:models.Ip4_177,
    178:models.Ip4_178,
    179:models.Ip4_179,
    180:models.Ip4_180,
    181:models.Ip4_181,
    182:models.Ip4_182,
    183:models.Ip4_183,
    184:models.Ip4_184,
    185:models.Ip4_185,
    186:models.Ip4_186,
    187:models.Ip4_187,
    188:models.Ip4_188,
    189:models.Ip4_189,
    190:models.Ip4_190,
    191:models.Ip4_191,
    192:models.Ip4_192,
    193:models.Ip4_193,
    194:models.Ip4_194,
    195:models.Ip4_195,
    196:models.Ip4_196,
    197:models.Ip4_197,
    198:models.Ip4_198,
    199:models.Ip4_199,
    200:models.Ip4_200,
    201:models.Ip4_201,
    202:models.Ip4_202,
    203:models.Ip4_203,
    204:models.Ip4_204,
    205:models.Ip4_205,
    206:models.Ip4_206,
    207:models.Ip4_207,
    208:models.Ip4_208,
    209:models.Ip4_209,
    210:models.Ip4_210,
    211:models.Ip4_211,
    212:models.Ip4_212,
    213:models.Ip4_213,
    214:models.Ip4_214,
    215:models.Ip4_215,
    216:models.Ip4_216,
    217:models.Ip4_217,
    218:models.Ip4_218,
    219:models.Ip4_219,
    220:models.Ip4_220,
    221:models.Ip4_221,
    222:models.Ip4_222,
    223:models.Ip4_223,
    224:models.Ip4_224,
    225:models.Ip4_225,
    226:models.Ip4_226,
    227:models.Ip4_227,
    228:models.Ip4_228,
    229:models.Ip4_229,
    230:models.Ip4_230,
    231:models.Ip4_231,
    232:models.Ip4_232,
    233:models.Ip4_233,
    234:models.Ip4_234,
    235:models.Ip4_235,
    236:models.Ip4_236,
    237:models.Ip4_237,
    238:models.Ip4_238,
    239:models.Ip4_239,
    240:models.Ip4_240,
    241:models.Ip4_241,
    242:models.Ip4_242,
    243:models.Ip4_243,
    244:models.Ip4_244,
    245:models.Ip4_245,
    246:models.Ip4_246,
    247:models.Ip4_247,
    248:models.Ip4_248,
    249:models.Ip4_249,
    250:models.Ip4_250,
    251:models.Ip4_251,
    252:models.Ip4_252,
    253:models.Ip4_253,
    254:models.Ip4_254,
    255:models.Ip4_255,
}

def ip_to_location(ip_str):
    """
    ip_to_location: Looks up the location information of an IP address.
    Uses ip database from http://hostip.info and publicly available zip code database pulled from
    http://scripts.ringsworld.com/calculators/zipcode-1.1.0/
    
    @ip_str: IPv4 address in "aaa.bbb.ccc.ddd" form.
    
    Outputs a tuple in (city, state, zip lat, lng) form.
    Return ("", "", None, None, None) if nothing is found.
    """
    a,b,c,d = ip_str.split(".")
    
    ip_records = ip_dict[int(a)].objects.filter(b=b, c=c)

    if ip_records == 0:
        return ("", "", None, None, None)

    city = ip_records[0].city
    country =ip_records[0].country

    location_records = models.Citybycountry.objects.filter( city = city, country = country)

    if location_records == 0:
        return ("", "", None, None, None)

    name = location_records[0].name
    state = location_records[0].state
    lat = location_records[0].lat
    lng = location_records[0].lng

    city = ",".join(urllib.unquote(name).split(',')[:-1])
    state = urllib.unquote(name).split(', ')[-1].strip()
   
    zip_records = models.ZipCode.objects.filter(city = string.upper(city), state_prefix = state)

    if zip_records == 0:
        return ("", "", None, None, None)

    zip_code = zip_records[0].zip_code
        
    return (unquote(city), unquote(state), zip_code, lat, lng)
    
def city_to_latlng(city, state):
    """
    city_to_latlng: Looks up the latitude and longitude of a city.
    
    Outputs a tuple in (lat, lng) form.
    Returns False is no such city is found.
    """
    city_state_records = models.ZipCode.objects.filter(city = string.upper(city), state_prefix = string.upper(state))
    
    if len(city_state_records) == 0:
        return False

    lat = city_state_records[0].lattitude
    lng = city_state_records[0].longitude
    
    return (lat, lng)

    
def zip_to_latlng(zip_code):
    """
    zip_to_latlng: Looks up the latitude and longitude of a zip code.

    Outputs a tuple in (lat, lng) form.
    Returns False is no such zip is found.
    """
    zip_records = models.ZipCode.objects.filter(zip_code = zip_code)
    
    if len(zip_records) == 0:
        return False

    lat = zip_records[0].lattitude
    lng = zip_records[0].longitude
    
    return (lat, lng)

def zip_to_location(zip_code):
    """
    zip_to_latlng: Looks up the latitude, longitude and state of a zip code.

    Outputs a tuple in (city, state, lat, lng) form.
    Returns False is no such zip is found.
    """
    zip_records = models.ZipCode.objects.filter(zip_code = zip_code)

    if len(zip_records) == 0:
        return False

    lat = zip_records[0].lattitude
    lng = zip_records[0].longitude
    city = zip_records[0].city.title()
    state = zip_records[0].state_prefix

    return (city, state, lat, lng)
