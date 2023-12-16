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
cm_type = "diverging"

# RGB-values of this colormap
cm_data = [
    [0.98146917, 0.56765131, 0.31114761],
    [0.98206949, 0.56329082, 0.30670174],
    [0.98265993, 0.55891430, 0.30226065],
    [0.98324038, 0.55452138, 0.29782449],
    [0.98381072, 0.55011169, 0.29339338],
    [0.98437085, 0.54568487, 0.28896748],
    [0.98492064, 0.54124051, 0.28454695],
    [0.98545995, 0.53677823, 0.28013196],
    [0.98598899, 0.53229735, 0.27572243],
    [0.98650753, 0.52779752, 0.27131863],
    [0.98701522, 0.52327846, 0.26692094],
    [0.98751193, 0.51873973, 0.26252959],
    [0.98799815, 0.51418031, 0.25814428],
    [0.98847317, 0.50960018, 0.25376574],
    [0.98893684, 0.50499886, 0.24939425],
    [0.98938970, 0.50037519, 0.24502951],
    [0.98983081, 0.49572932, 0.24067251],
    [0.99026075, 0.49106004, 0.23632295],
    [0.99067881, 0.48636722, 0.23198166],
    [0.99108539, 0.48164973, 0.22764856],
    [0.99147976, 0.47690746, 0.22332454],
    [0.99186257, 0.47213895, 0.21900935],
    [0.99223292, 0.46734418, 0.21470411],
    [0.99259105, 0.46252202, 0.21040900],
    [0.99293693, 0.45767155, 0.20612447],
    [0.99327005, 0.45279227, 0.20185141],
    [0.99359032, 0.44788323, 0.19759044],
    [0.99389784, 0.44294327, 0.19334206],
    [0.99419237, 0.43797148, 0.18910713],
    [0.99447359, 0.43296701, 0.18488665],
    [0.99474133, 0.42792878, 0.18068158],
    [0.99499541, 0.42285567, 0.17649298],
    [0.99523563, 0.41774653, 0.17232206],
    [0.99546176, 0.41260016, 0.16817015],
    [0.99567355, 0.40741533, 0.16403874],
    [0.99587072, 0.40219073, 0.15992950],
    [0.99605337, 0.39692456, 0.15584399],
    [0.99622085, 0.39161577, 0.15178453],
    [0.99637278, 0.38626295, 0.14775351],
    [0.99650912, 0.38086413, 0.14375324],
    [0.99662947, 0.37541770, 0.13978665],
    [0.99673326, 0.36992210, 0.13585709],
    [0.99682039, 0.36437508, 0.13196795],
    [0.99689027, 0.35877489, 0.12812340],
    [0.99694227, 0.35311967, 0.12432807],
    [0.99697629, 0.34740665, 0.12058678],
    [0.99699157, 0.34163385, 0.11690541],
    [0.99698743, 0.33579893, 0.11329039],
    [0.99696327, 0.32989930, 0.10974890],
    [0.99691834, 0.32393229, 0.10628898],
    [0.99685183, 0.31789514, 0.10291964],
    [0.99676287, 0.31178490, 0.09965089],
    [0.99665073, 0.30559812, 0.09649378],
    [0.99651387, 0.29933233, 0.09346085],
    [0.99635144, 0.29298362, 0.09056556],
    [0.99616172, 0.28654922, 0.08782291],
    [0.99594375, 0.28002467, 0.08524896],
    [0.99569541, 0.27340707, 0.08286127],
    [0.99541492, 0.26669267, 0.08067839],
    [0.99510016, 0.25987777, 0.07871988],
    [0.99474873, 0.25295884, 0.07700599],
    [0.99435807, 0.24593217, 0.07555732],
    [0.99392521, 0.23879448, 0.07439435],
    [0.99344667, 0.23154312, 0.07353678],
    [0.99291874, 0.22417551, 0.07300306],
    [0.99233746, 0.21668943, 0.07280975],
    [0.99169802, 0.20908430, 0.07297044],
    [0.99099539, 0.20136015, 0.07349554],
    [0.99022413, 0.19351815, 0.07439165],
    [0.98937805, 0.18556200, 0.07566058],
    [0.98845088, 0.17749644, 0.07729995],
    [0.98743579, 0.16932922, 0.07930212],
    [0.98632592, 0.16107009, 0.08165506],
    [0.98511434, 0.15273171, 0.08434203],
    [0.98379430, 0.14432960, 0.08734197],
    [0.98235954, 0.13588168, 0.09063034],
    [0.98080454, 0.12740829, 0.09417951],
    [0.97912481, 0.11893146, 0.09795965],
    [0.97731710, 0.11047431, 0.10193970],
    [0.97537961, 0.10206028, 0.10608823],
    [0.97331200, 0.09371248, 0.11037429],
    [0.97111546, 0.08545297, 0.11476831],
    [0.96879254, 0.07730230, 0.11924283],
    [0.96634703, 0.06927937, 0.12377291],
    [0.96378370, 0.06140158, 0.12833644],
    [0.96110803, 0.05368544, 0.13291390],
    [0.95832606, 0.04614679, 0.13748944],
    [0.95544409, 0.03879488, 0.14204922],
    [0.95246851, 0.03209071, 0.14658249],
    [0.94940568, 0.02630492, 0.15107989],
    [0.94626179, 0.02136874, 0.15553473],
    [0.94304278, 0.01721621, 0.15994164],
    [0.93975431, 0.01378460, 0.16429638],
    [0.93640164, 0.01101522, 0.16859663],
    [0.93298979, 0.00885275, 0.17283994],
    [0.92952330, 0.00724627, 0.17702561],
    [0.92600657, 0.00614769, 0.18115222],
    [0.92244349, 0.00551341, 0.18522003],
    [0.91883771, 0.00530296, 0.18922924],
    [0.91519259, 0.00547896, 0.19318023],
    [0.91151131, 0.00600651, 0.19707314],
    [0.90779662, 0.00685475, 0.20090948],
    [0.90405118, 0.00799431, 0.20468987],
    [0.90027744, 0.00939827, 0.20841516],
    [0.89647764, 0.01104187, 0.21208629],
    [0.89265376, 0.01290294, 0.21570469],
    [0.88880774, 0.01496029, 0.21927120],
    [0.88494137, 0.01719448, 0.22278676],
    [0.88105629, 0.01958763, 0.22625237],
    [0.87715401, 0.02212333, 0.22966908],
    [0.87323589, 0.02478649, 0.23303795],
    [0.86930322, 0.02756326, 0.23636009],
    [0.86535715, 0.03044095, 0.23963660],
    [0.86139900, 0.03340626, 0.24286769],
    [0.85742965, 0.03644913, 0.24605487],
    [0.85345013, 0.03955885, 0.24919880],
    [0.84946136, 0.04265189, 0.25230030],
    [0.84546425, 0.04564882, 0.25535997],
    [0.84145944, 0.04856138, 0.25837911],
    [0.83744790, 0.05139030, 0.26135777],
    [0.83343027, 0.05413783, 0.26429685],
    [0.82940715, 0.05680639, 0.26719724],
    [0.82537919, 0.05939787, 0.27005950],
    [0.82134701, 0.06191424, 0.27288419],
    [0.81731117, 0.06435748, 0.27567187],
    [0.81327221, 0.06672955, 0.27842310],
    [0.80923062, 0.06903239, 0.28113843],
    [0.80518688, 0.07126791, 0.28381840],
    [0.80114142, 0.07343797, 0.28646354],
    [0.79709466, 0.07554438, 0.28907440],
    [0.79304701, 0.07758873, 0.29165136],
    [0.78899904, 0.07957203, 0.29419440],
    [0.78495089, 0.08149667, 0.29670459],
    [0.78090287, 0.08336425, 0.29918244],
    [0.77685563, 0.08517513, 0.30162747],
    [0.77280920, 0.08693171, 0.30404090],
    [0.76876398, 0.08863498, 0.30642284],
    [0.76472035, 0.09028594, 0.30877340],
    [0.76067841, 0.09188632, 0.31109339],
    [0.75663866, 0.09343667, 0.31338260],
    [0.75260118, 0.09493859, 0.31564177],
    [0.74856627, 0.09639300, 0.31787110],
    [0.74453429, 0.09780061, 0.32007059],
    [0.74050524, 0.09916308, 0.32224115],
    [0.73647959, 0.10048063, 0.32438240],
    [0.73245747, 0.10175443, 0.32649486],
    [0.72843899, 0.10298562, 0.32857906],
    [0.72442440, 0.10417491, 0.33063516],
    [0.72041411, 0.10532252, 0.33266283],
    [0.71640810, 0.10642983, 0.33466291],
    [0.71240656, 0.10749751, 0.33663561],
    [0.70840968, 0.10852623, 0.33858112],
    [0.70441766, 0.10951664, 0.34049965],
    [0.70043068, 0.11046937, 0.34239140],
    [0.69644899, 0.11138487, 0.34425642],
    [0.69247269, 0.11226388, 0.34609507],
    [0.68850191, 0.11310701, 0.34790763],
    [0.68453682, 0.11391482, 0.34969430],
    [0.68057758, 0.11468782, 0.35145528],
    [0.67662433, 0.11542652, 0.35319080],
    [0.67267722, 0.11613140, 0.35490106],
    [0.66873641, 0.11680294, 0.35658627],
    [0.66480205, 0.11744152, 0.35824658],
    [0.66087433, 0.11804749, 0.35988211],
    [0.65695334, 0.11862138, 0.36149321],
    [0.65303918, 0.11916360, 0.36308009],
    [0.64913200, 0.11967454, 0.36464300],
    [0.64523191, 0.12015455, 0.36618214],
    [0.64133905, 0.12060401, 0.36769777],
    [0.63745362, 0.12102306, 0.36918988],
    [0.63357579, 0.12141195, 0.37065862],
    [0.62970556, 0.12177123, 0.37210450],
    [0.62584302, 0.12210119, 0.37352778],
    [0.62198836, 0.12240200, 0.37492856],
    [0.61814188, 0.12267361, 0.37630669],
    [0.61430345, 0.12291668, 0.37766294],
    [0.61047318, 0.12313145, 0.37899756],
    [0.60665147, 0.12331764, 0.38031017],
    [0.60283821, 0.12347584, 0.38160153],
    [0.59903343, 0.12360636, 0.38287205],
    [0.59523762, 0.12370877, 0.38412121],
    [0.59145054, 0.12378378, 0.38534998],
    [0.58767240, 0.12383138, 0.38655847],
    [0.58390349, 0.12385145, 0.38774656],
    [0.58014359, 0.12384457, 0.38891521],
    [0.57639323, 0.12381023, 0.39006385],
    [0.57265216, 0.12374907, 0.39119352],
    [0.56892072, 0.12366079, 0.39230402],
    [0.56519891, 0.12354565, 0.39339592],
    [0.56148689, 0.12340360, 0.39446939],
    [0.55778476, 0.12323467, 0.39552478],
    [0.55409263, 0.12303889, 0.39656240],
    [0.55041061, 0.12281627, 0.39758260],
    [0.54673884, 0.12256672, 0.39858564],
    [0.54307735, 0.12229036, 0.39957206],
    [0.53942641, 0.12198689, 0.40054185],
    [0.53578584, 0.12165663, 0.40149595],
    [0.53215618, 0.12129897, 0.40243391],
    [0.52853710, 0.12091435, 0.40335696],
    [0.52492902, 0.12050227, 0.40426488],
    [0.52133189, 0.12006277, 0.40515834],
    [0.51774574, 0.11959582, 0.40603795],
    [0.51417100, 0.11910085, 0.40690347],
    [0.51060741, 0.11857808, 0.40775604],
    [0.50705523, 0.11802716, 0.40859583],
    [0.50351468, 0.11744769, 0.40942304],
    [0.49998562, 0.11683970, 0.41023862],
    [0.49646827, 0.11620275, 0.41104278],
    [0.49296286, 0.11553644, 0.41183582],
    [0.48946927, 0.11484065, 0.41261864],
    [0.48598761, 0.11411499, 0.41339170],
    [0.48251827, 0.11335879, 0.41415501],
    [0.47906106, 0.11257191, 0.41490965],
    [0.47561609, 0.11175390, 0.41565614],
    [0.47218356, 0.11090413, 0.41639486],
    [0.46876362, 0.11002201, 0.41712623],
    [0.46535623, 0.10910714, 0.41785117],
    [0.46196148, 0.10815886, 0.41857026],
    [0.45857951, 0.10717649, 0.41928404],
    [0.45521056, 0.10615913, 0.41999282],
    [0.45185456, 0.10510621, 0.42069763],
    [0.44851159, 0.10401685, 0.42139911],
    [0.44518176, 0.10289016, 0.42209791],
    [0.44186518, 0.10172513, 0.42279468],
    [0.43856210, 0.10052057, 0.42348983],
    [0.43527244, 0.09927549, 0.42418439],
    [0.43199633, 0.09798862, 0.42487910],
    [0.42873385, 0.09665863, 0.42557467],
    [0.42548511, 0.09528403, 0.42627187],
    [0.42225022, 0.09386323, 0.42697146],
    [0.41902934, 0.09239445, 0.42767411],
    [0.41582257, 0.09087581, 0.42838063],
    [0.41262997, 0.08930526, 0.42909196],
    [0.40945164, 0.08768054, 0.42980894],
    [0.40628772, 0.08599914, 0.43053242],
    [0.40313832, 0.08425832, 0.43126329],
    [0.40000356, 0.08245503, 0.43200242],
    [0.39688358, 0.08058590, 0.43275073],
    [0.39377851, 0.07864718, 0.43350915],
    [0.39068849, 0.07663468, 0.43427863],
    [0.38761368, 0.07454372, 0.43506014],
    [0.38455422, 0.07236901, 0.43585468],
    [0.38151031, 0.07010456, 0.43666320],
    [0.37848209, 0.06774357, 0.43748678],
    [0.37546975, 0.06527825, 0.43832651],
    [0.37247348, 0.06269962, 0.43918348],
    [0.36949347, 0.05999723, 0.44005882],
    [0.36652996, 0.05715884, 0.44095365],
    [0.36358316, 0.05416994, 0.44186915],
    [0.36065333, 0.05101317, 0.44280653],
    [0.35774073, 0.04766742, 0.44376701],
    [0.35484564, 0.04410670, 0.44475186],
    [0.35196837, 0.04029596, 0.44576237],
    [0.34910922, 0.03626178, 0.44679989],
    [0.34626855, 0.03216581, 0.44786580],
    [0.34344673, 0.02800691, 0.44896150],
    [0.34479525, 0.03011158, 0.45429638],
    [0.34613346, 0.03223176, 0.45965293],
    [0.34746121, 0.03436717, 0.46503143],
    [0.34877836, 0.03651760, 0.47043210],
    [0.35008472, 0.03868289, 0.47585518],
    [0.35138014, 0.04085472, 0.48130087],
    [0.35266441, 0.04296709, 0.48676936],
    [0.35393732, 0.04503096, 0.49226089],
    [0.35519861, 0.04704978, 0.49777593],
    [0.35644809, 0.04902699, 0.50331425],
    [0.35768552, 0.05096558, 0.50887595],
    [0.35891065, 0.05286825, 0.51446111],
    [0.36012308, 0.05473718, 0.52007042],
    [0.36132264, 0.05657502, 0.52570329],
    [0.36250901, 0.05838396, 0.53135973],
    [0.36368177, 0.06016571, 0.53704038],
    [0.36484066, 0.06192249, 0.54274464],
    [0.36598531, 0.06365613, 0.54847251],
    [0.36711527, 0.06536814, 0.55422439],
    [0.36823026, 0.06706065, 0.55999942],
    [0.36932970, 0.06873483, 0.56579835],
    [0.37041332, 0.07039278, 0.57162010],
    [0.37148052, 0.07203568, 0.57746531],
    [0.37253096, 0.07366554, 0.58333283],
    [0.37356396, 0.07528343, 0.58922340],
    [0.37457917, 0.07689137, 0.59513575],
    [0.37557593, 0.07849067, 0.60107006],
    [0.37655370, 0.08008294, 0.60702579],
    [0.37751193, 0.08166994, 0.61300216],
    [0.37844990, 0.08325305, 0.61899914],
    [0.37936700, 0.08483398, 0.62501597],
    [0.38026259, 0.08641451, 0.63105181],
    [0.38113594, 0.08799630, 0.63710602],
    [0.38198627, 0.08958101, 0.64317808],
    [0.38281281, 0.09117040, 0.64926716],
    [0.38361478, 0.09276640, 0.65537217],
    [0.38439133, 0.09437088, 0.66149218],
    [0.38514160, 0.09598575, 0.66762618],
    [0.38586465, 0.09761300, 0.67377304],
    [0.38655954, 0.09925466, 0.67993157],
    [0.38722526, 0.10091282, 0.68610047],
    [0.38786079, 0.10258966, 0.69227835],
    [0.38846505, 0.10428739, 0.69846370],
    [0.38903692, 0.10600831, 0.70465491],
    [0.38957520, 0.10775473, 0.71085037],
    [0.39007863, 0.10952895, 0.71704847],
    [0.39054602, 0.11133359, 0.72324695],
    [0.39097605, 0.11317118, 0.72944369],
    [0.39136729, 0.11504419, 0.73563680],
    [0.39171830, 0.11695526, 0.74182396],
    [0.39202771, 0.11890722, 0.74800225],
    [0.39229376, 0.12090254, 0.75416986],
    [0.39251508, 0.12294425, 0.76032318],
    [0.39268979, 0.12503492, 0.76646005],
    [0.39281639, 0.12717761, 0.77257663],
    [0.39289285, 0.12937494, 0.77867040],
    [0.39291749, 0.13162993, 0.78473740],
    [0.39288841, 0.13394543, 0.79077400],
    [0.39280351, 0.13632422, 0.79677672],
    [0.39266080, 0.13876915, 0.80274140],
    [0.39245823, 0.14128306, 0.80866370],
    [0.39219363, 0.14386868, 0.81453923],
    [0.39186480, 0.14652870, 0.82036339],
    [0.39146948, 0.14926570, 0.82613134],
    [0.39100535, 0.15208221, 0.83183802],
    [0.39047010, 0.15498061, 0.83747815],
    [0.38986135, 0.15796316, 0.84304623],
    [0.38917673, 0.16103195, 0.84853655],
    [0.38841370, 0.16418890, 0.85394346],
    [0.38756993, 0.16743574, 0.85926073],
    [0.38664310, 0.17077394, 0.86448201],
    [0.38563066, 0.17420477, 0.86960116],
    [0.38453036, 0.17772920, 0.87461150],
    [0.38333992, 0.18134792, 0.87950642],
    [0.38205710, 0.18506128, 0.88427925],
    [0.38067977, 0.18886934, 0.88892321],
    [0.37920609, 0.19277172, 0.89343143],
    [0.37763396, 0.19676779, 0.89779739],
    [0.37596193, 0.20085638, 0.90201425],
    [0.37418852, 0.20503600, 0.90607549],
    [0.37231248, 0.20930470, 0.90997480],
    [0.37033274, 0.21366018, 0.91370612],
    [0.36824867, 0.21809962, 0.91726363],
    [0.36605991, 0.22261982, 0.92064188],
    [0.36376637, 0.22721716, 0.92383589],
    [0.36136834, 0.23188762, 0.92684116],
    [0.35886649, 0.23662681, 0.92965374],
    [0.35626183, 0.24142998, 0.93227029],
    [0.35355578, 0.24629207, 0.93468813],
    [0.35075016, 0.25120774, 0.93690524],
    [0.34784715, 0.25617141, 0.93892038],
    [0.34484932, 0.26117733, 0.94073302],
    [0.34175962, 0.26621960, 0.94234342],
    [0.33858131, 0.27129224, 0.94375258],
    [0.33531801, 0.27638923, 0.94496228],
    [0.33197362, 0.28150458, 0.94597501],
    [0.32855229, 0.28663239, 0.94679399],
    [0.32505842, 0.29176687, 0.94742306],
    [0.32149657, 0.29690241, 0.94786670],
    [0.31787148, 0.30203359, 0.94812995],
    [0.31418802, 0.30715526, 0.94821833],
    [0.31045115, 0.31226250, 0.94813780],
    [0.30666589, 0.31735072, 0.94789469],
    [0.30283722, 0.32241567, 0.94749562],
    [0.29897012, 0.32745341, 0.94694742],
    [0.29506951, 0.33246035, 0.94625709],
    [0.29114036, 0.33743319, 0.94543177],
    [0.28718771, 0.34236889, 0.94447877],
    [0.28321595, 0.34726502, 0.94340509],
    [0.27922991, 0.35211919, 0.94221798],
    [0.27523417, 0.35692938, 0.94092451],
    [0.27123292, 0.36169401, 0.93953153],
    [0.26723067, 0.36641155, 0.93804596],
    [0.26323146, 0.37108088, 0.93647434],
    [0.25923909, 0.37570121, 0.93482297],
    [0.25525803, 0.38027156, 0.93309840],
    [0.25129160, 0.38479167, 0.93130635],
    [0.24734346, 0.38926123, 0.92945255],
    [0.24341722, 0.39368008, 0.92754256],
    [0.23951634, 0.39804823, 0.92558166],
    [0.23564420, 0.40236584, 0.92357489],
    [0.23180405, 0.40663320, 0.92152704],
    [0.22799904, 0.41085070, 0.91944265],
    [0.22423224, 0.41501886, 0.91732601],
    [0.22050662, 0.41913826, 0.91518116],
    [0.21682507, 0.42320958, 0.91301190],
    [0.21319040, 0.42723357, 0.91082182],
    [0.20960575, 0.43121089, 0.90861456],
    [0.20607384, 0.43514238, 0.90639331],
    [0.20259697, 0.43902906, 0.90416074],
    [0.19917852, 0.44287159, 0.90192024],
    [0.19582057, 0.44667107, 0.89967401],
    [0.19252612, 0.45042831, 0.89742484],
    [0.18929740, 0.45414439, 0.89517479],
    [0.18613751, 0.45782009, 0.89292647],
    [0.18304825, 0.46145661, 0.89068136],
    [0.18003276, 0.46505470, 0.88844188],
    [0.17709324, 0.46861542, 0.88620962],
    [0.17423187, 0.47213980, 0.88398607],
    [0.17145104, 0.47562878, 0.88177280],
    [0.16875338, 0.47908322, 0.87957150],
    [0.16614094, 0.48250411, 0.87738341],
    [0.16361573, 0.48589242, 0.87520962],
    [0.16117982, 0.48924908, 0.87305129],
    [0.15883517, 0.49257499, 0.87090950],
    [0.15658363, 0.49587105, 0.86878520],
    [0.15442692, 0.49913815, 0.86667929],
    [0.15236659, 0.50237715, 0.86459259],
    [0.15040406, 0.50558893, 0.86252581],
    [0.14854056, 0.50877433, 0.86047964],
    [0.14677738, 0.51193412, 0.85845487],
    [0.14511541, 0.51506911, 0.85645205],
    [0.14355511, 0.51818016, 0.85447152],
    [0.14209689, 0.52126806, 0.85251368],
    [0.14074106, 0.52433354, 0.85057900],
    [0.13948815, 0.52737725, 0.84866830],
    [0.13833726, 0.53040007, 0.84678133],
    [0.13728797, 0.53340269, 0.84491842],
    [0.13634021, 0.53638567, 0.84308039],
    [0.13549217, 0.53934989, 0.84126673],
    [0.13474325, 0.54229587, 0.83947817],
    [0.13409162, 0.54522436, 0.83771454],
    [0.13353574, 0.54813595, 0.83597610],
    [0.13307362, 0.55103129, 0.83426291],
    [0.13270316, 0.55391097, 0.83257509],
    [0.13242183, 0.55677564, 0.83091249],
    [0.13222744, 0.55962580, 0.82927553],
    [0.13211666, 0.56246216, 0.82766360],
    [0.13208733, 0.56528511, 0.82607740],
    [0.13213586, 0.56809533, 0.82451634],
    [0.13225901, 0.57089337, 0.82298029],
    [0.13245416, 0.57367961, 0.82146982],
    [0.13271734, 0.57645471, 0.81998424],
    [0.13304513, 0.57921915, 0.81852343],
    [0.13343424, 0.58197339, 0.81708747],
    [0.13388124, 0.58471789, 0.81567635],
    [0.13438230, 0.58745317, 0.81428959],
    [0.13493386, 0.59017971, 0.81292704],
    [0.13553238, 0.59289795, 0.81158853],
    [0.13617435, 0.59560833, 0.81027389],
    [0.13685643, 0.59831124, 0.80898312],
    [0.13757490, 0.60100715, 0.80771573],
    [0.13832634, 0.60369650, 0.80647148],
    [0.13910735, 0.60637968, 0.80525012],
    [0.13991462, 0.60905709, 0.80405139],
    [0.14074489, 0.61172914, 0.80287500],
    [0.14159496, 0.61439620, 0.80172068],
    [0.14246171, 0.61705867, 0.80058811],
    [0.14334208, 0.61971690, 0.79947699],
    [0.14423310, 0.62237128, 0.79838698],
    [0.14513188, 0.62502214, 0.79731775],
    [0.14603558, 0.62766986, 0.79626895],
    [0.14694145, 0.63031477, 0.79524022],
    [0.14784682, 0.63295722, 0.79423118],
    [0.14874909, 0.63559754, 0.79324145],
    [0.14964572, 0.63823605, 0.79227065],
    [0.15053437, 0.64087306, 0.79131848],
    [0.15141266, 0.64350887, 0.79038457],
    [0.15227815, 0.64614381, 0.78946838],
    [0.15312857, 0.64877820, 0.78856946],
    [0.15396170, 0.65141233, 0.78768737],
    [0.15477540, 0.65404650, 0.78682168],
    [0.15556780, 0.65668093, 0.78597216],
    [0.15633676, 0.65931593, 0.78513827],
    [0.15708014, 0.66195180, 0.78431938],
    [0.15779597, 0.66458882, 0.78351501],
    [0.15848254, 0.66722720, 0.78272488],
    [0.15913804, 0.66986719, 0.78194856],
    [0.15976034, 0.67250910, 0.78118528],
    [0.16034759, 0.67515317, 0.78043451],
    [0.16089860, 0.67779955, 0.77969628],
    [0.16141103, 0.68044856, 0.77896954],
    [0.16188308, 0.68310045, 0.77825374],
    [0.16231366, 0.68575533, 0.77754890],
    [0.16270047, 0.68841353, 0.77685396],
    [0.16304181, 0.69107524, 0.77616842],
    [0.16333657, 0.69374059, 0.77549218],
    [0.16358230, 0.69640989, 0.77482412],
    [0.16377781, 0.69908326, 0.77416406],
    [0.16392124, 0.70176092, 0.77351133],
    [0.16401060, 0.70444309, 0.77286518],
    [0.16404480, 0.70712985, 0.77222549],
    [0.16402119, 0.70982152, 0.77159105],
    [0.16393900, 0.71251810, 0.77096201],
    [0.16379543, 0.71521992, 0.77033709],
    [0.16358942, 0.71792701, 0.76971626],
    [0.16331838, 0.72063962, 0.76909845],
    [0.16298099, 0.72335781, 0.76848350],
    [0.16257460, 0.72608182, 0.76787040],
    [0.16209779, 0.72881169, 0.76725897],
    [0.16154764, 0.73154765, 0.76664813],
    [0.16092280, 0.73428972, 0.76603783],
    [0.16021981, 0.73703815, 0.76542680],
    [0.15943759, 0.73979290, 0.76481521],
    [0.15857221, 0.74255425, 0.76420171],
    [0.15762192, 0.74532217, 0.76358622],
    [0.15658330, 0.74809684, 0.76296782],
    [0.15545331, 0.75087835, 0.76234593],
    [0.15422927, 0.75366674, 0.76172021],
    [0.15290674, 0.75646218, 0.76108958],
    [0.15148307, 0.75926466, 0.76045395],
    [0.14995353, 0.76207432, 0.75981237],
    [0.14831355, 0.76489125, 0.75916412],
    [0.14655968, 0.76771541, 0.75850916],
    [0.14468546, 0.77054698, 0.75784630],
    [0.14268557, 0.77338599, 0.75717506],
    [0.14055475, 0.77623242, 0.75649523],
    [0.13828504, 0.77908642, 0.75580572],
    [0.13586902, 0.78194802, 0.75510602],
    [0.13329946, 0.78481715, 0.75439598],
    [0.13056556, 0.78769398, 0.75367452],
    [0.12765661, 0.79057852, 0.75294107],
    [0.12456163, 0.79347072, 0.75219545],
    [0.12126592, 0.79637066, 0.75143682],
    [0.11775297, 0.79927839, 0.75066449],
]

# Create ListedColormap object for this colormap
cmap = ListedColormap(cm_data, name="cmr.guppy", N=511)
cmap_r = cmap.reversed()

# Register (reversed) cmap in MPL
mpl.colormaps.register(cmap=cmap)
mpl.colormaps.register(cmap=cmap_r)
