from datetime import date

dia= int(input('QUE DIA VOCÊ NASCEU? '))
mes= int(input('QUE MÊS VOCÊ NASCEU? '))
ano= int(input('QUE ANO VOCÊ NASCEU? '))
ano_atual= date.today().year
mes_atual= date.today().month
dia_atual= date.today().day
if ((ano_atual - ano) > 18):
    print('VOCÊ PODE TIRAR CNH')
elif ((ano_atual - ano) == 18 and mes_atual>mes):
    print('VOCÊ PODE TIRAR CNH')
elif ((ano_atual - ano) == 18 and mes_atual==mes and dia_atual>=dia):
    print('VOCÊ PODE TIRAR CNH')
else:
    print('VOCÊ NÃO PODE TIRAR CNH')

