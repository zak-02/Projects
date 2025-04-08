# INHERITANCE (create a Cheat class that will inherit the Pokemon class attributes but it will add to any character 150 a, 200 p
import sqlite3
import random
class Pokemon:
    def __init__(self,name,attack,powerMove):
        self.name=name
        self.attack=attack
        self.powerMove=powerMove
        self.health=1000
        self.halfHealth = self.health//2
        self.score=0

    def showStats(self):# self is used because the method is accessed locally and applies to both pokemon
        print('\nName: '+str(self.name)+'\n'+'Attack: '+str(self.attack)+'\n'+'power move: '+str(self.powerMove)+'\n'+'Health: '+str(self.health)+'\n'+'Score: '+str(self.score))

    def showScore(self):
        print('\nName: '+str(self.name)+'\n'+'Health: '+str(self.health)+'\n'+'Score: '+str(self.score))
        
    def attacks(self, opponent):
        opponent.health=opponent.health-self.attack
        if opponent.health<0:# if opponents health is less than 0, oppoonents health becomes 0 and the other player wins
            opponent.health=0
        #opponent.showStats()# this not a part of the if statement because you always want to show the stats

    def superAttack(self,opponent):
        opponent.health=opponent.health-self.powerMove
        if opponent.health<0:
            opponent.health=0

    def diceRoll(self):
        dice=input(self.name+' press enter to roll the dice: ')
        self.roll=random.randint(1,6)
        print(self.roll)
            
    def validatingAttacks(self,opponent):# self and opponent are used because the role of opponent can be swapped each time when
                                            #the method is called globally - this is to ensure that there is no repeated code in the
                                                    #method            
        self.diceRoll()
        if self.roll >=3:
        
            player1=input(str(self.name)+ ', which attack: ')# pika.name is used because the class is accessed globally - pikachu's
                                                                #attributes are accesssed outside the class
    
            while player1!='normal' and player1!='super':
                print('enter a suitable answer')
                player1=input(str(self.name)+ ', which attack: ')

            while player1=='super' and opponent.health>opponent.halfHealth:
                print('not allowed super attack')
                player1=input(str(self.name)+ ', which attack: ')

               
            if player1=='super':
                self.superAttack(opponent)
                opponent.showStats()
                self.score+=self.powerMove*opponent.health
                self.showScore()
            elif player1=='normal':
                self.attacks(opponent)
                opponent.showStats()
                self.score+=self.attack*opponent.health
                self.showScore()
                
        else:
            print('you miss a turn')


class Cheat(Pokemon):# the cheat class is inheriting the pokemon class
    def __init__(self,name,attack,powerMove):
        super().__init__(name, attack, powerMove)# inheriting the atttributes of the pokemon class so we can can change them (super)
        self.attack = 150
        self.powerMove = 200# only self.attack and self.powermove are defined because we WANT to change these from the pokemon class


for i in range (len(showScore1)):
    print(str(showScore1[i])+' ')
    
computerNumber=random.randint(1,5)
p1=input('Enter your name: ')
p2=input('Enter your name: ')
pikaGuess=int(input('pikachu guess the cheat number between 1 and 5: '))
chariGuess=int(input('charizard guess the cheat number between 1 and 5: '))
print(computerNumber)


if pikaGuess==computerNumber:
    print('pikachu gets to cheat')
    pika=Cheat('Pikachu',55,50)
else:
    pika=Pokemon('Pikachu',55,50) # instantiation - the attributes of the pokemon class that were made in the constructor
                                    # are applied to pika. 

if chariGuess==computerNumber:
    print('Charizard gets to cheat')
    chari=Cheat('Charizard',84,109)
else:
    chari=Pokemon('Charizard',84,109)




while pika.health!=0 and chari.health!=0:
    pika.validatingAttacks(chari)# the two pokemon take turns attacking each other. pika and chari are used because the attributes
                                    # of the class are accessed globally. in them ethod  'validatingAttacks', piks is self and chari is
                                    # the opponent - the self and opponent can be swapped between pika and chari because self and
                                    #opponent can apply to both pokemon inside the class
                                    
    chari.validatingAttacks(pika)# the method can be used repeatedly anywhere outside the class. in this case, it is used twice
                                 # so that pika and chari take turns attacking each other
if pika.health==0:
    print(str(chari.name)+' wins')

               

     
    
    
elif chari.health==0:
    print(str(pika.name)+' wins')
    
   

