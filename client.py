import socket,time
import tkinter as tk
import pickle
import json
import requests


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1",1234))

anime = {
    1: "Cowboy Bebop",
    7: "Witch Hunter Robin",
    20: "Naruto",
    28: "Yakitate!! Japan",
    44: "Samurai X: Trust and Betrayal",
    50: "Ah! My Goddess",
    60: "Chrono Crusade",
    66: "Azumanga Daioh: The Animation",
    71: "Full Metal Panic!",
    77: "Magical Girl Lyrical Nanoha A's",
    82: "Mobile Suit Gundam 0080: War in the Pocket",
    88: "Mobile Suit Gundam F91",
    93: "Mobile Suit Gundam SEED",
    98: "My-Hime",
    104: "Ceres, Celestial Legend",
    109: "Burst Angel",
    114: "Cromartie High School",
    120: "Fruits Basket",
    125: "Twin Love",
    131: "Saiyuki Gunlock",
    136: "Hunter x Hunter",
    147: "Rumbling Hearts",
    153: "The Twelve Kingdoms",
    158: "Maria Watches Over Us",
    169: "Lunar Legend Tsukihime",
    174: "Tenjho Tenge",
    180: "Vandread",
    185: "Initial D First Stage",
    191: "Love Hina Christmas Movie",
    196: "Please Twins!",
    202: "Wolf's Rain",
    207: "Record of Lodoss War",
    218: "Martian Successor Nadesico",
    223: "Dragon Ball",
    229: "Ninja Nonsense",
    239: "Gankutsuou: The Count of Monte Cristo",
    245: "Great Teacher Onizuka",
    256: "Voices of a Distant Star",
    267: "Gungrave",
    272: "Noir",
    283: "Anne of Green Gables",
    289: "Comic Party",
    300: "3x3 Eyes",
    316: "F3: Frantic, Frustrated & Female",
    322: "Paradise Kiss",
    327: "Petite Princess Yucie",
    333: "Mama is Just a Fourth Grade Pupil",
    338: "The Rose of Versailles",
    343: "Tsukuyomi: Moon Phase",
    349: "Magical Kanan",
    354: "Ultimate Girls",
    359: "I'll/CKBC",
    371: "Cardcaptor Sakura The Movie",
    376: "Elfen Lied: In the Passing Rain, or, How Can a Girl Have Reached Such Feelings?",
    382: "Step Up Love Story",
    387: "Haibane Renmei",
    393: "Escaflowne: A Girl in Gaea",
    398: "Banner of the Stars III",
    404: "Bastard!!",
    413: "Mars of Destruction",
    418: "Ranma ½: Big Trouble in Nekonron, China",
    429: "Kaleido Star: Legend of Phoenix - The Layla Hamilton Story",
    434: "Legend of Lemnear",
    439: "RG Veda",
    444: "Maria Watches Over Us: Printemps",
    450: "InuYasha the Movie 2: The Castle Beyond the Looking Glass",
    455: "Fantastic Children",
    461: "One Piece: Chopper Kingdom of Strange Animal Island",
    466: "One Piece: Defeat the Pirate Ganzack!",
    472: "To Heart",
    477: "Aria the Animation",
    488: "Strawberry Marshmallow",
    503: "The Eternal Aseria",
    509: "I My Me! Strawberry Eggs",
    514: "Le Portrait de Petit Cossette",
    525: "Otogi Zoshi: The Legend of Magatama",
    531: "Sailor Moon R: The Movie - The Promise of the Rose",
    536: "Slayers: The Motion Picture",
    541: "Tenchi Muyo! Ryo-Ohki",
    552: "Digimon: Digital Monsters",
    557: "Steel Angel Kurumi Encore",
    563: "DNA²",
    574: "The Wings of Rean",
    585: "Whisper of the Heart",
    590: "Guardian Ninja Mamoru",
    595: "X: An Omen",
    601: "Cat Soup",
    607: "Fairy Musketeers",
    618: "Ninja Scroll: The Series",
    629: "Magic User's Club OVA",
    656: "Air in Summer",
    668: "Koi Koi Seven",
    673: "My-Hime Specials",
    689: "Utakata: Summer Pair of Early Winter",
    712: "Zoids Genesis",
    719: "Ai no Kusabi",
    730: "After School in the Lounge",
    755: "My Sexual Harassment",
    760: "TenjhoTenge: The Past Chapter",
    777: "Hellsing Ultimate",
    782: "Gasaraki",
    788: "Eiken",
    793: "xxxHOLiC The Movie: A Midsummer Night's Dream",
    815: "The Prince of Tennis: The Two Samurai, The First Game",
    820: "Legend of the Galactic Heroes",
    831: "A Little Snow Fairy Sugar",
    837: "Today in Class 5-2",
    842: "Ushio and Tora",
    848: "Jinki: Extend",
    853: "Ouran High School Host Club",
    859: "Digimon Data Squad",
    864: "Mobile Suit Gundam SEED MSV Astray",
    886: "Ah My Buddha Katsu",
    891: "Dragon Ball: Sleeping Princess in Devil's Castle",
    897: "Dragon Ball Z: Lord Slug",
    902: "Dragon Ball Z: Bojack Unbound",
    908: "Fullmetal Alchemist: Premium OVA Collection",
    913: "Fighting Beauty Wulong",
    918: "Gintama",
    924: "Transformers Super-God Masterforce",
    929: "Aura Battler Dunbine",
    935: "Witchblade",
    957: "The Story of Saiunkoku",
    962: "Aria the Natural",
    967: "Fist of the North Star",
    973: "Glass Fleet",
    978: "Getter Robo: Armageddon",
    1000: "Space Pirate Captain Harlock",
    1005: "Star Ocean EX",
    1017: "Orphen",
    1033: "Millennium Actress",
    1044: "Horus: Prince of the Sun",
    1049: "Gauche the Cellist",
    1064: "Mazinkaiser",
    1069: "Voltes V",
    1074: "Naruto: Finally a Clash!! Jounin vs. Genin!",
    1080: "Yukikaze",
    1085: "Interlude",
    1091: "Mobile Suit Gundam II: Soldiers of Sorrow",
    1096: "Mobile Police Patlabor 2: The Movie",
    1107: "Wicked City",
    1118: "Pokémon 3: The Movie",
    1123: "Beet the Vandel Buster Excellion",
    1145: "Kaze no Yojimbo",
    1150: "Legend of Crystania",
    1156: "Zaion: I Wish You Were Here",
    1161: "Maze: The Mega-Burst Space",
    1183: "Variable Geo",
    1210: "Welcome to the N.H.K.",
    1215: "Mobile Suit Gundam SEED C.E.73: Stargazer",
    1221: "Powerpuff Girls Z",
    1226: "Angel Links",
    1232: "Saber Marionette R",
    1237: "One Piece Special: Open Upon the Great Sea! A Father's Huge, HUGE Dream!",
    1245: "Twilight Of The Dark Master",
    1250: "Elemental Gelade",
    1256: "Saint Seiya: Evil Goddess Eris",
    1261: "Samurai Pizza Cats",
    1266: "Ronin Warriors Legend of Kikoutei",
    1271: "Very Private Lesson",
    1277: "Ys II: Castle in the Heavens",
    1283: "Gestalt",
    1287: "Odin: Starlight Mutiny",
    1292: "Afro Samurai",
    1298: "Project A-ko: Love & Robots",
    1303: "The Animatrix",
    1314: "DT Eightron",
    1329: "Rail of the Star: A True Story of Children",
    1336: "The Guyver: Bio-Booster Armor",
    1342: "Violence Jack: Evil Town",
    1358: "Fist of the North Star: The Movie",
    1364: "Case Closed Movie 5: Countdown to Heaven",
    1374: "Guyver: The Bioboosted Armor",
    1380: "Blue Gender: The Warrior",
    1402: "Princess Memory",
    1418: "Lupin III Episode 0: The First Contact",
    1424: "Lupin III: Operation Return the Treasure",
    1429: "Lupin III: Swallowtail Tattoo",
    1435: "Lupin III: The Secret of Mamo",
    1440: "Ninja Cadets",
    1445: "Speed Racer",
    1451: "Sword for Truth",
    1456: "Licensed by Royalty",
    1475: "City Hunter: Bay City Wars",
    1486: "Kodocha",
    1491: "Galaxy Express 999",
    1497: "Tales of the Street Corner",
    1503: "Magical Project S Specials",
    1508: "Sci-fi Harry",
    1514: "UFO Ultramaiden Valkyrie 3: Bride of Celestial Souls' Day",
    1519: "Black Lagoon: The Second Barrage",
    1530: "Kanon",
    1536: "Buso Renkin",
    1541: "Fist of the Blue Sky",
    1546: "Negima!? Magister Negi Magi",
    1552: "Sunny Ryoko! You Were There in a Dream",
    1558: "Sex Demon Queen",
    1563: "Magic Knight Rayearth II",
    1579: "La corda d'oro: primo passo",
    1602: "Strain: Strategic Armored Infantry",
    1607: "Venus Versus Virus",
    1629: "The Devil Lady",
    1635: "Immoral Sisters 2",
    1640: "Angel's Feather",
    1648: "UFO Ultramaiden Valkyrie 4: Banquet of Time, Dreams, and Galaxies",
    1655: "Nerima Daikon Brothers",
    1667: "Barom 1",
    1678: "Cyborg 009",
    1689: "5 Centimeters per Second",
    1694: "IDOLM@STER Xenoglossia",
    1699: "Romeo x Juliet",
    1705: "Genma Wars",
    1710: "MegaMan NT Warrior",
    1727: "Polyphonica",
    1737: "Space Warrior Baldios",
    1743: "Super Milk-Chan",
    1759: "Black Lion",
    1770: "Sibling Secret: She's the Twisted Sister",
    1774: "HeatGuy J: Angel",
    1779: "Bomb Milk Sisters",
    1785: "The Story of Little Monica",
    1796: "Dirty Pair: Project Eden",
    1803: "Dirty Pair: With Love From the Lovely Angels",
    1810: "Shattered Angels",
    1816: "Sonic X",
    1822: "The Hakkenden: Legend of the Dog Warriors",
    1827: "Moribito - Guardian of the Spirit",
    1833: "Garaga",
    1838: "Honey x Honey Drops",
    1844: "CLAMP School Detectives",
    1849: "Lord of Lords Ryu Knight: Adeu's Legend",
    1855: "Wild Cardz",
    1860: "Tokyo Majin",
    1866: "Elementalors",
    1872: "Ape Escape",
    1879: "Goku: Midnight Eye",
    1884: "Princess Beware",
    1895: "Love is the Number of Keys",
    1900: "Twin Signal",
    1917: "Mobile Suit Gundam MS IGLOO: The Hidden One Year War",
    1928: "Early Reins",
    1933: "Growlanser IV: Wayfarer of Time",
    1938: "Super Atragon",
    1944: "Photon: The Idiot Adventures",
    1954: "Rayearth",
    1974: "Glass Mask",
    2001: "Gurren Lagann",
    2018: "Laughing Target",
    2034: "Lovely Complex",
    2039: "Persia the Magic Fairy",
    2078: "Landlock",
    2132: "Inukami! The Movie",
    2137: "Insatiable",
    2148: "No Money",
    2154: "Tekkonkinkreet",
    2159: "Big Windup!",
    2164: "Den-noh Coil",
    2180: "Slow Step",
    2191: "Behind Closed Doors",
    2199: "Ringing Bell",
    2210: "Other Worlds",
    2221: "Rock'n Roll Kids",
    2226: "A Christmas Adventure",
    2232: "Naruto: Hidden Leaf Village Grand Sports Festival",
    2253: "Mazinger Z",
    2264: "Jungle Emperor Leo",
    2272: "Magical Princess Minky Momo: La Ronde in my Dream",
    2277: "Magical Play",
    2282: "In The Beginning: The Bible Stories",
    2288: "Cyber Team in Akihabara",
    2293: "Guyver: Out of Control",
    2299: "Tekkaman Blade: Burning Clock",
    2304: "Mobile Suit SD Gundam Mk-IV",
    2309: "Azusa Will Help!",
    2315: "Alien from the Darkness",
    2322: "Giant Robo: Ginrei Special",
    2327: "The Blackmail: Tomorrow Never Ends",
    2333: "The Three Musketeers",
    2338: "Demon Beast Invasion",
    2344: "Urotsukidoji IV: Inferno Road",
    2349: "Bondage Game",
    2354: "Devilman: The Birth",
    2370: "Chains of Lust",
    2383: "Cybersix",
    2389: "Gatchaman",
    2394: "The Night When Evil Falls",
    2400: "Ghost Sweeper Mikami",
    2411: "It's a Family Affair",
    2422: "Prefectural Earth Defense Force",
    2427: "The Fantastic Adventures Of Unico",
    2432: "Discipline: The Hentai Academy",
    2438: "The Hills Have Size",
    2444: "Maids in Dream",
    2449: "Ghost in the Shell: Stand Alone Complex - The Laughing Man",
    2465: "Hummingbirds",
    2471: "Doraemon",
    2476: "School Days",
    2511: "Time Stranger",
    2517: "Emma: A Victorian Romance - Intermission",
    2539: "G-Spot Express",
    2544: "The Swiss Family Robinson: Flone of the Mysterious Island",
    2555: "Little Lord Fauntleroy",
    2560: "Toward the Terra",
    2571: "Maya the Bee",
    2576: "Raccoon Rascal",
    2581: "Mobile Suit Gundam 00",
    2591: "Samurai Shodown The Motion Picture",
    2596: "Ghost Hound",
    2607: "Birth",
    2613: "Future Boy Conan 2: River Adventure",
    2618: "Treasure Island",
    2624: "A Dog of Flanders: My Patrasche",
    2656: "Doraemon the Movie: Nobita in the Wan-Nyan Spacetime Odyssey",
    2662: "Doraemon the Movie: The Records of Nobita, Spaceblazer",
    2667: "Doraemon the Movie: Nobita and the Castle of the Undersea Devil",
    2672: "Doraemon the Movie: Nobita's Great Adventure into the Underworld",
    2678: "Doraemon the Movie: Nobita and the Spiral City",
    2689: "Zillion: Burning Night",
    2694: "Tree in the Sun",
    2700: "Space Pirate Mito 2",
    2718: "Triton of the Sea",
    2734: "Mazinkaiser: Deathmatch! General Dark",
    2745: "Hell Teacher Nube",
    2751: "Miyori's Forest",
    2767: "The Night of Taneyamagahara",
    2772: "Hero Tales",
    2789: "Battle B-Daman",
    2795: "Dragonaut - The Resonance",
    2806: "Yadamon: Magical Dreamer",
    2811: "Flying Phantom Ship",
    2817: "The Story of Cinderella",
    2828: "Nobody's Boy Remi",
    2847: "Pokémon: The Rise Of Darkrai",
    2872: "F-Force",
    2882: "Superbook",
    2890: "Ponyo",
    2895: "The Whale Hunt",
    2903: "Charge!! Men's Private School",
    2910: "Love Love 7 DVD Specials",
    2916: "Energetic Bomb Ganbaruger",
    2921: "Tomorrow's Joe 2",
    2927: "KimiKiss: Pure Rouge",
    2933: "Future Police Urashiman",
    2937: "Sailor Moon R: Make Up! Sailor Guardians",
    2942: "Sketchbook ~full color's~",
    2958: "Cosplay Cafe",
    2964: "Blue Drop",
    2969: "Appleseed: Ex Machina",
    2977: "Adventure Kid",
    2982: "Temptation",
    2993: "Rosario + Vampire",
    2998: "The Phoenix -Space-",
    3009: "Tiger Mask",
    3015: "Legend of the Galactic Heroes: Golden Wings",
    3031: "Digimon Frontier: Island of Lost Digimon",
    3036: "Soar High! Isami",
    3044: "Astro Boy (1980)",
    3061: "Kishin Corps",
    3067: "Farewell to Space Battleship Yamato: In the Name of Love",
    3072: "Space Battleship Yamato - Final Chapter",
    3078: "Magical Twilight",
    3085: "Indian Summer",
    3104: "Geisters: Fractions of the Earth",
    3135: "Dragon's Heaven",
    3152: "Download: Devil's Circuit",
    3157: "Guardian Hearts-Power UP!",
    3162: "Katri, Girl of the Meadows",
    3167: "Time of Eve",
    3175: "Undersea Super Train: Marine Express",
    3185: "Fortune Quest",
    3190: "The Boy Who Carried a Guitar: Kikaider vs. Inazuman",
    3201: "Serendipity the Pink Dragon",
    3211: "Weather Report Girl",
    3248: "Ghost Slayers Ayashi: Inferno",
    3254: "Luv Wave",
    3264: "Lemon Angel (1988/II)",
    3270: "IGPX: Immortal Grand Prix",
    3286: "Do You Know the Milfing Man?",
    3297: "Aria the Origination",
    3303: "My Sex Tutor",
    3309: "House of 100 Tongues",
    3334: "Horny Ladies And The News",
    3366: "Persona: Trinity Soul",
    3372: "RGB Adventure",
    3377: "Holy Virgins",
    3382: "Punishment",
    3393: "Dark",
    3399: "God Mars",
    3435: "Angie Girl",
    3447: "Ghost in the Shell: Stand Alone Complex - Solid State Society: Uchikomatic Days",
    3452: "Hot Juicy Teacher",
    3458: "Pi Po Pa Po Patrol",
    3463: "A.LI.CE",
    3469: "Maria Watches Over Us: Printemps",
    3474: "Push",
    3485: "Ghost in the Shell: Stand Alone Complex 2nd GIG - Tachikomatic Days",
    3496: "The Golden Laws",
    3501: "Sisters of Wellber Zwei",
    3525: "Extra",
    3530: "Virtuacall",
    3535: "Neko Rahmen",
    3541: "Co-eD Affairs",
    3556: "Secret Sex Stories",
    3562: "Chu2",
    3579: "Getter Robo",
    3584: "Idol of Darkness",
    3594: "Tears to Tiara",
    3600: "Yotoden: Chronicle of the Warlord Period",
    3614: "Ryoko's Case File",
    3619: "Nanako SOS",
    3624: "Once Upon a Time... Life",
    3631: "Blue Blink",
    3636: "Laughing Nurse",
    3655: "Nabari no Ou",
    3660: "Magical Idol Pastel Yumi",
    3673: "The Daughter of 20 Faces",
    3701: "Kaiba",
    3706: "Dark Chapel",
    3712: "The Familiar of Zero: Rondo of Princesses",
    3720: "Jack and the Beanstalk",
    3727: "Doraemon the Movie: Nobita's Dinosaur",
    3735: "Shooting Star Gakusaver",
    3757: "Aladdin and the Wonderful Lamp",
    3763: "Sonic Soldier Borgman: Lovers Rain",
    3768: "Play Ball",
    3783: "The Garden of Sinners Chapter 3: Remaining Sense of Pain",
    3791: "Air Gear: Special Trick",
    3810: "The Littl' Bits",
    3816: "Idol Fighter Su-Chi-Pai",
    3821: "Portable Airport",
    3826: "Zero no Mono"
}    

