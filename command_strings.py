import spotify_client
import google_functions
import program_execution

# TODO: Complete the list and figure out a way to get keywords from the input string to form better command calls
# SPOTIFY_STRS = [
#     "next song", "next track", "skip song", "skip track",
#     "previous song", "previous track", "last song", "last song"
#     "pause spotify", "pause music", "stop music", 
#     "resume music", "resume spotify", "resume song", "continue song", 
#         "continue music",
#     ""]

# TODO: Function calls and names still missing
command_strs = {
    "SPOTIFY": 
        {"next": 
            {"strings": ["next song", "next track", "skip song",
                            "skip track"],
            "command": spotify_client.next_song},
        
        "previous": 
            {"strings": ["previous song", "previous track", "last song",
                            "last song"],
            "command": spotify_client.previous_song},
        
        "pause": 
            {"strings": ["pause spotify", "pause music", "stop music"],
            "command": spotify_client.pause},
        
        "play": 
            {"strings": ["resume music", "resume spotify", 
                            "resume song", "continue song", "continue music", "play spotify"],
            "command": spotify_client.play},
        
        "mute":
            {"strings": ["mute spotify", "mute song", "mute music"],
            "command": spotify_client.mute},
        
        "unmute":
            {"strings": ["unmute music", "unmute song", 
                            "unmute spotify", "volume up", "increase volume"],
            "command": spotify_client.unmute},
        
        "maxVolume":
            {"strings": ["max volume spotify", "spotify max volume",
                            "full volume"],
            "command": spotify_client.fullVolume}
        },

    "GOOGLE": 
        {"search": 
            {"strings": ["search", "google"], 
            "command": google_functions.google_search}
        },

    "RUN": 
        {"execute": 
            {"strings": ["run", "open", "execute"],
            "command": program_execution.executeProgram}
        }
}



breakRecursion = False
def checkCommands(someDict, text):
    global breakRecursion
    if breakRecursion: return None
    if not isinstance(someDict, dict): return None

    if "strings" in someDict.keys():
        for entry in someDict["strings"]:
            if entry in text:
                someDict["command"](text)
                print("success")
                breakRecursion = True
    
    for subdict in someDict.values():
        r = checkCommands(subdict, text)



if __name__ == "__main__":
    # print(command_strs.keys())
    checkCommands(command_strs, "google dogs")
    # for value in COMMAND_STRS.values():
    #     for values in value.values():
    #         print(values)
    #         print()







