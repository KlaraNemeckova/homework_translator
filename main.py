english_list = ["bed","butterfly","table","water","horse"]
german_list = ["das Bett","der Schmetterling","der Tisch", "das Wasser", "das Pferd"]

eng_to_ger = dict(zip(english_list, german_list))
ger_to_eng = dict(zip(german_list, english_list))


def translate(eng_word, ger_word):
    word_list = input("Přejete si zobrazit anglický nebo německý seznam slov? ENG/GER ")
    if word_list == "ENG":
        print(english_list)
        eng_word = input("Vyberte slovo ")
        result = eng_to_ger.get(eng_word)
        print("{} is {} in german.".format(eng_word, result))

    elif word_list == "GER":
        print(german_list)
        ger_word = input("Vyberte slovo ")
        result = ger_to_eng.get(ger_word)
        print("{} is {} in english.".format(ger_word, result))

    else:
        print("Toto slovo není na seznamu.")
        translate(eng_word,ger_word)

def add():
    pass

def delete():
    pass

def replace(word):
    pass

def most_popular():
    pass
    # counter

def least_popular():
    pass
    # counter

translate(eng_word, ger_word)

