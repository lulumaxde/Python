def maiusculas(frase):

    tamanho = len(frase)
    String = ""
    
    for i in range(tamanho):
            if(frase[i] == 'A' or frase[i] == 'B' or frase[i] == 'C' or frase[i] == 'D' or frase[i] == 'E' or frase[i] == 'F'or frase[i] == 'G' or frase[i] == 'H'or frase[i] == 'I'or frase[i] == 'J'or frase[i] == ''or frase[i] == 'K'or frase[i] == 'L'or frase[i] == 'M'or frase[i] == 'N'or frase[i] == 'O'or frase[i] == 'P' or frase[i] == 'Q' or frase[i] == 'R' or frase[i] == 'S' or frase[i] == 'T' or frase[i] == 'U' or frase[i] == 'V' or frase[i] == 'W' or frase[i] == 'X' or frase[i] == 'Y' or frase[i] == 'Z'):
                String =String+frase[i]
            

    return String



