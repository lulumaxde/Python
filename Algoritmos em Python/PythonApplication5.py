contasegundos = int(input("Por favor, entre com o número de segundos que deseja converter: "))

dias = contasegundos//86400

restodias = contasegundos%86400

horas = restodias//3600

restohoras = restodias%3600

minutos = restohoras//60

restominutos = restohoras%60

segundos = restominutos



print(dias,"dias,",horas,"horas,",minutos,"minutos e",segundos,"segundos.")