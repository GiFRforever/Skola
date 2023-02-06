import sys, time, os, math as mt

tělesa: list[str] = [
    "_exit_",
    "krychle",
    "kvádr",
    "hranol",
    "jehlan",
    "kužel",
    "válec",
    "koule",
    "torus",
    "*komolá tělesa",
    "*pravidelné mnohostěny",
]

komolá_tělesa: list[str] = [
    "_zpět_",
    "komolý jehlan",
    "komolý kužel",
]

mnohostěny: list[str] = [
    "_zpět_",
    "čtyřstěn",
    "osmistěn",
    "dvanáctistěn",
    "dvacetistěn",
]

druhý_pád: dict[str, str] = {
    "krychle": "krychle",
    "kvádr": "kvádru",
    "hranol": "hranolu",
    "jehlan": "jehlanu",
    "kužel": "kužele",
    "válec": "válce",
    "koule": "koule",
    "torus": "torusu",
    "komolý jehlan": "komolého jehlanu",
    "komolý kužel": "komolého kužele",
    "čtyřstěn": "čtyřstěnu",
    "osmistěn": "osmistěnu",
    "dvanáctistěn": "dvanáctistěnu",
    "dvacetistěn": "dvacetistěnu",
}

koule: list[str] = [
    "                              ",
    "             ....             ",
    "       :~!7????77!!~^:.       ",
    "    .!J555555YYJ??77!!~^:     ",
    "   ~YPPGBBBGGP5YJJ?77!~~~^.   ",
    "  !55PGB#&&#BGP5YJ?77!!~~^^.  ",
    " .JY5PGGBBBBGP5\033[95m|–––––––––––|  r\033[0m",
    " .?JYY55PPP55YYJJ?77!!~~^^^:  ",
    "  ^???JJJJJJJJ??77!!~~^^^^^.  ",
    "   ^!7777777777!!!~~^^^^^:.   ",
    "    .:~!!!!!!~~~~^^^^^^:.     ",
    "       .::^^^^^^^::::.        ",
    "                              ",
]

kvádr: list[str] = [
    "                                        ",
    "    .:...............................:^ ",
    "  .:.:                              :.^ ",
    " ^:..^............................\033[93m:\033[0m:  : ",
    ".:  .:                            \033[93m:\033[0m   : ",
    " :   :                            \033[93m:\033[0m   : ",
    " :   :                            \033[93m: c\033[0m : ",
    " :   :                            \033[93m:\033[0m   : ",
    " :   :                            \033[93m:\033[0m   :.",
    " :  ::............................\033[93m^\033[0m..\033[93m:^\033[0m ",
    " ^.:                              \033[93m:.:.  b\033[0m",
    " \033[93m^:...............................:.\033[0m    ",
    "                 \033[93ma\033[0m                       ",
]

hranol: list[str] = [
    "          ........................  ..  ",
    "        ..Y.                       .^!  ",
    "      .:  ^                      ..  ^  ",
    "    ..    ^                    ..    ^  ",
    "  :^.     ^                  ..      ^  ",
    "  ~..........................\033[96m~\033[0m       ^  ",
    "  :       ^                  \033[96m^\033[0m       ^  ",
    "  :       ^                  \033[96m^\033[0m       ^  ",
    "  :       ^                  \033[96m^\033[0m       ^  ",
    "  :       ^                  \033[96m^\033[0m       ^  ",
    "  :       ^                  \033[96m^\033[0m       ^  ",
    "  :       ^                  \033[96m^\033[0m       ^  ",
    "  :       ^                  \033[96m^ h\033[0m     ^  ",
    "  :       ^                  \033[96m^\033[0m       ^  ",
    "  :       ^                  \033[96m^\033[0m       ^  ",
    "  :       ^                  \033[96m^\033[0m       ^  ",
    "  :       ^                  \033[96m^\033[0m       ^  ",
    "  :       !:................:\033[96m7\033[0m......:!  ",
    "  :     .:                   \033[96m~\033[0m    .:^.  ",
    "  :   ::                     \033[96m^\033[0m   .:     ",
    "  : :.                       \033[96m^\033[0m .:       ",
    "  \033[93m7^. .......................\033[96m!\033[0m.         ",
    "              \033[93ma\033[0m                         ",
]

