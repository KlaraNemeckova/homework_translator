english_list = ["bed","butterfly","table","water","horse"]
german_list = ["das Bett","der Schmetterling","der Tisch", "das Wasser", "das Pferd"]

eng_to_ger = dict(zip(english_list, german_list))
ger_to_eng = dict(zip(german_list, english_list))

print(english_list)

def add():
    new_eng = input("Anglické slovo: ")
    new_ger = input("Německé slovo: ")
    english_list.append(new_eng)
    german_list.append(new_ger)

add()


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
    user_choice = input("Vyberte možnost: 1 - přeložit 2 - přidat slovo, 3 - smazat slovo, 4 - nahradit slovo, "
                        "5 - nejpopulárnější, 6 - nejméně populární, 7 - ukončit program")
    if user_choice == 1:
        translate()
    elif user_choice == 2:
        add()
    elif user_choice == 3:
        delete()
    elif user_choice == 4:
        replace()
    elif user_choice == 5:
        most_popular()
    elif user_choice == 6:
        least_popular()
    elif user_choice == 7:
        break
    else:
        print("Zadejte volbu od 1 do 7")
        menu()
menu()

