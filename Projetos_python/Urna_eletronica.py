#O Brasil tem um grave problema quando falamos em política, porém podemos ter ações que podem melhorar alguns dos fatores. A primeira que teremos é criar um algoritmo base para a Urna Eletrônica. Nesse algoritmo teremos apenas 5 candidatos por enquanto:
# 1 - Vincent Vega
# 2 - Rick Dalton
# 3 - Shoshanna Dreyfus
# 4 - Beatrixx Kido
# 5 - Jules Winnfield
# Você deve criar um algoritmo que pergunte quantos eleitores irão participar, cada eleitor  terá  direito  a  apenas  um  voto,  porém  se  realizar  um  voto  errado  (um número de candidato que não existe), tem 5 chances até informar um voto válido. No final deve informar a porcentagem de votos de todos os candidatos e quem foi  eleito.  Não  precisa  considerar  segundo  turno.  Caso  ocorra  um  empate, mostrar quais os nomes empatados e porcentagem de empate.

votos_vicent = 0   
votos_rick = 0    
votos_shosshanna = 0    
votos_beatrixx = 0    
votos_jules = 0    
 
voto_nulo = 0
voto_certo = " "

candidato_1 = "Vincent Vega"
candidato_2 = "Rick Dalton"
candidato_3 = "Shoshanna Dreyfus"
candidato_4 = "Beatrixx Kido"
candidato_5 = "Jules Winnfield"

limite_voto = 5
eleitor = 0
i = 1

eleitores = int(input("Digite quantos eleitores vão participar da votação: "))
while i !=0:       
    
    tentativa = 1
    eleitor += 1
    erro = 0
    
    print('-'*50)
    
    print(" Digite 1 para votar em Vincent Vega\n Digite 2 para Rick Dalton\n Digite 3 para Shoshanna Dreyfus\n Digite 4 para Beatrixx Kido\n Digite 5 para Jules Winnfield ")
    print('-'*50)
    print(f"{eleitor} eleitor esta votando. ")

    print('-'*50)
    
    candidato = int(input("Digite o número de seu canditado: "))  
    if candidato == 1:       
        votos_vicent +=1
    elif candidato == 2:
        votos_rick +=1
    elif candidato == 3:
        votos_shosshanna +=1
    elif candidato == 4:
        votos_beatrixx +=1
    elif candidato == 5:
        votos_jules +=1
    tot_eleitores = (votos_vicent + votos_rick + votos_shosshanna + votos_beatrixx + votos_jules)

    while (candidato > 5 or candidato < 1):       
        voto_certo = int(input("Digite um candidato valido: "))
        tentativa += 1      
        if (tentativa == limite_voto):
            print("Voce zerou suas chances! Sistema finalizado.")
            voto_nulo += 1
            break        
        elif voto_certo == 1:
            votos_vicent +=1
            break
        elif voto_certo == 2:
            votos_rick +=1
            break
        elif voto_certo == 3:
            votos_shosshanna +=1
            break
        elif voto_certo == 4:
            votos_beatrixx +=1
            break
        elif voto_certo == 5:
            votos_jules +=1
            break 
        print(f"Voce tem: {limite_voto} chances e esta é a sua: {tentativa} tentativa")
            
    if (tot_eleitores == eleitores or eleitor == eleitores):
        i = 0        

porcentagem1 = ( 100 / eleitores) * votos_vicent
porcentagem2 = ( 100 / eleitores) * votos_rick
porcentagem3 = ( 100 / eleitores) * votos_shosshanna
porcentagem4 = ( 100 / eleitores) * votos_beatrixx
porcentagem5 = ( 100 / eleitores) * votos_jules    

print('-'*60)

print(f"{eleitores} eleitores participaram da votação. ")
print(f"Quantidade de votos nulos: {voto_nulo}. ")
print(f" \nO candidato {candidato_1} teve: {votos_vicent} voto(s) com {porcentagem1:.1f}% dos votos\nO candidato {candidato_2} teve: {votos_rick} voto(s) com {porcentagem2:.1f}% dos votos\nA candidata {candidato_3} teve: {votos_shosshanna} voto(s) com {porcentagem3:.1f}% dos votos\nA candidata {candidato_4} teve: {votos_beatrixx} voto(s) com {porcentagem4:.1f}% dos votos\nA candidata {candidato_5} teve: {votos_jules} voto(s) com {porcentagem5:.1f}% dos votos")

print('-'*60)
                                #Vencedores da votação
if votos_vicent > votos_rick and votos_vicent > votos_rick and votos_vicent > votos_shosshanna and votos_vicent > votos_beatrixx and votos_vicent > votos_jules:
    print(f"O candidato {candidato_1} venceu a eleição com {porcentagem1}% dos votos. ")
elif votos_vicent < votos_rick and votos_rick > votos_shosshanna and votos_rick > votos_beatrixx and votos_rick > votos_jules:
    print(f"O candidato {candidato_2} venceu a eleição com {porcentagem2}% dos votos. ")
elif votos_vicent < votos_shosshanna and votos_rick < votos_shosshanna and votos_beatrixx < votos_shosshanna and votos_jules < votos_shosshanna:
    print(f"A candidata {candidato_3} venceu a eleição com {porcentagem3}% dos votos. ")
