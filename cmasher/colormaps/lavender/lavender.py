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
    [0.00022628, 0.00012731, 0.00018041],
    [0.00081365, 0.00042889, 0.00063983],
    [0.00174260, 0.00086369, 0.00135487],
    [0.00301237, 0.00141020, 0.00232124],
    [0.00462645, 0.00205320, 0.00354023],
    [0.00659022, 0.00278050, 0.00501613],
    [0.00890955, 0.00358208, 0.00675498],
    [0.01159086, 0.00444910, 0.00876435],
    [0.01464139, 0.00537340, 0.01105340],
    [0.01806760, 0.00634788, 0.01363186],
    [0.02187663, 0.00736569, 0.01651095],
    [0.02607572, 0.00842034, 0.01970294],
    [0.03067145, 0.00950592, 0.02322078],
    [0.03567141, 0.01061629, 0.02707918],
    [0.04106850, 0.01174607, 0.03129316],
    [0.04652852, 0.01288959, 0.03587953],
    [0.05196240, 0.01404142, 0.04084816],
    [0.05737257, 0.01519657, 0.04592303],
    [0.06276218, 0.01634942, 0.05102940],
    [0.06813304, 0.01749501, 0.05617217],
    [0.07348667, 0.01862838, 0.06135607],
    [0.07882464, 0.01974444, 0.06658593],
    [0.08414820, 0.02083813, 0.07186642],
    [0.08945859, 0.02190424, 0.07720232],
    [0.09475636, 0.02293796, 0.08259778],
    [0.10004205, 0.02393437, 0.08805707],
    [0.10531609, 0.02488855, 0.09358449],
    [0.11057879, 0.02579547, 0.09918439],
    [0.11583040, 0.02665003, 0.10486124],
    [0.12107064, 0.02744761, 0.11061895],
    [0.12629918, 0.02818345, 0.11646160],
    [0.13151556, 0.02885291, 0.12239321],
    [0.13671988, 0.02945036, 0.12841904],
    [0.14191080, 0.02997205, 0.13454219],
    [0.14708768, 0.03041311, 0.14076718],
    [0.15224952, 0.03076905, 0.14709821],
    [0.15739512, 0.03103556, 0.15353940],
    [0.16252277, 0.03120918, 0.16009413],
    [0.16763145, 0.03128499, 0.16676750],
    [0.17271898, 0.03126021, 0.17356257],
    [0.17778331, 0.03113174, 0.18048291],
    [0.18282219, 0.03089684, 0.18753207],
    [0.18783313, 0.03055332, 0.19471328],
    [0.19281330, 0.03009975, 0.20202937],
    [0.19775957, 0.02953550, 0.20948273],
    [0.20266856, 0.02886073, 0.21707542],
    [0.20753682, 0.02807585, 0.22480982],
    [0.21235983, 0.02718462, 0.23268537],
    [0.21713353, 0.02618980, 0.24070336],
    [0.22185282, 0.02509787, 0.24886196],
    [0.22651292, 0.02391467, 0.25716101],
    [0.23110796, 0.02265073, 0.26559648],
    [0.23563205, 0.02131743, 0.27416461],
    [0.24007890, 0.01992890, 0.28286016],
    [0.24444178, 0.01850215, 0.29167631],
    [0.24871362, 0.01705740, 0.30060452],
    [0.25288699, 0.01561822, 0.30963447],
    [0.25695420, 0.01421171, 0.31875403],
    [0.26090744, 0.01286769, 0.32795026],
    [0.26473851, 0.01162142, 0.33720653],
    [0.26843933, 0.01051043, 0.34650595],
    [0.27200172, 0.00957681, 0.35582895],
    [0.27541768, 0.00886513, 0.36515546],
    [0.27867938, 0.00842414, 0.37446282],
    [0.28177937, 0.00830466, 0.38372800],
    [0.28471062, 0.00855961, 0.39292723],
    [0.28746668, 0.00924361, 0.40203606],
    [0.29004178, 0.01041207, 0.41102988],
    [0.29243091, 0.01212029, 0.41988454],
    [0.29462988, 0.01442271, 0.42857655],
    [0.29663543, 0.01737211, 0.43708347],
    [0.29844523, 0.02101878, 0.44538425],
    [0.30005791, 0.02540980, 0.45345950],
    [0.30147309, 0.03058837, 0.46129177],
    [0.30269133, 0.03659323, 0.46886569],
    [0.30371411, 0.04334598, 0.47616812],
    [0.30454379, 0.05030898, 0.48318821],
    [0.30518355, 0.05739721, 0.48991738],
    [0.30563736, 0.06457868, 0.49634929],
    [0.30590977, 0.07182667, 0.50247989],
    [0.30600599, 0.07911853, 0.50830715],
    [0.30593172, 0.08643496, 0.51383095],
    [0.30569335, 0.09375915, 0.51905274],
    [0.30529720, 0.10107699, 0.52397599],
    [0.30475023, 0.10837595, 0.52860524],
    [0.30405960, 0.11564525, 0.53294640],
    [0.30323249, 0.12287565, 0.53700645],
    [0.30227633, 0.13005912, 0.54079326],
    [0.30119873, 0.13718861, 0.54431540],
    [0.30000693, 0.14425848, 0.54758213],
    [0.29870847, 0.15126367, 0.55060309],
    [0.29731106, 0.15819975, 0.55338830],
    [0.29582176, 0.16506352, 0.55594799],
    [0.29424783, 0.17185217, 0.55829252],
    [0.29259638, 0.17856345, 0.56043231],
    [0.29087435, 0.18519568, 0.56237774],
    [0.28908853, 0.19174764, 0.56413908],
    [0.28724549, 0.19821856, 0.56572648],
    [0.28535159, 0.20460803, 0.56714986],
    [0.28341346, 0.21091570, 0.56841907],
    [0.28143672, 0.21714202, 0.56954343],
    [0.27942709, 0.22328751, 0.57053206],
    [0.27739045, 0.22935266, 0.57139394],
    [0.27533219, 0.23533837, 0.57213762],
    [0.27325712, 0.24124592, 0.57277113],
    [0.27117090, 0.24707608, 0.57330270],
    [0.26907752, 0.25283065, 0.57373949],
    [0.26698220, 0.25851068, 0.57408906],
    [0.26488888, 0.26411793, 0.57435809],
    [0.26280153, 0.26965407, 0.57455304],
    [0.26072485, 0.27512037, 0.57468060],
    [0.25866185, 0.28051893, 0.57474627],
    [0.25661612, 0.28585144, 0.57475572],
    [0.25459101, 0.29111969, 0.57471430],
    [0.25258988, 0.29632534, 0.57462719],
    [0.25061546, 0.30147031, 0.57449907],
    [0.24867033, 0.30655648, 0.57433433],
    [0.24675697, 0.31158568, 0.57413722],
    [0.24487763, 0.31655975, 0.57391170],
    [0.24303437, 0.32148051, 0.57366150],
    [0.24122899, 0.32634980, 0.57339009],
    [0.23946309, 0.33116943, 0.57310074],
    [0.23773805, 0.33594121, 0.57279649],
    [0.23605509, 0.34066688, 0.57248022],
    [0.23441531, 0.34534818, 0.57215469],
    [0.23281921, 0.34998691, 0.57182217],
    [0.23126725, 0.35458483, 0.57148490],
    [0.22975967, 0.35914363, 0.57114494],
    [0.22829674, 0.36366493, 0.57080434],
    [0.22687837, 0.36815034, 0.57046493],
    [0.22550382, 0.37260161, 0.57012801],
    [0.22417253, 0.37702034, 0.56979506],
    [0.22288415, 0.38140793, 0.56946772],
    [0.22163703, 0.38576615, 0.56914663],
    [0.22043022, 0.39009641, 0.56883303],
    [0.21926231, 0.39440021, 0.56852782],
    [0.21813127, 0.39867913, 0.56823140],
    [0.21703589, 0.40293442, 0.56794486],
    [0.21597335, 0.40716774, 0.56766805],
    [0.21494223, 0.41138023, 0.56740192],
    [0.21393931, 0.41557353, 0.56714604],
    [0.21296285, 0.41974871, 0.56690111],
    [0.21200937, 0.42390731, 0.56666651],
    [0.21107665, 0.42805045, 0.56644257],
    [0.21016123, 0.43217950, 0.56622867],
    [0.20926022, 0.43629563, 0.56602457],
    [0.20837044, 0.44040003, 0.56582984],
    [0.20748826, 0.44449394, 0.56564362],
    [0.20661079, 0.44857838, 0.56546561],
    [0.20573413, 0.45265454, 0.56529468],
    [0.20485470, 0.45672352, 0.56512989],
    [0.20396941, 0.46078623, 0.56497060],
    [0.20307415, 0.46484379, 0.56481536],
    [0.20216531, 0.46889717, 0.56466299],
    [0.20123956, 0.47294722, 0.56451243],
    [0.20029300, 0.47699491, 0.56436217],
    [0.19932194, 0.48104109, 0.56421071],
    [0.19832279, 0.48508660, 0.56405653],
    [0.19729225, 0.48913216, 0.56389824],
    [0.19622649, 0.49317857, 0.56373395],
    [0.19512204, 0.49722653, 0.56356194],
    [0.19397551, 0.50127671, 0.56338041],
    [0.19278376, 0.50532970, 0.56318764],
    [0.19154342, 0.50938609, 0.56298163],
    [0.19025129, 0.51344643, 0.56276039],
    [0.18890433, 0.51751123, 0.56252194],
    [0.18749962, 0.52158093, 0.56226424],
    [0.18603448, 0.52565592, 0.56198529],
    [0.18450617, 0.52973657, 0.56168299],
    [0.18291209, 0.53382322, 0.56135517],
    [0.18124987, 0.53791615, 0.56099970],
    [0.17951725, 0.54201560, 0.56061444],
    [0.17771219, 0.54612176, 0.56019726],
    [0.17583280, 0.55023478, 0.55974601],
    [0.17387742, 0.55435477, 0.55925857],
    [0.17184443, 0.55848181, 0.55873275],
    [0.16973252, 0.56261595, 0.55816641],
    [0.16754060, 0.56675717, 0.55755743],
    [0.16526782, 0.57090544, 0.55690372],
    [0.16291356, 0.57506067, 0.55620319],
    [0.16047751, 0.57922275, 0.55545378],
    [0.15795965, 0.58339154, 0.55465347],
    [0.15536026, 0.58756685, 0.55380025],
    [0.15268001, 0.59174847, 0.55289214],
    [0.14991996, 0.59593616, 0.55192720],
    [0.14708165, 0.60012965, 0.55090352],
    [0.14416711, 0.60432863, 0.54981923],
    [0.14117895, 0.60853277, 0.54867251],
    [0.13812044, 0.61274172, 0.54746155],
    [0.13499552, 0.61695510, 0.54618457],
    [0.13180906, 0.62117250, 0.54483985],
    [0.12856691, 0.62539349, 0.54342572],
    [0.12527601, 0.62961762, 0.54194054],
    [0.12194462, 0.63384441, 0.54038271],
    [0.11858243, 0.63807336, 0.53875064],
    [0.11520089, 0.64230397, 0.53704281],
    [0.11181315, 0.64653571, 0.53525762],
    [0.10843492, 0.65076802, 0.53339365],
    [0.10508441, 0.65500033, 0.53144949],
    [0.10178265, 0.65923203, 0.52942374],
    [0.09855384, 0.66346253, 0.52731504],
    [0.09542572, 0.66769118, 0.52512205],
    [0.09242918, 0.67191740, 0.52284316],
    [0.08960015, 0.67614047, 0.52047733],
    [0.08697804, 0.68035971, 0.51802331],
    [0.08460602, 0.68457443, 0.51547985],
    [0.08253010, 0.68878392, 0.51284557],
    [0.08079875, 0.69298747, 0.51011911],
    [0.07946223, 0.69718428, 0.50729957],
    [0.07856957, 0.70137357, 0.50438580],
    [0.07816623, 0.70555458, 0.50137626],
    [0.07829345, 0.70972648, 0.49826987],
    [0.07898555, 0.71388839, 0.49506582],
    [0.08026671, 0.71803947, 0.49176266],
    [0.08215118, 0.72217884, 0.48835903],
    [0.08464367, 0.72630551, 0.48485445],
    [0.08773729, 0.73041860, 0.48124711],
    [0.09141753, 0.73451708, 0.47753621],
    [0.09566267, 0.73859990, 0.47372098],
    [0.10044518, 0.74266608, 0.46979936],
    [0.10573581, 0.74671439, 0.46577169],
    [0.11150247, 0.75074383, 0.46163512],
    [0.11771455, 0.75475305, 0.45739056],
    [0.12434160, 0.75874093, 0.45303511],
    [0.13135571, 0.76270607, 0.44856941],
    [0.13873106, 0.76664714, 0.44399160],
    [0.14644456, 0.77056271, 0.43930090],
    [0.15447560, 0.77445122, 0.43449731],
    [0.16280658, 0.77831112, 0.42957909],
    [0.17142217, 0.78214072, 0.42454593],
    [0.18030921, 0.78593823, 0.41939798],
    [0.18945691, 0.78970175, 0.41413493],
    [0.19885649, 0.79342929, 0.40875670],
    [0.20850100, 0.79711872, 0.40326354],
    [0.21838520, 0.80076777, 0.39765598],
    [0.22850506, 0.80437400, 0.39193553],
    [0.23885825, 0.80793482, 0.38610368],
    [0.24944336, 0.81144744, 0.38016320],
    [0.26026002, 0.81490888, 0.37411775],
    [0.27130876, 0.81831597, 0.36797226],
    [0.28259096, 0.82166528, 0.36173301],
    [0.29411073, 0.82495305, 0.35540556],
    [0.30586837, 0.82817546, 0.34900319],
    [0.31786973, 0.83132816, 0.34253550],
    [0.33011592, 0.83440680, 0.33602138],
    [0.34261175, 0.83740653, 0.32947931],
    [0.35536011, 0.84032235, 0.32293457],
    [0.36836204, 0.84314916, 0.31641947],
    [0.38161778, 0.84588169, 0.30997279],
    [0.39512484, 0.84851475, 0.30364234],
    [0.40887749, 0.85104339, 0.29748583],
    [0.42286581, 0.85346311, 0.29157190],
    [0.43707091, 0.85577071, 0.28598374],
    [0.45146975, 0.85796396, 0.28081359],
    [0.46602713, 0.86004302, 0.27616680],
]

# Create ListedColormap object for this colormap
cmap = ListedColormap(cm_data, name="cmr.lavender", N=256)
cmap_r = cmap.reversed()

# Register (reversed) cmap in MPL
mpl.colormaps.register(cmap=cmap)
mpl.colormaps.register(cmap=cmap_r)
