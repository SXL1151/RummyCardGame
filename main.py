import streamlit as st
import random
import time
values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
nameError = True
# List of possible suits (H = Hearts, S = Spades, C = Clubs, D = Diamonds)
suits = ["H", "S", "C", "D"]

class Card:   #Creates the cards and stores
    def __init__(self, v, s):
        self.value = v
        self.suit = s
        pass
    def __repr__(self):
        return f"{self.value}{self.suit}"


class Deck:
    def __init__(self):  #Initializes self.cards for the deck
        self.cards = []
        pass
    def create_deck(self): #Creates the deck
        for s in suits:
            for v in values:
                self.cards.append(f"{v}{s}")
        return self.cards
    def __repr__(self):  #Returns self.card
        return self.cards
    def shuffle(self):   #Shuffles the deck
        random.shuffle(self.cards)
        return (self)
    def deal_one(self):   #Randomely deals a card
        if self.cards == "":
            return None
        card = random.choice(self.cards)
        return card
    def pop_one(self, card, cards):   #When called, this functions pops a card from the deck
        index = cards.index(card)
        cards.pop(index)
        self.cards = cards
        return cards
class Hand():
    def __init__(self, owner="Player"):  #Initializes the hand and its owner
        self.owner = owner
        self.cards = []
    def add_card(self, card):  #Adds a card to the hand
        self.cards.append(card)
        return self.cards
    def pop_one(self, card, cards):#Pops a card from the hand
        index = cards.index(card)
        cards.pop(index)
        self.cards = cards
        return cards
    def show(self): #Returns the hand as a string
        return f"{self.owner}'s hand: {str(self.cards)}"
    

st.session_state.intro = True
st.title("Gin Rummy")
set1 = ""
#Lines 62-91 initializes variables that would not get affected if the player reruns the games; saves the variables in session state.
if "type" not in st.session_state:
    st.session_state.type = "Hi"
if 'hand' not in st.session_state:
    st.session_state.hand = []
if "handObj" not in st.session_state:
    st.session_state.handObj = Hand()
if "deck" not in st.session_state:#Creates a deck object in a session state variable(so that the deck doesn't keep on changing)
    #Used ChatGPT to help me stop the deck from autoshuffling each time in lines 68-71
    deck = Deck()
    deck.create_deck()
    deck.shuffle()
    st.session_state.deck = deck
if "radio" not in st.session_state:
    st.session_state.radio = "TBD"
if "topCard" not in st.session_state:
    st.session_state.topCard = "TBD"
if "button" not in st.session_state:
    st.session_state.button = True
if "press" not in st.session_state:
    st.session_state.press = False
if "nameError" not in st.session_state:
    st.session_state.nameError = False
if "repr" not in st.session_state:
    st.session_state.repr = ""
if "shuffle" not in st.session_state:
        st.session_state.shuffle = True
if "deckFin" not in st.session_state:
    st.session_state.deckFin = ""
if "disposed" not in st.session_state:
    st.session_state.disposed = []
if "showCards" not in st.session_state:
    st.session_state.showCards = False
if "clicks" not in st.session_state:
    st.session_state.clicks = 0
if "bin" not in st.session_state:
    st.session_state.bin = []
if "end" not in st.session_state:
    st.session_state.end = False
if "setMeld" not in st.session_state:
    st.session_state.setMeld = []
if "setMeldFin" not in st.session_state:
    st.session_state.setMeldFin = []
if "beg" not in st.session_state:
    st.session_state.beg = True
if "handShuff" not in st.session_state:
    st.session_state.handShuff = True
if "players" not in st.session_state:
    st.session_state.players = []
if "cardsPerHand" not in st.session_state:
    st.session_state.cardsPerHand = 0
if "lenSet" not in st.session_state:
    st.session_state.lenSet = []
if "start" not in st.session_state:
    st.session_state.start = False