jehlan: list[str] = [
    "                                        ",
    "                   \033[96mT\033[0m                   ",
    "                  :\033[96m|\033[0m:                  ",
    "                 .?\033[96m|\033[0mJ.                 ",
    "                .!^\033[96m|\033[0m~~^                ",
    "               .~^ \033[96m|\033[0m:^:^               ",
    "               ~:: \033[96m|\033[0m ! .~.             ",
    "              ~.^  \033[96m|\033[0m ^: .~:            ",
    "             ~.:.  \033[96m|\033[0m .~   ^^           ",
    "            ~. ^   \033[96m|\033[0m  ~.   :^          ",
    "           ~. :.   \033[96m|\033[0m  :~    .~.        ",
    "          ~. .^    \033[96m|\033[0m   !.    .~:       ",
    "         ~.  :.    \033[96m| h\033[0m ^^      ^^      ",
    "        ~:  .:     \033[96m|\033[0m    !       :^     ",
    "       ~:   ^      \033[96m|\033[0m    ^:       .~.   ",
    "      ~:   .:      \033[96m|\033[0m    .~         ~.  ",
    "     ~:   .~:... : \033[96m|\033[0m:... !.: .... . 7~ ",
    "    ~:  .:         \033[96m|\033[0m     :~      .^^^. ",
    "   ^: .:           \033[96m⊥\033[0m      ~    .:^.    ",
    "  ^^.:                   ^^ :^:.      ",
    " \033[93m!7:::::::::::::::::::::::7^:\033[0m         ",
    "              \033[93ma\033[0m                       ",
]

komolý_jehlan: list[str] = [
    "                                                        ",
    "\033[32m  horní      \033[0m,,,,:::\033[96mT\033[0m^^^^^^^^::         ",
    "\033[32mpodstava ::::,,,,^,,\033[96m|\033[32m,~\033[0m...::'''.^.       ",
    "        :^      :.  \033[96m|\033[0m :^         ^:      ",
    "       :^      ..   \033[96m|\033[0m  ~.         :^     ",
    "      ^^      .:    \033[96m|\033[0m  .~          .^.   ",
    "     ^:       :     \033[96m|\033[0m   ^:           ^:  ",
    "    ^:       :      \033[96m| h\033[0m  ~            :^ ",
    "   ^:       :.......\033[96m|\033[0m.. .:~ . . . . . .^!",
    "  ^.    ...         \033[96m|\033[0m     ^:      ..:::'",
    " ^.  . .            \033[96m⊥\033[0m     ~   ..:::'    ",
    "\033[33m7^:::.....................^~:\033[0m::'        ",
    "      \033[33mspodní podstava\033[0m                   ",
]

krychle: list[str] = [
    "                             ",
    "    .:..................:^ ",
    "  .:.:                 :.^ ",
    " ^:..^...............\033[93m:\033[0m:  : ",
    ".:  .:               \033[93m:\033[0m   : ",
    " :   :               \033[93m:\033[0m   : ",
    " :   :               \033[93m: a\033[0m : ",
    " :   :               \033[93m:\033[0m   : ",
    " :   :               \033[93m:\033[0m   :",
    " :  ::...............\033[93m:\033[0m...\033[93m:\033[0m ",
    " ^.:                 \033[93m: .'  \033[93ma\033[0m",
    " \033[93m^:..................:'\033[0m    ",
    "            \033[93ma\033[0m               ",
]

kužel: list[str] = [
    "                                                  ",
    "                          \033[96m::\033[0m                      ",
    "                         :\033[96m~~\033[0m:                     ",
    "                       .^.\033[96m::\033[0m.^                    ",
    "                      :^  \033[96m..\033[0m :^                   ",
    "                     ^:   \033[96m..\033[0m  .^                  ",
    "                   .^.    \033[96m..\033[0m   .^.                ",
    "                  :^      \033[96m..\033[0m     ~.               ",
    "                 ^:       \033[96m..\033[0m      ^:              ",
    "               .^.        \033[96m..\033[0m       ^:             ",
    "              :^          \033[96m..   h\033[0m    :^            ",
    "             ^:           \033[96m..\033[0m         :^           ",
    "           .^.            \033[96m..\033[0m          .^.         ",
    "          :^              \033[96m..\033[0m           .^.        ",
    "         ^:               \033[96m..\033[0m             ^:       ",
    "       .^.                \033[96m..\033[0m              ^:      ",
    "      :^                  \033[96m:.\033[0m               :^     ",
    "     ^:           ....... \033[96m::\033[0m .....          :^    ",
    "   .^.  ......''''        \033[96m..\033[0m      ''''.....  .~   ",
    "  :^..''                  \033[96m..\033[0m               ''..~: ",
    " ~:                       \033[96m.\033[95m.....................!^\033[0m",
    " ^:                                \033[95mr\033[0m            .^:",
    "  .^::..                                   ..:^:. ",
    "     ''::::::........         .......:::::::''    ",
    "            '''''::::::::::::::::'''''           ",
]

