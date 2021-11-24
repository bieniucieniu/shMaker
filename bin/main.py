from func import *

sorceFile = "sorce/solutions1.txt"




if __name__ == "__main__":

    with open(sorceFile, "rt", encoding="utf-8") as inputFile:
        
        TasksAndSolutions = []
        
        taskAndSolutions = ["", "", []]

        for line in inputFile:
            if(doWordsAppearInStr(line, "Zad.")):
                if(taskAndSolutions[1]):
                    TasksAndSolutions.append(taskAndSolutions)
                    taskAndSolutions = taskAndSolutions = ["", "", []]

                taskAndSolutions[1] = line.translate(str.maketrans({"\n" : "", "\t" : ""}))

            elif(doWordsAppearInStr(line, "@", "$")):
                taskAndSolutions[2].append(line.translate(str.maketrans({"\n" : "", "\t" : ""})))


