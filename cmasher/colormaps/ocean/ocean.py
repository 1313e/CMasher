# %% IMPORTS
# Package imports
from matplotlib.cm import register_cmap
from matplotlib.colors import ListedColormap

# All declaration
__all__ = ['cmap']

# Author declaration
__author__ = "Ellert van der Velden (@1313e)"

# Package declaration
__package__ = 'cmasher'


# %% GLOBALS AND DEFINITIONS
# Type of this colormap (according to viscm)
cm_type = "linear"

# RGB-values of this colormap
cm_data = [[0.11036298, 0.00169078, 0.25302591],
           [0.11229459, 0.00603321, 0.25753772],
           [0.11418039, 0.01060839, 0.26205180],
           [0.11601976, 0.01542029, 0.26656554],
           [0.11781256, 0.02047271, 0.27107617],
           [0.11955872, 0.02576938, 0.27558127],
           [0.12125791, 0.03131406, 0.28007901],
           [0.12291032, 0.03711032, 0.28456726],
           [0.12451564, 0.04306596, 0.28904459],
           [0.12607398, 0.04880321, 0.29350935],
           [0.12758536, 0.05434134, 0.29796010],
           [0.12904948, 0.05971483, 0.30239578],
           [0.13046681, 0.06494994, 0.30681480],
           [0.13183678, 0.07006769, 0.31121644],
           [0.13315975, 0.07508463, 0.31559936],
           [0.13443582, 0.08001428, 0.31996246],
           [0.13566461, 0.08486802, 0.32430500],
           [0.13684632, 0.08965512, 0.32862590],
           [0.13798112, 0.09438344, 0.33292414],
           [0.13906902, 0.09905971, 0.33719884],
           [0.14010980, 0.10368981, 0.34144923],
           [0.14110359, 0.10827871, 0.34567440],
           [0.14205060, 0.11283068, 0.34987342],
           [0.14295089, 0.11734954, 0.35404547],
           [0.14380456, 0.12183862, 0.35818971],
           [0.14461171, 0.12630089, 0.36230534],
           [0.14537250, 0.13073893, 0.36639155],
           [0.14608708, 0.13515508, 0.37044756],
           [0.14675568, 0.13955140, 0.37447257],
           [0.14737854, 0.14392971, 0.37846582],
           [0.14795595, 0.14829167, 0.38242655],
           [0.14848823, 0.15263873, 0.38635403],
           [0.14897577, 0.15697221, 0.39024752],
           [0.14941899, 0.16129329, 0.39410632],
           [0.14981839, 0.16560300, 0.39792975],
           [0.15017448, 0.16990228, 0.40171715],
           [0.15048788, 0.17419196, 0.40546789],
           [0.15075895, 0.17847288, 0.40918140],
           [0.15098858, 0.18274564, 0.41285707],
           [0.15117765, 0.18701078, 0.41649434],
           [0.15132702, 0.19126881, 0.42009270],
           [0.15143729, 0.19552028, 0.42365170],
           [0.15150958, 0.19976554, 0.42717089],
           [0.15154514, 0.20400486, 0.43064985],
           [0.15154485, 0.20823862, 0.43408825],
           [0.15150992, 0.21246704, 0.43748576],
           [0.15144194, 0.21669026, 0.44084210],
           [0.15134177, 0.22090856, 0.44415707],
           [0.15121131, 0.22512197, 0.44743047],
           [0.15105189, 0.22933064, 0.45066217],
           [0.15086511, 0.23353464, 0.45385211],
           [0.15065279, 0.23773398, 0.45700024],
           [0.15041652, 0.24192875, 0.46010658],
           [0.15015834, 0.24611888, 0.46317121],
           [0.14988003, 0.25030442, 0.46619422],
           [0.14958370, 0.25448531, 0.46917580],
           [0.14927143, 0.25866151, 0.47211617],
           [0.14894527, 0.26283299, 0.47501556],
           [0.14860770, 0.26699964, 0.47787431],
           [0.14826061, 0.27116148, 0.48069273],
           [0.14790675, 0.27531836, 0.48347126],
           [0.14754834, 0.27947023, 0.48621032],
           [0.14718783, 0.28361704, 0.48891036],
           [0.14682792, 0.28775866, 0.49157193],
           [0.14647096, 0.29189507, 0.49419555],
           [0.14611965, 0.29602617, 0.49678180],
           [0.14577671, 0.30015187, 0.49933131],
           [0.14544466, 0.30427214, 0.50184468],
           [0.14512624, 0.30838691, 0.50432260],
           [0.14482421, 0.31249611, 0.50676574],
           [0.14454126, 0.31659970, 0.50917482],
           [0.14427999, 0.32069765, 0.51155052],
           [0.14404324, 0.32478990, 0.51389361],
           [0.14383368, 0.32887643, 0.51620483],
           [0.14365391, 0.33295724, 0.51848492],
           [0.14350657, 0.33703232, 0.52073465],
           [0.14339432, 0.34110164, 0.52295479],
           [0.14331970, 0.34516522, 0.52514612],
           [0.14328515, 0.34922308, 0.52730938],
           [0.14329311, 0.35327524, 0.52944536],
           [0.14334599, 0.35732173, 0.53155482],
           [0.14344605, 0.36136258, 0.53363854],
           [0.14359550, 0.36539784, 0.53569725],
           [0.14379638, 0.36942758, 0.53773169],
           [0.14405074, 0.37345185, 0.53974261],
           [0.14436051, 0.37747071, 0.54173074],
           [0.14472745, 0.38148424, 0.54369680],
           [0.14515323, 0.38549252, 0.54564147],
           [0.14563938, 0.38949565, 0.54756543],
           [0.14618737, 0.39349370, 0.54946937],
           [0.14679849, 0.39748677, 0.55135394],
           [0.14747394, 0.40147496, 0.55321979],
           [0.14821476, 0.40545839, 0.55506753],
           [0.14902183, 0.40943715, 0.55689775],
           [0.14989598, 0.41341137, 0.55871106],
           [0.15083789, 0.41738115, 0.56050803],
           [0.15184810, 0.42134661, 0.56228920],
           [0.15292704, 0.42530787, 0.56405511],
           [0.15407502, 0.42926506, 0.56580628],
           [0.15529223, 0.43321829, 0.56754318],
           [0.15657875, 0.43716769, 0.56926630],
           [0.15793461, 0.44111338, 0.57097610],
           [0.15935970, 0.44505549, 0.57267302],
           [0.16085384, 0.44899414, 0.57435748],
           [0.16241677, 0.45292945, 0.57602988],
           [0.16404815, 0.45686154, 0.57769062],
           [0.16574758, 0.46079053, 0.57934004],
           [0.16751459, 0.46471656, 0.58097850],
           [0.16934866, 0.46863973, 0.58260632],
           [0.17124925, 0.47256015, 0.58422382],
           [0.17321580, 0.47647795, 0.58583130],
           [0.17524768, 0.48039322, 0.58742905],
           [0.17734425, 0.48430608, 0.58901731],
           [0.17950488, 0.48821663, 0.59059635],
           [0.18172891, 0.49212496, 0.59216639],
           [0.18401567, 0.49603117, 0.59372765],
           [0.18636453, 0.49993535, 0.59528034],
           [0.18877485, 0.50383759, 0.59682463],
           [0.19124600, 0.50773796, 0.59836071],
           [0.19377738, 0.51163653, 0.59988874],
           [0.19636843, 0.51553338, 0.60140886],
           [0.19901859, 0.51942856, 0.60292121],
           [0.20172736, 0.52332213, 0.60442591],
           [0.20449428, 0.52721414, 0.60592309],
           [0.20731892, 0.53110462, 0.60741283],
           [0.21020090, 0.53499361, 0.60889524],
           [0.21313989, 0.53888113, 0.61037040],
           [0.21613558, 0.54276720, 0.61183834],
           [0.21918777, 0.54665182, 0.61329914],
           [0.22229631, 0.55053498, 0.61475288],
           [0.22546108, 0.55441667, 0.61619963],
           [0.22868205, 0.55829685, 0.61763942],
           [0.23195924, 0.56217550, 0.61907231],
           [0.23529267, 0.56605258, 0.62049821],
           [0.23868256, 0.56992800, 0.62191727],
           [0.24212914, 0.57380170, 0.62332955],
           [0.24563267, 0.57767357, 0.62473500],
           [0.24919352, 0.58154354, 0.62613362],
           [0.25281216, 0.58541146, 0.62752556],
           [0.25648909, 0.58927720, 0.62891076],
           [0.26022491, 0.59314062, 0.63028927],
           [0.26402031, 0.59700151, 0.63166124],
           [0.26787604, 0.60085972, 0.63302651],
           [0.27179297, 0.60471500, 0.63438542],
           [0.27577199, 0.60856714, 0.63573775],
           [0.27981416, 0.61241587, 0.63708388],
           [0.28392056, 0.61626091, 0.63842373],
           [0.28809239, 0.62010194, 0.63975752],
           [0.29233093, 0.62393864, 0.64108550],
           [0.29663759, 0.62777064, 0.64240764],
           [0.30101382, 0.63159754, 0.64372434],
           [0.30546117, 0.63541892, 0.64503589],
           [0.30998130, 0.63923432, 0.64634259],
           [0.31457598, 0.64304323, 0.64764481],
           [0.31924707, 0.64684514, 0.64894289],
           [0.32399647, 0.65063947, 0.65023744],
           [0.32882620, 0.65442561, 0.65152904],
           [0.33373835, 0.65820289, 0.65281838],
           [0.33873515, 0.66197064, 0.65410616],
           [0.34381881, 0.66572811, 0.65539330],
           [0.34899160, 0.66947452, 0.65668086],
           [0.35425586, 0.67320902, 0.65797005],
           [0.35961394, 0.67693076, 0.65926212],
           [0.36506831, 0.68063881, 0.66055847],
           [0.37062112, 0.68433222, 0.66186104],
           [0.37627487, 0.68800998, 0.66317142],
           [0.38203149, 0.69167107, 0.66449210],
           [0.38789330, 0.69531443, 0.66582512],
           [0.39386193, 0.69893900, 0.66717343],
           [0.39993898, 0.70254369, 0.66853995],
           [0.40612583, 0.70612744, 0.66992783],
           [0.41242330, 0.70968920, 0.67134073],
           [0.41883173, 0.71322799, 0.67278257],
           [0.42535095, 0.71674289, 0.67425759],
           [0.43198011, 0.72023305, 0.67577030],
           [0.43871767, 0.72369779, 0.67732549],
           [0.44556123, 0.72713656, 0.67892818],
           [0.45250758, 0.73054898, 0.68058357],
           [0.45955261, 0.73393492, 0.68229694],
           [0.46669130, 0.73729444, 0.68407356],
           [0.47391772, 0.74062788, 0.68591867],
           [0.48122519, 0.74393585, 0.68783723],
           [0.48860630, 0.74721920, 0.68983393],
           [0.49605306, 0.75047904, 0.69191302],
           [0.50355706, 0.75371673, 0.69407825],
           [0.51110961, 0.75693384, 0.69633279],
           [0.51870199, 0.76013211, 0.69867915],
           [0.52632555, 0.76331345, 0.70111918],
           [0.53397196, 0.76647982, 0.70365405],
           [0.54163332, 0.76963326, 0.70628425],
           [0.54930234, 0.77277581, 0.70900965],
           [0.55697237, 0.77590947, 0.71182953],
           [0.56463671, 0.77903637, 0.71474289],
           [0.57229081, 0.78215824, 0.71774790],
           [0.57992912, 0.78527710, 0.72084282],
           [0.58754828, 0.78839452, 0.72402527],
           [0.59514475, 0.79151213, 0.72729283],
           [0.60271552, 0.79463151, 0.73064297],
           [0.61025836, 0.79775402, 0.73407296],
           [0.61777160, 0.80088094, 0.73758006],
           [0.62525367, 0.80401348, 0.74116153],
           [0.63270387, 0.80715267, 0.74481460],
           [0.64012176, 0.81029943, 0.74853655],
           [0.64750659, 0.81345476, 0.75232480],
           [0.65485840, 0.81661944, 0.75617675],
           [0.66217728, 0.81979422, 0.76008994],
           [0.66946389, 0.82297967, 0.76406197],
           [0.67671761, 0.82617671, 0.76809057],
           [0.68393980, 0.82938567, 0.77217354],
           [0.69113094, 0.83260710, 0.77630879],
           [0.69829165, 0.83584151, 0.78049432],
           [0.70542264, 0.83908936, 0.78472824],
           [0.71252470, 0.84235106, 0.78900873],
           [0.71959870, 0.84562698, 0.79333408],
           [0.72664555, 0.84891744, 0.79770266],
           [0.73366565, 0.85222293, 0.80211288],
           [0.74066008, 0.85554371, 0.80656326],
           [0.74763018, 0.85887990, 0.81105246],
           [0.75457589, 0.86223209, 0.81557902],
           [0.76149887, 0.86560029, 0.82014175],
           [0.76839930, 0.86898498, 0.82473936],
           [0.77527874, 0.87238615, 0.82937078],
           [0.78213686, 0.87580444, 0.83403472],
           [0.78897545, 0.87923974, 0.83873025],
           [0.79579511, 0.88269234, 0.84345633],
           [0.80259581, 0.88616273, 0.84821182],
           [0.80937888, 0.88965094, 0.85299585],
           [0.81614498, 0.89315719, 0.85780751],
           [0.82289470, 0.89668175, 0.86264586],
           [0.82962861, 0.90022485, 0.86751000],
           [0.83634729, 0.90378676, 0.87239906],
           [0.84305129, 0.90736771, 0.87731217],
           [0.84974113, 0.91096796, 0.88224848],
           [0.85641734, 0.91458776, 0.88720714],
           [0.86308039, 0.91822735, 0.89218732],
           [0.86973073, 0.92188701, 0.89718817],
           [0.87636879, 0.92556701, 0.90220883],
           [0.88299495, 0.92926763, 0.90724844],
           [0.88960897, 0.93298940, 0.91230596],
           [0.89621156, 0.93673248, 0.91738058],
           [0.90280302, 0.94049718, 0.92247137],
           [0.90938335, 0.94428393, 0.92757732],
           [0.91595203, 0.94809341, 0.93269721],
           [0.92250973, 0.95192575, 0.93783015],
           [0.92905588, 0.95578166, 0.94297488],
           [0.93558995, 0.95966178, 0.94813012],
           [0.94211204, 0.96356654, 0.95329477],
           [0.94862035, 0.96749711, 0.95846718],
           [0.95511504, 0.97145390, 0.96364632],
           [0.96159359, 0.97543838, 0.96883050],
           [0.96805534, 0.97945125, 0.97401875],
           [0.97449688, 0.98349435, 0.97920966],
           [0.98091630, 0.98756881, 0.98440279],
           [0.98730941, 0.99167667, 0.98959791],
           [0.99367218, 0.99581976, 0.99479608],
           [1.00000000, 1.00000000, 1.00000000]]

# Create ListedColormap object for this colormap
cmap = ListedColormap(cm_data, name="cmr.ocean", N=len(cm_data))
cmap_r = cmap.reversed()

# Register (reversed) cmap in MPL
register_cmap(cmap=cmap)
register_cmap(cmap=cmap_r)
