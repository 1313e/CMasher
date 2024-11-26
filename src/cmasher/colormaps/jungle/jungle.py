import matplotlib as mpl
from matplotlib.colors import ListedColormap

# All declaration
__all__ = ["cmap"]

# Author declaration
__author__ = "Ellert van der Velden (@1313e)"

# Package declaration
__package__ = "cmasher"


# %% GLOBALS AND DEFINITIONS
# Type of this colormap
cm_type = "sequential"

# RGB-values of this colormap
cm_data = [
    [0.00000000, 0.00000000, 0.00000000],
    [0.00019351, 0.00025002, 0.00023457],
    [0.00064578, 0.00087808, 0.00081247],
    [0.00129011, 0.00184048, 0.00167903],
    [0.00209146, 0.00312128, 0.00280698],
    [0.00302526, 0.00471220, 0.00417683],
    [0.00407250, 0.00660860, 0.00577279],
    [0.00521756, 0.00880791, 0.00758133],
    [0.00644725, 0.01130885, 0.00959034],
    [0.00775008, 0.01411104, 0.01178878],
    [0.00911602, 0.01721468, 0.01416645],
    [0.01053590, 0.02062051, 0.01671372],
    [0.01200155, 0.02432961, 0.01942153],
    [0.01350548, 0.02834332, 0.02228126],
    [0.01504084, 0.03266319, 0.02528466],
    [0.01660128, 0.03729098, 0.02842381],
    [0.01818080, 0.04217682, 0.03169105],
    [0.01977392, 0.04703885, 0.03507902],
    [0.02137544, 0.05186049, 0.03858057],
    [0.02298043, 0.05664540, 0.04213855],
    [0.02458426, 0.06139682, 0.04560869],
    [0.02618252, 0.06611759, 0.04900021],
    [0.02777102, 0.07081024, 0.05231600],
    [0.02934608, 0.07547694, 0.05555875],
    [0.03090372, 0.08011979, 0.05873072],
    [0.03244028, 0.08474063, 0.06183400],
    [0.03395262, 0.08934103, 0.06487059],
    [0.03543729, 0.09392255, 0.06784217],
    [0.03689110, 0.09848657, 0.07075027],
    [0.03831142, 0.10303427, 0.07359646],
    [0.03969492, 0.10756690, 0.07638186],
    [0.04102707, 0.11208540, 0.07910787],
    [0.04228527, 0.11659088, 0.08177537],
    [0.04347964, 0.12108410, 0.08438555],
    [0.04461057, 0.12556603, 0.08693913],
    [0.04567943, 0.13003734, 0.08943713],
    [0.04668649, 0.13449882, 0.09188013],
    [0.04763275, 0.13895110, 0.09426894],
    [0.04851864, 0.14339483, 0.09660413],
    [0.04934466, 0.14783061, 0.09888626],
    [0.05011151, 0.15225894, 0.10111592],
    [0.05081931, 0.15668039, 0.10329347],
    [0.05146861, 0.16109540, 0.10541940],
    [0.05205968, 0.16550443, 0.10749406],
    [0.05259268, 0.16990792, 0.10951774],
    [0.05306799, 0.17430625, 0.11149079],
    [0.05348569, 0.17869981, 0.11341343],
    [0.05384589, 0.18308895, 0.11528585],
    [0.05414879, 0.18747399, 0.11710826],
    [0.05439441, 0.19185525, 0.11888080],
    [0.05458275, 0.19623303, 0.12060355],
    [0.05471388, 0.20060760, 0.12227661],
    [0.05478778, 0.20497922, 0.12390003],
    [0.05480437, 0.20934813, 0.12547382],
    [0.05476361, 0.21371457, 0.12699796],
    [0.05466543, 0.21807874, 0.12847242],
    [0.05450971, 0.22244086, 0.12989712],
    [0.05429637, 0.22680111, 0.13127197],
    [0.05402523, 0.23115967, 0.13259683],
    [0.05369619, 0.23551671, 0.13387156],
    [0.05330916, 0.23987237, 0.13509598],
    [0.05286390, 0.24422680, 0.13626985],
    [0.05236034, 0.24858015, 0.13739294],
    [0.05179842, 0.25293251, 0.13846504],
    [0.05117791, 0.25728402, 0.13948577],
    [0.05049876, 0.26163478, 0.14045483],
    [0.04976107, 0.26598485, 0.14137192],
    [0.04896461, 0.27033436, 0.14223658],
    [0.04810950, 0.27468336, 0.14304840],
    [0.04719609, 0.27903189, 0.14380704],
    [0.04622411, 0.28338007, 0.14451183],
    [0.04519423, 0.28772789, 0.14516241],
    [0.04410692, 0.29207539, 0.14575822],
    [0.04296228, 0.29642265, 0.14629850],
    [0.04176178, 0.30076961, 0.14678291],
    [0.04050562, 0.30511636, 0.14721047],
    [0.03918604, 0.30946283, 0.14758072],
    [0.03783947, 0.31380906, 0.14789277],
    [0.03647195, 0.31815501, 0.14814588],
    [0.03508872, 0.32250065, 0.14833920],
    [0.03369530, 0.32684595, 0.14847179],
    [0.03229772, 0.33119085, 0.14854272],
    [0.03090252, 0.33553528, 0.14855103],
    [0.02951610, 0.33987921, 0.14849548],
    [0.02814671, 0.34422247, 0.14837531],
    [0.02680054, 0.34856510, 0.14818865],
    [0.02548739, 0.35290686, 0.14793485],
    [0.02421570, 0.35724767, 0.14761236],
    [0.02299414, 0.36158745, 0.14721939],
    [0.02183379, 0.36592596, 0.14675485],
    [0.02074529, 0.37026306, 0.14621704],
    [0.01973935, 0.37459859, 0.14560386],
    [0.01882846, 0.37893235, 0.14491356],
    [0.01802601, 0.38326409, 0.14414427],
    [0.01734584, 0.38759356, 0.14329382],
    [0.01680281, 0.39192051, 0.14235987],
    [0.01641278, 0.39624464, 0.14133991],
    [0.01619280, 0.40056564, 0.14023126],
    [0.01616114, 0.40488317, 0.13903105],
    [0.01633746, 0.40919683, 0.13773620],
    [0.01674292, 0.41350621, 0.13634340],
    [0.01740029, 0.41781085, 0.13484911],
    [0.01833377, 0.42211027, 0.13324924],
    [0.01956908, 0.42640397, 0.13153901],
    [0.02113598, 0.43069127, 0.12971465],
    [0.02306455, 0.43497157, 0.12777044],
    [0.02538846, 0.43924413, 0.12570082],
    [0.02814416, 0.44350818, 0.12349954],
    [0.03137207, 0.44776278, 0.12116035],
    [0.03511448, 0.45200705, 0.11867424],
    [0.03942021, 0.45623984, 0.11603370],
    [0.04417431, 0.46045994, 0.11322918],
    [0.04920916, 0.46466600, 0.11024999],
    [0.05452634, 0.46885647, 0.10708429],
    [0.06012048, 0.47302966, 0.10371765],
    [0.06598976, 0.47718356, 0.10013507],
    [0.07213525, 0.48131592, 0.09631908],
    [0.07856109, 0.48542415, 0.09224944],
    [0.08527478, 0.48950525, 0.08790164],
    [0.09228739, 0.49355574, 0.08324793],
    [0.09961357, 0.49757150, 0.07825696],
    [0.10727180, 0.50154769, 0.07289181],
    [0.11528536, 0.50547856, 0.06710751],
    [0.12368232, 0.50935726, 0.06085183],
    [0.13249467, 0.51317558, 0.05406770],
    [0.14176036, 0.51692368, 0.04668662],
    [0.15151935, 0.52058996, 0.03863418],
    [0.16180957, 0.52416114, 0.03051659],
    [0.17265967, 0.52762277, 0.02295740],
    [0.18407026, 0.53096123, 0.01626664],
    [0.19599015, 0.53416743, 0.01084213],
    [0.20829227, 0.53724214, 0.00713645],
    [0.22076858, 0.54020073, 0.00557218],
    [0.23317267, 0.54307185, 0.00642422],
    [0.24528567, 0.54588989, 0.00975878],
    [0.25696534, 0.54868562, 0.01546593],
    [0.26814980, 0.55148151, 0.02334610],
    [0.27883484, 0.55429160, 0.03318458],
    [0.28904864, 0.55712354, 0.04459206],
    [0.29883247, 0.55998098, 0.05592558],
    [0.30823066, 0.56286517, 0.06688566],
    [0.31728554, 0.56577606, 0.07749587],
    [0.32603579, 0.56871282, 0.08779020],
    [0.33451451, 0.57167456, 0.09780296],
    [0.34275190, 0.57465993, 0.10756800],
    [0.35077332, 0.57766779, 0.11711491],
    [0.35860130, 0.58069691, 0.12647055],
    [0.36625377, 0.58374655, 0.13565630],
    [0.37374878, 0.58681542, 0.14469392],
    [0.38110064, 0.58990272, 0.15360051],
    [0.38832205, 0.59300768, 0.16239113],
    [0.39542449, 0.59612955, 0.17107933],
    [0.40241818, 0.59926762, 0.17967713],
    [0.40931090, 0.60242165, 0.18819305],
    [0.41611218, 0.60559066, 0.19663855],
    [0.42282774, 0.60877460, 0.20501947],
    [0.42946472, 0.61197286, 0.21334399],
    [0.43602884, 0.61518507, 0.22161838],
    [0.44252520, 0.61841096, 0.22984800],
    [0.44895849, 0.62165026, 0.23803775],
    [0.45533301, 0.62490272, 0.24619211],
    [0.46165277, 0.62816812, 0.25431517],
    [0.46792146, 0.63144622, 0.26241069],
    [0.47414227, 0.63473690, 0.27048171],
    [0.48031786, 0.63804017, 0.27853039],
    [0.48645176, 0.64135563, 0.28656078],
    [0.49254603, 0.64468340, 0.29457417],
    [0.49860334, 0.64802330, 0.30257327],
    [0.50462575, 0.65137531, 0.31055969],
    [0.51061564, 0.65473927, 0.31853581],
    [0.51657435, 0.65811539, 0.32650201],
    [0.52250433, 0.66150339, 0.33446111],
    [0.52840707, 0.66490332, 0.34241405],
    [0.53428376, 0.66831538, 0.35036109],
    [0.54013631, 0.67173936, 0.35830436],
    [0.54596609, 0.67517534, 0.36624475],
    [0.55177436, 0.67862334, 0.37418309],
    [0.55756234, 0.68208342, 0.38212013],
    [0.56333117, 0.68555563, 0.39005659],
    [0.56908196, 0.68904004, 0.39799314],
    [0.57481575, 0.69253672, 0.40593036],
    [0.58053354, 0.69604572, 0.41386885],
    [0.58623626, 0.69956713, 0.42180912],
    [0.59192484, 0.70310102, 0.42975163],
    [0.59760012, 0.70664747, 0.43769684],
    [0.60326294, 0.71020658, 0.44564516],
    [0.60891409, 0.71377843, 0.45359694],
    [0.61455432, 0.71736312, 0.46155254],
    [0.62018436, 0.72096076, 0.46951225],
    [0.62580483, 0.72457147, 0.47747616],
    [0.63141623, 0.72819546, 0.48544403],
    [0.63701943, 0.73183272, 0.49341672],
    [0.64261504, 0.73548338, 0.50139441],
    [0.64820356, 0.73914760, 0.50937699],
    [0.65378541, 0.74282559, 0.51736412],
    [0.65936139, 0.74651735, 0.52535668],
    [0.66493198, 0.75022303, 0.53335462],
    [0.67049743, 0.75394292, 0.54135715],
    [0.67605856, 0.75767699, 0.54936535],
    [0.68161571, 0.76142545, 0.55737876],
    [0.68716928, 0.76518849, 0.56539716],
    [0.69271996, 0.76896613, 0.57342132],
    [0.69826783, 0.77275873, 0.58144997],
    [0.70381368, 0.77656624, 0.58948428],
    [0.70935771, 0.78038896, 0.59752335],
    [0.71490046, 0.78422695, 0.60556759],
    [0.72044228, 0.78808042, 0.61361665],
    [0.72598361, 0.79194952, 0.62167051],
    [0.73152484, 0.79583441, 0.62972903],
    [0.73706637, 0.79973527, 0.63779208],
    [0.74260858, 0.80365225, 0.64585942],
    [0.74815191, 0.80758550, 0.65393108],
    [0.75369667, 0.81153524, 0.66200651],
    [0.75924338, 0.81550155, 0.67008608],
    [0.76479225, 0.81948473, 0.67816873],
    [0.77034390, 0.82348478, 0.68625514],
    [0.77589851, 0.82750204, 0.69434421],
    [0.78145665, 0.83153655, 0.70243622],
    [0.78701868, 0.83558852, 0.71053072],
    [0.79258496, 0.83965816, 0.71862706],
    [0.79815606, 0.84374554, 0.72672542],
    [0.80373228, 0.84785092, 0.73482480],
    [0.80931415, 0.85197441, 0.74292511],
    [0.81490220, 0.85611614, 0.75102602],
    [0.82049676, 0.86027638, 0.75912635],
    [0.82609851, 0.86445517, 0.76722613],
    [0.83170796, 0.86865268, 0.77532465],
    [0.83732559, 0.87286913, 0.78342073],
    [0.84295212, 0.87710457, 0.79151409],
    [0.84858819, 0.88135915, 0.79960379],
    [0.85423440, 0.88563308, 0.80768841],
    [0.85989158, 0.88992638, 0.81576731],
    [0.86556055, 0.89423920, 0.82383920],
    [0.87124208, 0.89857168, 0.83190237],
    [0.87693718, 0.90292388, 0.83995544],
    [0.88264688, 0.90729590, 0.84799664],
    [0.88837223, 0.91168783, 0.85602372],
    [0.89411443, 0.91609980, 0.86403417],
    [0.89987478, 0.92053187, 0.87202535],
    [0.90565464, 0.92498415, 0.87999392],
    [0.91145537, 0.92945683, 0.88793583],
    [0.91727845, 0.93395011, 0.89584668],
    [0.92312525, 0.93846431, 0.90372118],
    [0.92899695, 0.94299992, 0.91155311],
    [0.93489431, 0.94755771, 0.91933510],
    [0.94081746, 0.95213881, 0.92705910],
    [0.94676531, 0.95674488, 0.93471601],
    [0.95273499, 0.96137840, 0.94229623],
    [0.95872102, 0.96604282, 0.94979047],
    [0.96471459, 0.97074271, 0.95719144],
    [0.97070299, 0.97548379, 0.96449578],
    [0.97666993, 0.98027252, 0.97170685],
    [0.98259721, 0.98511519, 0.97883706],
    [0.98846790, 0.99001659, 0.98590874],
    [0.99427015, 0.99497869, 0.99295196],
    [1.00000000, 1.00000000, 1.00000000],
]

# Create ListedColormap object for this colormap
assert len(cm_data) == 256
cmap = ListedColormap(cm_data, name="cmr.jungle")
cmap_r = cmap.reversed()

# Register (reversed) cmap in MPL
mpl.colormaps.register(cmap=cmap)
mpl.colormaps.register(cmap=cmap_r)