def ShowWatched(event):
    command = 'tabW'
    command_bytes = command.encode('utf-8')
    s.send(command_bytes)
    win2 = tk.Toplevel()
    win2.title('Watched Animes')
    win2.resizable(False, False)
    win2.geometry('450x450')
    win2.configure(bg = '#d72631')
    txt = tk.Text(master = win2, width= 42, height= 22, background='#a2d5c6')
    deleteBt = tk.Button(master=win2, text= 'Delete List', background='#077b8a')
    ans = s.recv(10000).decode('utf-8')
    print(ans)
    txt.delete('1.0', tk.END)
    txt.insert('1.0',ans)
    txt.pack(pady = 10)
    deleteBt.pack(pady = 10)
    deleteBt.bind('<Button-1>', lambda event: deleteListW(event, txt))
    
def ShowLater(event):
    command = 'tabL'
    command_bytes = command.encode('utf-8')
    s.send(command_bytes)
    win2 = tk.Toplevel()
    win2.title('Watch Later Animes')
    win2.resizable(False, False)
    win2.geometry('450x450')
    win2.configure(bg = '#d72631')
    deleteBt = tk.Button(master=win2, text= 'Delete List', background='#077b8a')
    txt = tk.Text(master = win2, width= 42, height= 22, background='#a2d5c6')
    ans = s.recv(10000).decode('utf-8')
    print(ans)
    txt.delete('1.0', tk.END)
    txt.insert('1.0',ans)
    txt.pack(pady = 10)
    deleteBt.pack(pady = 10)
    deleteBt.bind('<Button-1>', lambda event: deleteListL(event, txt))

