import spotify_client
import google_functions
import program_execution
import data_struct

# TODO: Function calls and names still missing
command_strs = {
    "spotify": {
        "buzzwords": ["song, music", "spotify", "track"],

        "next": {
            "strings": ["next song", "next track", "skip song",
                            "skip track"],
            "command": spotify_client.next_song},
        
        "previous": {
            "strings": ["previous song", "previous track", "last song",
                            "last song"],
            "command": spotify_client.previous_song},
        
        "pause": {
            "strings": ["pause spotify", "pause music", "stop music"],
            "command": spotify_client.pause},
        
        "play": {
            "strings": ["resume music", "resume spotify", 
                            "resume song", "continue song", "continue music", "play spotify"],
            "command": spotify_client.play},
        
        "mute": {
            "strings": ["mute spotify", "mute song", "mute music"],
            "command": spotify_client.mute},
        
        "unmute": {
            "strings": ["unmute music", "unmute song", 
                            "unmute spotify", "volume up", "increase volume"],
            "command": spotify_client.unmute},
        
        "maxVolume": {
            "strings": ["max volume spotify", "spotify max volume",
                            "full volume"],
            "command": spotify_client.fullVolume}
        },

    "google": {
        "buzzwords": ["google", "search", "look up"],

        "search": {
            "strings": ["search", "google", "look up"], 
            "command": google_functions.google_search}
        },

    "run": {
        "buzzwords": ["run", "open", "execute"],

        "execute": {
            "strings": ["run", "open", "execute"],
            "command": program_execution.executeProgram}
        }
}


"""
This function checks every string. It doesnt use buzzwords to narrow down to the type of the program used. Instead, it recurses over every string to find a match.
"""
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


if not __name__ == "__main__":
    data_struct.make_tree(command_strs)


if __name__ == "__main__":
    data_struct.make_tree(command_strs)
    for i in data_struct.mainNodes:
        i.print_tree()
