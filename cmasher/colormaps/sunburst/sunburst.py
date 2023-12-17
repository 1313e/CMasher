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
    [0.00028691, 0.00020835, 0.00028279],
    [0.00102421, 0.00070903, 0.00101021],
    [0.00218033, 0.00144242, 0.00214845],
    [0.00375280, 0.00237790, 0.00368891],
    [0.00574727, 0.00349371, 0.00562841],
    [0.00817359, 0.00477242, 0.00796563],
    [0.01104432, 0.00619914, 0.01069976],
    [0.01437378, 0.00776073, 0.01382970],
    [0.01817764, 0.00944524, 0.01735364],
    [0.02247277, 0.01124162, 0.02126897],
    [0.02727694, 0.01313949, 0.02557207],
    [0.03260869, 0.01512908, 0.03025819],
    [0.03848721, 0.01720107, 0.03532137],
    [0.04472223, 0.01934661, 0.04074862],
    [0.05095008, 0.02155723, 0.04620189],
    [0.05718085, 0.02382484, 0.05156892],
    [0.06341877, 0.02614168, 0.05685075],
    [0.06966727, 0.02850036, 0.06204782],
    [0.07592916, 0.03089381, 0.06716019],
    [0.08220666, 0.03331529, 0.07218757],
    [0.08850155, 0.03575837, 0.07712945],
    [0.09481532, 0.03821687, 0.08198520],
    [0.10114895, 0.04068063, 0.08675399],
    [0.10750319, 0.04306161, 0.09143498],
    [0.11387855, 0.04536332, 0.09602729],
    [0.12027537, 0.04758808, 0.10053004],
    [0.12669388, 0.04973801, 0.10494242],
    [0.13313410, 0.05181515, 0.10926361],
    [0.13959587, 0.05382147, 0.11349284],
    [0.14607903, 0.05575879, 0.11762946],
    [0.15258333, 0.05762879, 0.12167284],
    [0.15910850, 0.05943303, 0.12562246],
    [0.16565413, 0.06117310, 0.12947786],
    [0.17221981, 0.06285040, 0.13323866],
    [0.17880518, 0.06446624, 0.13690456],
    [0.18540980, 0.06602187, 0.14047531],
    [0.19203321, 0.06751848, 0.14395075],
    [0.19867499, 0.06895715, 0.14733079],
    [0.20533472, 0.07033887, 0.15061537],
    [0.21201197, 0.07166460, 0.15380450],
    [0.21870632, 0.07293518, 0.15689824],
    [0.22541736, 0.07415142, 0.15989669],
    [0.23214472, 0.07531401, 0.16279996],
    [0.23888802, 0.07642364, 0.16560823],
    [0.24564687, 0.07748088, 0.16832171],
    [0.25242097, 0.07848626, 0.17094058],
    [0.25920996, 0.07944023, 0.17346508],
    [0.26601352, 0.08034324, 0.17589547],
    [0.27283134, 0.08119562, 0.17823199],
    [0.27966317, 0.08199764, 0.18047489],
    [0.28650868, 0.08274959, 0.18262446],
    [0.29336760, 0.08345167, 0.18468096],
    [0.30023971, 0.08410396, 0.18664460],
    [0.30712474, 0.08470663, 0.18851568],
    [0.31402240, 0.08525975, 0.19029445],
    [0.32093251, 0.08576327, 0.19198110],
    [0.32785482, 0.08621717, 0.19357587],
    [0.33478905, 0.08662148, 0.19507899],
    [0.34173503, 0.08697601, 0.19649062],
    [0.34869254, 0.08728060, 0.19781092],
    [0.35566125, 0.08753522, 0.19904011],
    [0.36264104, 0.08773953, 0.20017823],
    [0.36963165, 0.08789334, 0.20122542],
    [0.37663272, 0.08799656, 0.20218186],
    [0.38364424, 0.08804859, 0.20304740],
    [0.39066574, 0.08804944, 0.20382227],
    [0.39769703, 0.08799872, 0.20450641],
    [0.40473792, 0.08789596, 0.20509971],
    [0.41178790, 0.08774121, 0.20560237],
    [0.41884704, 0.08753353, 0.20601388],
    [0.42591463, 0.08727325, 0.20633459],
    [0.43299069, 0.08695948, 0.20656394],
    [0.44007455, 0.08659242, 0.20670212],
    [0.44716616, 0.08617128, 0.20674851],
    [0.45426479, 0.08569637, 0.20670331],
    [0.46137042, 0.08516677, 0.20656566],
    [0.46848219, 0.08458313, 0.20633582],
    [0.47560004, 0.08394454, 0.20601280],
    [0.48272316, 0.08325159, 0.20559662],
    [0.48985104, 0.08250434, 0.20508677],
    [0.49698340, 0.08170242, 0.20448225],
    [0.50411927, 0.08084690, 0.20378304],
    [0.51125803, 0.07993830, 0.20298844],
    [0.51839929, 0.07897664, 0.20209721],
    [0.52554202, 0.07796358, 0.20110904],
    [0.53268538, 0.07690049, 0.20002312],
    [0.53982852, 0.07578902, 0.19883855],
    [0.54697049, 0.07463129, 0.19755431],
    [0.55411028, 0.07342990, 0.19616934],
    [0.56124678, 0.07218810, 0.19468248],
    [0.56837880, 0.07090985, 0.19309253],
    [0.57550502, 0.06959997, 0.19139818],
    [0.58262400, 0.06826431, 0.18959809],
    [0.58973418, 0.06690989, 0.18769083],
    [0.59683382, 0.06554515, 0.18567490],
    [0.60392106, 0.06418012, 0.18354875],
    [0.61099403, 0.06282598, 0.18131023],
    [0.61805061, 0.06149625, 0.17895730],
    [0.62508803, 0.06020822, 0.17648890],
    [0.63210426, 0.05897851, 0.17390136],
    [0.63909578, 0.05783082, 0.17119418],
    [0.64606007, 0.05678752, 0.16836327],
    [0.65299326, 0.05587785, 0.16540731],
    [0.65989160, 0.05513269, 0.16232365],
    [0.66675096, 0.05458598, 0.15910942],
    [0.67356680, 0.05427454, 0.15576179],
    [0.68033403, 0.05423761, 0.15227799],
    [0.68704706, 0.05451589, 0.14865546],
    [0.69369969, 0.05515040, 0.14489185],
    [0.70028509, 0.05618108, 0.14098519],
    [0.70679624, 0.05764355, 0.13693176],
    [0.71322465, 0.05957213, 0.13273203],
    [0.71956187, 0.06199294, 0.12838347],
    [0.72579832, 0.06492701, 0.12388673],
    [0.73192387, 0.06838759, 0.11924309],
    [0.73792785, 0.07238015, 0.11445523],
    [0.74379911, 0.07690258, 0.10952793],
    [0.74952631, 0.08194530, 0.10446780],
    [0.75509807, 0.08749192, 0.09928513],
    [0.76050344, 0.09351949, 0.09399345],
    [0.76573234, 0.09999923, 0.08860931],
    [0.77077595, 0.10689714, 0.08315390],
    [0.77562724, 0.11417469, 0.07765262],
    [0.78028137, 0.12178994, 0.07213493],
    [0.78473594, 0.12969861, 0.06663478],
    [0.78899120, 0.13785534, 0.06119075],
    [0.79304987, 0.14621526, 0.05584590],
    [0.79691698, 0.15473527, 0.05064835],
    [0.80059949, 0.16337512, 0.04565234],
    [0.80410578, 0.17209842, 0.04091877],
    [0.80744502, 0.18087354, 0.03656330],
    [0.81062721, 0.18967261, 0.03284897],
    [0.81366202, 0.19847328, 0.02978095],
    [0.81655911, 0.20725703, 0.02735425],
    [0.81932773, 0.21600901, 0.02556368],
    [0.82197656, 0.22471783, 0.02440445],
    [0.82451354, 0.23337504, 0.02387282],
    [0.82694588, 0.24197470, 0.02396658],
    [0.82928000, 0.25051291, 0.02468537],
    [0.83152234, 0.25898625, 0.02603161],
    [0.83367755, 0.26739445, 0.02800850],
    [0.83575119, 0.27573587, 0.03062270],
    [0.83774693, 0.28401176, 0.03388176],
    [0.83966871, 0.29222281, 0.03779577],
    [0.84152000, 0.30037020, 0.04231855],
    [0.84330390, 0.30845547, 0.04718171],
    [0.84502314, 0.31648042, 0.05232334],
    [0.84668012, 0.32444703, 0.05769850],
    [0.84827700, 0.33235739, 0.06327080],
    [0.84981598, 0.34021329, 0.06901096],
    [0.85129899, 0.34801660, 0.07489554],
    [0.85272715, 0.35576999, 0.08090629],
    [0.85410285, 0.36347441, 0.08702799],
    [0.85542653, 0.37113285, 0.09324952],
    [0.85670046, 0.37874607, 0.09956104],
    [0.85792511, 0.38631664, 0.10595570],
    [0.85910167, 0.39384615, 0.11242769],
    [0.86023184, 0.40133560, 0.11897200],
    [0.86131603, 0.40878710, 0.12558544],
    [0.86235527, 0.41620202, 0.13226519],
    [0.86335049, 0.42358173, 0.13900904],
    [0.86430261, 0.43092748, 0.14581530],
    [0.86521249, 0.43824051, 0.15268270],
    [0.86608094, 0.44552198, 0.15961030],
    [0.86690878, 0.45277298, 0.16659744],
    [0.86769678, 0.45999455, 0.17364368],
    [0.86844571, 0.46718767, 0.18074877],
    [0.86915633, 0.47435325, 0.18791261],
    [0.86982940, 0.48149217, 0.19513520],
    [0.87046566, 0.48860521, 0.20241667],
    [0.87106589, 0.49569313, 0.20975721],
    [0.87163086, 0.50275663, 0.21715708],
    [0.87216162, 0.50979614, 0.22461634],
    [0.87265881, 0.51681240, 0.23213553],
    [0.87312317, 0.52380600, 0.23971510],
    [0.87355555, 0.53077744, 0.24735548],
    [0.87395712, 0.53772697, 0.25505684],
    [0.87432861, 0.54465512, 0.26281981],
    [0.87467085, 0.55156232, 0.27064498],
    [0.87498503, 0.55844876, 0.27853263],
    [0.87527217, 0.56531471, 0.28648326],
    [0.87553313, 0.57216055, 0.29449756],
    [0.87576930, 0.57898630, 0.30257577],
    [0.87598171, 0.58579221, 0.31071851],
    [0.87617147, 0.59257844, 0.31892638],
    [0.87634020, 0.59934489, 0.32719953],
    [0.87648888, 0.60609181, 0.33553878],
    [0.87661914, 0.61281908, 0.34394439],
    [0.87673240, 0.61952670, 0.35241687],
    [0.87683016, 0.62621463, 0.36095669],
    [0.87691421, 0.63288268, 0.36956410],
    [0.87698607, 0.63953083, 0.37823972],
    [0.87704779, 0.64615877, 0.38698363],
    [0.87710104, 0.65276640, 0.39579639],
    [0.87714801, 0.65935338, 0.40467811],
    [0.87719069, 0.66591948, 0.41362916],
    [0.87723137, 0.67246435, 0.42264965],
    [0.87727233, 0.67898764, 0.43173978],
    [0.87731605, 0.68548896, 0.44089961],
    [0.87736509, 0.69196788, 0.45012917],
    [0.87742214, 0.69842394, 0.45942844],
    [0.87749005, 0.70485663, 0.46879727],
    [0.87757175, 0.71126545, 0.47823549],
    [0.87767038, 0.71764981, 0.48774277],
    [0.87778914, 0.72400915, 0.49731878],
    [0.87793145, 0.73034282, 0.50696296],
    [0.87810081, 0.73665020, 0.51667477],
    [0.87830092, 0.74293060, 0.52645341],
    [0.87853556, 0.74918334, 0.53629808],
    [0.87880873, 0.75540769, 0.54620771],
    [0.87912449, 0.76160293, 0.55618122],
    [0.87948712, 0.76776830, 0.56621720],
    [0.87990092, 0.77390307, 0.57631429],
    [0.88037047, 0.78000643, 0.58647070],
    [0.88090027, 0.78607767, 0.59668473],
    [0.88149514, 0.79211598, 0.60695418],
    [0.88215974, 0.79812065, 0.61727700],
    [0.88289909, 0.80409090, 0.62765056],
    [0.88371798, 0.81002606, 0.63807240],
    [0.88462153, 0.81592540, 0.64853946],
    [0.88561459, 0.82178829, 0.65904886],
    [0.88670229, 0.82761408, 0.66959711],
    [0.88788952, 0.83340224, 0.68018083],
    [0.88918122, 0.83915225, 0.69079625],
    [0.89058234, 0.84486362, 0.70143930],
    [0.89209744, 0.85053601, 0.71210615],
    [0.89373153, 0.85616903, 0.72279183],
    [0.89548875, 0.86176252, 0.73349245],
    [0.89737373, 0.86731625, 0.74420272],
    [0.89939058, 0.87283016, 0.75491787],
    [0.90154313, 0.87830429, 0.76563309],
    [0.90383561, 0.88373862, 0.77634217],
    [0.90627132, 0.88913338, 0.78704028],
    [0.90885368, 0.89448881, 0.79772179],
    [0.91158625, 0.89980515, 0.80838000],
    [0.91447204, 0.90508277, 0.81900898],
    [0.91751403, 0.91032207, 0.82960244],
    [0.92071527, 0.91552347, 0.84015333],
    [0.92407894, 0.92068737, 0.85065379],
    [0.92760832, 0.92581419, 0.86109531],
    [0.93130674, 0.93090430, 0.87146916],
    [0.93517804, 0.93595804, 0.88176475],
    [0.93922654, 0.94097572, 0.89196965],
    [0.94345707, 0.94595767, 0.90206897],
    [0.94787482, 0.95090438, 0.91204440],
    [0.95248483, 0.95581688, 0.92187319],
    [0.95729065, 0.96069726, 0.93152703],
    [0.96229171, 0.96554987, 0.94097172],
    [0.96747854, 0.97038293, 0.95016887],
    [0.97282603, 0.97521057, 0.95908244],
    [0.97828739, 0.98005380, 0.96769236],
    [0.98379547, 0.98493815, 0.97601254],
    [0.98927857, 0.98988597, 0.98410494],
    [0.99468526, 0.99490795, 0.99206668],
    [1.00000000, 1.00000000, 1.00000000],
]

# Create ListedColormap object for this colormap
cmap = ListedColormap(cm_data, name="cmr.sunburst", N=256)
cmap_r = cmap.reversed()

# Register (reversed) cmap in MPL
mpl.colormaps.register(cmap=cmap)
mpl.colormaps.register(cmap=cmap_r)
