import streamlit as st
import toml
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
    def pop_one(self, card, cards):
        index = cards.index(card)
        cards.pop(index)
        self.cards = cards
        return self.cards
    def show(self):
        return f"{self.owner}'s hand: {str(self.cards)}"
    
files = [ "C:\\Users\\SXL1151\\.streamlit\\secrets.toml", "C:\\Users\\SXL1151\\Desktop\\.streamlit\\secrets.toml",]
players = []
st.session_state.intro = True
st.title("Rummy")
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
if once == True:
    hands = []
    deck_1 = Deck()
    deck_1.create_deck()
    deck_1.shuffle()
    st.text(deck_1.__repr__())
    st.text(players)
    for player in players:
        hand = Hand(player)
        for i in range(cardsPerHand):  
            dealt = deck_1.deal_one()          
            hand.add_card(dealt)
        hand2 = hand.show()
        hands.append(hand.cards)
    st.session_state.hands = hands
    finDeck = (deck_1.__repr__())
    finDeckStr = ""
    for card in finDeck:
        finDeckStr = finDeckStr + " " + card
    st.success(f"Deck: {finDeckStr}")
st.warning("Round 1")
st.warning(f"Please pass the device to {players[len(players)-(len(players))]}")
cardsUp = []
'''
st.error("Game will continue in 5 seconds")

if once == True:
    with st.spinner("Loading..."):
        time.sleep(5)
'''
if once == True: #Shreyas was here lol
    once = False
if once == False:
    while True:
        st.text(f"Hand: {st.session_state.hands[0]}")
        try:
            option = st.radio("Pick an option", [f"select {cardsUp[0]} from the cards up deck", "Pick top card from cards down deck"])
        except:
            option = st.radio("Pick an option", ["Pick top card from cards down deck", "hi"])
        disposalCard = st.radio("Pick a card to dispose", hands[0], key="disposalCard", on_change="disposalCard")
        popped = hand.pop_one(st.session_state.disposalCard, hands[0])
        hands[0] = hand.cards
        st.text(hand.cards)
        st.session_state.hands = hands
        if st.session_state.disposalCard == disposalCard:
            break
        else:
            continue
'''
cardsUp.append(disposalCard)
deck_1 = Deck()
''' #Shreyas was here again for 67 67 67