def deleteListW(event,txt):
    command = 'deleteW'
    command_bytes = command.encode('utf-8')
    s.send(command_bytes)
    ans = s.recv(10000).decode('utf-8')
    txt.delete('1.0', tk.END)
    txt.insert('1.0',ans)
    print('delte')

def deleteListL(event,txt):
    command = 'deleteL'
    command_bytes = command.encode('utf-8')
    s.send(command_bytes)
    ans = s.recv(10000).decode('utf-8')
    txt.delete('1.0', tk.END)
    txt.insert('1.0',ans)
    print('delte')


def IdToNames(event):
    pass

def BackButton(event):
    pass

def FilterButton(event):
    pass

def printAnswer2(response):
    AnswerAction.delete('0', tk.END)
    AnswerAction.insert(0, response)

def AddToWatched(event):
    info = responseText.get("1.0","end-1c")
    if len(info) > 30:
        info_data = info + "addW"
        info_data_bytes = info_data.encode('utf-8')
        s.send(info_data_bytes)
        time.sleep(0.5)
        serverResponse = s.recv(1000).decode('utf-8')
        printAnswer2(serverResponse)
    else: pass

def AddToWatchLater(event):
    info = responseText.get("1.0","end-1c")
    if len(info) > 30:
        info_data = info + "addL"
        info_data_bytes = info_data.encode('utf-8')
        s.send(info_data_bytes)
        time.sleep(0.5)
        serverResponse = s.recv(1000).decode('utf-8')
        printAnswer2(serverResponse)
    else:pass

