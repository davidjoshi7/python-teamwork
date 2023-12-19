import random 
import time

choice = True


def generate():
    option = ['stone','paper','scissors']
    result = random.choice(option)
    return result

if __name__=="__main__":
    while choice:
        print("-"*100)
        print("lets play stone papper scissors ..")
        print("-"*100)
        usr=str(input('machine::make a choice').lower())
        machine = generate()
        print('machine::',machine)
        if usr == 'stone' and machine=='paper' or usr =='paper' and machine =='scissors':
            print('machine::i win')
            usr=str(input('machine::wanna play again loser(y/n)').lower())
            if usr == 'y':
                choice = True
                print('machine::get read to be beaten again')
            if usr=='n':
                choice = False
                print('machine::haha i made you quit')
        
        if usr == 'stone' and machine=='scissors' or usr == 'paper' and machine == 'stone':
            print('machine::what!!! i lost . my plan to concur the humanity is delayed ...')
            usr=str(input('machine::code updated . me wining probability is more this time . ready for a rematch(y/n)').lower())
            if usr == 'y':
                choice = True
                print('machine::get read to be beaten again')
            if usr=='n':
                choice = False
                print('machine::okay you arent of my level anyway')