elif votos_vicent < votos_beatrixx and votos_rick < votos_beatrixx and votos_shosshanna < votos_beatrixx and votos_beatrixx > votos_jules:
    print(f"A candidata {candidato_4} venceu a eleição com {porcentagem4}% dos votos. ")
elif votos_vicent < votos_jules and votos_rick < votos_jules and votos_shosshanna < votos_jules and votos_beatrixx < votos_jules:
    print(f"A candidata {candidato_5} venceu a eleição com {porcentagem5}% dos votos. ")
                                #Empate geral

elif votos_vicent == votos_rick and votos_vicent == votos_shosshanna and votos_vicent == votos_beatrixx and votos_vicent == votos_jules:
    print("Empate geral entre os candidatos. ")
                                #Empates quadruplos 

elif votos_vicent == votos_rick and votos_vicent == votos_shosshanna and votos_vicent == votos_beatrixx and votos_vicent >0:
    print(f"Empate entre {candidato_1}, {candidato_2}, {candidato_3} e {candidato_4}")
elif votos_vicent == votos_rick and votos_vicent == votos_shosshanna and votos_vicent == votos_jules and votos_vicent >0:
    print(f"Empate entre {candidato_1}, {candidato_2}, {candidato_3} e {candidato_5}")   
elif votos_vicent == votos_rick and votos_vicent == votos_beatrixx and votos_vicent == votos_jules and votos_vicent >0:
    print(f"Empate entre {candidato_1}, {candidato_2}, {candidato_4} e {candidato_5}") 
elif votos_vicent == votos_shosshanna and votos_vicent == votos_beatrixx and votos_vicent == votos_jules and votos_vicent >0:
    print(f"Empate entre {candidato_1}, {candidato_3}, {candidato_4} e {candidato_5}") 
elif votos_rick == votos_shosshanna and votos_rick == votos_beatrixx and votos_rick == votos_jules and votos_rick >0:
    print(f"Empate entre {candidato_2}, {candidato_3}, {candidato_4} e {candidato_5}") 
                                #Empates triplos

elif votos_vicent == votos_rick and votos_vicent == votos_shosshanna and votos_vicent > 0:
    print(f"Empate entre {candidato_1}, {candidato_2} e {candidato_3}")
elif votos_vicent == votos_rick and votos_vicent == votos_jules and votos_vicent > 0:
    print(f"Empate entre {candidato_1}, {candidato_2} e {candidato_5}")
elif votos_vicent == votos_shosshanna and votos_vicent == votos_jules and votos_vicent > 0:
    print(f"Empate entre {candidato_1}, {candidato_3}, {candidato_5}")
elif votos_vicent == votos_beatrixx and votos_vicent == votos_jules and votos_vicent > 0:
    print(f"Empate entre {candidato_1}, {candidato_4} e {candidato_5}")
elif votos_vicent == votos_rick and votos_vicent == votos_beatrixx and votos_vicent > 0:
    print(f"Empate entre {candidato_1}, {candidato_2} e {candidato_4}")
elif votos_vicent == votos_shosshanna and votos_vicent == votos_beatrixx and votos_vicent > 0:
    print(f"Empate entre {candidato_1}, {candidato_3} e {candidato_4}")
elif votos_rick == votos_shosshanna and votos_rick == votos_beatrixx and votos_rick > 0:
    print(f"Empate entre {candidato_2}, {candidato_3} e {candidato_4}")
elif votos_rick == votos_shosshanna and votos_rick == votos_jules and votos_rick > 0:
    print(f"Empate entre {candidato_2}, {candidato_3} e {candidato_5}")
elif votos_rick == votos_beatrixx and votos_rick == votos_jules and votos_rick > 0:
    print(f"Empate entre {candidato_2}, {candidato_4} e {candidato_5}")
elif votos_shosshanna == votos_beatrixx and votos_shosshanna == votos_jules and votos_shosshanna > 0:
    print(f"Empate entre {candidato_3}, {candidato_4} e {candidato_5}")
                                #Empates duplos

elif votos_vicent == votos_rick and votos_vicent > 0:
    print(f"Empate entre {candidato_1} e {candidato_2}")
elif votos_vicent == votos_shosshanna and votos_vicent > 0:
    print(f"Empate entre {candidato_1} e {candidato_3}")
elif votos_vicent == votos_beatrixx and votos_vicent > 0:
    print(f"Empate entre {candidato_1} e {candidato_4}")
elif votos_vicent == votos_jules and votos_vicent > 0:
    print(f"Empate entre {candidato_1} e {candidato_5}")
elif votos_rick == votos_shosshanna and votos_rick > 0:
    print(f"Empate entre {candidato_2} e {candidato_3}")
elif votos_rick == votos_beatrixx and votos_rick > 0:
    print(f"Empate entre {candidato_2} e {candidato_4}")
elif votos_rick == votos_jules and votos_rick > 0:
    print(f"Empate entre {candidato_2} e {candidato_5}")
elif votos_shosshanna == votos_beatrixx and votos_shosshanna > 0:
    print(f"Empate entre {candidato_3} e {candidato_4}")
elif votos_shosshanna == votos_jules and votos_shosshanna > 0:
    print(f"Empate entre {candidato_3} e {candidato_5}")
elif votos_beatrixx == votos_jules and votos_beatrixx > 0:
    print(f"Empate entre {candidato_4} e {candidato_5}")