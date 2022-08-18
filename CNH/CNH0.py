import datetime
dia= int(input('QUE DIA VOCÊ NASCEU? '))
mes= int(input('QUE MÊS VOCÊ NASCEU? '))
ano= int(input('QUE ANO VOCÊ NASCEU? '))
if (ano<=2003):
    print('VOCÊ PODE TIRAR CNH')
elif(ano==2004 and mes<=7):
    print('VOCÊ PODE TIRAR CNH')
elif(ano==2004 and mes==8 and dia<=18):
    print('VOCÊ PODE TIRAR CNH')
else:
    print('VOCÊ NÃO PODE TIRAR CNH')