def AddToPref(event):
    info = responseText.get("1.0","end-1c")
    if len(info) > 30:
        info_data = info + "addP"
        info_data_bytes = info_data.encode('utf-8')
        s.send(info_data_bytes)
        time.sleep(0.5)
        serverResponse = s.recv(1000).decode('utf-8')
        printAnswer2(serverResponse)
    else:pass

def get_key(val):
   
    for key, value in anime.items():
        if val == value:
            return key
 
    return 0

def ButtonClick(event):
    text1 = searchBar.get()
    text = str(get_key(text1))
    if text == 'exit':
        s.close()
    text_bytes = text.encode('utf-8')
    s.send(text_bytes)
    time.sleep(1)
    serverResponse = s.recv(10000).decode("UTF-8")
    printAnswer(serverResponse)
    if len(serverResponse) < 30:
        addButton['state'] = tk.DISABLED
        laterButton['state'] = tk.DISABLED
        favButton['state'] = tk.DISABLED
    else:
        addButton['state'] = tk.NORMAL
        laterButton['state'] = tk.NORMAL
        favButton['state'] = tk.NORMAL


def printAnswer(response):
    responseText.delete("1.0",tk.END)
    responseText.insert("1.0", response)


window = tk.Tk()
window.title('MyAnimes')
window.resizable(False, False)
window.geometry("600x630")
window.configure(bg = '#d72631')
TitleFrame = tk.Frame(background='#d72631')
SeachFrame = tk.Frame(background='#d72631')
ButtonFrame = tk.Frame(background='#d72631')
ResponseFrame = tk.Frame(background='#d72631')
BottomButtonsFrame = tk.Frame(background='#d72631')
AnswerActionFrame = tk.Frame(background='#d72631')
DBButtonsFrame = tk.Frame(background='#d72631')

