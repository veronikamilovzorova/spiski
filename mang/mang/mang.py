import random
player_score = 0
computer_score = 0
choices = ["kivi", "paber", "käärid"]
print("Kivi purustab käärid. Käärid lõikasid paberit. Paberkatted kivi.")
player = input("Kas valida: kivi, paber või käärid (lõpeta)? ")
while player != "lõpeta":
    player = player.lower()
    computer = random.choiсe
    print("Sinu valik " +player+ ", arvuti valis " +computer+ ".")
    if player == computer:
        print("Joonista")
    elif player =="kivi":
        if computer == "käärid":
            print("sina võitsid!")
            player_score = player_score + 1
        else:
            print("Arvuti võitis!")
            computer_score = computer_score + 1
        print ("Konto kokku: teie ", player_score, "arvuti juures ", computer_score, "konto: sina ", player_score, "arvuti juures ", computer_score)
    elif player == "paber":
        if computer == "kivi":
            print ("Sina võitsid!")
            player_score = player_score + 1
        else:
            print("Arvuti võitis!")
            computer_score = computer_score + 1
        print ("Konto kokku: teie ", player_score, "arvuti juures",computer_score)
    elif player == "paber":
        if computer == "kivi":
            print ("SA võitsid!")
            player_score = player_score + 1
        else:
            print ("Arvuti võitis!")
            computer_score = computer_score + 1
        print ("Konto kokku: teie ", player_score, "arvuti juures ", computer_score)
    elif player == "käärid":
        if computer == "paber":
            print ("Sa võitsid!")
            player_score = player_score + 1
        else:
            print ("Arvuti võitis!")
            computer_score = computer_score + 1
        print ("Konto kokku: teie", player_score, "arvuti juures", computer_score)
    else:
        print ("Tekkis viga")
        player = input ("Kas valida: kivi, paber või käärid (lõpeta)? " )
