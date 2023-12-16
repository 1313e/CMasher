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
    [0.00016543, 0.00017235, 0.00023614],
    [0.00056507, 0.00059773, 0.00085492],
    [0.00115294, 0.00123867, 0.00184354],
    [0.00190503, 0.00207923, 0.00320909],
    [0.00280372, 0.00310993, 0.00496346],
    [0.00383417, 0.00432455, 0.00712121],
    [0.00498316, 0.00571890, 0.00969761],
    [0.00623839, 0.00729020, 0.01270841],
    [0.00758744, 0.00903673, 0.01617173],
    [0.00901874, 0.01095766, 0.02010290],
    [0.01051967, 0.01305290, 0.02452127],
    [0.01207825, 0.01532304, 0.02944250],
    [0.01368165, 0.01776930, 0.03488387],
    [0.01531606, 0.02039355, 0.04085579],
    [0.01696791, 0.02319825, 0.04696683],
    [0.01862249, 0.02618652, 0.05307570],
    [0.02026433, 0.02936211, 0.05918365],
    [0.02187713, 0.03272950, 0.06529073],
    [0.02344352, 0.03629391, 0.07139618],
    [0.02494467, 0.04006143, 0.07749896],
    [0.02636225, 0.04389129, 0.08359395],
    [0.02767477, 0.04771267, 0.08967853],
    [0.02886183, 0.05153595, 0.09574519],
    [0.02990029, 0.05536627, 0.10178747],
    [0.03076681, 0.05920868, 0.10779602],
    [0.03143784, 0.06306816, 0.11375905],
    [0.03188926, 0.06694974, 0.11966277],
    [0.03209927, 0.07085806, 0.12548923],
    [0.03204485, 0.07479790, 0.13121964],
    [0.03170914, 0.07877316, 0.13682947],
    [0.03107872, 0.08278722, 0.14229185],
    [0.03014850, 0.08684216, 0.14757605],
    [0.02892314, 0.09093857, 0.15264897],
    [0.02742180, 0.09507468, 0.15747575],
    [0.02567782, 0.09924639, 0.16202295],
    [0.02374284, 0.10344650, 0.16626052],
    [0.02168272, 0.10766529, 0.17016587],
    [0.01957446, 0.11189102, 0.17372630],
    [0.01750057, 0.11611087, 0.17694064],
    [0.01554158, 0.12031222, 0.17981907],
    [0.01377041, 0.12448375, 0.18238128],
    [0.01224870, 0.12861610, 0.18465359],
    [0.01102527, 0.13270222, 0.18666593],
    [0.01013654, 0.13673734, 0.18844911],
    [0.00960796, 0.14071870, 0.19003286],
    [0.00945611, 0.14464524, 0.19144452],
    [0.00969160, 0.14851694, 0.19270899],
    [0.01031902, 0.15233494, 0.19384744],
    [0.01134072, 0.15610072, 0.19487905],
    [0.01275549, 0.15981642, 0.19581928],
    [0.01456113, 0.16348428, 0.19668168],
    [0.01675444, 0.16710668, 0.19747760],
    [0.01933158, 0.17068605, 0.19821647],
    [0.02228850, 0.17422480, 0.19890610],
    [0.02562126, 0.17772520, 0.19955350],
    [0.02932575, 0.18118959, 0.20016348],
    [0.03339835, 0.18462010, 0.20074050],
    [0.03783568, 0.18801874, 0.20128825],
    [0.04256515, 0.19138746, 0.20180927],
    [0.04732039, 0.19472808, 0.20230550],
    [0.05208430, 0.19804224, 0.20277901],
    [0.05684929, 0.20133154, 0.20323032],
    [0.06160993, 0.20459744, 0.20366006],
    [0.06636254, 0.20784126, 0.20406847],
    [0.07110480, 0.21106422, 0.20445542],
    [0.07583546, 0.21426743, 0.20482045],
    [0.08055413, 0.21745189, 0.20516282],
    [0.08526112, 0.22061849, 0.20548155],
    [0.08995729, 0.22376802, 0.20577543],
    [0.09464400, 0.22690114, 0.20604306],
    [0.09932297, 0.23001842, 0.20628291],
    [0.10399629, 0.23312032, 0.20649326],
    [0.10866630, 0.23620720, 0.20667231],
    [0.11333562, 0.23927930, 0.20681819],
    [0.11800703, 0.24233678, 0.20692895],
    [0.12268344, 0.24537967, 0.20700274],
    [0.12736801, 0.24840794, 0.20703752],
    [0.13206401, 0.25142142, 0.20703121],
    [0.13677474, 0.25441989, 0.20698188],
    [0.14150347, 0.25740301, 0.20688783],
    [0.14625367, 0.26037038, 0.20674716],
    [0.15102874, 0.26332149, 0.20655811],
    [0.15583197, 0.26625581, 0.20631922],
    [0.16066665, 0.26917269, 0.20602911],
    [0.16553603, 0.27207145, 0.20568642],
    [0.17044314, 0.27495136, 0.20529017],
    [0.17539092, 0.27781164, 0.20483949],
    [0.18038218, 0.28065148, 0.20433362],
    [0.18541944, 0.28347005, 0.20377221],
    [0.19050512, 0.28626648, 0.20315496],
    [0.19564140, 0.28903991, 0.20248181],
    [0.20083015, 0.29178948, 0.20175306],
    [0.20607312, 0.29451432, 0.20096901],
    [0.21137172, 0.29721359, 0.20013034],
    [0.21672715, 0.29988644, 0.19923788],
    [0.22214038, 0.30253209, 0.19829263],
    [0.22761211, 0.30514975, 0.19729584],
    [0.23314282, 0.30773868, 0.19624890],
    [0.23873275, 0.31029817, 0.19515339],
    [0.24438198, 0.31282757, 0.19401100],
    [0.25009029, 0.31532625, 0.19282364],
    [0.25585738, 0.31779364, 0.19159329],
    [0.26168271, 0.32022921, 0.19032209],
    [0.26756557, 0.32263248, 0.18901231],
    [0.27350521, 0.32500300, 0.18766618],
    [0.27950062, 0.32734040, 0.18628626],
    [0.28555074, 0.32964434, 0.18487502],
    [0.29165448, 0.33191449, 0.18343498],
    [0.29781051, 0.33415064, 0.18196891],
    [0.30401760, 0.33635255, 0.18047943],
    [0.31027437, 0.33852004, 0.17896932],
    [0.31657935, 0.34065302, 0.17744148],
    [0.32293119, 0.34275134, 0.17589866],
    [0.32932838, 0.34481497, 0.17434382],
    [0.33576938, 0.34684390, 0.17277997],
    [0.34225277, 0.34883811, 0.17121001],
    [0.34877705, 0.35079763, 0.16963696],
    [0.35534066, 0.35272256, 0.16806399],
    [0.36194213, 0.35461298, 0.16649417],
    [0.36858009, 0.35646897, 0.16493051],
    [0.37525297, 0.35829071, 0.16337635],
    [0.38195932, 0.36007838, 0.16183489],
    [0.38869780, 0.36183214, 0.16030931],
    [0.39546704, 0.36355217, 0.15880289],
    [0.40226559, 0.36523875, 0.15731904],
    [0.40909213, 0.36689211, 0.15586112],
    [0.41594539, 0.36851250, 0.15443249],
    [0.42282416, 0.37010016, 0.15303652],
    [0.42972710, 0.37165543, 0.15167676],
    [0.43665302, 0.37317861, 0.15035671],
    [0.44360075, 0.37467001, 0.14907987],
    [0.45056916, 0.37612995, 0.14784975],
    [0.45755721, 0.37755874, 0.14666983],
    [0.46456375, 0.37895675, 0.14554374],
    [0.47158775, 0.38032436, 0.14447503],
    [0.47862821, 0.38166191, 0.14346724],
    [0.48568416, 0.38296977, 0.14252388],
    [0.49275469, 0.38424832, 0.14164842],
    [0.49983891, 0.38549792, 0.14084430],
    [0.50693599, 0.38671895, 0.14011489],
    [0.51404506, 0.38791181, 0.13946356],
    [0.52116534, 0.38907688, 0.13889354],
    [0.52829607, 0.39021456, 0.13840799],
    [0.53543653, 0.39132521, 0.13800994],
    [0.54258604, 0.39240923, 0.13770233],
    [0.54974396, 0.39346699, 0.13748795],
    [0.55690966, 0.39449889, 0.13736943],
    [0.56408256, 0.39550527, 0.13734929],
    [0.57126210, 0.39648653, 0.13742983],
    [0.57844776, 0.39744302, 0.13761321],
    [0.58563906, 0.39837510, 0.13790141],
    [0.59283552, 0.39928312, 0.13829622],
    [0.60003670, 0.40016744, 0.13879923],
    [0.60724220, 0.40102839, 0.13941187],
    [0.61445161, 0.40186631, 0.14013536],
    [0.62166458, 0.40268153, 0.14097075],
    [0.62888073, 0.40347438, 0.14191891],
    [0.63609975, 0.40424519, 0.14298058],
    [0.64332130, 0.40499426, 0.14415631],
    [0.65054506, 0.40572192, 0.14544653],
    [0.65777074, 0.40642849, 0.14685155],
    [0.66499813, 0.40711420, 0.14837155],
    [0.67222686, 0.40777944, 0.15000670],
    [0.67945657, 0.40842454, 0.15175708],
    [0.68668695, 0.40904986, 0.15362274],
    [0.69391762, 0.40965576, 0.15560372],
    [0.70114845, 0.41024245, 0.15770005],
    [0.70837887, 0.41081044, 0.15991188],
    [0.71560837, 0.41136022, 0.16223944],
    [0.72283661, 0.41189213, 0.16468302],
    [0.73006311, 0.41240664, 0.16724311],
    [0.73728696, 0.41290454, 0.16992039],
    [0.74450787, 0.41338611, 0.17271575],
    [0.75172465, 0.41385239, 0.17563038],
    [0.75893666, 0.41430395, 0.17866580],
    [0.76614250, 0.41474200, 0.18182389],
    [0.77334135, 0.41516724, 0.18510703],
    [0.78053127, 0.41558134, 0.18851800],
    [0.78771077, 0.41598558, 0.19206029],
    [0.79487796, 0.41638158, 0.19573806],
    [0.80203018, 0.41677161, 0.19955616],
    [0.80916467, 0.41715810, 0.20352042],
    [0.81627808, 0.41754393, 0.20763775],
    [0.82336641, 0.41793260, 0.21191626],
    [0.83042481, 0.41832838, 0.21636549],
    [0.83744739, 0.41873650, 0.22099658],
    [0.84442740, 0.41916297, 0.22582291],
    [0.85135614, 0.41961561, 0.23085986],
    [0.85822307, 0.42010398, 0.23612549],
    [0.86501518, 0.42063999, 0.24164089],
    [0.87171687, 0.42123795, 0.24743117],
    [0.87830796, 0.42191663, 0.25352456],
    [0.88476392, 0.42269894, 0.25995402],
    [0.89105353, 0.42361441, 0.26675528],
    [0.89713870, 0.42469934, 0.27396697],
    [0.90297311, 0.42599833, 0.28162702],
    [0.90850263, 0.42756409, 0.28976751],
    [0.91366763, 0.42945556, 0.29840528],
    [0.91840936, 0.43173187, 0.30753127],
    [0.92268010, 0.43444246, 0.31710142],
    [0.92645438, 0.43761557, 0.32703485],
    [0.92973622, 0.44125030, 0.33722476],
    [0.93255776, 0.44531707, 0.34755792],
    [0.93496881, 0.44976688, 0.35793893],
    [0.93702770, 0.45454143, 0.36829025],
    [0.93879037, 0.45958348, 0.37856247],
    [0.94030466, 0.46484294, 0.38873049],
    [0.94161285, 0.47027591, 0.39877692],
    [0.94274802, 0.47584738, 0.40869798],
    [0.94373625, 0.48152948, 0.41849613],
    [0.94459927, 0.48729936, 0.42817485],
    [0.94535537, 0.49313811, 0.43773793],
    [0.94601805, 0.49903156, 0.44719269],
    [0.94659665, 0.50496942, 0.45654895],
    [0.94710340, 0.51094028, 0.46580810],
    [0.94754294, 0.51693861, 0.47498097],
    [0.94792325, 0.52295717, 0.48407057],
    [0.94825061, 0.52899034, 0.49308073],
    [0.94852981, 0.53503389, 0.50201594],
    [0.94876435, 0.54108475, 0.51088110],
    [0.94895662, 0.54714081, 0.51968145],
    [0.94910860, 0.55320041, 0.52842168],
    [0.94922934, 0.55925760, 0.53709655],
    [0.94931274, 0.56531615, 0.54571978],
    [0.94936957, 0.57136941, 0.55428294],
    [0.94939588, 0.57741995, 0.56279566],
    [0.94939385, 0.58346663, 0.57125933],
    [0.94936862, 0.58950665, 0.57967159],
    [0.94932104, 0.59553985, 0.58803490],
    [0.94925112, 0.60156661, 0.59635233],
    [0.94916065, 0.60758632, 0.60462461],
    [0.94905115, 0.61359854, 0.61285258],
    [0.94892393, 0.61960303, 0.62103711],
    [0.94878009, 0.62559967, 0.62917910],
    [0.94862057, 0.63158846, 0.63727947],
    [0.94844916, 0.63756791, 0.64533610],
    [0.94826642, 0.64353831, 0.65335011],
    [0.94807105, 0.64950092, 0.66132426],
    [0.94786345, 0.65545611, 0.66925949],
    [0.94764883, 0.66140178, 0.67715195],
    [0.94742779, 0.66733825, 0.68500229],
    [0.94719628, 0.67326821, 0.69281534],
    [0.94696326, 0.67918779, 0.70058375],
    [0.94672432, 0.68509983, 0.70831247],
    [0.94648171, 0.69100389, 0.71600025],
    [0.94623948, 0.69689864, 0.72364423],
    [0.94599436, 0.70278636, 0.73124796],
    [0.94575276, 0.70866465, 0.73880651],
    [0.94551208, 0.71453544, 0.74632267],
    [0.94527502, 0.72039816, 0.75379466],
    [0.94504581, 0.72625156, 0.76121950],
    [0.94481859, 0.73209905, 0.76860231],
    [0.94460694, 0.73793516, 0.77593272],
    [0.94440291, 0.74376425, 0.78321739],
    [0.94420783, 0.74958643, 0.79045556],
]

# Create ListedColormap object for this colormap
cmap = ListedColormap(cm_data, name="cmr.dusk", N=256)
cmap_r = cmap.reversed()

# Register (reversed) cmap in MPL
mpl.colormaps.register(cmap=cmap)
mpl.colormaps.register(cmap=cmap_r)
