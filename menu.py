#MENU
email=[]
senga=[]
idade=[]
cpf=[]
sexo=[]
a=1
while a!=5:
	print(" |Menu:| ")
	print(" ---------------")
	print(" |1 - Cadastrar| \n |2 - Ler      | \n |3 - Deletar  | \n |4 - Atualizar| \n |5 - Sair     |")
	print(" ---------------")

	op=int(input(" • Escolha algum dos itens acima: "))
	if op==1:
		c=int(input("digite quantos cadastros deseja fazer:"))
		b=0
		while b<c:
			print(" •Menu de cadastro ",b+1,": ")			
			emai=str(input("email do  usuário:"))
			email.append(emai)
			
			seng=str(input("Senha do usuário: "))
			senga.append(seng)
			
			idad=int(input("Idade do usuário: "))
			idade.append(idad)
			
			cp=str(input("Cpf do usuário: "))
			cpf.append(cp)
			sex=str(input("menino ou menina: "))
			sexo.append(sex)
			yn=int(input(" •Deseja concluir o cadastro? \n 1-Sim\n 2-Não\n"))
			if yn==1:
				b=b+1
			elif yn==2:
				b=0
				#LER
	if op==2:
		t=0
		q=1
		while   t<c:
		  	    print("-------------------------------")
print("Cadastro", q)
print("-------------------------------")
print("Email do usuario:", email,[t])
print("Senha do usuário: ",senga,[t])
print("Idade do usuário: " , idade,[t])
print("Cpf do usuário: " , cpf,[t])
print("Menino ou Menina: " , sexo,[t])
print("-------------------------------")		  	    
t+=1
q+=1
    #DELETAR
if op==3:
		t=0
		q=1
		print('CADASTRO [OPÇÃO]')
		while t<c:
		  	    print("-------------------------------")
print("Cadastro" ,q)
print("-------------------------------")
print("Email do usuario:", email[t])
print("Senha do usuário: ",senga[t])
print("Idade do usuário: " , idade[t])
print("Cpf do usuário: " , cpf[t])
print("Menino ou Menina: " , sexo[t])
print("-------------------------------")		  	    
t+=1
q+=1
print('--> Digite 0 para apagar todos os registros!')
delet = int(input("•Qual registro deseja deletar? "))
if delet == 0:
			email=[]
			senga=[]
			idade=[]
			cpf=[]
			sexo=[]
else:
			email.pop(delet-1)
			senga.pop(delet-1)
			idade.pop(delet-1)
			cpf.pop(delet-1)
			sexo.pop(delet-1)
		print("===================")
		#ATUALIZAR
if  op==4: 
    t=0
q=1
print('CADASTRO [OPÇÃO]')
while t<c:
 print("-------------------------------")
print("Cadastro" ,q)
print("-------------------------------")
print("Email do usuario:", email[t])
print("Senha do usuário: ",senga[t])
print("Idade do usuário: " , idade[t])
print("Cpf do usuário: " , cpf[t])
print("Menino ou Menina: " , sexo[t])
print("-------------------------------")		  	    
t+=1
q+=1
print('--> Digite 0 para apagar todos os registros!')
at = int(input("•Qual registro deseja atualizar? "))
print("===================")
if at == 0:
			le=email
			ls=senga
			li=idade
			lc=cpf
			lse=sexo
			
			email=[]
			senga=[]
			idade=[]
			cpf=[]
			sexo=[]
			for h in range(len(le)):
						print('CADASTRO ',h+1)
						email.append(input('Novo nome: '))
						senga.append(input("Novo email: "))
						idade.append(input("Nova senha: "))
						cpf.append(input("Novo cpf: "))
						sexo.append(input("Novo número de telefone: "))
else:
						a = email[at-1]
						b = senga[at-1]
						c = idade[at-1]
						d = cpf[at-1]
						e = sexo[at-1]
						print('Atualizar registro ',at,':')
						email[at-1] = input('Novo nome: ')
						senga[at-1] = input('Novo email: ')
						idade[at-1] = input('Nova senha: ')
						cpf[at-1] = int(input('Novo cpf: '))
						sexo[at-1] = int(input('Novo N° de telefone: '))
atual = int(input('Atualizar dados? 1 - Sim  2 - Não '))
if atual == 1:
			print('ATUALIZADO !')
elif atual == 2 and at == 0:
			email=le
			senga=ls
			idade=li
			cpf=lc
			sexo=lse
			print('NÃO ATUALIZADO !')
elif atual == 2 and at != 0:
			email[at-1] = a
			senga[at-1] = b
			idade[at-1] = c					
			cpf[at-1] = d
			sexo[at-1] = e
			print('NÃO ATUALIZADO !')
						
			#SAIR
								
if  op==5:
		quit=int(input(" 1-Sair\n 2-Não sair \n"))
		if quit==1:
			a=5
		elif quit==2:
			a=1;