komolý_kužel: list[str] = [
    "                                        ",
    "            .:^~~~~\033[96m–\033[0m~~~~^^.             ",
    "          !~:.     \033[96m|\033[0m\033[31m–––––––|\033[0m?:          ",
    "         JY~.      \033[96m|\033[0m   \033[31mr2\033[0m ..?P^         ",
    "        J:  ::^^^^^^^^^^^^:.  J:        ",
    "       J^          \033[96m|\033[0m           J:       ",
    "      ?~           \033[96m|\033[0m            Y.      ",
    "     7!            \033[96m| h\033[0m           Y.     ",
    "    !!             \033[96m|\033[0m              Y.    ",
    "   ~?              \033[96m|\033[0m               Y.   ",
    "  ^?  .:^^^^^^^^:::\033[96m|\033[0m:::^^^^^^^^::. .J   ",
    " :B~^^:.           \033[96m|\033[0m            .:^^7G  ",
    ":5:                \033[96m|\033[0m                 ~Y.",
    "J~                 \033[95m+–––––––––––––––––––|\033[0m",
    " ^~:.                       \033[95mr1\033[0m     .^!: ",
    "   .:^~^::...              ..::^^^^:.   ",
    "         ..::^^^^^^^^^^^^^::...         ",
]

torus: list[str] = [
    """               @@@@@@@@@@               """,
    """          $$$$$#$######$#$$$$$          """,
    """       $$$##**************##$$$         """,
    """     #####***!!!!!!!!!!!!!!***#####     """,
    """    ###***!!!!=;;;:::;;;;=!!!!***###*   """,
    """  !*#***!!!==;::~------~::;==!!****#**  """,
    """  ******!!=;:~-,........,-~:;=!!******  """,
    """ !*****!!==:~-............-~:==!!*****! """,
    """ !*****!!=;:~,..        ..,~:;=!!*****! """,
    """;!!*****!!==~-.    \033[95mT\033[0m   \033[31mr  |––––––|\033[0m****!!;""",
    """:=!*******!!=;~  \033[95mR |\033[0m     ~;=!!*******!=:""",
    """:=!!*********!!=   \033[95m|\033[0m    =!!*********!!=:""",
    """ ;=!****#########**\033[95m|\033[0m!**#########****!=; """,
    """ ~;!!!***###$$$$$$@\033[95m|\033[0m@@$$$$$$###***!!!;~ """,
    """  ~;=!!***###$$$$@@\033[95m|\033[0m@@@@$$$###****!=;~  """,
    """   ~:;=!*****##$$$$\033[95m⊥\033[0m$$$$$##*****!=;:~   """,
    """    ,:;=!!******########*****!==;:.    """,
    """      ,~:;=!!*************!!=;:~,      """,
    """        ,~:;;===========;;:~,.         """,
    """           .,,-~~:::~~-,,.             """,
]

válec: list[str] = [
    "                                                  ",
    "               .....::::::::::.....               ",
    "         ..:....                  ....:..         ",
    "     .::.                                .::.     ",
    "   ::.                                      .::   ",
    " .^                                            ^. ",
    " !                                              ! ",
    ":!                      \033[96m––\033[0m                      !:",
    ".5.                     \033[96m||\033[0m                     .5.",
    ":^.^.                   \033[96m||\033[0m                   .^:^:",
    ":^  .:..                \033[96m||\033[0m                ..:.  ^:",
    ":^     ..:...           \033[96m||\033[0m           ...:..     ^:",
    ":^          ....:.......^^............          ^:",
    ":^                      \033[96m||\033[0m                      ^:",
    ":^                      \033[96m||\033[0m                      ^:",
    ":^                      \033[96m||\033[0m                      ^:",
    ":^                      \033[96m||\033[0m                      ^:",
    ":^                      \033[96m|| h\033[0m                    ^:",
    ":^                      \033[96m||\033[0m                      ^:",
    ":^                      \033[96m||\033[0m                      ^:",
    ":^                      \033[96m||\033[0m                      ^:",
    ":^                      \033[96m||\033[0m                      ^:",
    ":^          ....:.......\033[96m||\033[0m............          ^:",
    ":^     ..:...           \033[96m||\033[0m           ...:..     ^:",
    ":^  .:..                \033[96m||\033[0m                ..:.  ^:",
    ":^:^.                   \033[96m||\033[0m                   .^:^:",
    ".5.                     \033[96m||\033[0m                     .5.",
    ":!                      \033[96m|\033[95m|=======================|\033[0m",
    " !                               \033[95mr\033[0m              7 ",
    " .^                                            ^. ",
    "   ::.                                      .::   ",
    "     .::.                                .::.     ",
    "         ..:....                  ....:..         ",
    "               .....::::::::::.....               ",
]
# platónská tělesa

