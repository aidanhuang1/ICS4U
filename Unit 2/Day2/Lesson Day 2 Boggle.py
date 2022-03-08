'''
Day 2 File IO Lesson
Reading groups of lines

ICS4U
Aaron Quesnelle
'''

with open("boggledata41.txt") as file_in:

    #five problem sets
    for i in range(0, 5):

        board = []
        #create a matrix of the 4x4 board
        #read in the four lines of the board
        for i in range(0, 4):
            line = list(file_in.readline().strip())
            board.append(line)

        print(f'Board {board}')

        #read in the word count
        wordCount = int(file_in.readline())

        #read in the list of words, one per line
        wordList = []
        for i in range(0, wordCount):
            line = file_in.readline().strip()
            wordList.append(line)

        print(f'Words {wordList}')

        print("\n\n\n")


    
        
