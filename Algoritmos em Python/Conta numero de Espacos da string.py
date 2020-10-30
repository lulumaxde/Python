Frase = input(" Digite a frase : ")

NumerodeCaracteres = len(Frase);
NumerodeCaracteresSemEspaco = len(Frase.strip());
NumerodeEspacos = Frase.count(" ");

print("Numero de Caracteres = " + str(NumerodeCaracteres))
print("Numero de espaços = " + str(NumerodeEspacos))
