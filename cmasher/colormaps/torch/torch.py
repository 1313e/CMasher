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
    [0.00018674, 0.00024309, 0.00032846],
    [0.00061719, 0.00084935, 0.00120490],
    [0.00122069, 0.00177144, 0.00262798],
    [0.00195825, 0.00298986, 0.00462279],
    [0.00280055, 0.00449304, 0.00722338],
    [0.00372475, 0.00627288, 0.01046542],
    [0.00471098, 0.00832341, 0.01438856],
    [0.00574032, 0.01064008, 0.01903864],
    [0.00679734, 0.01321885, 0.02445963],
    [0.00786757, 0.01605625, 0.03069891],
    [0.00893480, 0.01914941, 0.03781465],
    [0.00998839, 0.02249507, 0.04557023],
    [0.01101400, 0.02609050, 0.05339050],
    [0.01200070, 0.02993262, 0.06127602],
    [0.01293701, 0.03401834, 0.06923620],
    [0.01381183, 0.03834435, 0.07728004],
    [0.01461545, 0.04282425, 0.08541390],
    [0.01533825, 0.04723936, 0.09364494],
    [0.01597013, 0.05159511, 0.10198189],
    [0.01650594, 0.05589322, 0.11042506],
    [0.01693189, 0.06013508, 0.11899186],
    [0.01724649, 0.06432140, 0.12767826],
    [0.01744333, 0.06845260, 0.13649094],
    [0.01751159, 0.07252853, 0.14544509],
    [0.01745185, 0.07654879, 0.15453837],
    [0.01726056, 0.08051255, 0.16377741],
    [0.01693538, 0.08441857, 0.17316890],
    [0.01647536, 0.08826521, 0.18271955],
    [0.01587933, 0.09205024, 0.19243892],
    [0.01515256, 0.09577134, 0.20232953],
    [0.01430001, 0.09942560, 0.21239768],
    [0.01332910, 0.10300963, 0.22264964],
    [0.01224907, 0.10651944, 0.23309309],
    [0.01107172, 0.10995036, 0.24373667],
    [0.00981597, 0.11329757, 0.25458355],
    [0.00850361, 0.11655554, 0.26563866],
    [0.00716035, 0.11971791, 0.27690797],
    [0.00581125, 0.12277618, 0.28840789],
    [0.00450280, 0.12572419, 0.30012860],
    [0.00327023, 0.12855046, 0.31209254],
    [0.00217453, 0.13124687, 0.32429006],
    [0.00127540, 0.13380111, 0.33673116],
    [0.00064532, 0.13619940, 0.34942367],
    [0.00037501, 0.13842855, 0.36236243],
    [0.00056765, 0.14047266, 0.37554654],
    [0.00134404, 0.14231344, 0.38897475],
    [0.00284733, 0.14393114, 0.40263945],
    [0.00524606, 0.14530762, 0.41651536],
    [0.00873427, 0.14641697, 0.43059260],
    [0.01353836, 0.14723942, 0.44482610],
    [0.01991589, 0.14775390, 0.45916396],
    [0.02815668, 0.14794231, 0.47353456],
    [0.03857510, 0.14779542, 0.48783537],
    [0.05054940, 0.14731894, 0.50192749],
    [0.06293976, 0.14654165, 0.51563197],
    [0.07567503, 0.14552303, 0.52873415],
    [0.08863747, 0.14435984, 0.54099536],
    [0.10167044, 0.14318579, 0.55217881],
    [0.11460358, 0.14215266, 0.56209426],
    [0.12727798, 0.14140630, 0.57062998],
    [0.13957016, 0.14106174, 0.57776658],
    [0.15140520, 0.14118753, 0.58356718],
    [0.16275559, 0.14180441, 0.58815099],
    [0.17362354, 0.14289807, 0.59166383],
    [0.18403847, 0.14442672, 0.59425747],
    [0.19403727, 0.14633755, 0.59607508],
    [0.20366121, 0.14857333, 0.59724520],
    [0.21295163, 0.15107815, 0.59787931],
    [0.22194634, 0.15380100, 0.59807267],
    [0.23067894, 0.15669707, 0.59790604],
    [0.23918109, 0.15972722, 0.59744604],
    [0.24747949, 0.16285884, 0.59674876],
    [0.25559602, 0.16606519, 0.59586227],
    [0.26355190, 0.16932369, 0.59482497],
    [0.27136484, 0.17261610, 0.59366947],
    [0.27905018, 0.17592772, 0.59242306],
    [0.28662135, 0.17924670, 0.59110859],
    [0.29408960, 0.18256370, 0.58974577],
    [0.30146622, 0.18587097, 0.58834956],
    [0.30876068, 0.18916254, 0.58693294],
    [0.31598070, 0.19243386, 0.58550761],
    [0.32313391, 0.19568127, 0.58408248],
    [0.33022762, 0.19890184, 0.58266421],
    [0.33726695, 0.20209368, 0.58126028],
    [0.34425866, 0.20525493, 0.57987398],
    [0.35120693, 0.20838466, 0.57851055],
    [0.35811722, 0.21148189, 0.57717197],
    [0.36499373, 0.21454609, 0.57586076],
    [0.37184029, 0.21757699, 0.57457888],
    [0.37866126, 0.22057427, 0.57332655],
    [0.38545996, 0.22353794, 0.57210464],
    [0.39223966, 0.22646807, 0.57091337],
    [0.39900390, 0.22936465, 0.56975182],
    [0.40575567, 0.23222785, 0.56861929],
    [0.41249767, 0.23505791, 0.56751499],
    [0.41923272, 0.23785502, 0.56643740],
    [0.42596355, 0.24061936, 0.56538467],
    [0.43269263, 0.24335117, 0.56435491],
    [0.43942233, 0.24605070, 0.56334601],
    [0.44615480, 0.24871822, 0.56235578],
    [0.45289226, 0.25135399, 0.56138159],
    [0.45963678, 0.25395822, 0.56042065],
    [0.46639030, 0.25653118, 0.55947011],
    [0.47315464, 0.25907314, 0.55852696],
    [0.47993153, 0.26158438, 0.55758806],
    [0.48672256, 0.26406518, 0.55665014],
    [0.49352925, 0.26651586, 0.55570984],
    [0.50035303, 0.26893672, 0.55476364],
    [0.50719518, 0.27132810, 0.55380795],
    [0.51405691, 0.27369038, 0.55283914],
    [0.52093926, 0.27602395, 0.55185350],
    [0.52784321, 0.27832923, 0.55084727],
    [0.53476959, 0.28060670, 0.54981663],
    [0.54171918, 0.28285684, 0.54875768],
    [0.54869257, 0.28508019, 0.54766658],
    [0.55569025, 0.28727737, 0.54653950],
    [0.56271257, 0.28944902, 0.54537258],
    [0.56975981, 0.29159583, 0.54416199],
    [0.57683207, 0.29371855, 0.54290392],
    [0.58392947, 0.29581796, 0.54159445],
    [0.59105191, 0.29789492, 0.54022986],
    [0.59819909, 0.29995039, 0.53880661],
    [0.60537066, 0.30198537, 0.53732113],
    [0.61256618, 0.30400095, 0.53576994],
    [0.61978528, 0.30599811, 0.53414922],
    [0.62702714, 0.30797815, 0.53245593],
    [0.63429091, 0.30994238, 0.53068698],
    [0.64157567, 0.31189215, 0.52883933],
    [0.64888083, 0.31382865, 0.52690924],
    [0.65620487, 0.31575361, 0.52489464],
    [0.66354654, 0.31766864, 0.52279290],
    [0.67090504, 0.31957510, 0.52060047],
    [0.67827849, 0.32147501, 0.51831584],
    [0.68566547, 0.32337014, 0.51593655],
    [0.69306469, 0.32526223, 0.51345982],
    [0.70047391, 0.32715362, 0.51088483],
    [0.70789208, 0.32904596, 0.50820811],
    [0.71531651, 0.33094193, 0.50542973],
    [0.72274598, 0.33284339, 0.50254642],
    [0.73017764, 0.33475320, 0.49955857],
    [0.73761008, 0.33667343, 0.49646310],
    [0.74504037, 0.33860712, 0.49326047],
    [0.75246632, 0.34055692, 0.48994927],
    [0.75988565, 0.34252558, 0.48652812],
    [0.76729532, 0.34451641, 0.48299749],
    [0.77469260, 0.34653258, 0.47935685],
    [0.78207495, 0.34857724, 0.47560502],
    [0.78943906, 0.35065406, 0.47174257],
    [0.79678167, 0.35276680, 0.46776985],
    [0.80409941, 0.35491935, 0.46368715],
    [0.81138874, 0.35711579, 0.45949501],
    [0.81864590, 0.35936045, 0.45519421],
    [0.82586689, 0.36165787, 0.45078585],
    [0.83304748, 0.36401286, 0.44627135],
    [0.84018318, 0.36643047, 0.44165250],
    [0.84726936, 0.36891593, 0.43693080],
    [0.85430107, 0.37147480, 0.43210830],
    [0.86127261, 0.37411315, 0.42718907],
    [0.86817848, 0.37683705, 0.42217546],
    [0.87501258, 0.37965302, 0.41707127],
    [0.88176832, 0.38256796, 0.41188129],
    [0.88843866, 0.38558908, 0.40661095],
    [0.89501643, 0.38872382, 0.40126470],
    [0.90149337, 0.39198022, 0.39585092],
    [0.90786100, 0.39536651, 0.39037728],
    [0.91411023, 0.39889127, 0.38485280],
    [0.92023130, 0.40256346, 0.37928813],
    [0.92621378, 0.40639229, 0.37369574],
    [0.93204657, 0.41038724, 0.36809018],
    [0.93771802, 0.41455801, 0.36248652],
    [0.94321560, 0.41891431, 0.35690498],
    [0.94852631, 0.42346593, 0.35136636],
    [0.95363654, 0.42822236, 0.34589628],
    [0.95853225, 0.43319287, 0.34052196],
    [0.96319906, 0.43838608, 0.33527536],
    [0.96762255, 0.44380966, 0.33019262],
    [0.97178846, 0.44947023, 0.32531310],
    [0.97568305, 0.45537281, 0.32068061],
    [0.97929365, 0.46152034, 0.31634312],
    [0.98260883, 0.46791377, 0.31235074],
    [0.98561917, 0.47455118, 0.30875671],
    [0.98831751, 0.48142796, 0.30561484],
    [0.99069973, 0.48853619, 0.30297922],
    [0.99276472, 0.49586504, 0.30090129],
    [0.99451475, 0.50340077, 0.29942856],
    [0.99595568, 0.51112687, 0.29860285],
    [0.99709661, 0.51902474, 0.29845833],
    [0.99794961, 0.52707424, 0.29902034],
    [0.99852928, 0.53525430, 0.30030464],
    [0.99885217, 0.54354361, 0.30231724],
    [0.99893646, 0.55192099, 0.30505475],
    [0.99880078, 0.56036642, 0.30850510],
    [0.99846401, 0.56886110, 0.31264890],
    [0.99794556, 0.57738725, 0.31746061],
    [0.99726313, 0.58592964, 0.32291032],
    [0.99643514, 0.59447366, 0.32896456],
    [0.99547765, 0.60300750, 0.33558838],
    [0.99440644, 0.61152037, 0.34274579],
    [0.99323628, 0.62000305, 0.35040078],
    [0.99198083, 0.62844770, 0.35851810],
    [0.99065270, 0.63684776, 0.36706378],
    [0.98926348, 0.64519784, 0.37600549],
    [0.98782383, 0.65349353, 0.38531279],
    [0.98634388, 0.66173108, 0.39495690],
    [0.98483345, 0.66990723, 0.40491060],
    [0.98330040, 0.67802014, 0.41514979],
    [0.98175370, 0.68606748, 0.42565062],
    [0.98020064, 0.69404809, 0.43639208],
    [0.97864823, 0.70196105, 0.44735464],
    [0.97710347, 0.70980558, 0.45851987],
    [0.97557296, 0.71758122, 0.46987077],
    [0.97406291, 0.72528774, 0.48139162],
    [0.97257924, 0.73292519, 0.49306792],
    [0.97112757, 0.74049376, 0.50488623],
    [0.96971327, 0.74799382, 0.51683411],
    [0.96834148, 0.75542588, 0.52890000],
    [0.96701711, 0.76279055, 0.54107315],
    [0.96574602, 0.77008809, 0.55334211],
    [0.96453202, 0.77731963, 0.56569846],
    [0.96338006, 0.78448582, 0.57813269],
    [0.96229481, 0.79158745, 0.59063598],
    [0.96128047, 0.79862551, 0.60320042],
    [0.96034121, 0.80560095, 0.61581843],
    [0.95948184, 0.81251453, 0.62848172],
    [0.95870567, 0.81936753, 0.64118430],
    [0.95801686, 0.82616092, 0.65391920],
    [0.95742003, 0.83289549, 0.66667882],
    [0.95691841, 0.83957252, 0.67945777],
    [0.95651582, 0.84619305, 0.69224991],
    [0.95621603, 0.85275815, 0.70504922],
    [0.95602277, 0.85926885, 0.71784986],
    [0.95593972, 0.86572619, 0.73064613],
    [0.95597055, 0.87213122, 0.74343247],
    [0.95611893, 0.87848492, 0.75620336],
    [0.95638859, 0.88478826, 0.76895337],
    [0.95678334, 0.89104214, 0.78167708],
    [0.95730717, 0.89724738, 0.79436904],
    [0.95796428, 0.90340468, 0.80702373],
    [0.95875958, 0.90951453, 0.81963494],
    [0.95969806, 0.91557730, 0.83219698],
    [0.96078541, 0.92159309, 0.84470397],
    [0.96202865, 0.92756153, 0.85714925],
    [0.96343698, 0.93348153, 0.86952433],
    [0.96502132, 0.93935129, 0.88182121],
    [0.96679684, 0.94516758, 0.89402922],
    [0.96878590, 0.95092490, 0.90613208],
    [0.97101994, 0.95661475, 0.91810827],
    [0.97354759, 0.96222377, 0.92991790],
    [0.97643957, 0.96773343, 0.94148791],
    [0.97978302, 0.97312565, 0.95268046],
    [0.98362318, 0.97840750, 0.96327718],
    [0.98782923, 0.98365208, 0.97309516],
    [0.99208207, 0.98897571, 0.98224704],
    [0.99614668, 0.99443276, 0.99111154],
    [1.00000000, 1.00000000, 1.00000000],
]

# Create ListedColormap object for this colormap
cmap = ListedColormap(cm_data, name="cmr.torch", N=256)
cmap_r = cmap.reversed()

# Register (reversed) cmap in MPL
mpl.colormaps.register(cmap=cmap)
mpl.colormaps.register(cmap=cmap_r)
