import time

def linha():#linha de separação
    print(10*'------')
    

def Funcionarios_login():
    funcionarios = ["ana","julia","lua"]
    Novato = ["Giovanna"]
    senha = [1234,5678,3456]
    
    
    
    if login_funcionios in funcionarios:
                    senha_funcionarios = int(input('Senha:'))
    if senha_funcionarios in senha:
                print(f'Bem vindo {login_funcionios}')
    else:
                    print('Senha incorreta')
                    
    while  login_funcionios not in funcionarios:
            for y in range(3):
                y = input('Repita o login:')


#Cadastro de novatos_login
def Login_Novato():
    Codigos = [0,2,4]
    novatos_login = []
    novatos_senha = []
    
    codigo_autoriza = int(input('Código de acesso:')) 
    linha()
    if codigo_autoriza in Codigos:
            username = input('Cadastro de login:')
            linha() #linha de separação
            password = int(input('Cadastro senha:'))
            linha()
            repete_senha = int(input('Repete a senha:'))
            linha()
            while repete_senha != password:
                p = int(input('Repita novamente:'))
                linha()
        
    novatos_login.append(username)
    novatos_senha.append(password)

    if codigo_autoriza not in Codigos:
            print('Cógido invalido')
            


    
    
    
    
                            # ----------  CÓDIGO PRINCIPAL----------
        
        
        
        

print("Início login")
opcoes = int(input('\t\t 1 - JÁ TRABALHO  \n \t\t2 - SOU NOVO'))


linha()
print('Carregando ......')
linha()

tempo = time.sleep(6.0)



if opcoes == 1:

    login_funcionios = input('Login:')      
    Funcionarios_login()


if opcoes == 2:
    Login_Novato()
    Funcionarios_login()


if opcoes == 0:
    print('Sessão encerrada')

