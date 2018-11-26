import time
import pandas as pd
import smtplib
import random

def line_count(fname):
    return sum(1 for line in open(fname,'r', encoding='UTF-8'))

def main():
    #A base aniversarios.txt deve ser: nome,dia,mes,funcao,email
    db = pd.read_csv('aniversarios.txt')

    nome_db = db['nome']
    dia_db = db['dia']
    mes_db = db['mes']
    funcao_db = db['funcao']
    email_db = db['email']

    dia = int(time.strftime('%d'))
    mes = int(time.strftime('%m'))

    aniversariante = []
    funcao = []
    email = []

    for i in range(len(dia_db)):
        if dia == dia_db[i] and mes == mes_db[i]:
            aniversariante.append(nome_db[i])
            funcao.append(funcao_db[i])
            email.append(email_db[i])
    
    subject = ''
    mensagem = ''
    if len(aniversariante) != 0:
        for i in range(len(aniversariante)):
            subject = subject + aniversariante[i] + ', '
        aniversario_nome = subject
        subject = subject + 'feliz aniversário!!!!'

        mensagem = aniversario_nome + '\n'
        mensagem = mensagem + 'Muitas felicidades neste dia ' + str(dia) + '/' + str(mes) + '!!' + '\n'
        mensagem = mensagem + 'Parabéns!!!! \n'

        #Arquivo de mensagens deve conter uma mensagem por linha
        f = open('mensagens.txt', 'r', encoding='UTF-8')
        lines = line_count('mensagens.txt')
        rand = random.randint(1,lines)
        for i in range(rand-1):
            f.readline()
        mensagem = mensagem + f.readline()
        mensagem = mensagem + '\n\n' + 'Abraços, ' + '\n' + 'Equipe NERDS'

        smtpserver = smtplib.SMTP("smtp.gmail.com",587)
        smtpserver.ehlo()
        smtpserver.starttls()
        smtpserver.ehlo
        smtpserver.login(user, pwd)
        header = 'To:' + to + '\n' + 'From: ' + user + '\n' + 'Subject: ' + subject + '\n'
        msg = header + mensagem
        smtpserver.sendmail(user, to, msg.encode("utf8"))
        smtpserver.close()
        
if __name__ == "__main__":
    to = 'labnerds@googlegroups.com'
    user = 'nerdsufes@gmail.com'
    pwd = 
    main()