čtyřstěn: list[str] = [
    "                                                         ",
    "                        \033[93m:GG\033[0m~                             ",
    "                     ~JB\033[93m@~\033[0m?G7                            ",
    "                  .7Y~ \033[93m?#\033[0m   ?G?                          ",
    "                ~5J.   \033[93m#!\033[0m     !P?.                       ",
    "             .!5?.    \033[93m:@.\033[0m       ^5Y.                     ",
    "           .?J^       \033[93mPG\033[0m          :Y5^                   ",
    "         ~5?.         \033[93m&!\033[0m            .Y5^                 ",
    "      .JP7           \033[93m:&\033[0m               .JP~               ",
    "    :Y5^             \033[93mG5\033[0m                  75!             ",
    "  ~5?.               \033[93m&~\033[0m                    !P?.          ",
    "Y@#^ ^^  ..         \033[93m~@\033[0m                       ~GY.        ",
    ".#P  .:  ^!: .7!  ~7\033[93m#Y\033[0m ^^   ..                 ^5J.      ",
    "  YB.              \033[93m.&:\033[0m ..   !^  :?^  ~!.  .^:    ^5Y:    ",
    "   ~#^             \033[93m!&\033[0m                 .   .::   :77&@~   ",
    "    .BY            \033[93mGP\033[0m                         .~7?7:     ",
    "      YB.         \033[93m.@^\033[0m                     .~?J7^.        ",
    "       ^#!        \033[93m?&\033[0m                  .^?Y?^.            ",
    "        .G5       \033[93m#P\033[0m              .^7J?^.                ",
    "          ?B.    \033[93m:@^\033[0m          .^7J7^.                    ",
    "           :B?   \033[93m5&\033[0m       .~?J7:.                        ",
    "             5G  \033[93m@?\033[0m   .~?J7^.                            ",
    "              7B5\033[93m@!\033[0m~JJ7^.                                ",
    "               :\033[93mPP\033[0m?^.                                    ",
]
osmistěn: list[str] = [
    "                                                                           ",
    "                          .J\033[93m&B\033[0m~                             ",
    "                        ~5YYP\033[93m&\033[0mYYJ.                          ",
    "                     .75?.:~ \033[93m7G\033[0m :?Y~                        ",
    "                   ^JY^   .   \033[93mB~\033[0m   !57.                     ",
    "                .!Y!.    ~^   \033[93m:&\033[0m     :JY^                   ",
    "              :?J^      7~     \033[93mP?\033[0m      .!Y!.                ",
    "            !Y!.       ..      \033[93m.&\033[0m         ^J?:              ",
    "         .??^          7.       \033[93mYY\033[0m          .?Y~            ",
    "       ~J7.           J.         \033[93m#:\033[0m            !5J.         ",
    "    .7J^      . .~:.75P~. :~ .!. \033[93m5G\033[0m   .          ^YY^       ",
    "  ^YJ: .: ~^ .!. :   :!       .  \033[93m.BY\033[0m..!:.7~ .!: .. ~B#~     ",
    ".#@&BY!?!:^..         ~~          \033[93m.#\033[0m        .:^~JY?P@@J     ",
    " .J#5^.:^^^^~!!!!!777!?Y7!~~^^^^::.\033[93mBY\033[0m.^~!7?77~^:.:?5!       ",
    "    ^YY:               ^^....:::^^^B&!^:.      :JY:         ",
    "      .J57.            :5         ^#.        ~J?.           ",
    "         ^5Y^           !^       ^#.      .JY^              ",
    "           .7Y7.         7      :&:     ^5Y:                ",
    "              ^5J:       !~    .&:    ~Y7.                  ",
    "                .7Y!.    .Y   .&^  .?Y^                     ",
    "                   :?J^   ^~ .#~ ~Y7.                       ",
    "                      ~Y?. :.#P?P!                          ",
    "                        :JYG@@5^                            ",
    "                           !!.                              ",
    "                                                            ",
    "                                                            ",
]
šestistěn: list[str] = [
    "                                                        ",
    "                ...................................     ",
    "             ^5&G!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!Y&@J   ",
    "           7GJ.:.                              :YY:GG   ",
    "        :JG7   ?7                           .!5J.  PG   ",
    "      !PY:     :.                         ^Y5^     GG   ",
    "   .JP7        J^                       75J.       BY   ",
    " ^BB!.         ^:                    :5G!          #!   ",
    "B&Y7!!7777!!!!!J?!!!!!!!!!!!!!!!!!!!G@~            &~   ",
    "&J             J.                   ?@             &!   ",
    "#?             ~.                   ?@             &~   ",
    "#?             Y.                   J&             &^   ",
    "#?             !                    J#             @^   ",
    "#?             J                    YB            .@^   ",
    "#?            .Y                    5B            .@^   ",
    "&?             7                    5P            .@:   ",
    "&?            :&!.^~: :^  :~.  :~: .#B .~.  ^:  :^?@.   ",
    "&?          .Y5^: .:. ..  .:   .:.  #G  :   ..  J&G^    ",
    "@7        !^ .                      BY        ?G?.      ",
    "@7     :..!                         #5     :YP!         ",
    "@~  .^.7.                           #Y   7PY:           ",
    "@!  7~                              #Y.YG?.             ",
    "\033[93m@@&7~~!~~~~~~~~~~~~!!!!7777777777777#&P^\033[0m ",
    "                                                        ",
    "                                                        ",
    "                                                        ",
]
dvanáctistěn: list[str] = [
    "                                                            ",
    "                                                            ",
    "                      ..^~7?7B5?7!^..                       ",
    "             ..:^~!!7!~^:.   &~  .:^~!7!^:.                 ",
    "           ~YG5^..           #~         .:~!?P7             ",
    "         !5!  ~!.            &!            .!:!5!           ",
    "      .7J~     .^~.      .^?Y?JY!.       :!^    ^5!         ",
    "    .7Y:         YG^:^J7Y?^.^: ^Y?PG^ ^^57        ~5!       ",
    "  .YJ:          .5::7?~.           :7?~.:!          !5~     ",
    " 5B~           .JY!:                  :!?5?          .5#:   ",
    " &!~77~^.  .~?JG!                        .557^.:^~!!7!^5#   ",
    " #    .:~!5&^ ^~                          .^.Y&!^.     !B   ",
    " &.        B~:7                            ~^B^        J5   ",
    " &:         #J                              B7         P7   ",
    " #^         :B:                            ?G?         #:   ",
    " G~      ..G^.B:                          ^B .?.       &:   ",
    " !#~~ :. :.::!!B.                        .&^ 7!:^^ ^^.~@:   ",
    "  7G.          ^&:                      .BY:         ?&7    ",
    "   .P~          ~#7! .              .~ :#J         .5?      ",
    "     JY          \033[93mBG77P5?G57!!!~!?JJ!Y5!J@:\033[0m       .YY.",
    "      ^P:      ~5~      :!....^^7^      :G7     ?P:         ",
    "       .5J   ~5^            ?Y:           ~5: ?P^           ",
    "         ?P?B7              ^!            .!&G~             ",
    "          .77!77!!^^..      :~     .:~!77!!^.               ",
    "                 ..::^^!!7~^YP^777~^:.                      ",
    "                           ....                             ",
    "                                                            ",
]
dvacetistěn: list[str] = [
    "                                                             ",
    "                       .^~5##&#?^.                           ",
    "                  .^!7!^!P5.~^!G7^!7~.                       ",
    "             .^!7!^:   !J.  :7 .Y?  .^77~:                   ",
    "        :^!77^.      757:  ^J#!.:~P~    .:~7~:.              ",
    "   :7?YY^~^ ~..^ .^7P!  . .!..7^.  JG::!  ~..!!J?~.          ",
    "  ~@#:           ^5!     .:.   !~   .PJ   . .: .!^YGP!       ",
    "  PP?P7.       :57     :~:      ~^.   ~5~        .~GB&       ",
    "  B~ :?J?.   .JJ.      ^.        .7.    JP.   .~7J5..B       ",
    "  G.  :!^?J:JP:      ?~            Y:    ^P?^??:^~. :G       ",
    "  B    .:.Y\033[93m@@Y!77!!BY!!777777!!!!!!!7G!~~~B@\33[0m#  :~.  ^J       ",
    " .#      ##..P^  .!:                  7:.5! ?Y.^    ~J       ",
    " :B     5!^^. ?7^..                   .Y#:  .5P     ?Y       ",
    " ~P   .B~   !..?#.                   :5~~: .! ?5    5Y       ",
    " JJ  ^G:    ^P&P:YJ :7 :! .7. ~! :!.7#: ~5BP   ?Y   P?       ",
    " P! ?P   ~:.: .Y~ J?              ~P^   .7..~^  75  P!       ",
    " #?Y5  7.:      ^: ~5.           ?J    ?.     !^ ?5 5~       ",
    " &@J:!           :: .5~        ~5^   7^         ^^J?5^       ",
    " !PBG5J~:..        ~. J?     .YJ   ~!             7@@.       ",
    "    .~J55Y?7!!~^^:. 7^ ^5.  !5.  .7.  ...:^^!?J5GBPJ^        ",
    "         .^!7!^:..:^~7J!7#Y#G^^??7?~^^::^~7?J7^:.            ",
    "             .:~!!^.   :!.&!.^~..  .:~!!!^.                  ",
    "                  :~77!^^:&.:~7^!7!~:.                       ",
    "                      .^!G#PB!^:.                            ",
]

