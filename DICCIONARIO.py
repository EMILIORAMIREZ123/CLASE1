import time
meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "ROFL": "una respuesta a una broma",
            "SHEESH": "ligera desaprobación",
            "CREEPY": "aterrador, siniestro",
            "AGGRO": "ponerse agresivo/enojado",
            }
word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
time.sleep(3)
    
if word in meme_dict.keys():
    print("El significado es:")
    print(meme_dict[word])
else:
    print("Esa palabra no esta en el dicionario")
    
    
    
    
