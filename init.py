
#################################################################
##          DATA STRUCTURE
#################################################################
#[id, name, artist]
class Song:
    def __init__(self, name, artist, pos) -> None:
        self.name:str = name
        self.artist:str = artist
        self.pos:int = pos

#################################################################
##          PARSING DATA
#################################################################
parsedLines = []

file = open('2_Liked Ones.txt')

# Read the first line that contains the columns
#['Name', 'Artist', 'Album']
line = file.readline()
keys = line.split('\t')


line = file.readline()
while line:
    parsedLine = {}
    values = line.split('\t')
    for i in range(len(keys)) :
        parsedLine[keys[i]] = values[i]
    
    parsedLines.append(parsedLine)
    line = file.readline()

file.close()


songs = []
i = 1
for parsedLine in parsedLines:
    songs.append(Song(name=parsedLine['Name'], artist=parsedLine['Artist'], pos=i))
    i += 1



#################################################################
##          FINDING DUPLICATES
#################################################################
#[id, name, artist]
import stringAlgorithm as SA

matchedSongs = []

for i in range(len(songs)-1):
    j = i + 1
    while j < len(songs):
        if songs[i].artist == songs[j].artist:
            if SA.matchString(songs[i].name, songs[j].name):
                matchedSongs.append({'Artist':songs[i].artist, 
                                     'pos1':songs[i].pos, 'Song1':songs[i].name, 
                                     'pos2':songs[j].pos, 'Song2':songs[j].name})
        j += 1

for song in matchedSongs:
    print(f'Artist: {song["Artist"]}\n\tSong {song["pos1"]}: "{song["Song1"]}"\n\tSong {song["pos2"]}: "{song["Song2"]}"')




