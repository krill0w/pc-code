# the backend for a simple mtg card search tool
# made by traditionallimb
# started 19.02.20
# finished __.__.__





from mtgsdk import Card
import json
import datetime

time = datetime.datetime.now()



def searchByName(searchTerm):
  cards = [(card.name) for card in Card.where(types=searchTerm).all()]
  tempList = []
  for i in cards:
    if i not in tempList:
      tempList.append(i)
  cards = tempList
  return cards


def searchByType(searchTerm):
  cards = [(card.name, card.types) for card in Card.where(types=searchTerm).all()]
  return cards


def searchByCMC(searchTerm):
  cards = [(card.name, card.cmc) for card in Card.where(cmc=searchTerm).all()]
  return cards


def searchBySubtype(searchTerm):
  cards = [(card.name, card.subtype, card.set_name) for card in Card.where(subtype=searchTerm).all()]
  return cards


def printCardTest():
  print('started at', time.strftime("%X"))
  print('working on it')
  cards = [(card.name) for card in Card.where(supertypes='legendary') \
          .where(types='creature') \
          .where(colors='red,white') \
          .where(pageSize=1) \
          .all()]
  print(cards[0])
  return cards[0]






def moreInfoName(searchTerm):
  cards = [(card.name) for card in Card.where(name=searchTerm).all()]
  return cards[0]


def moreInfoFlavour(searchTerm):
  cards = [(card.flavor) for card in Card.where(name=searchTerm).all()]
  return cards[0]


def moreInfoImage(searchTerm):
  cards = [(card.image_url) for card in Card.where(name=searchTerm).all()]
  return cards[0]


def getMultiverseID(searchTerm):
  cards = [(card.multiverse_id) for card in Card.where(name=searchTerm).all()]
  return cards[0]