#Lines 93 - 97; base url to get the images of cards
Clubs = "https://www.tekeye.uk/playing_cards/images/svg_playing_cards/fronts/png_96_dpi/clubs"
Spades = "https://www.tekeye.uk/playing_cards/images/svg_playing_cards/fronts/png_96_dpi/spades"
SpadesSimple = "https://www.tekeye.uk/playing_cards/images/svg_playing_cards/other/png_96_dpi/spades"
Hearts = "https://www.tekeye.uk/playing_cards/images/svg_playing_cards/fronts/png_96_dpi/hearts"
Diamonds = "https://www.tekeye.uk/playing_cards/images/svg_playing_cards/fronts/png_96_dpi/diamonds"
#Lines 99 - 112; attaches the string to the end of one of the base url and the full image url is created and can be called easily.
Ac = "_ace.png"
Two = "_2.png"
Three = "_3.png"
Four = "_4.png"
Five = "_5.png"
Six = "_6.png"
Seven = "_7.png"
Eight = "_8.png"
Nine = "_9.png"
Ten = "_10.png"
Jack = "_jack.png"
Queen = "_queen.png"
King = "_king.png"
Asimple = "_ace_simple.png"
st.markdown('''  
        :red[Welcome to the rummy card game!]
        ''')
try:
    if st.session_state.beg == True:
        playerCt = 2
        for i in range(int(playerCt)):
            name = st.text_input(f"Enter Player {i+1} Name", key=i)
            if name == "":
                st.session_state.players.append(f"Player {i+1}")
            elif name in st.session_state.players:
                st.error("Names cannot be the same(add unique identifier)") #Players enter names and the code checks for similar names
                st.session_state.nameError = True
            else:
                st.session_state.players.append(name)
                st.session_state.nameError = False
        if st.session_state.nameError == False: #If there is no name error, the following code continues
            st.text(f"{playerCt} players will be playing")
            st.session_state.cardsPerHand = 10
            st.success(f"Each player will recieve {st.session_state.cardsPerHand} cards")
            butPress = st.button("Start Game")
            if butPress:
                st.session_state.press = True
                st.text(st.session_state.players)
                st.session_state.beg = False
                st.rerun()
        else:
            pass
            
            
            

except Exception as ex:
    st.info(ex)

if st.session_state.beg == False:
    if st.session_state.handShuff == True:
        if st.button("Deal Hands"):
            for i in range(20):
                dealt = st.session_state.deck.deal_one() 
                popped = st.session_state.deck.pop_one(dealt, st.session_state.deck.cards)        #Creates hands for both players 
                st.session_state.bin.append(st.session_state.handObj.add_card(dealt))
            st.session_state.hand.append(st.session_state.bin)
            st.session_state.handShuff = False
            st.rerun()
