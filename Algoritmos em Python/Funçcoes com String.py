#Funções Utilizadas com String

time = "São Paulo"

time.upper() # Deixa tudo em maiúsculo
print(time) 
time.lower() # Deixa tudo em minúsculo
print(time)

"ana gosta de maça"

print("ana gosta de maça".capitalize()) # Deixa a primeira letra em maiúsculo o resto em minuscula

"BRAZIL"

print("BRAZIL".capitalize())

print("ana gosta de maça".count("a")) # Conta o número de vezes que uma caracter aparece na String


frase = " Python É Uma Linguagem Poderosa "

frase1 = "Eu torço para o São Paulo".replace("São Paulo", "Corinthians") # Substituí uma String


print("ana gosta de maça".capitalize().center(80)) #centraliza texto no meio de 80 caracteres

frase2 = " Python É Uma Linguagem Poderosa "

print(frase2.find("L")) #retorna posição

print(frase2.find("Po"))

print(frase2.find("BOM")) #retorna - não existe

frase.strip() #retira espaços

