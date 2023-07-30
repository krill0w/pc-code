from mtgsdk import Card
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
    cards = [(card.name, card.types) for card in Card.where(types=searchTerm)]
    return cards


"""def printCardTest():
    print("started at", time.strftime("%X"))
    print("working on it")
    cards = [card.name for card in Card.where(supertypes="legendary").where(types="creature").where(colors="red,white").where(pageSize=1).all()]
    print(cards)
    return cards[0]"""


