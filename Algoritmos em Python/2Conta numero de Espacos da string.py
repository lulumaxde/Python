#LISTA2

#Crie uma rotina que solicite uma frase ao usuário e retorne
#o número de caracteres na frase e o número de espaços.

Frase = input(" Digite a frase : ")

NumerodeCaracteres = len(Frase);
NumerodeCaracteresSemEspaco = len(Frase.strip());
NumerodeEspacos = Frase.count(" ");

print("Numero de Caracteres = " + str(NumerodeCaracteres))
print("Numero de espaços = " + str(NumerodeEspacos))
