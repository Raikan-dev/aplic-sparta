#Criando Janela:

janela = tk.Tk()
janela.title('Cadastro de Clientes Assinantes SPARTA')
janela. geometry("330x350")


def cadastrar_cliente():
    conexao = sqlite3.connect('clientes.db')
    c = conexao.cursor()

    #Inserir dados na tabela:
    c.execute("INSERT INTO clientes VALUES (:nome,:sobrenome,:cpf,:telefone)",
              {
                  'nome': entry_nome.get(),
                  'sobrenome': entry_sobrenome.get(),
                  'cpf': entry_cpf.get(),
                  'telefone': entry_telefone.get()
              })


    # Commit as mudanças:
    conexao.commit()

    # Fechar o banco de dados:
    conexao.close()

    # #Apaga os valores das caixas de entrada
    entry_nome.delete(0,"end")
    entry_sobrenome.delete(0,"end")
    entry_cpf.delete(0,"end")
    entry_telefone.delete(0,"end")

def exporta_clientes():
    conexao = sqlite3.connect('clientes.db')
    c = conexao.cursor()

    # Inserir dados na tabela:
    c.execute("SELECT *, oid FROM clientes")
    clientes_cadastrados = c.fetchall()
    # print(clientes_cadastrados)
    clientes_cadastrados=pd.DataFrame(clientes_cadastrados,columns=['nome','sobrenome','cpf','telefone','Id_banco'])
    clientes_cadastrados.to_excel('clientes.xlsx')

    # Commit as mudanças:
    conexao.commit()

    # Fechar o banco de dados:
    conexao.close()


#Rótulos Entradas:
label_nome = tk.Label(janela, text='Nome')
label_nome.grid(row=0,column=0, padx=10, pady=10)

label_sobrenome = tk.Label(janela, text='Sobrenome')
label_sobrenome.grid(row=1, column=0, padx=10, pady=10)

label_cpf = tk.Label(janela, text='cpf')
label_cpf.grid(row=2, column=0 , padx=10, pady=10)

label_telefone = tk.Label(janela, text='Telefone')
label_telefone.grid(row=3, column=0, padx=10, pady=10)

#Caixas Entradas:
entry_nome = tk.Entry(janela , width =35)
entry_nome.grid(row=0,column=1, padx=10, pady=10)

entry_sobrenome = tk.Entry(janela, width =35)
entry_sobrenome.grid(row=1, column=1, padx=10, pady=10)

entry_cpf = tk.Entry(janela, width =35)
entry_cpf.grid(row=2, column=1 , padx=10, pady=10)

entry_telefone = tk.Entry(janela, width =35)
entry_telefone.grid(row=3, column=1, padx=10, pady=10)

# Botão de Cadastrar

botao_cadastrar = tk.Button(text='Cadastrar Cliente', command=cadastrar_cliente)
botao_cadastrar.grid(row=4, column=0,columnspan=2, padx=10, pady=10 , ipadx = 80)

# Botão de Exportar

botao_exportar = tk.Button(text='Exportar para Excel', command=exporta_clientes)
botao_exportar.grid(row=5, column=0,columnspan=2, padx=10, pady=10 , ipadx = 80)


janela.mainloop()

def cadastrar_plano():
    conexao = sqlite3.connect('plano.db')
    c = conexao.cursor()

    #Inserir dados na tabela:
    c.execute("INSERT INTO plano VALUES (:id,:valor)",
              {
                  'id': entry_id.get(),
                  'valor': entry_valor.get(),
                 
              })


    # Commit as mudanças:
    conexao.commit()

    # Fechar o banco de dados:
    conexao.close()

    # #Apaga os valores das caixas de entrada
    entry_id.delete(0,"end")
    entry_valor.delete(0,"end")
    

def exporta_plano():
    conexao = sqlite3.connect('plano.db')
    c = conexao.cursor()

    # Inserir dados na tabela:
    c.execute("SELECT *, oid FROM plano")
    plano_cadastrados = c.fetchall()
    # print(clientes_cadastrados)
    plano_cadastrados_cadastrados=pd.DataFrame(plano_cadastrados,columns=['Id_banco','valor'])
    plano_cadastrados_cadastrados.to_excel('plano.xlsx')

    # Commit as mudanças:
    conexao.commit()

    # Fechar o banco de dados:
    conexao.close()


#Rótulos Entradas:
label_id = tk.Label(janela, text='id')
label_id.grid(row=0,column=0, padx=10, pady=10)

label_valor = tk.Label(janela, text='id')
label_valor.grid(row=1, column=0, padx=10, pady=10)

#Caixas Entradas:
entry_id = tk.Entry(janela , width =35)
entry_id.grid(row=0,column=1, padx=10, pady=10)

entry_valor = tk.Entry(janela, width =35)
entry_valor.grid(row=1, column=1, padx=10, pady=10)

# Botão de Cadastrar

botao_cadastrar = tk.Button(text='Cadastrar Plano', command=cadastrar_plano)
botao_cadastrar.grid(row=4, column=0,columnspan=2, padx=10, pady=10 , ipadx = 80)

# Botão de Exportar

botao_exportar = tk.Button(text='Exportar para Excel', command=exporta_plano)
botao_exportar.grid(row=5, column=0,columnspan=2, padx=10, pady=10 , ipadx = 80)



def cadastrar_barbearia():
    conexao = sqlite3.connect('barbearia.db')
    c = conexao.cursor()

    #Inserir dados na tabela:
    c.execute("INSERT INTO barbearia VALUES (:id)",
              {
                  'id': entry_id.get(),
                 
              })


    # Commit as mudanças:
    conexao.commit()

    # Fechar o banco de dados:
    conexao.close()

    # #Apaga os valores das caixas de entrada
    entry_id.delete(0,"end")
   
    

def exporta_barbearia():
    conexao = sqlite3.connect('barbearia.db')
    c = conexao.cursor()

    # Inserir dados na tabela:
    c.execute("SELECT *, oid FROM barbearia")
    barbearia_cadastrados = c.fetchall()
    # print(clientes_cadastrados)
    barbearia_cadastrados_cadastrados=pd.DataFrame(barbearia_cadastrados,columns=['Id_banco'])
    barbearia_cadastrados_cadastrados.to_excel('barbearia.xlsx')

    # Commit as mudanças:
    conexao.commit()

    # Fechar o banco de dados:
    conexao.close()


#Rótulos Entradas:
label_id = tk.Label(janela, text='id')
label_id.grid(row=0,column=0, padx=10, pady=10)

#Caixas Entradas:
entry_id = tk.Entry(janela , width =35)
entry_id.grid(row=0,column=1, padx=10, pady=10)


# Botão de Cadastrar

botao_cadastrar = tk.Button(text='Cadastrar Barbearia', command=cadastrar_barbearia)
botao_cadastrar.grid(row=4, column=0,columnspan=2, padx=10, pady=10 , ipadx = 80)

# Botão de Exportar

botao_exportar = tk.Button(text='Exportar para Excel', command=exporta_barbearia)
botao_exportar.grid(row=5, column=0,columnspan=2, padx=10, pady=10 , ipadx = 80)

janela.mainloop()