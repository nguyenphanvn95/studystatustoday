
from ..patrons_list import PATRONS_LIST
patrons_list = PATRONS_LIST.replace(",", "<br>")

ADDON_NAME = "Format Study Status" #🟢
CREATE_OR_FIXED = "Customized by" #🟢

def clink(name, text,url=None):
    if not url:
        return f'{name} : {text}<br>'
    return f'{name} : <a href="{url}">{text}</a><br>'

credits = """
<br><br><br>
<b>[ CREDIT ]</b>
<br><br><br>
""".replace('\n', '<br>')

patreon = """
Special Thanks
<b>[ PATRONS ]</b>
{patrons_list}
""".format(patrons_list=patrons_list).replace('\n', '<br>')

sound =("<b>[ SOUNDS & BGM ]</b><br>"+
clink("Sound Effect", "Koukaon lab","https://soundeffect-lab.info/",)+
clink("Music" , "MaouDamashii","https://maou.audio/",)+
clink("Catgirl Voice","Cici Fyre","https://cicifyre.itch.io/")+
clink("Robot Voice","Charlie Pennell Productions©","https://www.charliepennellproductions.com/")+
clink("classical music"," Bernd Krueger","http://www.piano-midi.de/")
)


caractor = ("<b>[ IMAGE&3D MATERIALS ]</b><br>" +
clink("Crops", "bluecarrot16, Daniel Eddeland (daneeklu),<br> Joshua Taylor, Richard Kettering (Jetrel).<br> Commissioned by castelonia", "https://opengameart.org/content/lpc-crops")+
clink("Farmer","Butter Milk","https://butterymilk.itch.io/")

            )


addons = """<b>[ INSPIRED BY ADD-ONS ]</b>
Fanfare
Anki Habitica for 2.1
Life Drain
Progress Bar
Progress Bar original
Progress Bar, cards...
Speed Focus Mode
Hitmarkers
HUMBLE PIE

""".replace('\n', '<br>')

budle = ("<b>[ BUNDLE SOURCE CODE ]</b><br>"+
clink ("BGM","Pyglet","https://pyglet.readthedocs.io/en/latest/index.html")+
clink ("webp","dwebp","https://developers.google.com/speed/webp/download")+
clink ("midi","FluidSynth","https://www.fluidsynth.org/")

)

thankYou = ("""
<br><br><br>
<h3>%s</h3><br>""" % ADDON_NAME +
clink(f"{CREATE_OR_FIXED}", "Shigeyuki","https://google.com")+
"""
<br>
Thank you very much!
<br><br><br><br>
""")