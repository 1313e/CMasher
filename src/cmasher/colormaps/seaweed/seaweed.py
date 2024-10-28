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
cm_type = "diverging"

# RGB-values of this colormap
cm_data = [
    [0.56895383, 0.94578930, 0.98486957],
    [0.56386975, 0.94121572, 0.98258388],
    [0.55880703, 0.93665230, 0.98030983],
    [0.55376595, 0.93209886, 0.97804728],
    [0.54874679, 0.92755521, 0.97579612],
    [0.54374984, 0.92302117, 0.97355622],
    [0.53877538, 0.91849656, 0.97132762],
    [0.53382379, 0.91398121, 0.96910998],
    [0.52889544, 0.90947493, 0.96690316],
    [0.52399068, 0.90497755, 0.96470700],
    [0.51910985, 0.90048887, 0.96252157],
    [0.51425342, 0.89600873, 0.96034649],
    [0.50942180, 0.89153694, 0.95818155],
    [0.50461542, 0.88707330, 0.95602676],
    [0.49983476, 0.88261765, 0.95388187],
    [0.49508032, 0.87816982, 0.95174655],
    [0.49035258, 0.87372959, 0.94962085],
    [0.48565211, 0.86929680, 0.94750440],
    [0.48097945, 0.86487127, 0.94539696],
    [0.47633517, 0.86045280, 0.94329851],
    [0.47171991, 0.85604124, 0.94120851],
    [0.46713426, 0.85163635, 0.93912714],
    [0.46257892, 0.84723800, 0.93705370],
    [0.45805454, 0.84284597, 0.93498838],
    [0.45356187, 0.83846010, 0.93293047],
    [0.44910162, 0.83408018, 0.93088016],
    [0.44467458, 0.82970605, 0.92883676],
    [0.44028155, 0.82533750, 0.92680025],
    [0.43592336, 0.82097436, 0.92477020],
    [0.43160087, 0.81661645, 0.92274623],
    [0.42731498, 0.81226355, 0.92072829],
    [0.42306662, 0.80791551, 0.91871576],
    [0.41885674, 0.80357214, 0.91670829],
    [0.41468636, 0.79923321, 0.91470581],
    [0.41055650, 0.79489858, 0.91270769],
    [0.40646820, 0.79056806, 0.91071353],
    [0.40242258, 0.78624145, 0.90872295],
    [0.39842079, 0.78191854, 0.90673569],
    [0.39446398, 0.77759918, 0.90475118],
    [0.39055336, 0.77328316, 0.90276895],
    [0.38669017, 0.76897031, 0.90078854],
    [0.38287568, 0.76466043, 0.89880947],
    [0.37911120, 0.76035335, 0.89683123],
    [0.37539808, 0.75604886, 0.89485330],
    [0.37173770, 0.75174680, 0.89287513],
    [0.36813148, 0.74744696, 0.89089615],
    [0.36458084, 0.74314918, 0.88891578],
    [0.36108727, 0.73885326, 0.88693338],
    [0.35765225, 0.73455903, 0.88494832],
    [0.35427732, 0.73026632, 0.88295991],
    [0.35096400, 0.72597493, 0.88096747],
    [0.34771388, 0.72168471, 0.87897025],
    [0.34452860, 0.71739544, 0.87696766],
    [0.34140971, 0.71310698, 0.87495878],
    [0.33835879, 0.70881917, 0.87294276],
    [0.33537746, 0.70453185, 0.87091878],
    [0.33246747, 0.70024480, 0.86888614],
    [0.32963027, 0.69595793, 0.86684369],
    [0.32686753, 0.69167106, 0.86479058],
    [0.32418090, 0.68738402, 0.86272586],
    [0.32157182, 0.68309670, 0.86064838],
    [0.31904200, 0.67880892, 0.85855725],
    [0.31659276, 0.67452060, 0.85645116],
    [0.31422570, 0.67023157, 0.85432910],
    [0.31194218, 0.66594173, 0.85218981],
    [0.30974343, 0.66165100, 0.85003194],
    [0.30763097, 0.65735922, 0.84785440],
    [0.30560579, 0.65306634, 0.84565568],
    [0.30366899, 0.64877230, 0.84343437],
    [0.30182158, 0.64447702, 0.84118902],
    [0.30006451, 0.64018042, 0.83891818],
    [0.29839851, 0.63588249, 0.83662023],
    [0.29682415, 0.63158321, 0.83429353],
    [0.29534188, 0.62728259, 0.83193639],
    [0.29395203, 0.62298064, 0.82954706],
    [0.29265471, 0.61867740, 0.82712373],
    [0.29144987, 0.61437293, 0.82466453],
    [0.29033727, 0.61006731, 0.82216755],
    [0.28931655, 0.60576065, 0.81963085],
    [0.28838692, 0.60145310, 0.81705234],
    [0.28754744, 0.59714485, 0.81442993],
    [0.28679697, 0.59283609, 0.81176148],
    [0.28613436, 0.58852701, 0.80904491],
    [0.28555767, 0.58421796, 0.80627791],
    [0.28506514, 0.57990921, 0.80345829],
    [0.28465461, 0.57560111, 0.80058378],
    [0.28432356, 0.57129406, 0.79765210],
    [0.28406935, 0.56698850, 0.79466098],
    [0.28388899, 0.56268490, 0.79160819],
    [0.28377907, 0.55838381, 0.78849144],
    [0.28373633, 0.55408575, 0.78530861],
    [0.28375675, 0.54979137, 0.78205753],
    [0.28383628, 0.54550134, 0.77873614],
    [0.28397071, 0.54121633, 0.77534252],
    [0.28415552, 0.53693710, 0.77187481],
    [0.28438589, 0.53266445, 0.76833133],
    [0.28465691, 0.52839918, 0.76471055],
    [0.28496349, 0.52414215, 0.76101112],
    [0.28530039, 0.51989423, 0.75723191],
    [0.28566228, 0.51565633, 0.75337201],
    [0.28604375, 0.51142934, 0.74943074],
    [0.28643934, 0.50721420, 0.74540771],
    [0.28684359, 0.50301182, 0.74130278],
    [0.28725110, 0.49882312, 0.73711611],
    [0.28765652, 0.49464897, 0.73284813],
    [0.28805465, 0.49049024, 0.72849958],
    [0.28844043, 0.48634777, 0.72407149],
    [0.28880899, 0.48222235, 0.71956516],
    [0.28915570, 0.47811472, 0.71498217],
    [0.28947616, 0.47402556, 0.71032435],
    [0.28976620, 0.46995551, 0.70559379],
    [0.29002201, 0.46590514, 0.70079278],
    [0.29024012, 0.46187492, 0.69592380],
    [0.29041739, 0.45786528, 0.69098948],
    [0.29055080, 0.45387660, 0.68599266],
    [0.29063788, 0.44990914, 0.68093625],
    [0.29067657, 0.44596310, 0.67582315],
    [0.29066460, 0.44203869, 0.67065661],
    [0.29060083, 0.43813590, 0.66543949],
    [0.29048347, 0.43425483, 0.66017515],
    [0.29031191, 0.43039538, 0.65486646],
    [0.29008514, 0.42655748, 0.64951661],
    [0.28980260, 0.42274100, 0.64412867],
    [0.28946412, 0.41894571, 0.63870549],
    [0.28906954, 0.41517140, 0.63325000],
    [0.28861886, 0.41141780, 0.62776504],
    [0.28811230, 0.40768461, 0.62225333],
    [0.28755020, 0.40397150, 0.61671753],
    [0.28693303, 0.40027813, 0.61116014],
    [0.28626141, 0.39660410, 0.60558358],
    [0.28553606, 0.39294904, 0.59999014],
    [0.28475776, 0.38931252, 0.59438199],
    [0.28392740, 0.38569413, 0.58876116],
    [0.28304551, 0.38209349, 0.58312997],
    [0.28211340, 0.37851012, 0.57748994],
    [0.28113191, 0.37494360, 0.57184298],
    [0.28010194, 0.37139349, 0.56619084],
    [0.27902460, 0.36785937, 0.56053501],
    [0.27790092, 0.36434077, 0.55487694],
    [0.27673171, 0.36083730, 0.54921829],
    [0.27551826, 0.35734849, 0.54356006],
    [0.27426154, 0.35387393, 0.53790354],
    [0.27296233, 0.35041320, 0.53225014],
    [0.27162179, 0.34696588, 0.52660078],
    [0.27024091, 0.34353156, 0.52095642],
    [0.26882066, 0.34010982, 0.51531804],
    [0.26736198, 0.33670027, 0.50968652],
    [0.26586579, 0.33330252, 0.50406268],
    [0.26433300, 0.32991617, 0.49844727],
    [0.26276452, 0.32654085, 0.49284099],
    [0.26116118, 0.32317620, 0.48724454],
    [0.25952369, 0.31982184, 0.48165870],
    [0.25785306, 0.31647741, 0.47608378],
    [0.25615011, 0.31314255, 0.47052025],
    [0.25441549, 0.30981692, 0.46496876],
    [0.25264988, 0.30650019, 0.45942985],
    [0.25085427, 0.30319200, 0.45390353],
    [0.24902902, 0.29989205, 0.44839071],
    [0.24717509, 0.29659999, 0.44289123],
    [0.24529292, 0.29331553, 0.43740577],
    [0.24338335, 0.29003833, 0.43193426],
    [0.24144672, 0.28676811, 0.42647740],
    [0.23948392, 0.28350454, 0.42103488],
    [0.23749522, 0.28024734, 0.41560743],
    [0.23548132, 0.27699621, 0.41019493],
    [0.23344281, 0.27375086, 0.40479743],
    [0.23138002, 0.27051101, 0.39941537],
    [0.22929346, 0.26727637, 0.39404881],
    [0.22718368, 0.26404667, 0.38869767],
    [0.22505111, 0.26082162, 0.38336206],
    [0.22289615, 0.25760095, 0.37804208],
    [0.22071916, 0.25438439, 0.37273786],
    [0.21852051, 0.25117168, 0.36744949],
    [0.21630063, 0.24796254, 0.36217684],
    [0.21405985, 0.24475672, 0.35691994],
    [0.21179852, 0.24155394, 0.35167878],
    [0.20951695, 0.23835394, 0.34645333],
    [0.20721544, 0.23515646, 0.34124357],
    [0.20489427, 0.23196124, 0.33604944],
    [0.20255371, 0.22876802, 0.33087087],
    [0.20019400, 0.22557654, 0.32570782],
    [0.19781533, 0.22238653, 0.32056036],
    [0.19541799, 0.21919773, 0.31542823],
    [0.19300218, 0.21600988, 0.31031131],
    [0.19056810, 0.21282271, 0.30520947],
    [0.18811594, 0.20963597, 0.30012257],
    [0.18564581, 0.20644937, 0.29505062],
    [0.18315781, 0.20326265, 0.28999356],
    [0.18065219, 0.20007554, 0.28495099],
    [0.17812907, 0.19688776, 0.27992272],
    [0.17558842, 0.19369904, 0.27490892],
    [0.17303042, 0.19050908, 0.26990920],
    [0.17045520, 0.18731761, 0.26492320],
    [0.16786267, 0.18412432, 0.25995112],
    [0.16525298, 0.18092894, 0.25499249],
    [0.16262619, 0.17773115, 0.25004698],
    [0.15998215, 0.17453064, 0.24511484],
    [0.15732108, 0.17132711, 0.24019523],
    [0.15464274, 0.16812022, 0.23528848],
    [0.15194729, 0.16490966, 0.23039385],
    [0.14923453, 0.16169508, 0.22551145],
    [0.14650450, 0.15847614, 0.22064069],
    [0.14375701, 0.15525248, 0.21578158],
    [0.14099209, 0.15202374, 0.21093349],
    [0.13820945, 0.14878954, 0.20609652],
    [0.13540914, 0.14554949, 0.20126983],
    [0.13259079, 0.14230318, 0.19645369],
    [0.12975439, 0.13905020, 0.19164720],
    [0.12689965, 0.13579012, 0.18685026],
    [0.12402633, 0.13252249, 0.18206251],
    [0.12113427, 0.12924684, 0.17728328],
    [0.11822306, 0.12596269, 0.17251255],
    [0.11529247, 0.12266952, 0.16774961],
    [0.11234219, 0.11936682, 0.16299391],
    [0.10937178, 0.11605402, 0.15824528],
    [0.10638087, 0.11273054, 0.15350305],
    [0.10336907, 0.10939579, 0.14876655],
    [0.10033589, 0.10604911, 0.14403530],
    [0.09728075, 0.10268982, 0.13930894],
    [0.09420317, 0.09931722, 0.13458657],
    [0.09110255, 0.09593055, 0.12986751],
    [0.08797823, 0.09252901, 0.12515108],
    [0.08482944, 0.08911176, 0.12043677],
    [0.08165547, 0.08567788, 0.11572357],
    [0.07845549, 0.08222641, 0.11101061],
    [0.07522859, 0.07875633, 0.10629697],
    [0.07197377, 0.07526652, 0.10158170],
    [0.06868996, 0.07175580, 0.09686375],
    [0.06537593, 0.06822288, 0.09214213],
    [0.06203045, 0.06466637, 0.08741545],
    [0.05865209, 0.06108477, 0.08268237],
    [0.05523929, 0.05747644, 0.07794145],
    [0.05179035, 0.05383959, 0.07319110],
    [0.04830336, 0.05017225, 0.06842958],
    [0.04477621, 0.04647226, 0.06365495],
    [0.04120655, 0.04273722, 0.05886508],
    [0.03760367, 0.03895554, 0.05405760],
    [0.03413181, 0.03526841, 0.04922982],
    [0.03080984, 0.03175438, 0.04437873],
    [0.02763951, 0.02841392, 0.03949145],
    [0.02462270, 0.02524760, 0.03474625],
    [0.02176139, 0.02225617, 0.03032120],
    [0.01905775, 0.01944055, 0.02621164],
    [0.01651413, 0.01680184, 0.02241310],
    [0.01413310, 0.01434141, 0.01892129],
    [0.01191752, 0.01206089, 0.01573220],
    [0.00987059, 0.00996225, 0.01284206],
    [0.00799593, 0.00804789, 0.01024745],
    [0.00629773, 0.00632073, 0.00794537],
    [0.00478089, 0.00478437, 0.00593333],
    [0.00345128, 0.00344338, 0.00420961],
    [0.00231620, 0.00230361, 0.00277352],
    [0.00138507, 0.00137296, 0.00162600],
    [0.00067095, 0.00066271, 0.00077085],
    [0.00019422, 0.00019111, 0.00021801],
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
    [0.12786107, 0.16777673, 0.09763865],
    [0.12997412, 0.17148010, 0.09977172],
    [0.13205940, 0.17518226, 0.10189504],
    [0.13411718, 0.17888350, 0.10400873],
    [0.13614773, 0.18258409, 0.10611291],
    [0.13815136, 0.18628425, 0.10820777],
    [0.14012821, 0.18998426, 0.11029335],
    [0.14207847, 0.19368438, 0.11236973],
    [0.14400236, 0.19738482, 0.11443703],
    [0.14590010, 0.20108579, 0.11649537],
    [0.14777176, 0.20478755, 0.11854474],
    [0.14961751, 0.20849029, 0.12058525],
    [0.15143754, 0.21219419, 0.12261699],
    [0.15323187, 0.21589951, 0.12463995],
    [0.15500067, 0.21960639, 0.12665422],
    [0.15674402, 0.22331504, 0.12865984],
    [0.15846194, 0.22702567, 0.13065680],
    [0.16015463, 0.23073840, 0.13264522],
    [0.16182200, 0.23445346, 0.13462501],
    [0.16346421, 0.23817098, 0.13659629],
    [0.16508121, 0.24189116, 0.13855900],
    [0.16667310, 0.24561414, 0.14051320],
    [0.16823984, 0.24934008, 0.14245885],
    [0.16978147, 0.25306913, 0.14439598],
    [0.17129797, 0.25680145, 0.14632457],
    [0.17278935, 0.26053718, 0.14824461],
    [0.17425557, 0.26427647, 0.15015608],
    [0.17569664, 0.26801945, 0.15205898],
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
    [0.19820323, 0.34000455, 0.18652296],
    [0.19912392, 0.34384679, 0.18824301],
    [0.20001726, 0.34769508, 0.18995302],
    [0.20088307, 0.35154952, 0.19165286],
    [0.20172116, 0.35541020, 0.19334241],
    [0.20253138, 0.35927720, 0.19502154],
    [0.20331352, 0.36315061, 0.19669012],
    [0.20406740, 0.36703051, 0.19834800],
    [0.20479282, 0.37091699, 0.19999504],
    [0.20548959, 0.37481011, 0.20163109],
    [0.20615750, 0.37870997, 0.20325598],
    [0.20679635, 0.38261664, 0.20486955],
    [0.20740594, 0.38653018, 0.20647165],
    [0.20798603, 0.39045069, 0.20806208],
    [0.20853643, 0.39437821, 0.20964067],
    [0.20905690, 0.39831284, 0.21120724],
    [0.20954722, 0.40225463, 0.21276157],
    [0.21000720, 0.40620364, 0.21430350],
    [0.21043655, 0.41015996, 0.21583278],
    [0.21083510, 0.41412363, 0.21734922],
    [0.21120261, 0.41809472, 0.21885260],
    [0.21153882, 0.42207329, 0.22034268],
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
    [0.21016426, 0.51574734, 0.25028968],
    [0.20969424, 0.51991715, 0.25136868],
    [0.20918971, 0.52409515, 0.25242546],
    [0.20865122, 0.52828125, 0.25345965],
    [0.20807868, 0.53247549, 0.25447057],
    [0.20747262, 0.53667781, 0.25545777],
    [0.20683348, 0.54088816, 0.25642071],
    [0.20616137, 0.54510656, 0.25735864],
    [0.20545721, 0.54933290, 0.25827113],
    [0.20472152, 0.55356716, 0.25915753],
    [0.20395477, 0.55780930, 0.26001707],
    [0.20315812, 0.56205922, 0.26084925],
    [0.20233248, 0.56631684, 0.26165339],
    [0.20147859, 0.57058214, 0.26242862],
    [0.20059794, 0.57485500, 0.26317436],
    [0.19969193, 0.57913529, 0.26388989],
    [0.19876208, 0.58342294, 0.26457444],
    [0.19780982, 0.58771785, 0.26522710],
    [0.19683726, 0.59201988, 0.26584716],
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
    [0.18279291, 0.65289815, 0.27060442],
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
    [0.17789306, 0.70125447, 0.26800080],
    [0.17816638, 0.70565274, 0.26743301],
    [0.17860845, 0.71004908, 0.26680607],
    [0.17923045, 0.71444295, 0.26611895],
    [0.18004387, 0.71883370, 0.26537122],
    [0.18105939, 0.72322073, 0.26456221],
    [0.18228709, 0.72760343, 0.26369128],
    [0.18373660, 0.73198114, 0.26275823],
    [0.18541627, 0.73635327, 0.26176250],
    [0.18733385, 0.74071914, 0.26070413],
    [0.18949565, 0.74507816, 0.25958292],
    [0.19190693, 0.74942970, 0.25839900],
    [0.19457156, 0.75377313, 0.25715255],
    [0.19749207, 0.75810789, 0.25584391],
    [0.20066962, 0.76243340, 0.25447357],
    [0.20410395, 0.76674911, 0.25304214],
    [0.20779347, 0.77105451, 0.25155039],
    [0.21173530, 0.77534914, 0.24999924],
    [0.21592528, 0.77963255, 0.24838964],
    [0.22035817, 0.78390435, 0.24672286],
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
    [0.37735564, 0.88281625, 0.19318617],
    [0.38509301, 0.88681328, 0.19050973],
    [0.39287107, 0.89080400, 0.18779975],
    [0.40068544, 0.89478897, 0.18505658],
    [0.40853278, 0.89876866, 0.18227902],
    [0.41641017, 0.90274351, 0.17946547],
    [0.42431417, 0.90671406, 0.17661570],
    [0.43224265, 0.91068072, 0.17372726],
    [0.44019310, 0.91464397, 0.17079872],
    [0.44816294, 0.91860430, 0.16782905],
    [0.45615107, 0.92256205, 0.16481447],
    [0.46415518, 0.92651773, 0.16175370],
    [0.47217347, 0.93047178, 0.15864467],
    [0.48020519, 0.93442455, 0.15548315],
    [0.48824904, 0.93837643, 0.15226599],
    [0.49630389, 0.94232784, 0.14898971],
    [0.50436874, 0.94627914, 0.14565037],
    [0.51244252, 0.95023076, 0.14224406],
    [0.52052475, 0.95418301, 0.13876531],
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
cmap = ListedColormap(cm_data, name="cmr.seaweed", N=511)
cmap_r = cmap.reversed()

# Register (reversed) cmap in MPL
mpl.colormaps.register(cmap=cmap)
mpl.colormaps.register(cmap=cmap_r)
