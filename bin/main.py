from func import *

sorceFile = "sorce/solutions1.txt"



if __name__ == "__main__":

    with open(sorceFile, "rt", encoding="utf-8") as inputFile:
        
        tasksAndSolutions = []
        

        for line in inputFile:
            if(doWordsAppearInOrder(line, "Zad.")):
                line = line.translate(str.maketrans({"\n" : "", "\t" : ""}))
                tasksAndSolutions.append(line)

            elif(doWordsAppearInOrder(line, "@", "$")):
                line = line.translate(str.maketrans({"\n" : "", "\t" : ""}))
                tasksAndSolutions.append(line)