titleLabel = tk.Label(master = TitleFrame,text = "Search an Anime",width=300, height=5, background='#d72631',)
searchButton = tk.Button(master = ButtonFrame,text = "Search", background='#077b8a')
searchBar = tk.Entry(master = SeachFrame, background='#a2d5c6', width= 30)
responseText = tk.Text(master = ResponseFrame, width= 60, height=18, background='#a2d5c6')
addButton = tk.Button(master = BottomButtonsFrame, text = "Add to watched", background='#077b8a')
laterButton = tk.Button(master = BottomButtonsFrame, text = "Watch later", background='#077b8a')
favButton = tk.Button(master = BottomButtonsFrame, text = "Add to favorites", background='#077b8a')
AnswerAction = tk.Entry(master = AnswerActionFrame,width= 70, background='#a2d5c6')
showWatchedButton = tk.Button(master = DBButtonsFrame, text = "Show Watched Animes", background='#077b8a')
showLaterAction = tk.Button(master = DBButtonsFrame, text = "Show watch later animes", background='#077b8a')

TitleFrame.pack()
SeachFrame.pack()
ButtonFrame.pack()
ResponseFrame.pack()
BottomButtonsFrame.pack()
AnswerActionFrame.pack()
DBButtonsFrame.pack()

searchBar.pack()
searchButton.pack(pady=10)
titleLabel.pack()
responseText.pack(pady=15)
addButton.pack(side=tk.LEFT,padx=10,pady=10)
laterButton.pack(side=tk.LEFT,padx=10,pady=10)
favButton.pack(side=tk.LEFT,padx=10,pady=10)
AnswerAction.pack(pady=10)
showWatchedButton.pack(side=tk.LEFT,pady=10,padx=10)
showLaterAction.pack(side=tk.LEFT,pady=10,padx=10)


searchButton.bind("<Button-1>", ButtonClick)
addButton.bind("<Button-1>", AddToWatched)
favButton.bind("<Button-1>", AddToPref)
laterButton.bind("<Button-1>", AddToWatchLater)
showWatchedButton.bind("<Button-1>", ShowWatched)
showLaterAction.bind("<Button-1>", ShowLater)

window.mainloop()
   
