from func import *

sorceFile1 = "sorce/solutions1.txt"

sorceFile2 = "sorce/tresc_zadan1.txt"

outputFile = "output/output.txt"


if __name__ == "__main__":
    
    TasksAndSolutions = []

    with open(sorceFile1, "rt", encoding="utf-8") as inputFile:
        
        taskAndSolutions = ["", "", []]

        for line in inputFile:
            if(doWordsAppearInStr(line, "Zad.")):
                if(taskAndSolutions[1]):
                    TasksAndSolutions.append(taskAndSolutions)
                    taskAndSolutions = taskAndSolutions = ["", "", []]

                taskAndSolutions[1] = line.translate(str.maketrans({"\n" : "", "\t" : ""}))

            elif(doWordsAppearInStr(line, "@", "$")):
                taskAndSolutions[2].append(line.translate(str.maketrans({"\n" : "", "\t" : ""})))
        
        TasksAndSolutions.append(taskAndSolutions)
    
    with open(sorceFile2, "rt", encoding="utf-8") as inputFile:

        for indx, line in enumerate(inputFile):
            if(doWordsAppearInStr(line, str(indx+1))):
                line = line.translate(str.maketrans({"\n" : "", "\t" : ""}))
                TasksAndSolutions[indx][0] = line

    with open(outputFile, "wt", encoding="utf-8") as output:
        for asd in TasksAndSolutions:
            output.writelines(asd[0] + f"\n")
            output.writelines(asd[1] + f"\n")
            for lsa in asd[2]:
                output.writelines(lsa + f"\n")