L_g = 5 #constante por causa da API
dis_cliente = 10 #cliente fornece
km_L = 30 #cliente fornece
dis_parada = 13 #cliente fornece
dis_casa = 3 #cliente fornece
dias_mes = 20 #cliente fornece
repeticao_dia = 1 #cliente fornece
manutencao = 2.5 #constante





#quantidade de km/L da moto em relação com a gasolina
KM_l=(km_L/L_g)  #6 km que vale 1 real


#soma de toda a Km do dia e multiplicada pela quantidade de vezes que faz trajeto no dia
Km_t= (dis_cliente + dis_parada + dis_casa) * repeticao_dia



KM = (Km_t/KM_l) #quanto a moto gasta no dia levando o passageiro



#multiplicar a quantidade de gasolina gasta no dia pela quantidade de dias no mês (20)
gasto = KM*dias_mes

lucro = gasto+(gasto*manutencao)


print(Km_t)
print(KM)


print(gasto)
print(lucro)