if st.session_state.handShuff == False:
    deck = "" 
    for z in range(6):
        for i, player in enumerate(st.session_state.players): #Game starts
            if st.session_state.button == True:
                st.warning(f"Round {z+1}")
                st.warning(f"Please pass the device to {player}")
                disposed = ""
                #Learned st.column through AI(ChatGPT)
                #I did not copy and paste, rather I learned the concept and applied to my code
                col1, col2, col3 = st.columns(3)
                subcol1, subcol2, subcol3, subcol4, subcol5 = st.columns(5)
                subColList = [subcol1, subcol2, subcol3, subcol4, subcol5,subcol1, subcol2, subcol3, subcol4, subcol5] #To align the interactive objects
                with col1:
                    if disposed != "": #Asks player to draw from deck or disposal pile
                        st.session_state.topCard = st.pills("Draw a new card", ["Select from disposal pile", "Select from deck"], key=f"pill {st.session_state.clicks}{i}{z}")
                    else:
                        st.session_state.topCard = st.pills("Draw a new card", ["Select from deck"], key=f"pill2 {st.session_state.clicks}{i}{z}")
                    if st.session_state.topCard:
                        st.session_state.radio = "TBD"
                    meldoset = st.multiselect("Create Melds or Sets",st.session_state.hand[0][0][st.session_state.cardsPerHand*i: st.session_state.cardsPerHand*(i+1)], max_selections = 4 , key=f"multi {st.session_state.clicks}{i}{z}")
                    st.session_state.setMeld = meldoset
                    meld = []
                    for char in st.session_state.setMeld:
                        listedChar = list(char)
                        for char2 in st.session_state.setMeld:
                            listedChar2 = list(char2)
                            if listedChar[0] == listedChar2[0]:
                                set1 = True
                            else:
                                set1 = False
                                break
                    st.info(meld)
                    if st.button("Form Set/Meld", key=f"buttonsetmeld {st.session_state.clicks}{i}{z}"):
                        suits = [card[-1] for card in st.session_state.setMeld]
                        values = [card[:0] for card in st.session_state.setMeld]
                        st.text(len(suits))
                        if len((suits)) < 3:
                            st.warning("Not a Run")
                        st.info(st.session_state.setMeld)
                        for card in st.session_state.setMeld:
                            cardList = list(card)
                            if len(cardList) == 3:
                                value = cardList[0] + cardList[1]
                            elif len(cardList) == 2:
                                value = cardList[0]
                            for card2 in st.session_state.setMeld:
                                cardList2 = list(card2)
                                if len(cardList) == 3:
                                    value2 = cardList[0] + cardList[1]
                                elif len(cardList2) == 2:
                                    value2 = cardList2[0]
                        if value == value2:
                            st.success("Run Approved")
                        if len(st.session_state.setMeld) in st.session_state.lenSet:
                            st.warning("You cannot have more than 1 4-card sets/runs")
                        elif set1 == True and ((len(st.session_state.setMeld)) == 3 or (len(st.session_state.setMeld)) == 4):
                            if st.session_state.setMeld in st.session_state.setMeldFin:
                                st.warning("Set/Meld already approved")
                        
                            else:
                                st.success("Set Approved")
                                st.session_state.setMeldFin.append(st.session_state.setMeld)
                            
                        elif set == True and ((len(st.session_state.setMeld)) != 3 or (len(st.session_state.setMeld)) != 4):
                            st.error("Not a set")
                            meldoset = ""
                            st.session_state.setMeld = []
                        else:
                            st.error("Not a set")
                            meldoset = ""
                        st.session_state.setMeld = []
                    st.info(st.session_state.setMeldFin)
                with col2:
                    st.session_state.radio = st.radio("Pick a card to dispose", st.session_state.hand[0][0][st.session_state.cardsPerHand*i: st.session_state.cardsPerHand*(i+1)], key=f"radio {st.session_state.clicks}{i}{z}") #Asks player for a card to dispose
                    for j, card in enumerate(st.session_state.hand[0][0][st.session_state.cardsPerHand*i: st.session_state.cardsPerHand*(i+1)]):
                        cardList = list(card)
                        with subColList[(j*0)+j]: #The following code creates an image for each card in the players hand
                            if st.session_state.showCards == False:
                                st.image("https://i.ebayimg.com/images/g/MjgAAOSw2OliE9eG/s-l1200.jpg")
                            else:
                                card2 = ""
                                if cardList[0] == "A":
                                    if cardList[1] == "S":
                                        st.image(SpadesSimple + Asimple)
                                    elif cardList[1] == "C":
                                        st.image(Clubs + Ac)
                                    elif cardList[1] == "H":
                                        st.image(Hearts + Ac)
                                    else:
                                        st.image(Diamonds + Ac)
                                if cardList[0] == "2":
                                    if cardList[1] == "S":
                                        st.image(Spades + Two)
                                    elif cardList[1] == "C":
                                        st.image(Clubs + Two)
                                    elif cardList[1] == "H":
                                        st.image(Hearts + Two)
                                    else:
                                        st.image(Diamonds + Two)
                                if cardList[0] == "3":
                                    if cardList[1] == "S":
                                        st.image(Spades + Three)
                                    elif cardList[1] == "C":
                                        st.image(Clubs + Three)
                                    elif cardList[1] == "H":
                                        st.image(Hearts + Three)
                                    else:
                                        st.image(Diamonds + Three)
                                if cardList[0] == "4":
                                    if cardList[1] == "S":
                                        st.image(Spades + Four)
                                    elif cardList[1] == "C":
                                        st.image(Clubs + Four)
                                    elif cardList[1] == "H":
                                        st.image(Hearts + Four)
                                    else:
                                        st.image(Diamonds + Four)
                                if cardList[0] == "5":
                                    if cardList[1] == "S":
                                        st.image(Spades + Five)
                                    elif cardList[1] == "C":
                                        st.image(Clubs + Five)
                                    elif cardList[1] == "H":
                                        st.image(Hearts + Five)
                                    else:
                                        st.image(Diamonds + Five)
                                if cardList[0] == "6":
                                    if cardList[1] == "S":
                                        st.image(Spades + Six)
                                    elif cardList[1] == "C":
                                        st.image(Clubs + Six)
                                    elif cardList[1] == "H":
                                        st.image(Hearts + Six)
                                    else:
                                        st.image(Diamonds + Six)
                                if cardList[0] == "7":
                                    if cardList[1] == "S":
                                        st.image(Spades + Seven)
                                    elif cardList[1] == "C":
                                        st.image(Clubs + Seven)
                                    elif cardList[1] == "H":
                                        st.image(Hearts + Seven)
                                    else:
                                        st.image(Diamonds + Seven)
                                if cardList[0] == "8":
                                    if cardList[1] == "S":
                                        st.image(Spades + Eight)
                                        card = Spades + King
                                    elif cardList[1] == "C":
                                        st.image(Clubs + Eight)
                                        card = Spades + King
                                    elif cardList[1] == "H":
                                        st.image(Hearts + Eight)
                                        card = Spades + King
                                    else:
                                        st.image(Diamonds + Eight)
                                        card = Spades + King

                                if cardList[0] == "9":
                                    if cardList[1] == "S":
                                        st.image(Spades + Nine)
                                        card = Spades + Nine
                                    elif cardList[1] == "C":
                                        st.image(Clubs + Nine)
                                        card = Clubs + Nine
                                    elif cardList[1] == "H":
                                        st.image(Hearts + Nine)
                                        card = Hearts + Nine
                                    else:
                                        st.image(Diamonds + Nine)
                                        card = Diamonds + Nine
                                if cardList[0] + cardList[1] == "10":
                                    if cardList[2] == "S":
                                        st.image(Spades + Ten)
                                        card = Spades + Ten
                                    elif cardList[2] == "C":
                                        st.image(Clubs + Ten)
                                        card = Clubs + Ten
                                    elif cardList[2] == "H":
                                        st.image(Hearts + Ten)
                                        card = Hearts + Ten
                                    else:
                                        st.image(Diamonds + Ten)
                                        card = Diamonds + Ten
                                if cardList[0] == "J":
                                    if cardList[1] == "S":
                                        st.image(Spades + Jack)
                                        card = Spades + Jack
                                    elif cardList[1] == "C":
                                        st.image(Clubs + Jack)
                                        card = Clubs + Jack
                                    elif cardList[1] == "H":
                                        st.image(Hearts + Jack)
                                        card = Hearts + Jack
                                    else:
                                        st.image(Diamonds + Jack)
                                        card = Diamonds + Jack
                                if cardList[0] == "Q":
                                    if cardList[1] == "S":
                                        st.image(Spades + Queen)
                                        card = Spades + Queen
                                    elif cardList[1] == "C":
                                        st.image(Clubs + Queen)
                                        card = Clubs + Queen
                                    elif cardList[1] == "H":
                                        st.image(Hearts + Queen)
                                        card = Clubs + Queen
                                    else:
                                        st.image(Diamonds + Queen)
                                        card = Spades + Queen
                                if cardList[0] == "K":
                                    if cardList[1] == "S":
                                        st.image(Spades + King)
                                        card = Spades + King
                                    elif cardList[1] == "C":
                                        st.image(Clubs + King)
                                        card = Clubs + King
                                    elif cardList[1] == "H":
                                        st.image(Hearts + King)
                                        card = Hearts + King
                                    else:
                                        st.image(Diamonds + King)
                                        card = Diamonds + King
                            setmelds = st.checkbox("", key=f"box 2{st.session_state.clicks}{j}{i}{z}")
                            
                            continue
                st.divider()
                st.info(st.session_state.setMeldFin)
                with col3:#Includes options to confirm, show cards, and hide cards
                    if st.button("Confirm", key=f"button {st.session_state.clicks}{i}{j}{z}"):
                        new_hand = st.session_state.handObj.pop_one(st.session_state.radio, st.session_state.hand[0][0][st.session_state.cardsPerHand*i: st.session_state.cardsPerHand*(i+1)])
                        st.info(new_hand)
                        if st.session_state.topCard == "Select from deck":
                            new_card = st.session_state.deck.cards[0]
                            st.session_state.deck.pop_one(new_card, st.session_state.deck.cards)
                            st.warning(new_card)
                        elif st.session_state.topCard == "Select from disposal pile":
                            new_card = st.session_state.disposed[0]
                            st.session_state.disposed.pop(0)
                            st.info(new_card)
                        else:
                            st.error("Please complete choose an option to draw a new card")#Makes player to choose an option to draw a new card
                            st.session_state.button = True
                            continue
                        new_hand.append(new_card)
                        if st.session_state.topCard != "":
                            st.success(f"New Hand: {new_hand}")#Shows the player their new hand
                            for j, card in enumerate(new_hand):
                                cardList = list(card)
                                with subColList[(j*0)+j]:#Provides images for updated hand
                                    if st.session_state.showCards == False:
                                        st.image("https://i.ebayimg.com/images/g/MjgAAOSw2OliE9eG/s-l1200.jpg")
                                    else:
                                        if cardList[0] == "A":
                                            if cardList[1] == "S":
                                                st.image(SpadesSimple + Asimple)
                                            elif cardList[1] == "C":
                                                st.image(Clubs + Ac)
                                            elif cardList[1] == "H":
                                                st.image(Hearts + Ac)
                                            else:
                                                st.image(Diamonds + Ac)
                                        if cardList[0] == "2":
                                            if cardList[1] == "S":
                                                st.image(Spades + Two)
                                            elif cardList[1] == "C":
                                                st.image(Clubs + Two)
                                            elif cardList[1] == "H":
                                                st.image(Hearts + Two)
                                            else:
                                                st.image(Diamonds + Two)
                                        if cardList[0] == "3":
                                            if cardList[1] == "S":
                                                st.image(Spades + Three)
                                            elif cardList[1] == "C":
                                                st.image(Clubs + Three)
                                            elif cardList[1] == "H":
                                                st.image(Hearts + Three)
                                            else:
                                                st.image(Diamonds + Three)
                                        if cardList[0] == "4":
                                            if cardList[1] == "S":
                                                st.image(Spades + Four)
                                            elif cardList[1] == "C":
                                                st.image(Clubs + Four)
                                            elif cardList[1] == "H":
                                                st.image(Hearts + Four)
                                            else:
                                                st.image(Diamonds + Four)
                                        if cardList[0] == "5":
                                            if cardList[1] == "S":
                                                st.image(Spades + Five)
                                            elif cardList[1] == "C":
                                                st.image(Clubs + Five)
                                            elif cardList[1] == "H":
                                                st.image(Hearts + Five)
                                            else:
                                                st.image(Diamonds + Five)
                                        if cardList[0] == "6":
                                            if cardList[1] == "S":
                                                st.image(Spades + Six)
                                            elif cardList[1] == "C":
                                                st.image(Clubs + Six)
                                            elif cardList[1] == "H":
                                                st.image(Hearts + Six)
                                            else:
                                                st.image(Diamonds + Six)
                                        if cardList[0] == "7":
                                            if cardList[1] == "S":
                                                st.image(Spades + Seven)
                                            elif cardList[1] == "C":
                                                st.image(Clubs + Seven)
                                            elif cardList[1] == "H":
                                                st.image(Hearts + Seven)
                                            else:
                                                st.image(Diamonds + Seven)
                                        if cardList[0] == "8":
                                            if cardList[1] == "S":
                                                st.image(Spades + Eight)
                                            elif cardList[1] == "C":
                                                st.image(Clubs + Eight)
                                            elif cardList[1] == "H":
                                                st.image(Hearts + Eight)
                                            else:
                                                st.image(Diamonds + Eight)
                                        if cardList[0] == "9":
                                            if cardList[1] == "S":
                                                st.image(Spades + Nine)
                                            elif cardList[1] == "C":
                                                st.image(Clubs + Nine)
                                            elif cardList[1] == "H":
                                                st.image(Hearts + Nine)
                                            else:
                                                st.image(Diamonds + Nine)
                                        if cardList[0] + cardList[1] == "10":
                                            if cardList[2] == "S":
                                                st.image(Spades + Ten)
                                            elif cardList[2] == "C":
                                                st.image(Clubs + Ten)
                                            elif cardList[2] == "H":
                                                st.image(Hearts + Ten)
                                            else:
                                                st.image(Diamonds + Ten)
                                        if cardList[0] == "J":
                                            if cardList[1] == "S":
                                                st.image(Spades + Jack)
                                            elif cardList[1] == "C":
                                                st.image(Clubs + Jack)
                                            elif cardList[1] == "H":
                                                st.image(Hearts + Jack)
                                            else:
                                                st.image(Diamonds + Jack)
                                        if cardList[0] == "Q":
                                            if cardList[1] == "S":
                                                st.image(Spades + Queen)
                                            elif cardList[1] == "C":
                                                st.image(Clubs + Queen)
                                            elif cardList[1] == "H":
                                                st.image(Hearts + Queen)
                                            else:
                                                st.image(Diamonds + Queen)
                                        if cardList[0] == "K":
                                            if cardList[1] == "S":
                                                st.image(Spades + King)
                                            elif cardList[1] == "C":
                                                st.image(Clubs + King)
                                            elif cardList[1] == "H":
                                                st.image(Hearts + King)
                                            else:
                                                st.image(Diamonds + King)
                                    st.checkbox("", key=f"box 4{st.session_state.clicks}{j}")
                                    continue
                            if st.button("Pass to next person"): #Asks player to pass the device to the next player
                                st.session_state.button = False
                                st.session_state.clicks += 1
                                break
                        st.session_state.hand[0][0][:st.session_state.cardsPerHand] = new_hand
                        st.session_state.disposed.append(st.session_state.radio)
                        st.info(f"Disposed card: {st.session_state.radio}")
                        st.session_state.button = False
                    if st.button("Show Cards",key=f"buttonpres {st.session_state.clicks}{i}{z}"):
                        st.session_state.showCards = True
                        st.rerun()
                    if st.button("Hide Cards",key=f"buttonpres2 {st.session_state.clicks}{i}{z}"):
                        st.session_state.showCards = False
                        st.rerun()
                    if st.button("Call Gin", key=f"buttongin {st.session_state.clicks}{i}{j}{z}"):
                        st.session_state.end = True
                    if st.button("Knock", key=f"buttonknock {st.session_state.clicks}{i}{j}{z}"):
                        st.session_state.end = True        


                

                
