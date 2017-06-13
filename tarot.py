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
            print("There are 10 cards drawn in a Celtic Cross layout.")
            print("The Present represents what is happening to the querent right now, and is represented by the "+self.usedCards[0]+". Its meaning is: \n"+self.interpretation.card(self.usedCards[0])+".")
            print("The Challenge lays atop the Present card and represents the immediate problem or challenge facing the querent. It is represented by the "+self.usedCards[1]+". Its meaning is \n"+self.interpretation.card(self.usedCards[0])+".")
            print("The Past stants to the left and represents the events leading up to the present situation. It is represented by the "+self.usedCards[2]+". Its meaning is: \n"+self.interpretation.card(self.usedCards[2])+".")
            print("The Future stands to the right and represents what is likely to occur soon. It is represented by the "+self.usedCards[3]+". Its meaning is \n"+self.interpretation.card(self.usedCards[3])+".")
            print("The Above card is above these cards, and reflects the querent's goal, aspiration or best outcome.  It is represented by the "+self.usedCards[4]+". Its meaning is \n"+self.interpretation.card(self.usedCards[4])+".")
            print("The Below card is below these cards, and reflects what is written within the querent's subconscious, delving deeper into the core foundation. It is represented by the "+self.usedCards[4]+". Its meaning is \n"+self.interpretation.card(self.usedCards[4])+".")
            print("These other cards are laid out to the right of the cross. It is represented by the "+self.usedCards[5]+". Its meaning is \n"+self.interpretation.card(self.usedCards[5])+".")
            print("The Advice card takes into account everything happening within the querent's life and provides a recommedation. It is represented by the "+self.usedCards[6]+". Its meaning is \n"+self.interpretation.card(self.usedCards[6])+".")
            print("The External Influences card highlights the people, energies, or events which will affect the outcome of the question. It is represented by the "+self.usedCards[7]+". Its meaning is \n"+self.interpretation.card(self.usedCards[7])+".")
            print("The Hopes and Fears card represents the person's hopes and fears. This can be a complicated card to interpret. It is represented by the "+self.usedCards[8]+". Its meaning is \n"+self.interpretation.card(self.usedCards[8])+".")
            print("The Outcome card represents where the situation is headed and if/how the issue will be resolved, if it is resolved. It is represented by the "+self.usedCards[9]+". Its meaning is \n"+self.interpretation.card(self.usedCards[9])+".")
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