# vrací velikost konzole
velikost = lambda: os.get_terminal_size()[0]

# čištění konzole
clear = lambda: os.system("cls")


def clean(n) -> None:
    for _ in range(n):
        sys.stdout.write("\033[F")
        sys.stdout.write("\033[K")


def clean2(n) -> None:
    sys.stdout.write("\033[F")
    print(" " * n, end="\r")


# vstupy
def vstup_float(txt) -> float:
    while True:
        a: str = ""
        try:
            return float(a := input(txt))
        except:
            clean2(len(txt) + len(a))
            print("\033[93mChybný vstup\033[0m", end="\r")
            time.sleep(1)


def vstup_float_min(txt, min) -> int:
    while True:
        a: str = ""
        try:
            if int((a := input(txt))) > min:
                return int(a)
            raise ValueError
        except:
            clean2(len(txt) + len(a))
            print("\033[93mChybný vstup\033[0m", end="\r")
            time.sleep(1)


# zadávání rozměrů těles
def zadejte_strany(
    *args, počet_stran=0, výška=0, poloměr=0, kolikastranný=0, **kwargs
) -> None:
    for a in args:
        if type(a) == tuple:
            rozměry[a[0]] = vstup_float(f"Zadejte \033[{str(a[1])}m{a[0]}: ")
            print("\033[0m", end="")
        else:
            rozměry[a] = vstup_float(f"Zadejte \033[93m{a}: ")
            print("\033[0m", end="")
    if kolikastranný:
        rozměry["kolikastranný"] = vstup_float_min("Zadejte kolikati je stranný: ", 2)

    if počet_stran:
        rozměry["strany"] = [
            x
            for n in range(počet_stran)
            for x in [vstup_float_min(f"Zadejte stranu \033[93m{chr(n+97)}: ", 0)]
            if not print("\033[0m", end="")
        ]
    if výška:
        rozměry["výška"] = vstup_float("Zadejte \033[96mvýšku: ")
        print("\033[0m", end="")
    if poloměr:
        rozměry["poloměr"] = vstup_float("Zadejte \033[95mpoloměr: ")
        print("\033[0m", end="")


