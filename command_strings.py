import spotify_client
import google_functions
import program_execution
# import data_struct

# TODO: Function calls and names still missing
command_strs = {
    "spotify": {
        "command": None,
        "visits": 0,
        "strings": ["song, music", "spotify", "track"],
        "freq": 0,

        "next": {
            "visits": 0,
            "strings": ["next song", "next track", "skip song",
                            "skip track"],
            "command": spotify_client.next_song,
            "freq": 0},
        
        "previous": {
            "visits": 0,
            "strings": ["previous song", "previous track", "last song",
                            "last song"],
            "command": spotify_client.previous_song,
            "freq": 0},
        
        "pause": {
            "visits": 0,
            "strings": ["pause spotify", "pause music", "stop music"],
            "command": spotify_client.pause,
            "freq": 0},
        
        "play": {
            "visits": 0,
            "strings": ["resume music", "resume spotify", 
                            "resume song", "continue song", "continue music", "play spotify"],
            "command": spotify_client.play,
            "freq": 0},
        
        "mute": {
            "visits": 0,
            "strings": ["mute spotify", "mute song", "mute music"],
            "command": spotify_client.mute,
            "freq": 0},
        
        "unmute": {
            "visits": 0,
            "strings": ["unmute music", "unmute song", 
                            "unmute spotify", "volume up", "increase volume"],
            "command": spotify_client.unmute,
            "freq": 0},
        
        "maxVolume": {
            "visits": 0,
            "strings": ["max volume spotify", "spotify max volume",
                            "full volume"],
            "command": spotify_client.fullVolume,
            "freq": 0}
        },

    "search": {
        "command": None,
        "visits": 0,
        "strings": ["google", "search", "look up"],
        "freq": 0,

        "google": {
            "visits": 0,
            "strings": ["search", "google", "look up"], 
            "command": google_functions.google_search,
            "freq": 0
            }
        },

    "process handling": {
        "command": None,
        "visits": 0,
        "strings": ["run", "open", "execute", "terminate", "kill"],
        "freq": 0,

        "execute": {
            "visits": 0,
            "strings": ["run", "open", "execute"],
            "command": program_execution.executeProgram,
            "freq": 0},

        "terminate": {
            "visits": 0,
            "strings": ["stop", "end", "terminate", "kill"],
            "command": program_execution.terminateProgram,
            "freq": 0}
    }
}


"""
This function checks every string. It doesnt use strings to narrow down to the type of the program used. Instead, it recurses over every string to find a match.
"""
# breakRecursion = False
# def checkCommands(someDict, text):
#     global breakRecursion
#     if breakRecursion: return None
#     if not isinstance(someDict, dict): return None

#     if "strings" in someDict.keys():
#         for entry in someDict["strings"]:
#             if entry in text:
#                 someDict["command"](text)
#                 print("success")
#                 breakRecursion = True
    
#     for subdict in someDict.values():
#         r = checkCommands(subdict, text)


# # if not __name__ == "__main__":
# #     data_struct.make_tree(command_strs)

# def get_all_values(nested_dictionary):
#     for key, value in nested_dictionary.items():
#         if type(value) is dict:
#             get_all_values(value)
#         else:
#             print(key, ":", value)


if __name__ == "__main__":
    print()
    # data_struct.make_tree(command_strs)
    # for i in data_struct.mainNodes:
    #     i.print_tree()
    # myprint(command_strs)
 