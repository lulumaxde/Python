# -*- coding: utf-8 -*-
import string
import sys
import unicodedata

def menor_nome(names_array):
    
    if len(names_array) > 0:
        sizes = []
        nome = []
        minimum = sys.maxsize
        index = 0

        for name in names_array:
            raw = name.replace(" ", "")
            nome.append(raw)

        for name in nome:
            raw = unicodedata.normalize("NFKD", name).encode("ASCII","ignore")
            str_raw = raw.decode("ASCII")
            
            sizes.append(len(str_raw))

        for i,value in enumerate(sizes):
            if value < minimum:
                minimum = value
                index = i
        return nome[index].capitalize()
    
       

 


    
            
            
                

            
   


