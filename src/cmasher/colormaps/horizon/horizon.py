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
    [0.05120212, 0.20493541, 0.04200355],
    [0.04946476, 0.20843164, 0.04853604],
    [0.04768645, 0.21190842, 0.05492319],
    [0.04587175, 0.21536581, 0.06119401],
    [0.04402407, 0.21880399, 0.06737112],
    [0.04214835, 0.22222308, 0.07347112],
    [0.04024605, 0.22562327, 0.07950738],
    [0.03832887, 0.22900475, 0.08549036],
    [0.03645451, 0.23236768, 0.09142810],
    [0.03462894, 0.23571232, 0.09732757],
    [0.03285849, 0.23903888, 0.10319420],
    [0.03114972, 0.24234760, 0.10903221],
    [0.02950816, 0.24563876, 0.11484546],
    [0.02793953, 0.24891261, 0.12063700],
    [0.02644936, 0.25216946, 0.12640933],
    [0.02504310, 0.25540958, 0.13216447],
    [0.02372577, 0.25863329, 0.13790420],
    [0.02250207, 0.26184091, 0.14363008],
    [0.02137659, 0.26503276, 0.14934336],
    [0.02035368, 0.26820920, 0.15504511],
    [0.01943744, 0.27137055, 0.16073624],
    [0.01863172, 0.27451716, 0.16641756],
    [0.01794011, 0.27764941, 0.17208975],
    [0.01736597, 0.28076764, 0.17775344],
    [0.01691240, 0.28387223, 0.18340917],
    [0.01658226, 0.28696355, 0.18905744],
    [0.01637818, 0.29004196, 0.19469873],
    [0.01630255, 0.29310785, 0.20033347],
    [0.01635755, 0.29616158, 0.20596208],
    [0.01654513, 0.29920352, 0.21158498],
    [0.01686704, 0.30223406, 0.21720255],
    [0.01732482, 0.30525355, 0.22281521],
    [0.01791985, 0.30826237, 0.22842336],
    [0.01865331, 0.31126087, 0.23402742],
    [0.01952622, 0.31424940, 0.23962780],
    [0.02053948, 0.31722833, 0.24522495],
    [0.02169389, 0.32019799, 0.25081928],
    [0.02299009, 0.32315871, 0.25641124],
    [0.02442852, 0.32611083, 0.26200135],
    [0.02600961, 0.32905466, 0.26759014],
    [0.02773372, 0.33199051, 0.27317810],
    [0.02960115, 0.33491867, 0.27876577],
    [0.03161231, 0.33783944, 0.28435362],
    [0.03376728, 0.34075308, 0.28994229],
    [0.03606628, 0.34365986, 0.29553239],
    [0.03850955, 0.34656003, 0.30112450],
    [0.04108360, 0.34945383, 0.30671918],
    [0.04369584, 0.35234148, 0.31231709],
    [0.04634609, 0.35522319, 0.31791891],
    [0.04902975, 0.35809917, 0.32352528],
    [0.05174292, 0.36096958, 0.32913679],
    [0.05448207, 0.36383461, 0.33475417],
    [0.05724422, 0.36669440, 0.34037811],
    [0.06002691, 0.36954909, 0.34600926],
    [0.06282804, 0.37239882, 0.35164829],
    [0.06564579, 0.37524368, 0.35729595],
    [0.06847875, 0.37808379, 0.36295290],
    [0.07132582, 0.38091921, 0.36861979],
    [0.07418605, 0.38375001, 0.37429737],
    [0.07705878, 0.38657626, 0.37998631],
    [0.07994362, 0.38939798, 0.38568726],
    [0.08284025, 0.39221520, 0.39140093],
    [0.08574858, 0.39502793, 0.39712798],
    [0.08866872, 0.39783618, 0.40286905],
    [0.09160083, 0.40063991, 0.40862482],
    [0.09454524, 0.40343911, 0.41439592],
    [0.09750240, 0.40623372, 0.42018297],
    [0.10047285, 0.40902369, 0.42598658],
    [0.10345722, 0.41180896, 0.43180736],
    [0.10645624, 0.41458944, 0.43764589],
    [0.10947069, 0.41736504, 0.44350273],
    [0.11250146, 0.42013565, 0.44937843],
    [0.11554945, 0.42290116, 0.45527354],
    [0.11861566, 0.42566143, 0.46118854],
    [0.12170113, 0.42841634, 0.46712393],
    [0.12480692, 0.43116572, 0.47308021],
    [0.12793418, 0.43390941, 0.47905777],
    [0.13108405, 0.43664726, 0.48505706],
    [0.13425772, 0.43937906, 0.49107850],
    [0.13745641, 0.44210464, 0.49712242],
    [0.14068139, 0.44482379, 0.50318916],
    [0.14393388, 0.44753630, 0.50927912],
    [0.14721521, 0.45024195, 0.51539251],
    [0.15052666, 0.45294052, 0.52152958],
    [0.15386954, 0.45563176, 0.52769064],
    [0.15724518, 0.45831543, 0.53387584],
    [0.16065493, 0.46099128, 0.54008532],
    [0.16410012, 0.46365905, 0.54631923],
    [0.16758209, 0.46631846, 0.55257774],
    [0.17110220, 0.46896923, 0.55886083],
    [0.17466180, 0.47161109, 0.56516851],
    [0.17826223, 0.47424374, 0.57150082],
    [0.18190485, 0.47686688, 0.57785774],
    [0.18559099, 0.47948020, 0.58423910],
    [0.18932200, 0.48208341, 0.59064476],
    [0.19309922, 0.48467617, 0.59707453],
    [0.19692396, 0.48725816, 0.60352827],
    [0.20079756, 0.48982905, 0.61000567],
    [0.20472133, 0.49238850, 0.61650634],
    [0.20869655, 0.49493619, 0.62302990],
    [0.21272453, 0.49747176, 0.62957592],
    [0.21680655, 0.49999486, 0.63614389],
    [0.22094387, 0.50250514, 0.64273327],
    [0.22513777, 0.50500224, 0.64934347],
    [0.22938948, 0.50748580, 0.65597379],
    [0.23370023, 0.50995545, 0.66262342],
    [0.23807124, 0.51241085, 0.66929154],
    [0.24250371, 0.51485161, 0.67597723],
    [0.24699882, 0.51727737, 0.68267948],
    [0.25155776, 0.51968777, 0.68939720],
    [0.25618166, 0.52208244, 0.69612923],
    [0.26087167, 0.52446102, 0.70287427],
    [0.26562890, 0.52682315, 0.70963094],
    [0.27045450, 0.52916844, 0.71639788],
    [0.27534952, 0.53149656, 0.72317338],
    [0.28031500, 0.53380718, 0.72995570],
    [0.28535197, 0.53609996, 0.73674297],
    [0.29046143, 0.53837457, 0.74353318],
    [0.29564438, 0.54063070, 0.75032423],
    [0.30090190, 0.54286799, 0.75711406],
    [0.30623475, 0.54508622, 0.76389991],
    [0.31164380, 0.54728515, 0.77067913],
    [0.31713013, 0.54946441, 0.77744930],
    [0.32269435, 0.55162390, 0.78420705],
    [0.32833726, 0.55376340, 0.79094925],
    [0.33405973, 0.55588270, 0.79767267],
    [0.33986219, 0.55798177, 0.80437332],
    [0.34574553, 0.56006041, 0.81104769],
    [0.35171005, 0.56211869, 0.81769130],
    [0.35775629, 0.56415660, 0.82429982],
    [0.36388476, 0.56617416, 0.83086867],
    [0.37009551, 0.56817161, 0.83739254],
    [0.37638876, 0.57014916, 0.84386617],
    [0.38276483, 0.57210700, 0.85028410],
    [0.38922337, 0.57404563, 0.85664003],
    [0.39576414, 0.57596554, 0.86292758],
    [0.40238675, 0.57786735, 0.86913994],
    [0.40909059, 0.57975179, 0.87526994],
    [0.41587479, 0.58161976, 0.88130997],
    [0.42273825, 0.58347228, 0.88725200],
    [0.42967954, 0.58531058, 0.89308758],
    [0.43669694, 0.58713608, 0.89880786],
    [0.44378865, 0.58895025, 0.90440375],
    [0.45095197, 0.59075502, 0.90986548],
    [0.45818386, 0.59255247, 0.91518302],
    [0.46548140, 0.59434473, 0.92034631],
    [0.47284026, 0.59613452, 0.92534464],
    [0.48025633, 0.59792453, 0.93016747],
    [0.48772420, 0.59971800, 0.93480395],
    [0.49523869, 0.60151811, 0.93924353],
    [0.50279305, 0.60332867, 0.94347562],
    [0.51038035, 0.60515354, 0.94749013],
    [0.51799302, 0.60699683, 0.95127752],
    [0.52562276, 0.60886290, 0.95482895],
    [0.53326055, 0.61075628, 0.95813660],
    [0.54089693, 0.61268160, 0.96119384],
    [0.54852201, 0.61464352, 0.96399544],
    [0.55612555, 0.61664668, 0.96653782],
    [0.56369715, 0.61869560, 0.96881919],
    [0.57122637, 0.62079461, 0.97083966],
    [0.57870293, 0.62294778, 0.97260138],
    [0.58611690, 0.62515878, 0.97410852],
    [0.59345886, 0.62743089, 0.97536723],
    [0.60072008, 0.62976687, 0.97638554],
    [0.60789255, 0.63216901, 0.97717328],
    [0.61496935, 0.63463897, 0.97774163],
    [0.62194456, 0.63717790, 0.97810303],
    [0.62881333, 0.63978638, 0.97827083],
    [0.63557139, 0.64246460, 0.97825958],
    [0.64221637, 0.64521208, 0.97808333],
    [0.64874609, 0.64802811, 0.97775716],
    [0.65515995, 0.65091147, 0.97729525],
    [0.66145729, 0.65386079, 0.97671270],
    [0.66763916, 0.65687431, 0.97602282],
    [0.67370672, 0.65995014, 0.97523912],
    [0.67966166, 0.66308627, 0.97437441],
    [0.68550617, 0.66628056, 0.97344079],
    [0.69124281, 0.66953086, 0.97244953],
    [0.69687448, 0.67283494, 0.97141104],
    [0.70240428, 0.67619061, 0.97033489],
    [0.70783525, 0.67959574, 0.96923048],
    [0.71317066, 0.68304818, 0.96810611],
    [0.71841411, 0.68654591, 0.96696868],
    [0.72356861, 0.69008694, 0.96582608],
    [0.72863772, 0.69366938, 0.96468399],
    [0.73362481, 0.69729141, 0.96354790],
    [0.73853295, 0.70095131, 0.96242362],
    [0.74336531, 0.70464743, 0.96131591],
    [0.74812511, 0.70837822, 0.96022860],
    [0.75281534, 0.71214223, 0.95916557],
    [0.75743893, 0.71593807, 0.95813027],
    [0.76199870, 0.71976445, 0.95712571],
    [0.76649723, 0.72362008, 0.95615554],
    [0.77093730, 0.72750385, 0.95522147],
    [0.77532149, 0.73141472, 0.95432543],
    [0.77965215, 0.73535163, 0.95346986],
    [0.78393156, 0.73931358, 0.95265702],
    [0.78816217, 0.74329980, 0.95188713],
    [0.79234591, 0.74730926, 0.95116355],
    [0.79648507, 0.75134136, 0.95048561],
    [0.80058154, 0.75539524, 0.94985563],
    [0.80463728, 0.75947021, 0.94927436],
    [0.80865418, 0.76356569, 0.94874201],
    [0.81263401, 0.76768102, 0.94825976],
    [0.81657845, 0.77181554, 0.94782902],
    [0.82048921, 0.77596880, 0.94744944],
    [0.82436790, 0.78014026, 0.94712160],
    [0.82821607, 0.78432945, 0.94684598],
    [0.83203520, 0.78853589, 0.94662301],
    [0.83582675, 0.79275914, 0.94645298],
    [0.83959213, 0.79699880, 0.94633614],
    [0.84333271, 0.80125448, 0.94627267],
    [0.84704981, 0.80552581, 0.94626268],
    [0.85074472, 0.80981245, 0.94630624],
    [0.85441869, 0.81411407, 0.94640342],
    [0.85807301, 0.81843019, 0.94655530],
    [0.86170881, 0.82276067, 0.94676083],
    [0.86532727, 0.82710522, 0.94701992],
    [0.86892955, 0.83146352, 0.94733281],
    [0.87251687, 0.83583513, 0.94770051],
    [0.87609023, 0.84022003, 0.94812149],
    [0.87965078, 0.84461782, 0.94859652],
    [0.88319967, 0.84902818, 0.94912585],
    [0.88673785, 0.85345106, 0.94970831],
    [0.89026664, 0.85788588, 0.95034577],
    [0.89378682, 0.86233276, 0.95103602],
    [0.89729980, 0.86679103, 0.95178136],
    [0.90080638, 0.87126081, 0.95257969],
    [0.90430789, 0.87574153, 0.95343269],
    [0.90780531, 0.88023308, 0.95433945],
    [0.91129976, 0.88473520, 0.95530001],
    [0.91479261, 0.88924736, 0.95631568],
    [0.91828479, 0.89376951, 0.95738519],
    [0.92177761, 0.89830123, 0.95850923],
    [0.92527251, 0.90284199, 0.95968902],
    [0.92877058, 0.90739163, 0.96092377],
    [0.93227318, 0.91194972, 0.96221406],
    [0.93578185, 0.91651572, 0.96356097],
    [0.93929811, 0.92108910, 0.96496554],
    [0.94282334, 0.92566945, 0.96642807],
    [0.94635913, 0.93025622, 0.96794982],
    [0.94990705, 0.93484879, 0.96953234],
    [0.95346868, 0.93944654, 0.97117756],
    [0.95704550, 0.94404882, 0.97288796],
    [0.96063880, 0.94865495, 0.97466688],
    [0.96424925, 0.95326453, 0.97651764],
    [0.96787684, 0.95787729, 0.97844493],
    [0.97152024, 0.96249335, 0.98045445],
    [0.97517606, 0.96711358, 0.98255287],
    [0.97883780, 0.97174000, 0.98474752],
    [0.98249464, 0.97637636, 0.98704544],
    [0.98613036, 0.98102876, 0.98945147],
    [0.98972324, 0.98570598, 0.99196519],
    [0.99324786, 0.99041918, 0.99457717],
    [0.99667949, 0.99518036, 0.99726622],
    [1.00000000, 1.00000000, 1.00000000],
]

# Create ListedColormap object for this colormap
cmap = ListedColormap(cm_data, name="cmr.horizon", N=256)
cmap_r = cmap.reversed()

# Register (reversed) cmap in MPL
mpl.colormaps.register(cmap=cmap)
mpl.colormaps.register(cmap=cmap_r)