# %% IMPORTS
# Package imports
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
    [0.00020697, 0.00019319, 0.00015064],
    [0.00071850, 0.00067188, 0.00050625],
    [0.00148836, 0.00139629, 0.00101895],
    [0.00249411, 0.00235040, 0.00166547],
    [0.00371991, 0.00352518, 0.00243075],
    [0.00515301, 0.00491508, 0.00330407],
    [0.00678244, 0.00651659, 0.00427743],
    [0.00859844, 0.00832749, 0.00534470],
    [0.01059209, 0.01034650, 0.00650110],
    [0.01275517, 0.01257298, 0.00774287],
    [0.01508002, 0.01500676, 0.00906704],
    [0.01755949, 0.01764806, 0.01047122],
    [0.02018686, 0.02049736, 0.01195353],
    [0.02295578, 0.02355537, 0.01351242],
    [0.02586033, 0.02682294, 0.01514673],
    [0.02889486, 0.03030111, 0.01685540],
    [0.03205406, 0.03399100, 0.01863764],
    [0.03533289, 0.03789383, 0.02049279],
    [0.03872659, 0.04196773, 0.02242030],
    [0.04217872, 0.04601566, 0.02441974],
    [0.04555743, 0.05003522, 0.02649069],
    [0.04887329, 0.05402876, 0.02863281],
    [0.05212920, 0.05799834, 0.03084584],
    [0.05532777, 0.06194584, 0.03312947],
    [0.05847142, 0.06587296, 0.03548345],
    [0.06156235, 0.06978122, 0.03790755],
    [0.06460262, 0.07367200, 0.04040157],
    [0.06759412, 0.07754654, 0.04287963],
    [0.07053851, 0.08140606, 0.04533580],
    [0.07343748, 0.08525157, 0.04777207],
    [0.07629244, 0.08908410, 0.05018930],
    [0.07910481, 0.09290454, 0.05258851],
    [0.08187581, 0.09671377, 0.05497037],
    [0.08460672, 0.10051254, 0.05733578],
    [0.08729854, 0.10430163, 0.05968528],
    [0.08995234, 0.10808172, 0.06201951],
    [0.09256912, 0.11185344, 0.06433911],
    [0.09514971, 0.11561744, 0.06664450],
    [0.09769494, 0.11937428, 0.06893616],
    [0.10020561, 0.12312452, 0.07121454],
    [0.10268247, 0.12686865, 0.07348006],
    [0.10512619, 0.13060718, 0.07573309],
    [0.10753739, 0.13434057, 0.07797395],
    [0.10991666, 0.13806926, 0.08020294],
    [0.11226456, 0.14179369, 0.08242036],
    [0.11458160, 0.14551424, 0.08462648],
    [0.11686828, 0.14923132, 0.08682155],
    [0.11912504, 0.15294527, 0.08900579],
    [0.12135232, 0.15665646, 0.09117943],
    [0.12355049, 0.16036523, 0.09334265],
    [0.12571996, 0.16407188, 0.09549567],
    [0.12786107, 0.16777674, 0.09763865],
    [0.12997412, 0.17148010, 0.09977172],
    [0.13205940, 0.17518226, 0.10189504],
    [0.13411718, 0.17888350, 0.10400873],
    [0.13614773, 0.18258409, 0.10611291],
    [0.13815136, 0.18628425, 0.10820778],
    [0.14012821, 0.18998427, 0.11029335],
    [0.14207847, 0.19368438, 0.11236973],
    [0.14400236, 0.19738482, 0.11443703],
    [0.14590010, 0.20108579, 0.11649537],
    [0.14777176, 0.20478755, 0.11854474],
    [0.14961751, 0.20849029, 0.12058525],
    [0.15143754, 0.21219419, 0.12261699],
    [0.15323187, 0.21589950, 0.12463995],
    [0.15500067, 0.21960639, 0.12665422],
    [0.15674402, 0.22331504, 0.12865984],
    [0.15846194, 0.22702567, 0.13065680],
    [0.16015463, 0.23073840, 0.13264522],
    [0.16182200, 0.23445346, 0.13462501],
    [0.16346421, 0.23817098, 0.13659629],
    [0.16508122, 0.24189116, 0.13855900],
    [0.16667310, 0.24561414, 0.14051320],
    [0.16823984, 0.24934008, 0.14245885],
    [0.16978147, 0.25306913, 0.14439598],
    [0.17129797, 0.25680145, 0.14632457],
    [0.17278935, 0.26053718, 0.14824461],
    [0.17425557, 0.26427647, 0.15015608],
    [0.17569663, 0.26801945, 0.15205898],
    [0.17711247, 0.27176627, 0.15395325],
    [0.17850307, 0.27551705, 0.15583890],
    [0.17986834, 0.27927193, 0.15771585],
    [0.18120829, 0.28303103, 0.15958412],
    [0.18252277, 0.28679449, 0.16144360],
    [0.18381180, 0.29056242, 0.16329431],
    [0.18507521, 0.29433495, 0.16513615],
    [0.18631298, 0.29811219, 0.16696909],
    [0.18752499, 0.30189426, 0.16879306],
    [0.18871111, 0.30568128, 0.17060798],
    [0.18987132, 0.30947334, 0.17241382],
    [0.19100541, 0.31327058, 0.17421046],
    [0.19211332, 0.31707308, 0.17599786],
    [0.19319491, 0.32088096, 0.17777593],
    [0.19425003, 0.32469433, 0.17954455],
    [0.19527859, 0.32851326, 0.18130368],
    [0.19628040, 0.33233788, 0.18305319],
    [0.19725533, 0.33616828, 0.18479298],
    [0.19820323, 0.34000455, 0.18652297],
    [0.19912392, 0.34384679, 0.18824301],
    [0.20001726, 0.34769508, 0.18995302],
    [0.20088307, 0.35154952, 0.19165286],
    [0.20172116, 0.35541020, 0.19334241],
    [0.20253138, 0.35927720, 0.19502154],
    [0.20331352, 0.36315061, 0.19669012],
    [0.20406740, 0.36703051, 0.19834800],
    [0.20479282, 0.37091699, 0.19999504],
    [0.20548959, 0.37481011, 0.20163108],
    [0.20615750, 0.37870997, 0.20325598],
    [0.20679635, 0.38261664, 0.20486955],
    [0.20740594, 0.38653018, 0.20647165],
    [0.20798603, 0.39045069, 0.20806208],
    [0.20853642, 0.39437821, 0.20964067],
    [0.20905690, 0.39831284, 0.21120724],
    [0.20954722, 0.40225463, 0.21276157],
    [0.21000720, 0.40620364, 0.21430350],
    [0.21043655, 0.41015996, 0.21583278],
    [0.21083510, 0.41412363, 0.21734923],
    [0.21120261, 0.41809472, 0.21885260],
    [0.21153882, 0.42207329, 0.22034267],
    [0.21184357, 0.42605938, 0.22181924],
    [0.21211652, 0.43005308, 0.22328199],
    [0.21235755, 0.43405441, 0.22473074],
    [0.21256639, 0.43806343, 0.22616519],
    [0.21274279, 0.44208020, 0.22758508],
    [0.21288663, 0.44610475, 0.22899016],
    [0.21299752, 0.45013715, 0.23038007],
    [0.21307544, 0.45417741, 0.23175461],
    [0.21312003, 0.45822559, 0.23311339],
    [0.21313121, 0.46228173, 0.23445615],
    [0.21310872, 0.46634585, 0.23578254],
    [0.21305240, 0.47041800, 0.23709224],
    [0.21296211, 0.47449819, 0.23838490],
    [0.21283762, 0.47858647, 0.23966014],
    [0.21267891, 0.48268283, 0.24091764],
    [0.21248571, 0.48678734, 0.24215696],
    [0.21225808, 0.49089997, 0.24337778],
    [0.21199575, 0.49502077, 0.24457961],
    [0.21169885, 0.49914973, 0.24576212],
    [0.21136719, 0.50328687, 0.24692481],
    [0.21100088, 0.50743218, 0.24806729],
    [0.21059989, 0.51158567, 0.24918907],
    [0.21016426, 0.51574734, 0.25028967],
    [0.20969425, 0.51991715, 0.25136868],
    [0.20918971, 0.52409515, 0.25242546],
    [0.20865122, 0.52828126, 0.25345965],
    [0.20807868, 0.53247549, 0.25447057],
    [0.20747262, 0.53667781, 0.25545777],
    [0.20683348, 0.54088816, 0.25642071],
    [0.20616137, 0.54510656, 0.25735864],
    [0.20545721, 0.54933290, 0.25827113],
    [0.20472152, 0.55356716, 0.25915753],
    [0.20395477, 0.55780930, 0.26001707],
    [0.20315812, 0.56205922, 0.26084926],
    [0.20233248, 0.56631684, 0.26165339],
    [0.20147859, 0.57058214, 0.26242862],
    [0.20059794, 0.57485500, 0.26317436],
    [0.19969193, 0.57913530, 0.26388989],
    [0.19876208, 0.58342294, 0.26457444],
    [0.19780982, 0.58771785, 0.26522710],
    [0.19683725, 0.59201988, 0.26584716],
    [0.19584656, 0.59632889, 0.26643382],
    [0.19484008, 0.60064473, 0.26698623],
    [0.19382040, 0.60496724, 0.26750351],
    [0.19279039, 0.60929627, 0.26798477],
    [0.19175317, 0.61363164, 0.26842906],
    [0.19071216, 0.61797316, 0.26883542],
    [0.18967131, 0.62232060, 0.26920296],
    [0.18863480, 0.62667375, 0.26953070],
    [0.18760720, 0.63103238, 0.26981765],
    [0.18659349, 0.63539622, 0.27006278],
    [0.18559909, 0.63976501, 0.27026507],
    [0.18462988, 0.64413847, 0.27042348],
    [0.18369221, 0.64851629, 0.27053695],
    [0.18279292, 0.65289815, 0.27060442],
    [0.18193923, 0.65728373, 0.27062473],
    [0.18113908, 0.66167266, 0.27059683],
    [0.18040090, 0.66606455, 0.27051968],
    [0.17973362, 0.67045901, 0.27039219],
    [0.17914666, 0.67485561, 0.27021328],
    [0.17864991, 0.67925392, 0.26998191],
    [0.17825354, 0.68365350, 0.26969688],
    [0.17796837, 0.68805386, 0.26935721],
    [0.17780567, 0.69245449, 0.26896199],
    [0.17777682, 0.69685486, 0.26851024],
    [0.17789306, 0.70125447, 0.26800081],
    [0.17816638, 0.70565274, 0.26743301],
    [0.17860845, 0.71004908, 0.26680607],
    [0.17923045, 0.71444295, 0.26611895],
    [0.18004387, 0.71883370, 0.26537122],
    [0.18105939, 0.72322073, 0.26456221],
    [0.18228709, 0.72760342, 0.26369128],
    [0.18373660, 0.73198114, 0.26275823],
    [0.18541627, 0.73635326, 0.26176250],
    [0.18733385, 0.74071915, 0.26070413],
    [0.18949565, 0.74507816, 0.25958292],
    [0.19190693, 0.74942970, 0.25839900],
    [0.19457156, 0.75377313, 0.25715255],
    [0.19749207, 0.75810789, 0.25584391],
    [0.20066962, 0.76243339, 0.25447357],
    [0.20410395, 0.76674911, 0.25304214],
    [0.20779347, 0.77105451, 0.25155039],
    [0.21173529, 0.77534914, 0.24999924],
    [0.21592528, 0.77963255, 0.24838964],
    [0.22035816, 0.78390435, 0.24672285],
    [0.22502766, 0.78816421, 0.24499995],
    [0.22992658, 0.79241182, 0.24322256],
    [0.23504696, 0.79664694, 0.24139178],
    [0.24038016, 0.80086939, 0.23950942],
    [0.24591708, 0.80507904, 0.23757683],
    [0.25164822, 0.80927581, 0.23559549],
    [0.25756372, 0.81345968, 0.23356748],
    [0.26365374, 0.81763069, 0.23149389],
    [0.26990833, 0.82178892, 0.22937628],
    [0.27631742, 0.82593451, 0.22721671],
    [0.28287131, 0.83006765, 0.22501628],
    [0.28956046, 0.83418857, 0.22277634],
    [0.29637553, 0.83829753, 0.22049822],
    [0.30330751, 0.84239486, 0.21818320],
    [0.31034775, 0.84648090, 0.21583243],
    [0.31748795, 0.85055602, 0.21344693],
    [0.32472025, 0.85462063, 0.21102760],
    [0.33203722, 0.85867516, 0.20857518],
    [0.33943185, 0.86272004, 0.20609025],
    [0.34689758, 0.86675575, 0.20357323],
    [0.35442831, 0.87078274, 0.20102431],
    [0.36201838, 0.87480149, 0.19844353],
    [0.36966256, 0.87881249, 0.19583070],
    [0.37735564, 0.88281626, 0.19318616],
    [0.38509301, 0.88681328, 0.19050973],
    [0.39287107, 0.89080400, 0.18779975],
    [0.40068544, 0.89478897, 0.18505658],
    [0.40853278, 0.89876866, 0.18227902],
    [0.41641017, 0.90274351, 0.17946547],
    [0.42431417, 0.90671406, 0.17661570],
    [0.43224265, 0.91068072, 0.17372726],
    [0.44019310, 0.91464397, 0.17079872],
    [0.44816294, 0.91860430, 0.16782905],
    [0.45615107, 0.92256205, 0.16481446],
    [0.46415519, 0.92651773, 0.16175370],
    [0.47217347, 0.93047178, 0.15864467],
    [0.48020519, 0.93442455, 0.15548315],
    [0.48824904, 0.93837643, 0.15226599],
    [0.49630389, 0.94232783, 0.14898971],
    [0.50436874, 0.94627914, 0.14565037],
    [0.51244252, 0.95023076, 0.14224406],
    [0.52052475, 0.95418301, 0.13876532],
    [0.52861493, 0.95813624, 0.13520830],
    [0.53671258, 0.96209078, 0.13156672],
    [0.54481726, 0.96604696, 0.12783355],
    [0.55292825, 0.97000517, 0.12400180],
    [0.56104561, 0.97396567, 0.12006166],
    [0.56916921, 0.97792875, 0.11600264],
    [0.57729897, 0.98189469, 0.11181264],
    [0.58543490, 0.98586376, 0.10747761],
    [0.59357707, 0.98983624, 0.10298105],
]

# Create ListedColormap object for this colormap
cmap = ListedColormap(cm_data, name="cmr.nuclear", N=256)
cmap_r = cmap.reversed()

# Register (reversed) cmap in MPL
mpl.colormaps.register(cmap=cmap)
mpl.colormaps.register(cmap=cmap_r)
