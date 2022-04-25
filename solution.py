# this is just the data, the actual code begins on line 159

colorString = """Red
Orange
Yellow
Green
Cyan
Blue
Magenta
Purple
White
Black
Gray
Grey
Silver
Pink
Maroon
Brown
Beige
Tan
Peach
Lime
Olive
Turquoise
Teal
Navy blue
Indigo
Violet"""

soundString = """gibber
screech
growl
Hum
buzz
Chirrup
Chirp
Twitter
Tweet
Sing
whistle
bleat
grunt
Mew
Purr
Meow
Hiss
yowl
Moo
Low
Bawl
bellow
cheep
Cluck
cackle
crow
low
moo
Chirp
creak
caw
bell
bark
click
bray
coo
quack
scream
Trumpet
roar
Buzz
hum
Bark
Yelp
simper
croak
bleat
bleat
Cackle
quack
chirp
squeak
squeak
Cackle
cluck
Whisper
Whistle
Cry
Scream
Sing
talk
grunt
Neigh
Snort
Whinny
nicker
hum
Laugh
scream
howl
chortle
Scream
Bellow
wail
bleat
Sing
warble
Roar
growl
squeak 
squeal
Chatter
Gibber
Whoop
screech
whine
Pipe
Sing
warble
Chirp
Bark
Hiss
low hum
Hoot
Scream
Screech
shriek
Bellow
low
Talk
Screech
squawk
scream
Snort
Grunt
Squeal
oink
coo
Squeak
drum
squeak
croak
bellow
crow
Scream
squawk
bark
bleat
hiss
Growl
roar
gobble
scream
sing
Howl
Cry
yell
whinny"""

soundArray = soundString.split("\n")
colorArray = colorString.split("\n")

for i in range(len(soundArray)):
    for a in range(len(soundArray[i])):
        soundChange = soundArray[i].upper()
        soundChangeArray = list(soundChange)

        soundChangeArray[a] = chr(ord(soundChangeArray[a]) + 1)

        # print(soundChangeArray)

        for b in range(len(colorArray)):
            colorCheck = colorArray[b].upper()
            colorCheckArray = list(colorCheck)

            if soundChangeArray == colorCheckArray:
                print('potential solution')
                print(soundChange)
                print(soundChangeArray)
                print('')
