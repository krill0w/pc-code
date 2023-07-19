import scrython

def searchByMultiple(searchTerm):
  card = scrython.cards.Named(fuzzy="Black Lotus", )
  print(card.name())
