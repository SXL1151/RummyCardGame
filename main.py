import streamlit as st
st.session_state.intro = True
st.title("Rummy")
st.markdown('''
:red[Welcome to the rummy card game!]
''')
try:
  playerCt = st.selectbox("How many players will be playing?", ("2", "3", "4", "5",
"6"))
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
