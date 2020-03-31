from matplotlib.colors import ListedColormap

cm_type = "diverging"

cm_data = [[0.08752792, 0.05445008, 0.15633391],
           [0.09204695, 0.05639320, 0.16203897],
           [0.09650895, 0.05829607, 0.16786880],
           [0.10090870, 0.06016328, 0.17382488],
           [0.10524039, 0.06200004, 0.17990780],
           [0.10949779, 0.06381198, 0.18611729],
           [0.11367403, 0.06560565, 0.19245137],
           [0.11776199, 0.06738816, 0.19890668],
           [0.12175433, 0.06916725, 0.20547828],
           [0.12564365, 0.07095122, 0.21215945],
           [0.12942267, 0.07274885, 0.21894186],
           [0.13308433, 0.07456920, 0.22581549],
           [0.13662198, 0.07642163, 0.23276864],
           [0.14002950, 0.07831532, 0.23978863],
           [0.14330141, 0.08025937, 0.24686136],
           [0.14643291, 0.08226244, 0.25397225],
           [0.14941998, 0.08433262, 0.26110614],
           [0.15225934, 0.08647727, 0.26824775],
           [0.15494847, 0.08870295, 0.27538192],
           [0.15748551, 0.09101525, 0.28249390],
           [0.15986928, 0.09341878, 0.28956951],
           [0.16209917, 0.09591718, 0.29659525],
           [0.16417504, 0.09851308, 0.30355858],
           [0.16609723, 0.10120815, 0.31044773],
           [0.16786643, 0.10400316, 0.31725196],
           [0.16948361, 0.10689806, 0.32396152],
           [0.17095007, 0.10989202, 0.33056744],
           [0.17226726, 0.11298355, 0.33706178],
           [0.17343684, 0.11617055, 0.34343746],
           [0.17446061, 0.11945041, 0.34968818],
           [0.17534051, 0.12282010, 0.35580842],
           [0.17607859, 0.12627622, 0.36179338],
           [0.17667704, 0.12981506, 0.36763888],
           [0.17713811, 0.13343270, 0.37334141],
           [0.17746410, 0.13712505, 0.37889811],
           [0.17765753, 0.14088788, 0.38430647],
           [0.17772085, 0.14471691, 0.38956469],
           [0.17765681, 0.14860777, 0.39467122],
           [0.17746800, 0.15255614, 0.39962515],
           [0.17715730, 0.15655769, 0.40442584],
           [0.17672775, 0.16060812, 0.40907299],
           [0.17618229, 0.16470324, 0.41356679],
           [0.17552411, 0.16883893, 0.41790767],
           [0.17475650, 0.17301117, 0.42209636],
           [0.17388287, 0.17721606, 0.42613389],
           [0.17290686, 0.18144976, 0.43002153],
           [0.17183216, 0.18570864, 0.43376083],
           [0.17066251, 0.18998919, 0.43735357],
           [0.16940200, 0.19428801, 0.44080170],
           [0.16805489, 0.19860183, 0.44410739],
           [0.16662536, 0.20292760, 0.44727300],
           [0.16511815, 0.20726230, 0.45030103],
           [0.16353786, 0.21160317, 0.45319416],
           [0.16188934, 0.21594754, 0.45595518],
           [0.16017794, 0.22029285, 0.45858702],
           [0.15840893, 0.22463672, 0.46109273],
           [0.15658782, 0.22897695, 0.46347542],
           [0.15472045, 0.23331142, 0.46573832],
           [0.15281289, 0.23763816, 0.46788473],
           [0.15087146, 0.24195534, 0.46991799],
           [0.14890271, 0.24626125, 0.47184151],
           [0.14691347, 0.25055433, 0.47365872],
           [0.14491106, 0.25483305, 0.47537315],
           [0.14290279, 0.25909612, 0.47698827],
           [0.14089618, 0.26334235, 0.47850753],
           [0.13889947, 0.26757056, 0.47993450],
           [0.13692086, 0.27177976, 0.48127266],
           [0.13496883, 0.27596907, 0.48252547],
           [0.13305232, 0.28013764, 0.48369643],
           [0.13118042, 0.28428476, 0.48478897],
           [0.12936216, 0.28840987, 0.48580637],
           [0.12760751, 0.29251232, 0.48675218],
           [0.12592585, 0.29659172, 0.48762958],
           [0.12432688, 0.30064769, 0.48844181],
           [0.12282043, 0.30467992, 0.48919206],
           [0.12141630, 0.30868816, 0.48988346],
           [0.12012416, 0.31267225, 0.49051910],
           [0.11895347, 0.31663207, 0.49110196],
           [0.11791336, 0.32056757, 0.49163494],
           [0.11701255, 0.32447876, 0.49212087],
           [0.11625924, 0.32836571, 0.49256249],
           [0.11566099, 0.33222853, 0.49296243],
           [0.11522492, 0.33606732, 0.49332344],
           [0.11495702, 0.33988228, 0.49364800],
           [0.11486213, 0.34367370, 0.49393834],
           [0.11494478, 0.34744177, 0.49419705],
           [0.11520786, 0.35118683, 0.49442624],
           [0.11565340, 0.35490919, 0.49462809],
           [0.11628239, 0.35860921, 0.49480473],
           [0.11709469, 0.36228726, 0.49495819],
           [0.11808882, 0.36594380, 0.49509011],
           [0.11926311, 0.36957912, 0.49520286],
           [0.12061397, 0.37319378, 0.49529773],
           [0.12213744, 0.37678822, 0.49537642],
           [0.12382885, 0.38036291, 0.49544055],
           [0.12568303, 0.38391827, 0.49549190],
           [0.12769383, 0.38745486, 0.49553160],
           [0.12985495, 0.39097318, 0.49556102],
           [0.13215972, 0.39447374, 0.49558142],
           [0.13460127, 0.39795707, 0.49559400],
           [0.13717257, 0.40142368, 0.49559986],
           [0.13986655, 0.40487412, 0.49560002],
           [0.14267615, 0.40830893, 0.49559543],
           [0.14559445, 0.41172862, 0.49558704],
           [0.14861463, 0.41513371, 0.49557582],
           [0.15172999, 0.41852479, 0.49556227],
           [0.15493410, 0.42190240, 0.49554701],
           [0.15822077, 0.42526707, 0.49553070],
           [0.16158414, 0.42861927, 0.49551431],
           [0.16501848, 0.43195963, 0.49549772],
           [0.16851844, 0.43528863, 0.49548162],
           [0.17207896, 0.43860678, 0.49546650],
           [0.17569522, 0.44191466, 0.49545222],
           [0.17936270, 0.44521270, 0.49543967],
           [0.18307720, 0.44850150, 0.49542829],
           [0.18683470, 0.45178148, 0.49541885],
           [0.19063154, 0.45505319, 0.49541097],
           [0.19446429, 0.45831712, 0.49540465],
           [0.19832966, 0.46157369, 0.49540031],
           [0.20222478, 0.46482343, 0.49539724],
           [0.20614689, 0.46806681, 0.49539538],
           [0.21009336, 0.47130421, 0.49539508],
           [0.21406195, 0.47453613, 0.49539550],
           [0.21805055, 0.47776300, 0.49539633],
           [0.22205719, 0.48098524, 0.49539725],
           [0.22608011, 0.48420325, 0.49539786],
           [0.23011762, 0.48741741, 0.49539800],
           [0.23416837, 0.49062812, 0.49539682],
           [0.23823107, 0.49383575, 0.49539374],
           [0.24230459, 0.49704067, 0.49538818],
           [0.24638792, 0.50024322, 0.49537945],
           [0.25048021, 0.50344372, 0.49536687],
           [0.25458073, 0.50664248, 0.49534967],
           [0.25868887, 0.50983982, 0.49532705],
           [0.26280416, 0.51303600, 0.49529816],
           [0.26692622, 0.51623130, 0.49526213],
           [0.27105469, 0.51942595, 0.49521840],
           [0.27518951, 0.52262020, 0.49516568],
           [0.27933064, 0.52581426, 0.49510297],
           [0.28347814, 0.52900834, 0.49502922],
           [0.28763217, 0.53220259, 0.49494334],
           [0.29179280, 0.53539718, 0.49484473],
           [0.29596043, 0.53859225, 0.49473212],
           [0.30013555, 0.54178792, 0.49460405],
           [0.30431866, 0.54498430, 0.49445941],
           [0.30851002, 0.54818143, 0.49429795],
           [0.31271059, 0.55137942, 0.49411748],
           [0.31692102, 0.55457829, 0.49391701],
           [0.32114182, 0.55777805, 0.49369614],
           [0.32537418, 0.56097873, 0.49345256],
           [0.32961865, 0.56418028, 0.49318613],
           [0.33387640, 0.56738267, 0.49289495],
           [0.33814830, 0.57058585, 0.49257816],
           [0.34243538, 0.57378975, 0.49223461],
           [0.34673877, 0.57699426, 0.49186297],
           [0.35105947, 0.58019927, 0.49146232],
           [0.35539867, 0.58340466, 0.49103141],
           [0.35975757, 0.58661028, 0.49056899],
           [0.36413716, 0.58981597, 0.49007450],
           [0.36853902, 0.59302156, 0.48954576],
           [0.37296371, 0.59622684, 0.48898352],
           [0.37741303, 0.59943162, 0.48838510],
           [0.38188799, 0.60263568, 0.48775010],
           [0.38638958, 0.60583879, 0.48707812],
           [0.39091937, 0.60904071, 0.48636723],
           [0.39547834, 0.61224120, 0.48561706],
           [0.40006746, 0.61544001, 0.48482731],
           [0.40468823, 0.61863685, 0.48399620],
           [0.40934175, 0.62183146, 0.48312299],
           [0.41402871, 0.62502358, 0.48220800],
           [0.41875042, 0.62821291, 0.48124980],
           [0.42350802, 0.63139917, 0.48024749],
           [0.42830248, 0.63458208, 0.47920045],
           [0.43313462, 0.63776134, 0.47810840],
           [0.43800511, 0.64093668, 0.47697128],
           [0.44291513, 0.64410781, 0.47578781],
           [0.44786547, 0.64727443, 0.47455752],
           [0.45285688, 0.65043626, 0.47327996],
           [0.45789008, 0.65359301, 0.47195472],
           [0.46296570, 0.65674441, 0.47058142],
           [0.46808433, 0.65989019, 0.46915974],
           [0.47324633, 0.66303010, 0.46768979],
           [0.47845245, 0.66616385, 0.46617069],
           [0.48370315, 0.66929119, 0.46460213],
           [0.48899883, 0.67241186, 0.46298382],
           [0.49433987, 0.67552562, 0.46131548],
           [0.49972657, 0.67863224, 0.45959684],
           [0.50515923, 0.68173147, 0.45782765],
           [0.51063806, 0.68482310, 0.45600765],
           [0.51616327, 0.68790691, 0.45413659],
           [0.52173499, 0.69098269, 0.45221420],
           [0.52735335, 0.69405024, 0.45024025],
           [0.53301842, 0.69710936, 0.44821445],
           [0.53873026, 0.70015988, 0.44613656],
           [0.54448886, 0.70320160, 0.44400627],
           [0.55029423, 0.70623437, 0.44182330],
           [0.55614598, 0.70925806, 0.43958801],
           [0.56204429, 0.71227248, 0.43729959],
           [0.56798909, 0.71527748, 0.43495760],
           [0.57398027, 0.71827292, 0.43256168],
           [0.58001770, 0.72125865, 0.43011141],
           [0.58610124, 0.72423455, 0.42760637],
           [0.59223071, 0.72720048, 0.42504609],
           [0.59840589, 0.73015634, 0.42243016],
           [0.60462588, 0.73310215, 0.41975946],
           [0.61089116, 0.73603767, 0.41703201],
           [0.61720154, 0.73896279, 0.41424719],
           [0.62355679, 0.74187742, 0.41140432],
           [0.62995669, 0.74478146, 0.40850267],
           [0.63640004, 0.74767501, 0.40554339],
           [0.64288738, 0.75055785, 0.40252410],
           [0.64941862, 0.75342984, 0.39944362],
           [0.65599353, 0.75629090, 0.39630098],
           [0.66261097, 0.75914117, 0.39309691],
           [0.66927108, 0.76198049, 0.38982957],
           [0.67597411, 0.76480867, 0.38649681],
           [0.68271984, 0.76762564, 0.38309731],
           [0.68950640, 0.77043173, 0.37963294],
           [0.69633514, 0.77322649, 0.37609915],
           [0.70320587, 0.77600985, 0.37249427],
           [0.71011710, 0.77878207, 0.36881911],
           [0.71706926, 0.78154293, 0.36507064],
           [0.72406277, 0.78429221, 0.36124564],
           [0.73109609, 0.78703020, 0.35734467],
           [0.73816957, 0.78975670, 0.35336444],
           [0.74528382, 0.79247145, 0.34930088],
           [0.75243681, 0.79517489, 0.34515515],
           [0.75962972, 0.79786659, 0.34092168],
           [0.76686259, 0.80054644, 0.33659700],
           [0.77413333, 0.80321494, 0.33218183],
           [0.78144402, 0.80587139, 0.32766798],
           [0.78879297, 0.80851618, 0.32305486],
           [0.79618046, 0.81114915, 0.31833738],
           [0.80360708, 0.81377001, 0.31350943],
           [0.81107072, 0.81637931, 0.30857037],
           [0.81857375, 0.81897625, 0.30350935],
           [0.82611350, 0.82156155, 0.29832601],
           [0.83369193, 0.82413452, 0.29300924],
           [0.84130759, 0.82669553, 0.28755484],
           [0.84896098, 0.82924432, 0.28195349],
           [0.85665198, 0.83178087, 0.27619635],
           [0.86437995, 0.83430528, 0.27027480],
           [0.87214576, 0.83681719, 0.26417549],
           [0.87994802, 0.83931699, 0.25788906],
           [0.88778819, 0.84180409, 0.25139755],
           [0.89566452, 0.84427902, 0.24468901],
           [0.90357867, 0.84674113, 0.23774045],
           [0.91152892, 0.84919093, 0.23053474],
           [0.91951673, 0.85162784, 0.22304277],
           [0.92754082, 0.85405223, 0.21523836],
           [0.93560204, 0.85646372, 0.20708390],
           [0.94369997, 0.85886238, 0.19853799],
           [0.95183441, 0.86124822, 0.18954940],
           [0.96000625, 0.86362083, 0.18005051],
           [0.96821377, 0.86598077, 0.16996509],
           [0.97645964, 0.86832697, 0.15917699],
           [0.97230631, 0.86410298, 0.17137243],
           [0.96817236, 0.85988698, 0.18263638],
           [0.96405767, 0.85567890, 0.19312651],
           [0.95996213, 0.85147870, 0.20296022],
           [0.95588562, 0.84728633, 0.21222766],
           [0.95182803, 0.84310174, 0.22099977],
           [0.94778924, 0.83892487, 0.22933352],
           [0.94376913, 0.83475567, 0.23727546],
           [0.93976761, 0.83059409, 0.24486422],
           [0.93578456, 0.82644009, 0.25213222],
           [0.93181986, 0.82229360, 0.25910699],
           [0.92787341, 0.81815459, 0.26581215],
           [0.92394511, 0.81402300, 0.27226813],
           [0.92003485, 0.80989877, 0.27849272],
           [0.91614251, 0.80578186, 0.28450156],
           [0.91226801, 0.80167222, 0.29030845],
           [0.90841124, 0.79756979, 0.29592564],
           [0.90457210, 0.79347452, 0.30136410],
           [0.90075050, 0.78938625, 0.30663640],
           [0.89694634, 0.78530499, 0.31174929],
           [0.89315953, 0.78123074, 0.31671014],
           [0.88938996, 0.77716343, 0.32152624],
           [0.88563753, 0.77310302, 0.32620423],
           [0.88190217, 0.76904944, 0.33075016],
           [0.87818377, 0.76500265, 0.33516961],
           [0.87448224, 0.76096259, 0.33946772],
           [0.87079754, 0.75692907, 0.34365179],
           [0.86712956, 0.75290208, 0.34772516],
           [0.86347821, 0.74888164, 0.35169034],
           [0.85984338, 0.74486771, 0.35555111],
           [0.85622499, 0.74086022, 0.35931100],
           [0.85262297, 0.73685912, 0.36297329],
           [0.84903727, 0.73286421, 0.36654341],
           [0.84546783, 0.72887541, 0.37002416],
           [0.84191450, 0.72489282, 0.37341600],
           [0.83837720, 0.72091638, 0.37672148],
           [0.83485585, 0.71694603, 0.37994302],
           [0.83135044, 0.71298154, 0.38308526],
           [0.82786091, 0.70902282, 0.38615067],
           [0.82438708, 0.70506999, 0.38913865],
           [0.82092886, 0.70112301, 0.39205118],
           [0.81748619, 0.69718177, 0.39489074],
           [0.81405915, 0.69324586, 0.39766320],
           [0.81064746, 0.68931561, 0.40036558],
           [0.80725103, 0.68539095, 0.40299953],
           [0.80386981, 0.68147170, 0.40556804],
           [0.80050384, 0.67755756, 0.40807540],
           [0.79715283, 0.67364884, 0.41051893],
           [0.79381663, 0.66974547, 0.41290006],
           [0.79049538, 0.66584700, 0.41522459],
           [0.78718878, 0.66195364, 0.41749086],
           [0.78389662, 0.65806549, 0.41969880],
           [0.78061893, 0.65418215, 0.42185308],
           [0.77735553, 0.65030367, 0.42395422],
           [0.77410607, 0.64643026, 0.42600082],
           [0.77087060, 0.64256150, 0.42799786],
           [0.76764884, 0.63869750, 0.42994524],
           [0.76444038, 0.63483850, 0.43184168],
           [0.76124537, 0.63098390, 0.43369376],
           [0.75806321, 0.62713418, 0.43549817],
           [0.75489367, 0.62328927, 0.43725682],
           [0.75173668, 0.61944883, 0.43897390],
           [0.74859150, 0.61561344, 0.44064568],
           [0.74545821, 0.61178251, 0.44227876],
           [0.74233604, 0.60795662, 0.44386982],
           [0.73922476, 0.60413554, 0.44542227],
           [0.73612388, 0.60031940, 0.44693680],
           [0.73303281, 0.59650845, 0.44841337],
           [0.72995125, 0.59270250, 0.44985524],
           [0.72687835, 0.58890209, 0.45126027],
           [0.72381389, 0.58510691, 0.45263291],
           [0.72075691, 0.58131760, 0.45397020],
           [0.71770716, 0.57753389, 0.45527643],
           [0.71466371, 0.57375638, 0.45654907],
           [0.71162617, 0.56998498, 0.45779091],
           [0.70859383, 0.56622007, 0.45900107],
           [0.70556608, 0.56246190, 0.46017957],
           [0.70254257, 0.55871041, 0.46132829],
           [0.69952247, 0.55496631, 0.46244364],
           [0.69650587, 0.55122906, 0.46353039],
           [0.69349201, 0.54749944, 0.46458368],
           [0.69048082, 0.54377736, 0.46560431],
           [0.68747240, 0.54006263, 0.46659324],
           [0.68446651, 0.53635569, 0.46754664],
           [0.68146358, 0.53265619, 0.46846528],
           [0.67846409, 0.52896386, 0.46934874],
           [0.67546840, 0.52527879, 0.47019366],
           [0.67247734, 0.52160058, 0.47099912],
           [0.66949219, 0.51792834, 0.47176667],
           [0.66651382, 0.51426197, 0.47249216],
           [0.66354359, 0.51060077, 0.47317454],
           [0.66058303, 0.50694396, 0.47381289],
           [0.65763401, 0.50329035, 0.47440820],
           [0.65469814, 0.49963924, 0.47495810],
           [0.65177728, 0.49598959, 0.47546188],
           [0.64887336, 0.49234027, 0.47591936],
           [0.64598839, 0.48869007, 0.47633058],
           [0.64312434, 0.48503773, 0.47669587],
           [0.64028317, 0.48138199, 0.47701580],
           [0.63746686, 0.47772144, 0.47729158],
           [0.63467718, 0.47405484, 0.47752392],
           [0.63191582, 0.47038092, 0.47771389],
           [0.62918439, 0.46669840, 0.47786301],
           [0.62648439, 0.46300599, 0.47797295],
           [0.62381715, 0.45930246, 0.47804556],
           [0.62118390, 0.45558657, 0.47808287],
           [0.61858584, 0.45185702, 0.47808744],
           [0.61602380, 0.44811279, 0.47806093],
           [0.61349857, 0.44435278, 0.47800543],
           [0.61101081, 0.44057593, 0.47792309],
           [0.60856108, 0.43678123, 0.47781598],
           [0.60614979, 0.43296770, 0.47768617],
           [0.60377775, 0.42913395, 0.47753704],
           [0.60144495, 0.42527927, 0.47736966],
           [0.59915143, 0.42140290, 0.47718541],
           [0.59689760, 0.41750361, 0.47698690],
           [0.59468383, 0.41358024, 0.47677644],
           [0.59250953, 0.40963243, 0.47655396],
           [0.59037564, 0.40565836, 0.47632320],
           [0.58828141, 0.40165778, 0.47608359],
           [0.58622750, 0.39762903, 0.47583796],
           [0.58421330, 0.39357166, 0.47558598],
           [0.58223972, 0.38948372, 0.47533061],
           [0.58030586, 0.38536492, 0.47507075],
           [0.57841241, 0.38121345, 0.47480850],
           [0.57655944, 0.37702803, 0.47454448],
           [0.57474666, 0.37280766, 0.47427844],
           [0.57297432, 0.36855083, 0.47401098],
           [0.57124263, 0.36425593, 0.47374248],
           [0.56955195, 0.35992123, 0.47347328],
           [0.56790244, 0.35554510, 0.47320318],
           [0.56629420, 0.35112584, 0.47293172],
           [0.56472785, 0.34666127, 0.47265897],
           [0.56320351, 0.34214951, 0.47238401],
           [0.56172146, 0.33758850, 0.47210589],
           [0.56028194, 0.33297609, 0.47182336],
           [0.55888586, 0.32830936, 0.47153590],
           [0.55753367, 0.32358572, 0.47124193],
           [0.55622551, 0.31880273, 0.47093915],
           [0.55496240, 0.31395695, 0.47062611],
           [0.55374496, 0.30904514, 0.47030041],
           [0.55257347, 0.30406426, 0.46995879],
           [0.55144881, 0.29901043, 0.46959832],
           [0.55037180, 0.29387961, 0.46921543],
           [0.54934312, 0.28866767, 0.46880585],
           [0.54836331, 0.28337036, 0.46836450],
           [0.54743281, 0.27798325, 0.46788553],
           [0.54655335, 0.27250023, 0.46736366],
           [0.54572418, 0.26691752, 0.46679015],
           [0.54494611, 0.26122929, 0.46615697],
           [0.54421965, 0.25542966, 0.46545463],
           [0.54354471, 0.24951304, 0.46467190],
           [0.54292042, 0.24347433, 0.46379561],
           [0.54234547, 0.23730858, 0.46281089],
           [0.54181850, 0.23101058, 0.46170127],
           [0.54133660, 0.22457662, 0.46044762],
           [0.54089573, 0.21800426, 0.45902849],
           [0.54048993, 0.21129340, 0.45741984],
           [0.54011135, 0.20444658, 0.45559554],
           [0.53974974, 0.19747001, 0.45352766],
           [0.53939197, 0.19037462, 0.45118730],
           [0.53902216, 0.18317655, 0.44854603],
           [0.53862106, 0.17589851, 0.44557755],
           [0.53816743, 0.16856853, 0.44226005],
           [0.53763832, 0.16122001, 0.43857839],
           [0.53701068, 0.15388966, 0.43452608],
           [0.53626319, 0.14661471, 0.43010623],
           [0.53537752, 0.13943055, 0.42533151],
           [0.53433952, 0.13236830, 0.42022284],
           [0.53313977, 0.12545307, 0.41480732],
           [0.53177340, 0.11870344, 0.40911581],
           [0.53023966, 0.11213143, 0.40318059],
           [0.52854096, 0.10574340, 0.39703360],
           [0.52668202, 0.09954118, 0.39070529],
           [0.52466926, 0.09352285, 0.38422348],
           [0.52250991, 0.08768408, 0.37761339],
           [0.52021160, 0.08201884, 0.37089742],
           [0.51778203, 0.07652007, 0.36409532],
           [0.51522862, 0.07118027, 0.35722460],
           [0.51255860, 0.06599163, 0.35030011],
           [0.50977863, 0.06094655, 0.34333528],
           [0.50689496, 0.05603766, 0.33634148],
           [0.50391330, 0.05125798, 0.32932918],
           [0.50083896, 0.04660102, 0.32230706],
           [0.49767676, 0.04206078, 0.31528306],
           [0.49443108, 0.03764276, 0.30826420],
           [0.49110593, 0.03356397, 0.30125676],
           [0.48770496, 0.02984242, 0.29426634],
           [0.48423146, 0.02645180, 0.28729801],
           [0.48068844, 0.02336814, 0.28035634],
           [0.47707863, 0.02056959, 0.27344554],
           [0.47340452, 0.01803618, 0.26656945],
           [0.46966836, 0.01574960, 0.25973167],
           [0.46587219, 0.01369308, 0.25293551],
           [0.46201789, 0.01185122, 0.24618404],
           [0.45810716, 0.01020982, 0.23948016],
           [0.45414154, 0.00875572, 0.23282671],
           [0.45012244, 0.00747681, 0.22622625],
           [0.44605117, 0.00636181, 0.21968130],
           [0.44192891, 0.00540022, 0.21319431],
           [0.43775674, 0.00458224, 0.20676758],
           [0.43353569, 0.00389871, 0.20040338],
           [0.42926666, 0.00334101, 0.19410391],
           [0.42495054, 0.00290101, 0.18787129],
           [0.42058814, 0.00257104, 0.18170764],
           [0.41618023, 0.00234379, 0.17561497],
           [0.41172753, 0.00221230, 0.16959531],
           [0.40723076, 0.00216991, 0.16365061],
           [0.40269059, 0.00221024, 0.15778278],
           [0.39810772, 0.00232709, 0.15199371],
           [0.39348279, 0.00251448, 0.14628522],
           [0.38881650, 0.00276662, 0.14065906],
           [0.38410952, 0.00307780, 0.13511698],
           [0.37936257, 0.00344249, 0.12966061],
           [0.37457637, 0.00385525, 0.12429151],
           [0.36975169, 0.00431070, 0.11901117],
           [0.36488933, 0.00480356, 0.11382099],
           [0.35999013, 0.00532862, 0.10872222],
           [0.35505497, 0.00588075, 0.10371602],
           [0.35008480, 0.00645486, 0.09880340],
           [0.34508059, 0.00704595, 0.09398521],
           [0.34004340, 0.00764909, 0.08926215],
           [0.33497431, 0.00825943, 0.08463472],
           [0.32987446, 0.00887226, 0.08010324],
           [0.32474504, 0.00948294, 0.07566780],
           [0.31958729, 0.01008700, 0.07132830],
           [0.31440248, 0.01068007, 0.06708440],
           [0.30919190, 0.01125804, 0.06293552],
           [0.30395689, 0.01181694, 0.05888084],
           [0.29869880, 0.01235296, 0.05491933],
           [0.29341896, 0.01286266, 0.05104966],
           [0.28811873, 0.01334278, 0.04727029],
           [0.28279946, 0.01379025, 0.04357948],
           [0.27746243, 0.01420247, 0.03996876],
           [0.27210897, 0.01457691, 0.03650532],
           [0.26674028, 0.01491157, 0.03329780],
           [0.26135760, 0.01520452, 0.03032903],
           [0.25596200, 0.01545438, 0.02758269],
           [0.25055465, 0.01565982, 0.02504343],
           [0.24513648, 0.01582004, 0.02269678],
           [0.23970842, 0.01593445, 0.02052915],
           [0.23427137, 0.01600264, 0.01852784],
           [0.22882608, 0.01602462, 0.01668094],
           [0.22337319, 0.01600063, 0.01497736],
           [0.21791331, 0.01593113, 0.01340679],
           [0.21244693, 0.01581682, 0.01195962],
           [0.20697446, 0.01565863, 0.01062697],
           [0.20149620, 0.01545767, 0.00940060],
           [0.19601235, 0.01521528, 0.00827290],
           [0.19052302, 0.01493295, 0.00723683],
           [0.18502821, 0.01461235, 0.00628594],
           [0.17952783, 0.01425529, 0.00541426],
           [0.17402172, 0.01386364, 0.00461633],
           [0.16850954, 0.01343953, 0.00388712],
           [0.16299085, 0.01298517, 0.00322204]]

test_cm = ListedColormap(cm_data, name="primary")
