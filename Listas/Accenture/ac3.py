def main():
    valorCOM = 1
    valorFINANC = 35
    classifSERVICO = "DDRD"

    if valorCOM == 1 or valorCOM == 10:
        if valorFINANC == 35 or valorFINANC == 36 or valorFINANC == 38 or valorFINANC == 40 or valorFINANC == 42:
            indicadorSITU = 2
        else:
            indicadorSITU = 1
        if (valorCOM == 1 and (valorFINANC == 36 or valorFINANC == 38)) or (classifSERVICO == 'LIRT' and indicadorSITU == 1):
            print("SITUACAO A")
        else:
            if(classifSERVICO == "LTCA" or classifSERVICO == "LTRA"  or classifSERVICO == "TUPC" or classifSERVICO == "TUPM" or classifSERVICO == "DDRD") and (valorCOM == 15 or valorCOM == 16 or valorCOM == 17):
                print("SITUACAO B")
            else:
                print("SITUACAO C")
    else:
        if (valorFINANC == 35 or valorFINANC == 36 or valorFINANC == 38 or valorFINANC == 40 or valorFINANC == 42):
            print("SITUACAO D")
        else:
            if ( valorFINANC != 36 and valorFINANC != 38 and classifSERVICO == 'LIRT' ):
                print("SITUACAO E")
            else:
                print("SITUACAO F")
            
            

main()