# výpočet oběmu a povrchu
class ED:
    def __init__(self, těleso="") -> None:
        self.těleso: str = těleso
        self.oběm: float = 0
        self.povrch: float = 0
        try:
            if len(globals()[self.těleso.replace(" ", "_")][0]) + 40 > velikost():
                raise Exception
            for line in globals()[self.těleso.replace(" ", "_")]:
                print(40 * " " + line)
            for _ in range(len(globals()[self.těleso.replace(" ", "_")])):
                sys.stdout.write("\033[F")
        except:
            pass
        print(f"\n\033[95m{self.těleso.capitalize()}\033[0m\n")

    def output(self) -> None:
        print(
            f"\n\033[95mOběm\033[0m   {druhý_pád[self.těleso]} je: \033[96m{round(self.oběm, 4)}\033[0m"
        )
        print(
            f"\033[95mPovrch\033[0m {druhý_pád[self.těleso]} je: \033[96m{round(self.povrch, 4)}\033[0m"
        )
        input("\nStiskni enter pro pokračování...")
        # sys.stdout.write("\033[F")
        # print("\033[33m" + "─" * 32 + "\033[0m")
        clear()

    # obecná tělesa

    def krychle(self) -> None:
        zadejte_strany(počet_stran=1)
        self.oběm = rozměry["strany"][0] ** 3
        self.povrch = 6 * rozměry["strany"][0] ** 2
        self.output()

    def kvádr(self) -> None:
        zadejte_strany(počet_stran=3)
        self.oběm = rozměry["strany"][0] * rozměry["strany"][1] * rozměry["strany"][2]
        self.povrch = 2 * (
            rozměry["strany"][0] * rozměry["strany"][1]
            + rozměry["strany"][0] * rozměry["strany"][2]
            + rozměry["strany"][1] * rozměry["strany"][2]
        )
        self.output()

    def hranol(self) -> None:
        zadejte_strany(počet_stran=1, výška=1, kolikastranný=1)
        self.oběm = (
            rozměry["kolikastranný"]
            * rozměry["výška"]
            * rozměry["strany"][0] ** 2
            / (4 * mt.tan(mt.pi / rozměry["kolikastranný"]))
        )
        self.povrch = rozměry["kolikastranný"] * rozměry["strany"][0] * rozměry[
            "výška"
        ] + rozměry["kolikastranný"] * rozměry["strany"][0] ** 2 / (
            2 * mt.tan(mt.pi / rozměry["kolikastranný"])
        )
        self.output()

    def jehlan(self) -> None:
        zadejte_strany(počet_stran=1, výška=1, kolikastranný=1)
        self.oběm = (
            rozměry["kolikastranný"]
            * rozměry["výška"]
            * rozměry["strany"][0] ** 2
            / (12 * mt.tan(mt.pi / rozměry["kolikastranný"]))
        )
        self.povrch = rozměry["kolikastranný"] * rozměry["strany"][0] * (
            rozměry["výška"] ** 2
            + rozměry["strany"][0] ** 2
            / (4 * mt.tan(mt.pi / rozměry["kolikastranný"]) ** 2)
        ) ** 0.5 / 2 + rozměry["kolikastranný"] * rozměry["strany"][0] ** 2 / (
            4 * mt.tan(mt.pi / rozměry["kolikastranný"])
        )
        self.output()

    def kužel(self) -> None:
        zadejte_strany(poloměr=1, výška=1)
        self.oběm = mt.pi * rozměry["poloměr"] ** 2 * rozměry["výška"] / 3
        self.povrch = (
            mt.pi
            * rozměry["poloměr"]
            * (rozměry["poloměr"] ** 2 + rozměry["výška"] ** 2) ** 0.5
        )
        self.output()

    def válec(self) -> None:
        zadejte_strany(výška=1, poloměr=1)
        self.oběm = mt.pi * rozměry["poloměr"] ** 2 * rozměry["výška"]
        self.povrch = 2 * mt.pi * rozměry["poloměr"] * rozměry["výška"]
        self.output()

    def koule(self) -> None:
        zadejte_strany(poloměr=1)
        self.oběm = 4 / 3 * mt.pi * rozměry["poloměr"] ** 3
        self.povrch = 4 * mt.pi * rozměry["poloměr"] ** 2
        self.output()

    def torus(self) -> None:
        zadejte_strany(("vnitřní poloměr", "31"), poloměr=1)
        self.oběm = (
            2 * mt.pi**2 * rozměry["poloměr"] * rozměry["vnitřní poloměr"] ** 2
        )
        self.povrch = 4 * mt.pi**2 * rozměry["poloměr"] * rozměry["vnitřní poloměr"]
        self.output()

    # komolá tělesa

    def komolý_jehlan(self) -> None:
        zadejte_strany(
            ("délku spodní podstavy", "33"),
            ("délku horní podstavy", "32"),
            výška=1,
            kolikastranný=1,
        )
        s1: float = (
            rozměry["kolikastranný"] * rozměry["délku spodní podstavy"] ** 2
        ) / (4 * mt.tan(mt.pi / rozměry["kolikastranný"]))
        s2: float = (
            rozměry["kolikastranný"] * rozměry["délku horní podstavy"] ** 2
        ) / (4 * mt.tan(mt.pi / rozměry["kolikastranný"]))
        r1: float = rozměry["délku spodní podstavy"] / (
            2 * mt.tan(mt.pi / rozměry["kolikastranný"])
        )
        r2: float = rozměry["délku horní podstavy"] / (
            2 * mt.tan(mt.pi / rozměry["kolikastranný"])
        )
        c: float = mt.sqrt((r1 - r2) ** 2 + rozměry["výška"] ** 2)
        spl: float = (
            (rozměry["délku spodní podstavy"] + rozměry["délku horní podstavy"])
            * c
            * rozměry["kolikastranný"]
            / 2
        )
        self.oběm = (s1 + mt.sqrt(s1 * s2) + s2) * rozměry["výška"] / 3
        self.povrch = s1 + s2 + spl
        self.output()

    def komolý_kužel(self) -> None:
        zadejte_strany(
            ("poloměr spodní podstavy", "95"),
            ("poloměr vrchní podstavy", "31"),
            výška=1,
        )
        self.oběm = (
            mt.pi
            * rozměry["výška"]
            * (
                rozměry["poloměr spodní podstavy"] ** 2
                + rozměry["poloměr vrchní podstavy"] ** 2
                + rozměry["poloměr spodní podstavy"]
                * rozměry["poloměr vrchní podstavy"]
            )
            / 3
        )
        self.povrch = mt.pi * (
            (rozměry["poloměr spodní podstavy"] + rozměry["poloměr vrchní podstavy"])
            * mt.sqrt(
                rozměry["poloměr spodní podstavy"] ** 2
                - 2
                * rozměry["poloměr spodní podstavy"]
                * rozměry["poloměr vrchní podstavy"]
                + rozměry["poloměr vrchní podstavy"] ** 2
                + rozměry["výška"] ** 2
            )
            + rozměry["poloměr spodní podstavy"] ** 2
            + rozměry["poloměr vrchní podstavy"] ** 2
        )
        self.output()

    # platónská tělesa

    def čtyřstěn(self) -> None:
        zadejte_strany(počet_stran=1)
        self.oběm = mt.sqrt(2) * rozměry["strany"][0] ** 3 / 12
        self.povrch = mt.sqrt(3) * rozměry["strany"][0] ** 2
        self.output()

    def osmistěn(self) -> None:
        zadejte_strany(počet_stran=1)
        self.oběm = mt.sqrt(2) * rozměry["strany"][0] ** 3 / 3
        self.povrch = mt.sqrt(3) * 2 * rozměry["strany"][0] ** 2
        self.output()

    def dvanáctistěn(self) -> None:
        zadejte_strany(počet_stran=1)
        self.oběm = (mt.sqrt(5) * 7 + 15) * rozměry["strany"][0] ** 3 / 4
        self.povrch = mt.sqrt(25 + 10 * mt.sqrt(5)) * 3 * rozměry["strany"][0] ** 2
        self.output()

    def dvacetistěn(self) -> None:
        zadejte_strany(počet_stran=1)
        self.oběm = (mt.sqrt(5) + 3) * 5 * rozměry["strany"][0] ** 3 / 12
        self.povrch = mt.sqrt(3) * 5 * rozměry["strany"][0] ** 2
        self.output()


