mijn_dict = {'vis' : 10,'vlees' : 25,'overig' : 15}
totaal = 50

def presenteer(inkomsten, totaal):    
    for k, v in inkomsten.items():
        print(k,":",v,"euro")
    print(26*"=")
    totaal = f"totaal : {sum(inkomsten.values())} euro"
    return totaal
