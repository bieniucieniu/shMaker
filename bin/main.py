from func import *

sorceFile1 = "sorce/solutions1.txt"

sorceFile2 = "sorce/tresc_zadan1.txt"

outputBeginning = "output/osp_"
outputExtension = ".sh"

bashUserPrefix = "user1@DESKTOP-BPJBSKP:/$"

if __name__ == "__main__":
    
    TasksAndSolutions = []

    with open(sorceFile1, "rt", encoding="utf-8") as inputFile:
        
        taskAndSolutions = ["", "", ""]

        for line in inputFile:
            if(doWordsAppearInStr(line, "Zad.")):
                if(taskAndSolutions[1]):
                    TasksAndSolutions.append(taskAndSolutions)
                    taskAndSolutions = taskAndSolutions = ["", "", []]

                taskAndSolutions[1] = line.translate(str.maketrans({'\n' : '', '\t' : ''}))

            elif(doWordsAppearInStr(line, "@", "$")):
                _line = ''.join(line.split('$')[1:])
                if (taskAndSolutions[2]):
                    taskAndSolutions[2] += _line.translate(str.maketrans({'\n' : '', '\t' : ''}))
                    taskAndSolutions[2] += f"\n"
                else:
                    taskAndSolutions[2] = _line.translate(str.maketrans({'\n' : '', '\t' : ''}))
                    taskAndSolutions[2] += f"\n"

        TasksAndSolutions.append(taskAndSolutions)
    
    with open(sorceFile2, "rt", encoding="utf-8") as inputFile:

        for indx, line in enumerate(inputFile):
            if(doWordsAppearInStr(line, str(indx+1))):
                line = line.translate(str.maketrans({'\n' : '', '\t' : ''}))
                TasksAndSolutions[indx][0] = line

    

    for Indx, out in enumerate(TasksAndSolutions):
        if Indx < 9:
            indx = "0" + str(Indx+1)
        else:
            indx = str(Indx+1)

        with open(f"{outputBeginning}{indx}{outputExtension}", "wt", encoding="utf-8", newline='\n') as outputFile:
            pass
            outputFile.writelines(
                f"#!/bin/bash"
                f"\n\n"
                f". funkcje_wspolne.sh\n"
                f"function tresc() {{\n"
                f"echo {out[0]}\n"
                f"}}\n\n"
                f"function rozwiazanie() {{\n"
                f"echo {out[2]}"
                f"}}\n\n"
                f"function opis() {{\n"
                f"echo {out[1]}\n"
                f"}}\n\n"
                f"function uruchom() {{\n"
                f"{out[2]}"
                f"}}"
            )


