#!/bin/python

class CharactorCardNames:
    Bart_Cassidy   = "Bart_Cassidy"
    #Bart Cassidy = Butch Cassidy – Each time he loses a life point, he immediately draws a normalcard from the deck. (4 life points)
    Black_Jack     = "Black_Jack"
    #Black Jack = Tom Ketchum (known as Black Jack) – During phase 1 of his turn, he must show the second normalcard he draws: if it's a Heart or Diamond, he draws one additional normalcard that turn (without revealing it). (4 life points)
    Calamity_Janet = "Calamity_Janet"
    #Calamity Janet = Calamity Jane – She can use "Bang!" cards as "Missed!" cards and vice versa. She is still subject to "Bang!" limitations: If she plays a Missed! normalcard as a "Bang!", she cannot play another "Bang!" normalcard that turn (unless she has a Volcanic in play). (4 life points)
    EI_Gringo      = "EI_Gringo"
    #El Gringo = gringo (slang Spanish word) – Each time he loses a life point due to a normalcard played by another player, he draws a random normalcard from the hands of that player (one normalcard for each life). If the player has no more cards, he does not draw. (3 life points)
    Jesse_Jones    = "Jesse_Jones"
    #Jesse Jones = Jesse James – During phase 1 of his turn, he may choose to draw the first normalcard from the deck, or randomly from the hand of any other player. Then he draws the second normalcard from the deck. (4 life points)
    Jourdonnais    = "Jourdonnais"
    #Jourdonnais = "Frenchy" Jourdonnais, the riverboat captain in The Big Sky novel and movie (Fictional person) – He is considered to have Barrel in play at all times; he can "draw!" when he is the target of a BANG!, and on a Heart he is missed. If he has another real Barrel normalcard in play he can count both of them, giving him two chances to cancel the BANG! before playing a Missed! (4 life points)
    Kit_Carlson    = "Kit_Carlson"
    #Kit Carlson = Kit Carson – During the phase 1 of his turn, he looks at the top three cards of the deck: he chooses 2 to draw, and puts the other one back on the top of the deck, face down. (4 life points)
    Lucky_Duke     = "Lucky_Duke"
    #Lucky Duke = Lucky Luke (Fictional person) – Each time he is required to "draw!", he flips the top two cards from the deck, and chooses the result he prefers. Discard both cards afterward. (4 life points)
    Paul_Regret    = "Paul_Regret"
    #Paul Regret = Paul Regret – The Comancheros (film) – He is considered to have a Mustang in play at all times; all other players must add 1 to the distance to him. If he has another real Mustang in play, he can count both of them, increasing all distance to him by a total of 2. (3 life points)
    Pedro_Ramirez  = "Pedro_Ramirez"
    #Pedro Ramirez = Tuco Ramirez – The Ugly in the film The Good, the Bad and the Ugly (Fictional person) – During phase 1 of his turn, he may choose to draw the first normalcard from the top of the discard pile or from the deck. Then he draws the second normalcard from the deck. (4 life points)
    Rose_Doolan    = "Rose_Doolan"
    #Rose Doolan = She is considered to have a Scope (Appaloosa in older versions) in play at all times; she sees the other players at a distance decreased by 1. If she has another real Scope in play, she can count both of them, reducing her distance to all other players by a total of 2. (4 life points)
    Sid_Ketchum    = "Sid_Ketchum"
    #Sid Ketchum = Tom Ketchum – At any time, he may discard 2 cards from his hand to regain one life point. If he is willing and able, he can use this ability more than once at a time. (4 life points)
    Slab_Killer    = "Slab_Killer"
    #Slab the Killer = Angel Eyes, the Bad in the film The Good, the Bad and the Ugly (Fictional person) – Players trying to cancel his BANG! cards need to play 2 Missed!. The Barrel effect, if successfully used, only counts as one Missed! (4 life points)
    Suzy_Lafayette = "Suzy_Lafayette"
    #Suzy Lafayette = As soon as she has no cards in her hand, she instantly draws a normalcard from the draw pile. (4 life points)
    Vulture_Sam    = "Vulture_Sam"
    #Vulture Sam = Whenever a character is eliminated from the game, Sam takes all the cards that player had in his hand and in play, and adds them to his hand. (4 life points)
    Willy_Kid      = "Willy_Kid"
    #Willy the Kid = Billy the Kid – He can play any number of "Bang!" cards. (4 life points)

class CharactorCard(object):
    def __init__(self, person, hp):
        self.__person__ = person
        self.__hp__   = hp
        self.__key__  = person

    def __get_person__(self):
        return self.__person__
    person = property(__get_person__, doc="The person name of charactorcard")

    def __get_hp__(self):
        return self.__hp__
    hp = property(__get_hp__, doc = "The init hp of this charactorcard")


    def __get_key__(self):  return self.__key__
    key = property(__get_key__, doc = "The key of this charactorcard")

    def __deepcopy__(self, memodict={}):
        return CharactorCardsDict[self.__key__]


CharactorCardsDict = dict()
CharactorCardsDict[CharactorCardNames.Jesse_Jones] = CharactorCard(CharactorCardNames.Jesse_Jones, 4)
CharactorCardsDict[CharactorCardNames.Vulture_Sam] = CharactorCard(CharactorCardNames.Vulture_Sam, 4)
CharactorCardsDict[CharactorCardNames.Bart_Cassidy] = CharactorCard(CharactorCardNames.Bart_Cassidy, 4)
CharactorCardsDict[CharactorCardNames.Calamity_Janet] = CharactorCard(CharactorCardNames.Calamity_Janet, 4)
CharactorCardsDict[CharactorCardNames.Black_Jack]  = CharactorCard(CharactorCardNames.Black_Jack, 4)
CharactorCardsDict[CharactorCardNames.Jourdonnais] = CharactorCard(CharactorCardNames.Jourdonnais, 4)
CharactorCardsDict[CharactorCardNames.Kit_Carlson] = CharactorCard(CharactorCardNames.Kit_Carlson, 4)
CharactorCardsDict[CharactorCardNames.Rose_Doolan] = CharactorCard(CharactorCardNames.Rose_Doolan, 4)
CharactorCardsDict[CharactorCardNames.Suzy_Lafayette] = CharactorCard(CharactorCardNames.Suzy_Lafayette, 4)
CharactorCardsDict[CharactorCardNames.Sid_Ketchum] = CharactorCard(CharactorCardNames.Sid_Ketchum, 4)
CharactorCardsDict[CharactorCardNames.EI_Gringo] = CharactorCard(CharactorCardNames.EI_Gringo, 3)
CharactorCardsDict[CharactorCardNames.Lucky_Duke] = CharactorCard(CharactorCardNames.Lucky_Duke, 4)
CharactorCardsDict[CharactorCardNames.Slab_Killer] = CharactorCard(CharactorCardNames.Slab_Killer, 4)
CharactorCardsDict[CharactorCardNames.Paul_Regret] = CharactorCard(CharactorCardNames.Paul_Regret, 3)
CharactorCardsDict[CharactorCardNames.Pedro_Ramirez] = CharactorCard(CharactorCardNames.Pedro_Ramirez, 4)
CharactorCardsDict[CharactorCardNames.Willy_Kid] = CharactorCard(CharactorCardNames.Willy_Kid, 4)