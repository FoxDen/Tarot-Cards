#use beautifulsoup or something like this to parse data from a website and output the results. Be sure to credit this website!
#Use the website http://www.paranormality.com/tarot_meanings.shtml
from bs4 import BeautifulSoup
import urllib.request

class deckMeanings():
    upOrDown = ""
    def card(self, givenCard):
        cardInput = givenCard.lower().split(' ')
        if(len(cardInput)>2): #If the length of the cardInput array is greater than or equal to one, AKA if it's a minor arcana card...
            ArcCard = "http://www.paranormality.com/tarot_"+cardInput[0]+"_of_"+cardInput[2].strip(",")+".shtml"
            self.upOrDown = cardInput[3]
        else:                  #If the length of the cardInput array is lesser than one, AKA it's a major arcana card...
            ArcCard = "http://www.paranormality.com/tarot_"+cardInput[0].replace('-','_').strip(",")+".shtml"
            self.upOrDown = cardInput[1] 

        return ArcCard
    def getSite(self, ArcCard):
        local_filename, headers = urllib.request.urlretrieve(ArcCard)
        html = open(local_filename)
        BeautifulSoup(html, "html.parser")
        if(self.upOrDown=="Upwards"):
            return 0
            #retrieve the coding after "upwards"
        else:
            return 0
            #retrieve the coding after "downwards"

deck = deckMeanings()
card1 = "Empress, Upwards"
card2 = "Ten of PENTACLES, Downwards"
card3 = "Wheel-Of-Fortune, Downwards"
card4 = "Queen of SWORDS, Upwards"
deck.getSite(deck.card(card1))
print(deck.card(card2))
print(deck.card(card3))
print(deck.card(card4))

#02/12/17: imported urllib, made it so that it would retrieve the website listed. Used BeautifulSoup. Also made the loop for the tarot cards possible.