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
                if v == "H":
                    st.text("show")
                    v = st.markdown('''
:hearts:

''')
                elif v == "S":
                    v = st.markdown('''
:spades:
''')
                elif v == "C":
                    v = st.markdown('''
:clubs:
''')
                elif v == "D":
                    v = st.markdown('''
:diamonds:
''')
                self.cards.append(f"{v}{s}")
    def __repr__(self):
        return self.cards
    def shuffle(self):
        random.shuffle(self.cards)
        return (self)
    def deal_one(self):
        if self.cards == "":
            return None
        card = random.choice(self.cards)
        index = self.cards.index(card)
        self.cards.pop(index)
        return card
    def pop_one(self, card, cards):
        index = cards.index(card)
        cards.pop(index)
        
class Hand:
    def __init__(self, owner="Player"):
        self.owner = owner
        self.cards = []
    def add_card(self, card):
        
        self.cards.append(card)
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
st.title("Rummy")
set = []
if "type" not in st.session_state:
    st.session_state.type = "Hi"
if 'hand' not in st.session_state:
    st.session_state.hand = []
if "deck" not in st.session_state:
    st.session_state.deck = "TBD"
if "radio" not in st.session_state:
    st.session_state.radio = "TBD"
st.text(st.session_state.type)
st.session_state.type = st.radio("Hi", ["hie", 'l'])
st.text(st.session_state.type)

st.markdown('''
            
            :red[Welcome to the rummy card game!]
            ''')
try:
    playerCt = st.selectbox("How many players will be playing?", ("2", "3", "4", "5", "6"))
    for i in range(int(playerCt)):
        name = st.text_input(f"Enter Player {i+1} Name", key=i)
        if name == "":
            players.append(f"Player {i+1}")
        elif name in players:
            st.error("Names cannot be the same(add unique identifier)")
            nameError = True
        else:
            players.append(name)
            nameError = False
        
    if nameError == False:
        st.text(f"{playerCt} players will be playing")
        if playerCt == "2":
            cardsPerHand = 13
        elif playerCt == ("3") or playerCt == ("4"):
            cardsPerHand = 7
        else:
            cardsPerHand = 6
        st.success(f"Each player will recieve {cardsPerHand} cards")
        if playerCt:
            butPress = st.button("Start Game")
            nameError = False
        if nameError == False:
            if butPress:
                st.session_state["press"] = True
            if st.session_state["press"] == True:
                st.success("Game has started!")
                once = True
                
                
                

except:
    pass
try:
    deck_1 = Deck()
    deck_1.create_deck()
    deck_1.shuffle()
    st.session_state.deck = deck_1.__repr__()
    st.text(st.session_state.deck)
    st.text(players)
    for player in players:
        hand = Hand(player)
        for i in range(cardsPerHand):  
            dealt = deck_1.deal_one()          
            hand.add_card(dealt)
            hand2 = hand.show()
        st.session_state.hand.append(hand.cards)
    finDeck = (deck_1.__repr__())
    finDeckStr = ""
    for card in finDeck:
        finDeckStr = finDeckStr + " " + card
    st.session_state.deck = finDeckStr
    st.success(f"Deck: {st.session_state.deck}")
    st.warning("Round 1")
    st.warning(f"Please pass the device to {players[len(players)-(len(players))]}")
    st.success(st.session_state.hand[0])
    for card in st.session_state.hand[0]:
        values = card[0]
    set1 = []
    row1 = []
    for value in values:
        count = values.count(value[0])
        if count == 3 or count == 4:
            set1.append(value)
            for value2 in values:
                if value2[0] == value[0]:
                    set1.append(value2)
            st.info(set1)
        else:
            valueset = 0
            valueset = int(value[0])
            type = value[1]
            for value3 in values:
                if value3[1] != type:
                    break
                else:
                    if (int(value3[0]) - 1) == valueset:
                        valueset = int(value3[0])
                        row1.append(value)
                        row1.append(value3)
            st.info(row1)



    st.session_state.radio = st.radio("Pick a card to dispose", st.session_state.hand[0])
    with st.spinner("Loading...", show_time=True):
        time.sleep(15)
    popped = hand.pop_one(st.session_state.radio, st.session_state.hand[0])
    st.success(st.session_state.hand[0])

    
    
except Exception as ex:
    st.error(ex)
