# s = open('helloWorld.txt', 'r')
# print(s.read())

with open('helloWorld.txt') as file:

    # NOTE THAT THERE IS A POINTER, AND WHEN YOU DO FILE.READLINE(), IT RETURNS THAT LINE
    # BUT THE FILE POINTER ALSO MOVES DOWN.
    # THIS ALSO APPLIES TO FILE.READLINES(), WHICH RETURNS ALL THE LINES AS A LIST OF STRINGS AND THE POINTER IS AT THE END
    # SO WHEN YOU PERFORM FILE.READLINES() PRIOR TO FILE.READ(), YOU WILL GET NOTHING BECAUSE THE FILE POINTER IS
    # ALREADY AT THE END
    file.readline()
    file.readlines()
    print(file.read())

with open('helloWorld.txt') as file:
    print(file.readline())