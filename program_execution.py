import subprocess

def executeProgram(text):
    process = isolate_processName(text)
    subprocess.run(process, shell = True)


def terminateProgram(text):
    process = isolate_processName(text)
    command = "pkill " + process
    subprocess.run(command, shell=True)


def isolate_processName(text):
    wordsToRemove = ["process", "program", "stop", "execute", "kill", "run", "open", "close", "end", "start"]
    for i in wordsToRemove:
        if i in text:
            text = text.replace(i, '').strip()
    return text


if __name__ == "__main__":
    process = "Discord"
    command = "pkill " + process
    print(command)
    subprocess.run(command, shell=True)