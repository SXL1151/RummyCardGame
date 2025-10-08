import streamlit as st
import toml
import random
values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

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
class Hand:
    def __init__(self, owner="Player"):
        self.owner = owner
        self.cards = []
    def add_card(self, card):
        self.cards.append(card)
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
        else:
            players.append(name)
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
    if butPress:
        st.success("Game has started!")
except:
    pass
deck_1 = Deck()
deck_1.create_deck()
st.text(deck_1.__repr__())
st.text(players)
for player in players:
    for i in range(cardsPerHand):
        hand = Hand(player)
        hand.add_card(deck_1.deal_one())
        st.text(hand.show())











