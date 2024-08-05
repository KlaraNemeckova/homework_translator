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


def delete():
    pass

def replace():
    pass

def most_popular():
    pass
    # counter

def least_popular():
    pass
    # counter

def menu():
    user_choice = input("Vyberte možnost: 1 - přidat slovo, 2 - smazat slovo, 3 - nahradit slovo, "
                        "4 - nejpopulárnější, 5 - nejméně populární")
    if user_choice == 1:
        add()
    elif user_choice == 2:
        delete()
    elif user_choice == 3:
        replace()
    elif user_choice == 4:
        most_popular()
    elif user_choice == 5:
        least_popular()
    else:
        print("Zadejte volbu od 1 do 5")

translate(eng_word, ger_word)