# menu pro platónská tělesa
def pravidelné_mnohostěny() -> None:
    clean(len(tělesa) + 4)
    print(
        "\nVšechna podporovaná pravidelná tělesa:\n",
        *[f"{i}: {n}\n" for i, n in enumerate(mnohostěny)],
    )
    těleso: str = input("Zadej těleso: ")
    try:
        těleso = mnohostěny[int(těleso)]
    except:
        pass
    if těleso == "_zpět_" or těleso not in mnohostěny:
        clean(len(mnohostěny) + 4)
        return
    elif těleso in mnohostěny:
        clean(len(mnohostěny) + 4)
        getattr(globals()["ED"](těleso=těleso), těleso)()
    else:
        clear()
        exit()


# menu pro komolá tělesa
def komolá() -> None:
    clean(len(tělesa) + 4)
    print(
        "\nVšechna podporovaná pravidelná tělesa:\n",
        *[f"{i}: {n}\n" for i, n in enumerate(komolá_tělesa)],
    )
    těleso: str = input("Zadej těleso: ")
    try:
        těleso = komolá_tělesa[int(těleso)]
    except:
        pass
    if těleso == "_zpět_" or těleso not in komolá_tělesa:
        clean(len(komolá_tělesa) + 4)
        return
    elif těleso in komolá_tělesa:
        clean(len(komolá_tělesa) + 4)
        getattr(globals()["ED"](těleso=těleso), těleso.replace(" ", "_"))()
    else:
        clear()
        exit()


# hlavní menu
def main() -> None:
    print(
        "\nVšechna podporovaná pravidelná tělesa:\n",
        *[f"{i}: {n}\n" for i, n in enumerate(tělesa)],
    )
    těleso: str = input("Zadej těleso: ")
    try:
        těleso = tělesa[int(těleso)]
    except:
        pass
    if těleso == "*komolá tělesa":
        komolá()
        return
    elif těleso == "*pravidelné mnohostěny":
        pravidelné_mnohostěny()
        return
    elif těleso == "_exit_":
        clear()
        exit()
    elif těleso in tělesa:
        clean(len(tělesa) + 4)
        getattr(globals()["ED"](těleso=těleso), těleso)()
    else:
        clear()
        exit()


# spuštění
if __name__ == "__main__":
    while True:
        rozměry: dict = {
            "strany": [],
            "výška": 0,
            "poloměr": 0,
            "kolikastranný": 0,
        }
        main()
