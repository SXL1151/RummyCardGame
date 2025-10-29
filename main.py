import streamlit as st
import random
import time
values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
nameError = True
# List of possible suits (H = Hearts, S = Spades, C = Clubs, D = Diamonds)
suits = ["H", "S", "C", "D"]

class Card:
    def __init__(self, v, s):
        self.value = v
        self.suit = s
        pass
    def __repr__(self):
        return f"{self.value}{self.suit}"


class Deck:
    def __init__(self):
        self.cards = []
        pass
    def create_deck(self):
        for s in suits:
            for v in values:
                self.cards.append(f"{v}{s}")
        return self.cards
    def __repr__(self):
        return self.cards
    def shuffle(self):
        random.shuffle(self.cards)
        return (self)
    def deal_one(self):
        if self.cards == "":
            return None
        card = random.choice(self.cards)
        return card
    def pop_one(self, card, cards):
        index = cards.index(card)
        cards.pop(index)
        self.cards = cards
        return cards
class Hand():
    def __init__(self, owner="Player"):
        self.owner = owner
        self.cards = []
    def add_card(self, card):
        self.cards.append(card)
        return self.cards
    def pop_one(self, card, cards):#Shreyas was here for 67 67 67
        index = cards.index(card)
        cards.pop(index)
        self.cards = cards
        return cards
    def show(self):
        return f"{self.owner}'s hand: {str(self.cards)}"
    
files = [ "C:\\Users\\SXL1151\\.streamlit\\secrets.toml", "C:\\Users\\SXL1151\\Desktop\\.streamlit\\secrets.toml",]
players = []
st.session_state.intro = True
st.title("Gin Rummy")
set = []
if "type" not in st.session_state:
    st.session_state.type = "Hi"
if 'hand' not in st.session_state:
    st.session_state.hand = []
if "deck" not in st.session_state:
    st.session_state.deck = ""
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
Clubs = "https://www.tekeye.uk/playing_cards/images/svg_playing_cards/fronts/png_96_dpi/clubs"
Spades = "https://www.tekeye.uk/playing_cards/images/svg_playing_cards/fronts/png_96_dpi/spades"
SpadesSimple = "https://www.tekeye.uk/playing_cards/images/svg_playing_cards/other/png_96_dpi/spades"
Hearts = "https://www.tekeye.uk/playing_cards/images/svg_playing_cards/fronts/png_96_dpi/hearts"
Diamonds = "https://www.tekeye.uk/playing_cards/images/svg_playing_cards/fronts/png_96_dpi/diamonds"
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
    playerCt = 2
    for i in range(int(playerCt)):
        name = st.text_input(f"Enter Player {i+1} Name", key=i)
        if name == "":
            players.append(f"Player {i+1}")
        elif name in players:
            st.error("Names cannot be the same(add unique identifier)")
            st.session_state.nameError = True
        else:
            players.append(name)
            st.session_state.nameError = False
    if st.session_state.nameError == False:
        st.text(f"{playerCt} players will be playing")
        cardsPerHand = 10
        st.success(f"Each player will recieve {cardsPerHand} cards")
        butPress = st.button("Start Game")
        if butPress:
            st.session_state.press = True
            st.text(players)
            st.session_state.beg = False
    else:
        pass
            
            
            

except Exception as ex:
    st.info(ex)
try:
    st.session_state.deck = Deck()
    st.session_state.deck.create_deck()
    st.session_state.deck.shuffle()
    st.session_state.deck.__repr__()
    if st.session_state.button == True:
        deck = "" 
        for player in players:
            hand = Hand(player)
            for i in range(20):
                dealt = st.session_state.deck.deal_one() 
                popped = st.session_state.deck.pop_one(dealt, st.session_state.deck.cards)         
                st.session_state.bin.append(hand.add_card(dealt))
            st.session_state.hand.append(st.session_state.bin)
        for card in st.session_state.deck.cards:
            st.session_state.deckFin = st.session_state.deckFin + " " + card
        st.success(f"Deck: {st.session_state.deckFin}")
        while True:
            for i, player in enumerate(players):
                if st.session_state.button == True:
                    st.warning(f"Round {i+1}")
                    st.warning(f"Please pass the device to {player}")
                    disposed = ""
                    #Learned st.column through AI(ChatGPT)
                    #I did not copy and paste, rather I learned the concept and applied to my code
                    col1, col2, col3 = st.columns(3)
                    subcol1, subcol2, subcol3, subcol4, subcol5 = st.columns(5)
                    subColList = [subcol1, subcol2, subcol3, subcol4, subcol5,subcol1, subcol2, subcol3, subcol4, subcol5]
                    with col1:
                        if disposed != "":
                            st.session_state.topCard = st.pills("Draw a new card", ["Select from disposal pile", "Select from deck"], key=f"pill {st.session_state.clicks}{i}")
                        else:
                            st.session_state.topCard = st.pills("Draw a new card", ["Select from deck"], key=f"pill2 {st.session_state.clicks}{i}")
                        if st.session_state.topCard:
                            st.session_state.radio = "TBD"
                    with col2:
                        st.session_state.radio = st.radio("Pick a card to dispose", st.session_state.hand[0][0][cardsPerHand*i: cardsPerHand*(i+1)], key=f"radio {st.session_state.clicks}{i}")
                        for j, card in enumerate(st.session_state.hand[0][0][cardsPerHand*i: cardsPerHand*(i+1)]):
                            cardList = list(card)
                            with subColList[(j*0)+j]:
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
                                st.checkbox("", key=f"box 2{st.session_state.clicks}{j}{i}")
                                continue
                    st.divider()
                    with col3:
                        if st.button("Confirm", key=f"button {st.session_state.clicks}{i}{j}"):
                            st.session_state.disposed.append(st.session_state.radio)
                            st.info(f"Disposed card: {st.session_state.radio}")
                            st.session_state.button = False
                        if st.button("Show Cards",key=f"buttonpres {st.session_state.clicks}{i}"):
                            st.session_state.showCards = True
                            st.rerun()
                        if st.button("Hide Cards",key=f"buttonpres2 {st.session_state.clicks}{i}"):
                            st.session_state.showCards = False
                            st.rerun()
                        if st.session_state.button == False:
                            new_hand = hand.pop_one(st.session_state.radio, st.session_state.hand[0][0][cardsPerHand*i: cardsPerHand*(i+1)])
                            if st.session_state.topCard == "Select from deck":
                                new_card = st.session_state.deck.cards[0]
                                st.warning(new_card)
                            else:

                                new_card = st.session_state.disposed[0]
                                st.session_state.disposed.pop(0)
                                st.info(new_card)
                            new_hand.append(new_card)
                            st.session_state.hand[0][0][:cardsPerHand] = new_hand
                    if st.session_state.button == False:
                        if st.session_state.topCard != None:
                            st.success(f"New Hand: {st.session_state.hand[0][0][cardsPerHand*i: cardsPerHand*(i+1)]}")
                        for j, card in enumerate(st.session_state.hand[0][0][cardsPerHand*i: cardsPerHand*(i+1)]):
                            cardList = list(card)
                            with subColList[(j*0)+j]:
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
                        if st.button("Pass to next person"):
                            st.session_state.button = False
                            st.session_state.clicks += 1
                            continue
                        else:
                            st.error("Please complete choose an option to draw a new card")
                            st.session_state.button = True
                            break
except Exception as ex:
    st.error(ex)

                    

                    
