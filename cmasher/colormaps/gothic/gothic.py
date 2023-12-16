# %% IMPORTS
# Package imports
from matplotlib.cm import register_cmap
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
    [0.00022649, 0.00022910, 0.00031182],
    [0.00077840, 0.00079290, 0.00113382],
    [0.00159984, 0.00163930, 0.00245269],
    [0.00266528, 0.00274461, 0.00428120],
    [0.00395849, 0.00409339, 0.00663880],
    [0.00546798, 0.00567421, 0.00954830],
    [0.00718515, 0.00747791, 0.01303467],
    [0.00910336, 0.00949680, 0.01712462],
    [0.01121743, 0.01172416, 0.02184643],
    [0.01352313, 0.01415380, 0.02723157],
    [0.01601749, 0.01678021, 0.03330968],
    [0.01869814, 0.01959811, 0.04011305],
    [0.02156343, 0.02260244, 0.04721513],
    [0.02461231, 0.02578830, 0.05432991],
    [0.02784400, 0.02915056, 0.06147219],
    [0.03125867, 0.03268450, 0.06864621],
    [0.03485696, 0.03638535, 0.07585626],
    [0.03863990, 0.04024821, 0.08310696],
    [0.04254022, 0.04410497, 0.09040632],
    [0.04639767, 0.04789374, 0.09775640],
    [0.05022354, 0.05162006, 0.10515897],
    [0.05402191, 0.05528547, 0.11261940],
    [0.05779662, 0.05889104, 0.12014343],
    [0.06155178, 0.06243863, 0.12772925],
    [0.06529081, 0.06592868, 0.13538279],
    [0.06901713, 0.06936153, 0.14310832],
    [0.07273433, 0.07273846, 0.15090327],
    [0.07644541, 0.07605830, 0.15877799],
    [0.08015380, 0.07932217, 0.16672834],
    [0.08386255, 0.08252920, 0.17476031],
    [0.08757482, 0.08567907, 0.18287581],
    [0.09129370, 0.08877136, 0.19107609],
    [0.09502232, 0.09180485, 0.19936574],
    [0.09876374, 0.09477899, 0.20774495],
    [0.10252109, 0.09769241, 0.21621704],
    [0.10629756, 0.10054351, 0.22478540],
    [0.11009612, 0.10333189, 0.23344741],
    [0.11392040, 0.10605364, 0.24221459],
    [0.11777319, 0.10870908, 0.25107973],
    [0.12165794, 0.11129534, 0.26004821],
    [0.12557835, 0.11380905, 0.26912617],
    [0.12953738, 0.11624924, 0.27830963],
    [0.13353853, 0.11861304, 0.28760113],
    [0.13758582, 0.12089616, 0.29700716],
    [0.14168277, 0.12309581, 0.30652782],
    [0.14583290, 0.12520905, 0.31616285],
    [0.15004006, 0.12723199, 0.32591433],
    [0.15430818, 0.12916040, 0.33578414],
    [0.15864133, 0.13098977, 0.34577396],
    [0.16304362, 0.13271526, 0.35588521],
    [0.16751926, 0.13433168, 0.36611899],
    [0.17207255, 0.13583352, 0.37647604],
    [0.17670781, 0.13721490, 0.38695670],
    [0.18142943, 0.13846959, 0.39756080],
    [0.18624181, 0.13959098, 0.40828762],
    [0.19114950, 0.14057178, 0.41913654],
    [0.19615879, 0.14140103, 0.43011315],
    [0.20127248, 0.14207389, 0.44120766],
    [0.20649533, 0.14258118, 0.45241820],
    [0.21183438, 0.14290899, 0.46374998],
    [0.21729120, 0.14305271, 0.47518766],
    [0.22287411, 0.14299452, 0.48673874],
    [0.22858492, 0.14272762, 0.49838769],
    [0.23442846, 0.14223868, 0.51012852],
    [0.24041153, 0.14150950, 0.52195977],
    [0.24653595, 0.14052980, 0.53386424],
    [0.25280563, 0.13928398, 0.54583022],
    [0.25922382, 0.13775610, 0.55784319],
    [0.26579287, 0.13593012, 0.56988544],
    [0.27251407, 0.13379018, 0.58193583],
    [0.27939017, 0.13131543, 0.59397558],
    [0.28641815, 0.12849429, 0.60597212],
    [0.29359608, 0.12531100, 0.61789520],
    [0.30092102, 0.12174958, 0.62971203],
    [0.30838669, 0.11779912, 0.64138310],
    [0.31598416, 0.11345296, 0.65286466],
    [0.32370335, 0.10870592, 0.66411204],
    [0.33153133, 0.10355911, 0.67507732],
    [0.33945245, 0.09802110, 0.68571083],
    [0.34744873, 0.09210897, 0.69596281],
    [0.35550034, 0.08584927, 0.70578548],
    [0.36358689, 0.07927728, 0.71513562],
    [0.37168725, 0.07244065, 0.72397518],
    [0.37977968, 0.06540337, 0.73227241],
    [0.38784538, 0.05823842, 0.74000589],
    [0.39586560, 0.05104328, 0.74716157],
    [0.40382546, 0.04393252, 0.75373581],
    [0.41171205, 0.03707994, 0.75973304],
    [0.41951581, 0.03113051, 0.76516566],
    [0.42722995, 0.02627780, 0.77005240],
    [0.43485041, 0.02254326, 0.77441703],
    [0.44237532, 0.01993019, 0.77828689],
    [0.44980504, 0.01842521, 0.78169165],
    [0.45714116, 0.01800397, 0.78466211],
    [0.46438685, 0.01863137, 0.78722931],
    [0.47154595, 0.02026647, 0.78942384],
    [0.47862279, 0.02286426, 0.79127531],
    [0.48562248, 0.02637598, 0.79281178],
    [0.49254975, 0.03075392, 0.79405996],
    [0.49940978, 0.03594920, 0.79504459],
    [0.50620760, 0.04187490, 0.79578858],
    [0.51294795, 0.04804067, 0.79631318],
    [0.51963531, 0.05428576, 0.79663794],
    [0.52627418, 0.06055136, 0.79678042],
    [0.53286860, 0.06679720, 0.79675676],
    [0.53942235, 0.07299590, 0.79658160],
    [0.54593888, 0.07912923, 0.79626820],
    [0.55242141, 0.08518541, 0.79582845],
    [0.55887290, 0.09115729, 0.79527303],
    [0.56529598, 0.09704113, 0.79461154],
    [0.57169303, 0.10283559, 0.79385256],
    [0.57806618, 0.10854111, 0.79300376],
    [0.58441731, 0.11415935, 0.79207188],
    [0.59074810, 0.11969293, 0.79106288],
    [0.59705991, 0.12514519, 0.78998205],
    [0.60335393, 0.13051994, 0.78883403],
    [0.60963110, 0.13582141, 0.78762282],
    [0.61589221, 0.14105404, 0.78635175],
    [0.62213784, 0.14622255, 0.78502354],
    [0.62836819, 0.15133188, 0.78364088],
    [0.63458330, 0.15638712, 0.78220579],
    [0.64078327, 0.16139341, 0.78071920],
    [0.64696749, 0.16635619, 0.77918275],
    [0.65313532, 0.17128101, 0.77759719],
    [0.65928609, 0.17617352, 0.77596229],
    [0.66541828, 0.18103975, 0.77427894],
    [0.67153070, 0.18588580, 0.77254589],
    [0.67762128, 0.19071819, 0.77076311],
    [0.68368769, 0.19554374, 0.76892983],
    [0.68972752, 0.20036966, 0.76704387],
    [0.69573739, 0.20520370, 0.76510410],
    [0.70171345, 0.21005419, 0.76310873],
    [0.70765122, 0.21493014, 0.76105549],
    [0.71354536, 0.21984144, 0.75894196],
    [0.71938982, 0.22479904, 0.75676434],
    [0.72517692, 0.22981504, 0.75452029],
    [0.73089783, 0.23490311, 0.75220632],
    [0.73654188, 0.24007866, 0.74981898],
    [0.74209653, 0.24535951, 0.74735337],
    [0.74754621, 0.25076605, 0.74480608],
    [0.75287203, 0.25632210, 0.74217347],
    [0.75805069, 0.26205525, 0.73945391],
    [0.76305360, 0.26799846, 0.73664524],
    [0.76784504, 0.27419030, 0.73374933],
    [0.77238053, 0.28067532, 0.73077521],
    [0.77660515, 0.28750518, 0.72773900],
    [0.78045259, 0.29473488, 0.72467579],
    [0.78384670, 0.30241794, 0.72164512],
    [0.78670902, 0.31059259, 0.71874385],
    [0.78897660, 0.31925931, 0.71611399],
    [0.79062680, 0.32836053, 0.71392763],
    [0.79169757, 0.33777583, 0.71234976],
    [0.79228253, 0.34735000, 0.71148822],
    [0.79250047, 0.35693781, 0.71136831],
    [0.79246219, 0.36643432, 0.71194630],
    [0.79225552, 0.37577702, 0.71314290],
    [0.79194128, 0.38493841, 0.71486841],
    [0.79156129, 0.39391031, 0.71703954],
    [0.79114212, 0.40269700, 0.71958365],
    [0.79070192, 0.41130730, 0.72244042],
    [0.79025225, 0.41975284, 0.72556003],
    [0.78980010, 0.42804628, 0.72890161],
    [0.78935136, 0.43619867, 0.73243180],
    [0.78890961, 0.44422092, 0.73612296],
    [0.78847776, 0.45212273, 0.73995217],
    [0.78805691, 0.45991379, 0.74390018],
    [0.78764865, 0.46760210, 0.74795084],
    [0.78725425, 0.47519495, 0.75209048],
    [0.78687527, 0.48269849, 0.75630739],
    [0.78651193, 0.49011920, 0.76059152],
    [0.78616514, 0.49746237, 0.76493422],
    [0.78583563, 0.50473290, 0.76932797],
    [0.78552435, 0.51193508, 0.77376622],
    [0.78523222, 0.51907284, 0.77824323],
    [0.78495930, 0.52615032, 0.78275401],
    [0.78470661, 0.53317070, 0.78729412],
    [0.78447501, 0.54013703, 0.79185964],
    [0.78426477, 0.54705248, 0.79644711],
    [0.78407686, 0.55391957, 0.80105343],
    [0.78391180, 0.56074090, 0.80567585],
    [0.78376990, 0.56751904, 0.81031190],
    [0.78365226, 0.57425593, 0.81495931],
    [0.78355900, 0.58095395, 0.81961605],
    [0.78349056, 0.58761517, 0.82428023],
    [0.78344742, 0.59424151, 0.82895010],
    [0.78343013, 0.60083478, 0.83362397],
    [0.78343875, 0.60739694, 0.83830025],
    [0.78347352, 0.61392977, 0.84297736],
    [0.78353464, 0.62043503, 0.84765369],
    [0.78362220, 0.62691443, 0.85232762],
    [0.78373623, 0.63336968, 0.85699741],
    [0.78387665, 0.63980249, 0.86166123],
    [0.78404339, 0.64621454, 0.86631706],
    [0.78423630, 0.65260749, 0.87096269],
    [0.78445522, 0.65898300, 0.87559564],
    [0.78469987, 0.66534278, 0.88021310],
    [0.78496997, 0.67168853, 0.88481190],
    [0.78526547, 0.67802185, 0.88938842],
    [0.78558632, 0.68434435, 0.89393852],
    [0.78593226, 0.69065780, 0.89845746],
    [0.78630345, 0.69696380, 0.90293981],
    [0.78670062, 0.70326377, 0.90737936],
    [0.78712384, 0.70955954, 0.91176894],
    [0.78757479, 0.71585226, 0.91610042],
    [0.78805464, 0.72214351, 0.92036445],
    [0.78856633, 0.72843421, 0.92455044],
    [0.78911225, 0.73472575, 0.92864619],
    [0.78969759, 0.74101847, 0.93263811],
    [0.79032808, 0.74731276, 0.93651077],
    [0.79101128, 0.75360852, 0.94024693],
    [0.79175692, 0.75990501, 0.94382751],
    [0.79257770, 0.76620057, 0.94723181],
    [0.79348922, 0.77249259, 0.95043776],
    [0.79451090, 0.77877713, 0.95342266],
    [0.79566591, 0.78504882, 0.95616426],
    [0.79698112, 0.79130071, 0.95864218],
    [0.79848627, 0.79752446, 0.96083977],
    [0.80021362, 0.80371000, 0.96274721],
    [0.80219478, 0.80984665, 0.96436298],
    [0.80445852, 0.81592365, 0.96569591],
    [0.80702759, 0.82193135, 0.96676508],
    [0.80991695, 0.82786181, 0.96759987],
    [0.81313163, 0.83371013, 0.96823544],
    [0.81666752, 0.83947432, 0.96871053],
    [0.82051272, 0.84515522, 0.96906397],
    [0.82464985, 0.85075562, 0.96933430],
    [0.82905719, 0.85628094, 0.96955070],
    [0.83371225, 0.86173646, 0.96974494],
    [0.83859186, 0.86712891, 0.96993795],
    [0.84367394, 0.87246480, 0.97014857],
    [0.84893783, 0.87775040, 0.97039275],
    [0.85436441, 0.88299168, 0.97068376],
    [0.85993707, 0.88819452, 0.97102728],
    [0.86563985, 0.89336380, 0.97143559],
    [0.87145948, 0.89850444, 0.97191191],
    [0.87738390, 0.90362072, 0.97246084],
    [0.88340230, 0.90871656, 0.97308653],
    [0.88950517, 0.91379548, 0.97379189],
    [0.89568421, 0.91886073, 0.97457879],
    [0.90193159, 0.92391520, 0.97545036],
    [0.90824013, 0.92896161, 0.97640976],
    [0.91460519, 0.93400236, 0.97745383],
    [0.92101920, 0.93903977, 0.97859073],
    [0.92747939, 0.94407584, 0.97981503],
    [0.93397877, 0.94911266, 0.98113520],
    [0.94051433, 0.95415199, 0.98254880],
    [0.94708174, 0.95919565, 0.98405798],
    [0.95367627, 0.96424545, 0.98566600],
    [0.96029209, 0.96930345, 0.98737864],
    [0.96692477, 0.97437166, 0.98919662],
    [0.97356753, 0.97945267, 0.99112429],
    [0.98021157, 0.98454986, 0.99316620],
    [0.98684468, 0.98966802, 0.99532645],
    [0.99344927, 0.99481436, 0.99760652],
    [1.00000000, 1.00000000, 1.00000000],
]

# Create ListedColormap object for this colormap
cmap = ListedColormap(cm_data, name="cmr.gothic", N=256)
cmap_r = cmap.reversed()

# Register (reversed) cmap in MPL
register_cmap(cmap=cmap)
register_cmap(cmap=cmap_r)
