#Spotify
#preconditions: start bot when playing a song in the playlist you want to delete content in
import tekore as tk
import msvcrt, time
client_id = '580c2924d4534dc2afef75036152f192'
client_secret = '898fbbcb95c3417988a7059209b2ea48'
redirect_uri = 'https://example.com/callback'

print("1) Approve the spotify authorization")
print("2) copy and paste the url after approval in the terminal")
print()
user_token = tk.prompt_for_user_token(
    client_id,
    client_secret,
    redirect_uri,
    scope=tk.scope.every
)
Spotify = tk.Spotify(user_token)

def clean():
    print()
    print("Cleaning Mode On (press enter to end cleaning mode)")
    song = Spotify.playback_currently_playing()
    deletedSongs = []

    if song == None:
        print("Please start by playing a song in the playlist that you want to clean")
        return "Failed Preconditions"

    print("Playing: " + song.item.name)
    #Check users current playing and performs deltions as nessecary until user input in terminal 
    while True:
        currentSong = Spotify.playback_currently_playing()
        currentSongDuration = Spotify.playback_currently_playing().item.duration_ms
        #on song change
        if (currentSong.item.name != song.item.name):
            print("Playing: " + currentSong.item.name)
            if(songProgress < 0.95):
                songID = song.item.uri
                context = Spotify.playback_currently_playing().context
                playlist = context.uri[context.uri.index('playlist')+9:]
                Spotify.playlist_remove(playlist,[songID])
                print("deleted " + song.item.name)
                deletedSongs.append(song.item.name)
            song = currentSong
                
        #update progress
        songProgress = Spotify.playback_currently_playing().progress_ms / currentSongDuration

        #break if user input
        if msvcrt.kbhit():
            if msvcrt.getwche() == '\r':
                break
        time.sleep(1)
    
    print("Cleaning Mode Off")
    print()
    print("Deleted Songs:")
    for i in deletedSongs:
        print(i)

clean()

 





        

