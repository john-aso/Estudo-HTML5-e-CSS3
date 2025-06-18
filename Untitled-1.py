
def getBattery(eventos):
    bateria = 50  

    
    for evento in eventos:
        bateria += evento  

        
        if bateria > 100:
            bateria = 100

       
        elif bateria < 0:
            bateria = 0

    return bateria  


n = 4
eventos = [10, -20, 61, -15]


print(getBattery(eventos))
