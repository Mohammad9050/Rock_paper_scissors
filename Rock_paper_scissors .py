import random
Round, point1, point2 = 1, 0, 0
def re_start():
    restart = input('Do you want play again[y/n]?')
    if restart == 'y':
        global Round, point1, point2
        Round , point1, point2 = 1, 0, 0
        start()
    if restart == 'n':
        exit()
def start():
    global Round, point1, point2
    text = '----------- Round {} -----------'.format(Round)
    choice_txt = '''
    1. Scissor
    2. Rock
    3. Paper
    '''
    print(text)
    print(choice_txt)
    choice = int(input())
    Round += 1
    enemy(choice)
def enemy(choice):
    e_choice = random.randint(1, 3)
    result(choice, e_choice)
def result(opp1, opp2):
    global point1, point2
    while point1 < 3 and point2 < 3:
        if opp1 == opp2:
            print('equal')
            print('you = ', point1, 'pc = ', point2 )
        elif (opp1 == 1 and opp2 == 3) or (opp1 == 2 and opp2 == 1 ) or (opp1 == 3 and opp2 == 2):
            point1 += 1
            print('win round')
            print('you = ', point1, 'pc = ', point2 )
        elif (opp2 == 1 and opp1 == 3) or (opp2 == 2 and opp1 == 1 ) or (opp2 == 3 and opp1 == 2):
            point2 += 1
            print('lost round')
            print('you = ', point1, 'pc = ', point2 )
        if point1 == 3 :
            print('THE END')
            print('You Won')
            re_start()
            break
        if point2 == 3:
            print('THE END')
            print('You Lost')
            re_start()
            break
        start()
start()
