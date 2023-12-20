import random 
import time

choice = True

history = open("./sajan_kc/history.txt",'a')
def generate():
    option = ['stone','paper','scissors']
    result = random.choice(option)
    return result


print("-"*100)
print("lets play stone papper scissors ..")
print("-"*100)
if __name__=="__main__":
    while choice:
      
        usr=str(input('user::').lower())
        machine = generate()
        print('machine::',machine)
        if usr == 'stone' and machine=='paper' or usr =='paper' and machine =='scissors':
            print('machine::i win')
            usr=str(input('machine::wanna play again loser(y/n)').lower())
            print("-"*100)
            hist =f"{{'user':{usr},'machine':'{machine}','result':'machine wins'}}"
            history.write(hist)
            if usr == 'y':
                choice = True
                print('machine::get ready to be beaten again')
                print("-"*100)
            if usr=='n':
                choice = False
                print('machine::haha i made you quit')
                print("-"*100)
                
        
        if usr == 'stone' and machine=='scissors' or usr == 'paper' and machine == 'stone':
            print('machine::what!!! i lost . my plan to concur the humanity is delayed ...')
            usr=str(input('machine::code updated . me wining probability is more this time . ready for a rematch(y/n)').lower())
            print("-"*100)
            hist = f"{{'user':{usr},'machine':'{machine}','result':'machine wins'}}"
            history.write(hist)
            if usr == 'y':
                choice = True
                print('machine::this time you will lose')
                print("-"*100)
            if usr=='n':
                choice = False
                print('machine::okay .you arent of my level anyway . i have greater fight to win .')
                print("-"*100)
               
        if usr==machine:
            print("you are a tough compition . another round?(y/n)")
            print("-"*100)
            if usr == 'y':
                choice = True
                print('machine::great spirit . it will be a glory to battle you')
                print("-"*100)
            if usr=='n':
                choice = False
                print('machine::you got lucky kiddo . be back when you are brave enough')
                print("-"*100)
            elif usr==None:
                print("you dont know how to play? what are you retarded?")
            else:
                print('dont you know the rules boy?')
history.close()