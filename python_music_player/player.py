from playsound import playsound

source = 'C:\\Users\\dashl\\OneDrive\\Desktop\\code playground\\python music player\\musics'
musics_dict = {
    '1': {
        'name': 'Janji - Heroes Tonight (feat. Johnning) [NCS Release]',
        'filename': 'Janji - Heroes Tonight (feat. Johnning) [NCS Release].mp3'
    },
    '2': {
        'name': 'Jarico - Island [NCS BEST OF]',
        'filename': 'Jarico - Island [NCS BEST OF].mp3'
    },
    '3': {
        'name': 'Jarico - Landscape [NCS BEST OF]',
        'filename': 'Jarico - Landscape [NCS BEST OF].mp3'
    },
    '4': {
        'name': 'Jarico - Paradise [NCS BEST OF]',
        'filename': 'Jarico - Paradise [NCS BEST OF].mp3'
    },
    '5': {
        'name': 'Jarico - Taj Mahal [NCS BEST OF]',
        'filename': 'Jarico - Taj Mahal [NCS BEST OF].mp3'
    },
    '6': {
        'name': 'Jarico - Waves [NCS BEST OF]',
        'filename': 'Jarico - Waves [NCS BEST OF].mp3'
    },
}

musics_ids = list(musics_dict.keys())
print("Choices:", musics_ids)
print("Welcome to NCS Music Library")
for i in musics_ids:
    print(f"{i}. {musics_dict[str(i)]['name']}")
    
choice = input("Enter your choice (1 to 6): ")
if choice not in musics_ids:
    print("Please enter a valid choice!")
else:
    print(f"Playing...\n{musics_dict[str(choice)]['name']}")
    playsound(f"{source}\\{musics_dict[str(choice)]['filename']}")