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
    [0.00017349, 0.00019533, 0.00025655],
    [0.00059221, 0.00067750, 0.00092984],
    [0.00121203, 0.00140234, 0.00200731],
    [0.00201644, 0.00234817, 0.00349882],
    [0.00299956, 0.00349901, 0.00541963],
    [0.00416255, 0.00484105, 0.00778710],
    [0.00551226, 0.00636121, 0.01061897],
    [0.00706076, 0.00804639, 0.01393240],
    [0.00882503, 0.00988326, 0.01774150],
    [0.01082647, 0.01185807, 0.02205744],
    [0.01309032, 0.01395686, 0.02688592],
    [0.01564467, 0.01616578, 0.03222658],
    [0.01851927, 0.01847146, 0.03807261],
    [0.02174414, 0.02086148, 0.04423843],
    [0.02534829, 0.02332468, 0.05031776],
    [0.02935885, 0.02585131, 0.05630031],
    [0.03380051, 0.02843306, 0.06217914],
    [0.03869539, 0.03106288, 0.06794949],
    [0.04391432, 0.03373472, 0.07360907],
    [0.04919604, 0.03644326, 0.07915750],
    [0.05454023, 0.03918377, 0.08459591],
    [0.05994022, 0.04191092, 0.08992649],
    [0.06539041, 0.04454725, 0.09515237],
    [0.07088571, 0.04710653, 0.10027668],
    [0.07642223, 0.04959208, 0.10530298],
    [0.08199630, 0.05200710, 0.11023442],
    [0.08760543, 0.05435397, 0.11507442],
    [0.09324732, 0.05663497, 0.11982592],
    [0.09892011, 0.05885206, 0.12449165],
    [0.10462229, 0.06100695, 0.12907411],
    [0.11035269, 0.06310110, 0.13357554],
    [0.11611032, 0.06513579, 0.13799796],
    [0.12189405, 0.06711239, 0.14234302],
    [0.12770344, 0.06903174, 0.14661238],
    [0.13353792, 0.07089473, 0.15080742],
    [0.13939664, 0.07270240, 0.15492926],
    [0.14527950, 0.07445523, 0.15897902],
    [0.15118585, 0.07615405, 0.16295756],
    [0.15711534, 0.07779942, 0.16686569],
    [0.16306781, 0.07939174, 0.17070409],
    [0.16904279, 0.08093159, 0.17447334],
    [0.17503989, 0.08241944, 0.17817391],
    [0.18105903, 0.08385552, 0.18180624],
    [0.18709992, 0.08524014, 0.18537066],
    [0.19316229, 0.08657359, 0.18886747],
    [0.19924590, 0.08785609, 0.19229686],
    [0.20535051, 0.08908784, 0.19565901],
    [0.21147591, 0.09026896, 0.19895405],
    [0.21762187, 0.09139956, 0.20218203],
    [0.22378819, 0.09247971, 0.20534299],
    [0.22997467, 0.09350942, 0.20843692],
    [0.23618110, 0.09448869, 0.21146377],
    [0.24240729, 0.09541747, 0.21442345],
    [0.24865303, 0.09629569, 0.21731585],
    [0.25491815, 0.09712324, 0.22014081],
    [0.26120243, 0.09789997, 0.22289815],
    [0.26750567, 0.09862571, 0.22558766],
    [0.27382768, 0.09930026, 0.22820910],
    [0.28016821, 0.09992344, 0.23076222],
    [0.28652709, 0.10049495, 0.23324670],
    [0.29290412, 0.10101448, 0.23566222],
    [0.29929909, 0.10148169, 0.23800843],
    [0.30571178, 0.10189625, 0.24028496],
    [0.31214195, 0.10225778, 0.24249139],
    [0.31858937, 0.10256590, 0.24462733],
    [0.32505382, 0.10282011, 0.24669229],
    [0.33153506, 0.10301998, 0.24868579],
    [0.33803282, 0.10316499, 0.25060735],
    [0.34454684, 0.10325464, 0.25245644],
    [0.35107688, 0.10328834, 0.25423248],
    [0.35762262, 0.10326554, 0.25593491],
    [0.36418378, 0.10318562, 0.25756313],
    [0.37076004, 0.10304797, 0.25911650],
    [0.37735107, 0.10285192, 0.26059439],
    [0.38395657, 0.10259675, 0.26199608],
    [0.39057617, 0.10228176, 0.26332089],
    [0.39720948, 0.10190626, 0.26456809],
    [0.40385611, 0.10146948, 0.26573694],
    [0.41051564, 0.10097068, 0.26682666],
    [0.41718763, 0.10040907, 0.26783645],
    [0.42387163, 0.09978383, 0.26876549],
    [0.43056722, 0.09909406, 0.26961286],
    [0.43727383, 0.09833905, 0.27037774],
    [0.44399090, 0.09751796, 0.27105923],
    [0.45071788, 0.09662999, 0.27165640],
    [0.45745416, 0.09567434, 0.27216832],
    [0.46419910, 0.09465021, 0.27259402],
    [0.47095201, 0.09355687, 0.27293249],
    [0.47771219, 0.09239358, 0.27318273],
    [0.48447885, 0.09115970, 0.27334370],
    [0.49125120, 0.08985466, 0.27341437],
    [0.49802837, 0.08847796, 0.27339366],
    [0.50480943, 0.08702925, 0.27328050],
    [0.51159341, 0.08550832, 0.27307380],
    [0.51837934, 0.08391501, 0.27277238],
    [0.52516613, 0.08224945, 0.27237510],
    [0.53195254, 0.08051228, 0.27188094],
    [0.53873730, 0.07870435, 0.27128882],
    [0.54551907, 0.07682692, 0.27059766],
    [0.55229662, 0.07488124, 0.26980608],
    [0.55906835, 0.07286990, 0.26891316],
    [0.56583253, 0.07079626, 0.26791804],
    [0.57258771, 0.06866360, 0.26681931],
    [0.57933193, 0.06647729, 0.26561621],
    [0.58606325, 0.06424367, 0.26430788],
    [0.59277979, 0.06197002, 0.26289314],
    [0.59947918, 0.05966658, 0.26137160],
    [0.60615929, 0.05734455, 0.25974222],
    [0.61281759, 0.05501854, 0.25800460],
    [0.61945139, 0.05270628, 0.25615853],
    [0.62605826, 0.05042744, 0.25420305],
    [0.63263505, 0.04820781, 0.25213867],
    [0.63917874, 0.04607650, 0.24996544],
    [0.64568614, 0.04406738, 0.24768365],
    [0.65215403, 0.04221892, 0.24529361],
    [0.65857878, 0.04057534, 0.24279654],
    [0.66495673, 0.03917498, 0.24019368],
    [0.67128412, 0.03809881, 0.23748664],
    [0.67755703, 0.03738500, 0.23467744],
    [0.68377146, 0.03707101, 0.23176853],
    [0.68992334, 0.03719575, 0.22876282],
    [0.69600854, 0.03779932, 0.22566367],
    [0.70202299, 0.03892272, 0.22247481],
    [0.70796252, 0.04060518, 0.21920081],
    [0.71382312, 0.04281527, 0.21584653],
    [0.71960090, 0.04555099, 0.21241731],
    [0.72529217, 0.04879068, 0.20891881],
    [0.73089342, 0.05250438, 0.20535724],
    [0.73640145, 0.05665649, 0.20173920],
    [0.74181339, 0.06120823, 0.19807139],
    [0.74712677, 0.06611983, 0.19436077],
    [0.75233948, 0.07135215, 0.19061439],
    [0.75744991, 0.07686772, 0.18683921],
    [0.76245686, 0.08263149, 0.18304222],
    [0.76735964, 0.08861113, 0.17923010],
    [0.77215800, 0.09477718, 0.17540912],
    [0.77685215, 0.10110303, 0.17158523],
    [0.78144269, 0.10756477, 0.16776400],
    [0.78593066, 0.11414097, 0.16395065],
    [0.79031742, 0.12081273, 0.16014938],
    [0.79460464, 0.12756326, 0.15636407],
    [0.79879424, 0.13437776, 0.15259798],
    [0.80288839, 0.14124323, 0.14885380],
    [0.80688938, 0.14814834, 0.14513362],
    [0.81079969, 0.15508309, 0.14143925],
    [0.81462184, 0.16203887, 0.13777184],
    [0.81835836, 0.16900849, 0.13413165],
    [0.82201181, 0.17598572, 0.13051869],
    [0.82558491, 0.18296465, 0.12693377],
    [0.82908005, 0.18994124, 0.12337539],
    [0.83249982, 0.19691138, 0.11984331],
    [0.83584655, 0.20387208, 0.11633606],
    [0.83912274, 0.21082034, 0.11285311],
    [0.84233043, 0.21775456, 0.10939203],
    [0.84547192, 0.22467268, 0.10595188],
    [0.84854935, 0.23157321, 0.10253126],
    [0.85156453, 0.23845546, 0.09912776],
    [0.85451935, 0.24531865, 0.09573962],
    [0.85741560, 0.25216222, 0.09236499],
    [0.86025494, 0.25898585, 0.08900196],
    [0.86303895, 0.26578944, 0.08564856],
    [0.86576909, 0.27257301, 0.08230278],
    [0.86844672, 0.27933676, 0.07896256],
    [0.87107311, 0.28608100, 0.07562583],
    [0.87364960, 0.29280584, 0.07229109],
    [0.87617742, 0.29951158, 0.06895674],
    [0.87865734, 0.30619915, 0.06561995],
    [0.88109037, 0.31286901, 0.06227903],
    [0.88347791, 0.31952107, 0.05893377],
    [0.88582012, 0.32615688, 0.05558035],
    [0.88811848, 0.33277612, 0.05221941],
    [0.89037312, 0.33938027, 0.04884759],
    [0.89258534, 0.34596912, 0.04546571],
    [0.89475509, 0.35254428, 0.04207040],
    [0.89688378, 0.35910531, 0.03865698],
    [0.89897132, 0.36565369, 0.03535486],
    [0.90101819, 0.37219010, 0.03221081],
    [0.90302556, 0.37871430, 0.02922685],
    [0.90499322, 0.38522773, 0.02640095],
    [0.90692160, 0.39173097, 0.02373367],
    [0.90881111, 0.39822457, 0.02122584],
    [0.91066237, 0.40470882, 0.01887928],
    [0.91247553, 0.41118450, 0.01669477],
    [0.91425074, 0.41765232, 0.01467355],
    [0.91598827, 0.42411283, 0.01281748],
    [0.91768836, 0.43056659, 0.01112866],
    [0.91935119, 0.43701414, 0.00960944],
    [0.92097696, 0.44345602, 0.00826240],
    [0.92256581, 0.44989274, 0.00709035],
    [0.92411787, 0.45632484, 0.00609634],
    [0.92563324, 0.46275282, 0.00528364],
    [0.92711202, 0.46917718, 0.00465574],
    [0.92855425, 0.47559841, 0.00421637],
    [0.92995998, 0.48201699, 0.00396944],
    [0.93132934, 0.48843330, 0.00391931],
    [0.93266260, 0.49484757, 0.00407079],
    [0.93395944, 0.50126052, 0.00442786],
    [0.93521984, 0.50767260, 0.00499531],
    [0.93644377, 0.51408422, 0.00577811],
    [0.93763131, 0.52049570, 0.00678164],
    [0.93878286, 0.52690705, 0.00801202],
    [0.93989780, 0.53331914, 0.00947390],
    [0.94097604, 0.53973234, 0.01117305],
    [0.94201800, 0.54614663, 0.01311613],
    [0.94302350, 0.55256245, 0.01530913],
    [0.94399205, 0.55898045, 0.01775781],
    [0.94492407, 0.56540055, 0.02046936],
    [0.94581941, 0.57182313, 0.02345037],
    [0.94667745, 0.57824886, 0.02670705],
    [0.94749906, 0.58467735, 0.03024754],
    [0.94828330, 0.59110947, 0.03407803],
    [0.94903036, 0.59754529, 0.03820619],
    [0.94974035, 0.60398491, 0.04256985],
    [0.95041255, 0.61042902, 0.04695588],
    [0.95104780, 0.61687720, 0.05136417],
    [0.95164477, 0.62333052, 0.05579248],
    [0.95220472, 0.62978827, 0.06024077],
    [0.95272605, 0.63625167, 0.06470738],
    [0.95321010, 0.64271996, 0.06919261],
    [0.95365529, 0.64919431, 0.07369536],
    [0.95406283, 0.65567405, 0.07821597],
    [0.95443136, 0.66216015, 0.08275377],
    [0.95476168, 0.66865224, 0.08730898],
    [0.95505298, 0.67515090, 0.09188131],
    [0.95530533, 0.68165618, 0.09647082],
    [0.95551873, 0.68816819, 0.10107749],
    [0.95569231, 0.69468751, 0.10570120],
    [0.95582710, 0.70121362, 0.11034214],
    [0.95592170, 0.70774740, 0.11500014],
    [0.95597639, 0.71428878, 0.11967526],
    [0.95599118, 0.72083780, 0.12436751],
    [0.95596516, 0.72739504, 0.12907682],
    [0.95589879, 0.73396029, 0.13380322],
    [0.95579151, 0.74053390, 0.13854665],
    [0.95564270, 0.74711627, 0.14330709],
    [0.95545271, 0.75370724, 0.14808447],
    [0.95522092, 0.76030718, 0.15287873],
    [0.95494670, 0.76691644, 0.15768983],
    [0.95463009, 0.77353503, 0.16251766],
    [0.95427085, 0.78016311, 0.16736214],
    [0.95386807, 0.78680113, 0.17222320],
    [0.95342137, 0.79344930, 0.17710075],
    [0.95293106, 0.80010747, 0.18199461],
    [0.95239596, 0.80677622, 0.18690475],
    [0.95181553, 0.81345580, 0.19183105],
    [0.95118934, 0.82014641, 0.19677340],
    [0.95051739, 0.82684801, 0.20173162],
    [0.94979844, 0.83356118, 0.20670566],
    [0.94903187, 0.84028615, 0.21169543],
    [0.94821703, 0.84702320, 0.21670082],
    [0.94735371, 0.85377234, 0.22172164],
    [0.94644078, 0.86053406, 0.22675786],
    [0.94547732, 0.86730868, 0.23180941],
    [0.94446250, 0.87409648, 0.23687620],
    [0.94339547, 0.88089777, 0.24195816],
]

# Create ListedColormap object for this colormap
cmap = ListedColormap(cm_data, name="cmr.ember", N=256)
cmap_r = cmap.reversed()

# Register (reversed) cmap in MPL
register_cmap(cmap=cmap)
register_cmap(cmap=cmap_r)
