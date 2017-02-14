import random
from deckMeanings import deckMeanings

#tarot card generator and reader!
#Set up deck first.

class deck:
    deckFaces = ["WANDS", "PENTACLES", "SWORDS", "CUPS"]
    majArc = ["FOOL","MAGICIAN","HIGH-PRIESTESS", "EMPRESS", "EMPEROR",
              "POPE","LOVERS","CHARIOT","STRENGTH","HERMIT","WHEEL-OF-FORTUNE",
              "JUSTICE","HANGED MAN","DEATH","TEMPERANCE","DEVIL","TOWER","STAR",
              "MOON","SUN","JUDGEMENT","WORLD","FOOL"]
    deckNumbers = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Page", "Knight" "Queen", "King"]
    deckUpright = ["Upright","Downwards"]
    deckOfCards = []
    usedCards = []

    for face in deckFaces:
        for num in deckNumbers:
            deckOfCards.append(num+" of "+face)

    for face in majArc:
        deckOfCards.append(face)

    interpretation = deckMeanings()

    def generateRandom(self):
        card = random.randint(1,len(self.deckOfCards))
        upOrDown = random.randint(0,1)
        
        returnedCard = self.deckOfCards[card]+", "+self.deckUpright[upOrDown]
        self.usedCards.append(returnedCard)
        self.deckOfCards.remove(self.deckOfCards[card])
        #if it throws an error, do something
        return returnedCard

    def printDeck(self):
        for i in range(len(self.deckOfCards)):
            print(self.deckOfCards[i])
    
    def printCards(self, type):
        if type == "threeDeck":
            print("The Past is represented by: the "+self.usedCards[0]+". Its meaning is: \n"+self.interpretation.card(self.usedCards[0])+".")
            print("The Present is represented by: the "+self.usedCards[1]+". Its meaning is: \n"+self.interpretation.card(self.usedCards[1])+".")
            print("The Future is represented by: the "+self.usedCards[2]+". Its meaning is: \n"+self.interpretation.card(self.usedCards[2])+".")
        elif type == "multipleCards":
            print("In progress.")
        else:
            print("Your card is: the "+self.usedCards[0]+". Its meaning is: "+self.interpretation.card(self.usedCards[0]+"."))

    def clearCards(self):
        self.usedCards.clear()

    def askQuestion(self,question):
        while (question.endswith("?")==False):
            print("This is no question. Please, enter one.")
            question = input()
        print("Thank you. I will now draw the cards. Would you prefer:")
        print("1) The three-card spread, showing past, present and future")
        print("2) The one-card spread, showing only the answer to your question")
        print("3) The celtic cross spread, showing 10 cards")

        number = input("Please input the number there.")

        if(number == "1"):
            for x in range(0,3):
                newTarotDeck.generateRandom()
            newTarotDeck.printCards("threeDeck")
        elif(number == "2"):
            newTarotDeck.generateRandom()
            newTarotDeck.printCards("singleCard")
        elif(number == "3"):
            for x in range(0,10):
                newTarotDeck.generateRandom()
            newTarotDeck.printCards("multipleCards")
        else:
            print("Working on the other ones!")


newTarotDeck = deck()
question = input("This is nothing more than a tarot deck app I'm testing out. I'd like to thank the paranormality website for giving me the interpretations of their cards. \n"+
                 "Please focus first, and clear your mind. Then, enter the question you want answered.")

newTarotDeck.askQuestion(question)
newQuestion = input("Would you like to ask another question? Y/N")

while(newQuestion == "Y"):
    newTarotDeck.clearCards()
    question = input("Focus, and clear your mind before entering the question you want asked.")
    newTarotDeck.askQuestion(question)
    newQuestion = input("Anything else? Y/N")

if(newQuestion == "N"):
    print("Thank you then! Have a nice day.")
        

#First, import a script getting the information about the tarots from a website! be sure to credit this website. 