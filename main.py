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
if "topCard" not in st.session_state:
    st.session_state.topCard = "TBD"
if "button" not in st.session_state:
    st.session_state.button = False
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
    st.text(players)
    deck = Deck()
    deck.create_deck()
    deck.shuffle()
    deck.__repr__()
    finDeckStr = ""
    for card in st.session_state.deck.__repr__():
        finDeckStr = finDeckStr + " " + card
    st.session_state.deck = (finDeckStr)
    for player in players:
        hand = Hand(player)
        for i in range(cardsPerHand):  
            dealt = deck.deal_one()          
            hand.add_card(dealt)
            hand2 = hand.show()
        st.session_state.hand.append(hand.cards)
    st.success(f"Deck: {st.session_state.deck}")
    st.warning("Round 1")
    st.warning(f"Please pass the device to {players[len(players)-(len(players))]}")
    st.success(st.session_state.hand[0])
    '''
    sets1 = []
    single = False
    for j, card in enumerate(st.session_state.hand[0]):
        for i, card2 in enumerate(st.session_state.hand[0]):
            if (card[0] == card2[0]) and (card2 not in sets1) and (card not in sets1) and (card != card2):
                sets1.append(card)
                st.session_state.hand[0].pop(j)
                sets1.append(card2)
                st.session_state.hand[0].pop(i)
    for char in st.session_state.hand[0]:
        sets1.append(char)
    for i, val in enumerate(sets1):
        for j, vals in enumerate(sets1):
            if val == vals:
                sets1.pop(j)
                break
    #st.session_state.hand[0] = sets1
    st.info(sets1)
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
            st.success(value[0])
            valueset = int(value[0])
            type = value[0]
            for value3 in values:
                st.success("hi" + str(value3[0]))
                if value3[0] != type:
                    break
                else:
                    if ((int(value3[0]) - 1)) == valueset:
                        valueset = int(value3[0])
                        row1.append(value)
                        row1.append(value3)
            st.info(row1)
'''
    if st.session_state.button == False:
        disposed = ""
        if disposed != "":
            st.session_state.topCard = st.pills("Pick a new card", ["Select from disposal pile", "Select from deck"])
        else:
            st.session_state.topCard = st.pills("Pick a new card", ["Select from deck"])
        if st.session_state.topCard:
            st.session_state.radio = "TBD"
        st.session_state.radio = st.radio("Pick a card to dispose", st.session_state.hand[0])
        disposed = st.session_state.radio
        st.info(f"Disposed card: {disposed}")
        if st.button("Confirm"):
            st.session_state.button = True
    if st.session_state.button == True:
        new_hand = hand.pop_one(st.session_state.radio, st.session_state.hand[0])
        st.session_state.hand[0] = new_hand
        st.success(f"New Hand: {st.session_state.hand[0]}")
        
    

    
    
except Exception as ex:
    st.text(ex)
