from tkinter import *
from classes import*


#Após importar a pasta adjunta do projeto, iniciamos a construcao do Sistema da plataforma

class Sistema:
    def __init__(self):
        self.id_plano = 0
        self.id_usuario = 0
        self.id_aula = 0
        self.id_categoria = 0
        self.Usuario = []
        self.Aula = []
        self.Plano = []
        self.categoria = []
        self.Aula_categoria = []
        self.Usuario_aula = []
        self.Usuario_plano = []
        self.Categoria_plano = []


    #Adicianando um novo plano ao projeto
    def adicionar_plano(self, descricao, valor, titulo):
        self.id_plano += 1
        id = self.id_plano
        plan = Plano(id, valor, titulo, descricao)
        self.Plano.append(plan)
        return plan

    
    
    #Busca um plano pelo identificador na lista de plano
    def procurar_plano(self):
        id = int(input('Digite o Id do plano:')) 
        for plan in self.Plano:
            if (plan.id == id):
                return plan
        
        return None

    #Lista todos os planos
    def listar_planos(self):
        for plan in self.Plano:
            i+=1
            texto = Label(self.janela, text=f"Id = {plan.id}\nTitulo = {plan.titulo}\nDescrição: {plan.descricao}\nValor = R${plan.valor}")
            texto.grid(column=0, row=i, padx=10, pady=10)
    
    def obter_id_plano(self, id_usuario):
        for relacao in self.Usuario_plano:
            if relacao.id_usuario == id_usuario:
                return relacao.id_plano
        return None



    #Cria uma nova categoria de aulas
    def adicionar_categoria(self, nome):
        self.id_categoria += 1
        id = self.id_categoria
        cat = Categoria(id, nome)
        self.categoria.append(cat)
        return cat

    #Busca uma categoria pelo identificador na lista de categorias
    def procurar_categoria(self):
        id = int(input('Digite o Id da categoria:')) 
        for cat in self.categoria:
            if (cat.id == id):
                return cat
        
        return None

    #Lista todas as categorias
    def listar_categorias(self):
        for cat in self.categoria:
            print(f"Id = {cat.id}, Nome = {cat.nome}")

    #Adiciona uma categoria no plano
    def adicionar_categoria_plano(self, id_categoria, id_plano):
        cat_plan = Categoria_plano(id_categoria, id_plano)
        self.Categoria_plano.append(cat_plan)
        return cat_plan

    def obter_id_categoria(self, id_plano):
        for cat_plan in self.Categoria_plano:
            plano_id_int = int(cat_plan.plano_id)

            if (plano_id_int == id_plano):
                return cat_plan.categoria_id
    
        return None

    #Adiciona uma aula na categoria
    def adicionar_aula_categoria(self, id_categoria, id_aula):
        aula_categoria = Aula_Categoria(id_categoria, id_aula)
        self.Aula_categoria.append(aula_categoria)

    def obter_id_aula(self, id_categoria):

        for aula_categoria in self.Aula_Categoria:
            if(aula_categoria.id_categoria == id_categoria):
                return aula_categoria.id_aula

        return None


    #Adiciona uma nova aula
    def adicionar_aula_ao_curso(self, url, titulo, id_categoria):
        self.id_aula += 1
        id = self.id_aula
        aul = Aula(id, url, titulo)
        self.Aula.append(aul)
        self.adicionar_aula_categoria(id_categoria, id)
        return aul
    
    
    
    def acessar_usuario(self, nome):
        self.limpar_interface()
        texto = Label(self.janela, text="Digite seu email:")
        texto.grid(column=0, row=0, padx=10, pady=10)

        email_entry = Entry(self.janela)
        email_entry.grid(column=0, row=1, padx=10, pady=10)

        # Conferindo se o email já está cadastrado
        if self.procurar_usuario(email_entry.get) is None:
                email_entry.bind('<Return>', lambda event: self.menu_3(nome))
        else:
                for usu in self.Usuario:
                        if usu.email == email_entry.get():
                                self.limpar_interface()
                                texto = Label(self.janela, text="Digite sua senha:")
                                texto.grid(column=0, row=0, padx=10, pady=10)

                                senha_entry = Entry(self.janela)
                                senha_entry.grid(column=0, row=1, padx=10, pady=10)

                                if usu.senha == senha_entry.get():
                                        return usu
                                else:
                                        texto = Label(self.janela, text="Senha incorreta. Tente novamente.")
                                        texto.grid(column=0, row=2, padx=10, pady=10)
                                        email_entry.bind('<Return>', lambda event: self.menu_3(nome))
                                        break  # Sair do loop for quando a senha é incorreta
                        else:
                                texto = Label(self.janela, text="Email incorreto. Tente novamente.")
                                texto.grid(column=0, row=3, padx=10, pady=10)
                                self.acessar_usuario(nome)  # Usar self.acessar_usuario para chamada recursiva


    def menu_3(self, nome):
        self.limpar_interface()
        # Criando a mensagem de boas-vindas
        mensagem = Label(self.janela, text=f"Seu email não existe no sistema. Escolha uma das opções:")
        mensagem.grid(column=0, row=0, padx=10, pady=10)

        # Criando os botões
        botao1 = Button(self.janela, text="Criar Conta", command=lambda event=None: self.interface_criar_conta_email(nome))
        botao1.grid(column=0, row=1, padx=10, pady=10)

        botao2 = Button(self.janela, text="Acessar Conta", command=lambda event=None: self.acessar_usuario(nome))
        botao2.grid(column=0, row=2, padx=10, pady=10)

        botao3 = Button(self.janela, text="Sair", command=self.janela.quit)
        botao3.grid(column=0, row=3, padx=10, pady=10)
                
    def procurar_aula_por_id(self, id_aula):
        for aula in self.Aula:
            if aula.id == id_aula:
                print(f'Aula encontrada: {aula.url}')
                return aula
        print(f'Aula com ID {id_aula} não encontrada.')
        return None

    def listar_videos_por_categoria(self, id_plano):
        id = int(id_plano)
        if id == 1:
            
            for aul in self.Aula:
                
                print(aula.id)
                x = int(aula.id)
                if x == 1:
                    print("A URL da aula com ID 1 é: {}".format(aula.url))
                    return



            print("Seu plano é: DESAFIO GEOMÉTRICO\nAqui estão as aulas da sua categoria: ")

            for aul in Aula:
                print(f"\nID da Aula: {aula_item.id}\nTítulo: {aula_item.titulo}\nURL: {aula_item.url}\n")




        elif(id == 2):
            print("Seu plano é: DESAFIO DE EQUAÇÕES")


    # Buscar se o email já tem cadastro
    def procurar_usuario(self, email):
        for usu in self.Usuario:
                if usu.email == email:
                        return usu
        return None


    def listar_videos(self, id_plano):
        self.limpar_interface()

        frame = Frame(self.janela)
        frame.grid(column=0, row=1, padx=10, pady=10)

        texto = Label(self.janela, text=f"Escolha o video que deseja assistir:")
        texto.grid(column=0, row=0, padx=10, pady=10)

        if id_plano == '1':
            self.adicionar_botao_link(frame, "Vídeo Poligonos", "https://www.youtube.com/watch?v=5e8Ua4RhhXg")
            self.adicionar_botao_link(frame, "Vídeo Ângulos e Retas", "https://www.youtube.com/watch?v=o-srrvPTo0Y")
            botao3 = Button(self.janela, text="Sair", command=self.janela.quit)
            botao3.grid(column=0, row=4, padx=10, pady=10)
        else:
            self.adicionar_botao_link(frame, "Vídeo Equação do Segundo Grau", "https://www.youtube.com/watch?v=1VjauwyHV0o")
            self.adicionar_botao_link(frame, "Vídeo Sistemas de Equações", "https://www.youtube.com/watch?v=YTJPkVMdKho")
            botao3 = Button(self.janela, text="Sair", command=self.janela.quit)
            botao3.grid(column=0, row=4, padx=10, pady=10)

    def adicionar_botao_link(self, frame, texto, url):
        botao = Button(frame, text=texto, command=lambda: self.abrir_link(url))
        botao.pack(pady=5)

 
    def abrir_link(self, url):
        import webbrowser
        webbrowser.open(url)


    def escolher_plano(self, id_usuario):
        self.limpar_interface()
        # Criando a mensagem de boas-vindas
        texto = Label(self.janela, text=f"Esses são os planos disponíveis")
        texto.grid(column=0, row=0, padx=10, pady=10)
        row_index = 1

        for plan in self.Plano:
                texto = Label(self.janela, text=f"Id = {plan.id}\nTitulo = {plan.titulo}\nDescrição: {plan.descricao}\nValor = R${plan.valor}")
                texto.grid(column=0, row=row_index, padx=10, pady=10)
                row_index += 1

        texto = Label(self.janela, text="Digite o id do plano escolhido:")
        texto.grid(column=0, row=3, padx=10, pady=10)

        
        id_plano = Entry(self.janela)
        id_plano.grid(column=0, row=4, padx=10, pady=10)
        
        plano_usuario = Usuario_plano(id_plano, id_usuario)
        self.Usuario_plano.append(plano_usuario)
        id_plano.bind('<Return>', lambda event: self.listar_videos(id_plano.get()))

        
        return id_plano


    def menu2(self, nome, id_usuario):
        self.limpar_interface()
        # Criando a mensagem de boas-vindas
        texto = Label(self.janela, text=f"Seja Bem-vindo(a), {nome}! Seu cadastro foi efetuado!")
        texto.grid(column=0, row=1, padx=10, pady=10)
        # Criando os botões
        botao1 = Button(self.janela, text="Escolher Plano", command=lambda event=None: self.escolher_plano(id_usuario))
        botao1.grid(column=0, row=2, padx=10, pady=10)

        botao2 = Button(self.janela, text="Acessar Conta", command=lambda event=None: self.acessar_usuario(nome))
        botao2.grid(column=0, row=3, padx=10, pady=10)

        botao3 = Button(self.janela, text="Sair", command=self.janela.quit)
        botao3.grid(column=0, row=4, padx=10, pady=10)




    def adicionar_usuario(self, nome, email, senha):
        self.id_usuario += 1
        id = self.id_usuario
        usu = Usuario(id, email, senha)
        self.Usuario.append(usu)
        self.menu2(nome, id)


    def interface_criar_conta_email(self, nome):
        self.limpar_interface()
        texto = Label(self.janela, text="Digite seu email:")
        texto.grid(column=0, row=0, padx=10, pady=10)

        email_entry = Entry(self.janela)
        email_entry.grid(column=0, row=1, padx=10, pady=10)

        #Conferindo se o email ja esta cadastrado
        if self.procurar_usuario(email_entry.get()) is None:
            email_entry.bind('<Return>', lambda event: self.interface_criar_conta_senha(nome, email_entry.get()))

        else:
            texto = Label(self.janela, text="Esse email ja esta cadastrado! Escolha uma ds opções:")
            texto.grid(column=0, row=0, padx=10, pady=10)
            # Criando os botões de retornar para cadastrar novamente 
            botao1 = Button(self.janela, text="Criar Conta", command=lambda: self.interface_criar_conta_email(nome, email_entry.get()))
            botao1.grid(column=0, row=1, padx=10, pady=10)

            botao1 = Button(self.janela, text="Acessar Conta", command=self.acessar_usuario(nome))
            botao1.grid(column=0, row=1, padx=10, pady=10)


    def interface_criar_conta_senha(self, nome, email):
        self.limpar_interface()
        texto = Label(self.janela, text="Digite sua senha:")
        texto.grid(column=0, row=0, padx=10, pady=10)
        senha_entry = Entry(self.janela)
        senha_entry.grid(column=0, row=1, padx=10, pady=10)
        senha_entry.bind('<Return>', lambda event: self.adicionar_usuario(nome, email, senha_entry.get()))


    def limpar_interface(self):
        # Limpa todos os widgets atuais
        for widget in self.janela.winfo_children():
            widget.grid_forget()
    def menu(self, nome):
        self.limpar_interface()
        # Criando a mensagem de boas-vindas
        mensagem = Label(self.janela, text=f"Bem-vindo, {nome}! Escolha uma das opções.")
        mensagem.grid(column=0, row=0, padx=10, pady=10)

        # Criando os botões
        botao1 = Button(self.janela, text="Criar Conta", command=lambda event=None: self.interface_criar_conta_email(nome))
        botao1.grid(column=0, row=1, padx=10, pady=10)

        botao2 = Button(self.janela, text="Acessar Conta", command=lambda event=None: self.acessar_usuario(nome))
        botao2.grid(column=0, row=2, padx=10, pady=10)

        botao3 = Button(self.janela, text="Sair", command=self.janela.quit)
        botao3.grid(column=0, row=3, padx=10, pady=10)

    def iniciar_interface(self):
        self.janela = Tk()

        # Adicionando título
        self.janela.title('Project System Streaming')

        # Imprimindo o texto
        texto = Label(self.janela, text="Digite seu nome:")
        texto.grid(column=0, row=0, padx=10, pady=10)

        nome = Entry(self.janela)
        nome.grid(column=0, row=1, padx=10, pady=10)
        
        nome.bind('<Return>', lambda event=None: self.menu(nome.get()))

        self.janela.mainloop()