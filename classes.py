class Pessoa: 
    def __init__(self, primeiroNome, sobrenome, endereco, cpf, email, usuario, senha):
        self.primeiroNome = str(primeiroNome)
        self.sobrenome = str(sobrenome)
        self.endereco = str(endereco)
        self.cpf = (cpf)
        self.email = str(email)
        self.__usuario = str(usuario)  # Atributo privado
        self.__senha = str(senha)      # Atributo privado

    @property
    def usuario(self):
        return self.__usuario  # Getter para o atributo privado
    
    @usuario.setter 
    def usuario(self, novousuario):
        self.__usuario = novousuario 

    @property
    def senha(self):
        return self.__senha  # Getter para o atributo privado
    
    @senha.setter 
    def senha(self, novasenha):
        self.__senha = novasenha

class Professor(Pessoa):
    def __init__(self, cpf, primeiroNome, sobrenome, endereco, email, usuario, senha, formacao):
        super().__init__(primeiroNome, sobrenome, endereco, cpf, email, usuario, senha)
        self.formacao = str(formacao)
        self.disciplinas = []
        self.segmentos = []
        self.turmas = []
        self.ativo = "True" 

    def salvar_professor(self):
        try:
            # Tenta abrir o arquivo para leitura
            with open('professores.txt', 'r') as arquivo:
                for linha in arquivo:
                    dados = linha.strip().split(';')
                    # Verifica se a linha tem dados suficientes antes de acessar o índice
                    if len(dados) > 3 and dados[3] == str(self.cpf):  # O RA está na posição 8
                        print("Erro: Já existe um professor com este cpf.")
                        return  # Sai da função se o RA já existir
                
            # Se o RA não existir, salva o estudante
            with open('professores.txt', 'a') as arquivo:
                arquivo.write(f"{self.cpf};{self.primeiroNome};{self.sobrenome};{self.email};{self.usuario};{self.senha};{self.formacao};{self.ativo}\n")
            print("Profesor salvo com sucesso!") 
        except Exception as e:
            print(f"Ocorreu um erro ao salvar o professor: {e}")

    def editar_professor(self, cpf, novo_primeiroNome=None, novo_sobrenome=None, novo_endereco=None, novo_email=None, novo_usuario=None, nova_senha=None, nova_formacao=None):
        try:
            linhas = []
            encontrado = False

            # Ler o arquivo e atualizar o estudante correspondente ao RA fornecido
            with open('professores.txt', 'r') as arquivo:
                for linha in arquivo:
                    dados = linha.strip().split(';')
                    if len(dados) > 0 and dados[0] == str(cpf):  # O RA está na posição 8
                        encontrado = True
                        # Atualiza os dados conforme os novos valores fornecidos
                        if novo_primeiroNome is not None:
                            dados[1] = novo_primeiroNome
                        if novo_sobrenome is not None:
                            dados[2] = novo_sobrenome
                        if novo_endereco is not None:
                            dados[3] = novo_endereco
                        if novo_email is not None:
                            dados[4] = novo_email
                        if novo_usuario is not None:
                            dados[5] = novo_usuario
                        if nova_senha is not None:
                            dados[6] = nova_senha
                        if nova_formacao is not None:
                            dados[7] = nova_formacao
                        
                        # Adiciona a linha atualizada à lista
                        linhas.append(';'.join(dados))
                    else:
                        linhas.append(linha.strip())  # Mantém a linha original se não for o estudante editado

            if not encontrado:
                print("Erro: Professor com cpf não encontrado.")
                return
            
            # Reescrever o arquivo com as linhas atualizadas
            with open('professores.txt', 'w') as arquivo:
                for linha in linhas:
                    arquivo.write(linha + '\n')
            
            print("Professor editado com sucesso!")

        except Exception as e:
            print(f"Ocorreu um erro ao editar o professor: {e}")

    def desativar_professor(self, cpf):
        try:
            linhas = []
            encontrado = False

            # Ler o arquivo e atualizar o status do estudante correspondente ao RA fornecido
            with open('professores.txt', 'r') as arquivo:
                for linha in arquivo:
                    dados = linha.strip().split(';')
                    if len(dados) > 0 and dados[0] == str(cpf):  # O RA está na posição 8
                        encontrado = True
                        if dados[7] == "True":
                            dados[7] = "False"
                            print("Professor desativado com sucesso!")
                        else:
                            dados[7] = "True"  # Atualiza o status para inativo (desativado)
                            print("Professor ativado com sucesso!")

                        linhas.append(';'.join(dados))
                    else:
                        linhas.append(linha.strip())  # Mantém a linha original se não for o estudante editado

            if not encontrado:
                print("Erro: Professor com cpf não encontrado.")
                return
            
            # Reescrever o arquivo com as linhas atualizadas
            with open('professores.txt', 'w') as arquivo:
                for linha in linhas:
                    arquivo.write(linha + '\n')

        except Exception as e:
            print(f"Ocorreu um erro ao desativar o professor: {e}")

    def deletar_professor(self, cpf):
        try:
            linhas = []
            encontrado = False
            
            
            with open('professores.txt', 'r') as arquivo:
                for linha in arquivo:
                    dados = linha.strip().split(';')
                    if len(dados) > 0 and dados[0] != str(cpf):  
                        linhas.append(linha.strip())
                    else:
                        encontrado = True  # Se encontrar o RA, marca como encontrado
            
            if not encontrado:
                print("Erro: Professor com cpf não encontrado.")
                return
            
            # Reescrever o arquivo com as linhas filtradas
            with open('professores.txt', 'w') as arquivo:
                for linha in linhas:
                    arquivo.write(linha + '\n')
            
            print("Professor deletado com sucesso!")
        
        except Exception as e:
            print(f"Ocorreu um erro ao deletar o professor: {e}")

class Estudante(Pessoa):
    def __init__(self,ra, primeiroNome, sobrenome, endereco, cpf, email, usuario, senha, filiacao, emailResponsavel, turma, curso, segmento):
        super().__init__(primeiroNome, sobrenome, endereco, cpf, email, usuario, senha)
        self.filiacao = str(filiacao)
        self.emailResponsavel = str(emailResponsavel)
        self.ra = str(ra)
        self.turma = turma if turma else []
        self.curso = curso if curso else []
        self.segmento = segmento  
        self.ativo = "True"
        
    def salvar_estudante(self):
        try:
            # Tenta abrir o arquivo para leitura
            with open('estudantes.txt', 'r') as arquivo:
                for linha in arquivo:
                    dados = linha.strip().split(';')
                    # Verifica se a linha tem dados suficientes antes de acessar o índice
                    if len(dados) > 8 and dados[8] == str(self.ra):  # O RA está na posição 8
                        print("Erro: Já existe um estudante com este RA.")
                        return  # Sai da função se o RA já existir
                
            # Se o RA não existir, salva o estudante
            with open('estudantes.txt', 'a') as arquivo:
                arquivo.write(f"{self.ra}; {self.primeiroNome};{self.sobrenome};{self.endereco};{self.cpf};{self.email};{self.usuario};{self.senha};{self.filiacao};{self.emailResponsavel};{self.turma};{self.curso};{self.segmento};{self.ativo}\n")
            print("Estudante salvo com sucesso!") 
        except Exception as e:
            print(f"Ocorreu um erro ao salvar o estudante: {e}")

        

    def editar_estudante(self, ra, novo_primeiroNome=None, novo_sobrenome=None, novo_endereco=None, novo_email=None, novo_usuario=None, nova_senha=None, nova_filiacao=None, novo_emailResponsavel=None, nova_turma=None, novo_curso=None, novo_segmento=None):
        try:
            linhas = []
            encontrado = False

            # Ler o arquivo e atualizar o estudante correspondente ao RA fornecido
            with open('estudantes.txt', 'r') as arquivo:
                for linha in arquivo:
                    dados = linha.strip().split(';')
                    if len(dados) > 0 and dados[0] == str(ra):  # O RA está na posição 8
                        encontrado = True
                        # Atualiza os dados conforme os novos valores fornecidos
                        if novo_primeiroNome is not None:
                            dados[1] = novo_primeiroNome
                        if novo_sobrenome is not None:
                            dados[2] = novo_sobrenome
                        if novo_endereco is not None:
                            dados[3] = novo_endereco
                        if novo_email is not None:
                            dados[5] = novo_email
                        if novo_usuario is not None:
                            dados[6] = novo_usuario
                        if nova_senha is not None:
                            dados[7] = nova_senha
                        if nova_filiacao is not None:
                            dados[8] = nova_filiacao
                        if novo_emailResponsavel is not None:
                            dados[9] = novo_emailResponsavel
                        if nova_turma is not None:
                            dados[10] = nova_turma
                        if novo_curso is not None:
                            dados[11] = novo_curso
                        if novo_segmento is not None:
                            dados[12] = novo_segmento
                        
                        # Adiciona a linha atualizada à lista
                        linhas.append(';'.join(dados))
                    else:
                        linhas.append(linha.strip())  # Mantém a linha original se não for o estudante editado

            if not encontrado:
                print("Erro: Estudante com RA não encontrado.")
                return
            
            # Reescrever o arquivo com as linhas atualizadas
            with open('estudantes.txt', 'w') as arquivo:
                for linha in linhas:
                    arquivo.write(linha + '\n')
            
            print("Estudante editado com sucesso!")

        except Exception as e:
            print(f"Ocorreu um erro ao editar o estudante: {e}")

    def desativar_estudante(self, ra):
        try:
            linhas = []
            encontrado = False

            # Ler o arquivo e atualizar o status do estudante correspondente ao RA fornecido
            with open('estudantes.txt', 'r') as arquivo:
                for linha in arquivo:
                    dados = linha.strip().split(';')
                    if len(dados) > 0 and dados[0] == str(ra):  # O RA está na posição 8
                        encontrado = True
                        if dados[13] == "True":
                            dados[13] = "False"
                            print("Estudante desativado com sucesso!")

                        else:
                            dados[13] = "True"  # Atualiza o status para inativo (desativado)
                            print("Estudante ativado com sucesso!")

                        linhas.append(','.join(dados))
                    else:
                        linhas.append(linha.strip())  # Mantém a linha original se não for o estudante editado

            if not encontrado:
                print("Erro: Estudante com RA não encontrado.")
                return
            
            # Reescrever o arquivo com as linhas atualizadas
            with open('estudantes.txt', 'w') as arquivo:
                for linha in linhas:
                    arquivo.write(linha + '\n')

        except Exception as e:
            print(f"Ocorreu um erro ao desativar o estudante: {e}")

    def deletar_estudante(self, ra):

        try:
            linhas = []
            encontrado = False
            
            # Ler o arquivo e manter apenas os estudantes que não correspondem ao RA fornecido
            with open('estudantes.txt', 'r') as arquivo:
                for linha in arquivo:
                    dados = linha.strip().split(';')
                    if len(dados) > 0 and dados[0] != str(ra):  # O RA está na posição 8
                        linhas.append(linha.strip())
                    else:
                        encontrado = True  # Se encontrar o RA, marca como encontrado
            
            if not encontrado:
                print("Erro: Estudante com RA não encontrado.")
                return
            
            # Reescrever o arquivo com as linhas filtradas
            with open('estudantes.txt', 'w') as arquivo:
                for linha in linhas:
                    arquivo.write(linha + '\n')
            
            print("Estudante deletado com sucesso!")
        
        except Exception as e:
            print(f"Ocorreu um erro ao deletar o estudante: {e}")

class Disciplina:
    def __init__(self, id, descricao, segmento, professorTitular):
        self.id = (id)
        self.descricao = str(descricao)
        self.segmento = str(segmento)
        self.professorTitular = professorTitular
        self.ativo = "True"

    def salvar_disciplina(self):
        try:
            # Tenta abrir o arquivo para leitura
            with open('disciplinas.txt', 'r') as arquivo:
                for linha in arquivo:
                    dados = linha.strip().split(';')
                    # Verifica se a linha tem dados suficientes antes de acessar o índice
                    if len(dados) > 0 and dados[0] == str(self.id):  # O RA está na posição 8
                        print("Erro: Já existe uma disciplina com este ID.")
                        return  # Sai da função se o RA já existir
                
            # Se o RA não existir, salva o estudante
            with open('disciplinas.txt', 'a') as arquivo:
                arquivo.write(f"{self.id};{self.descricao};{self.segmento};{self.professorTitular};{self.ativo}\n")
            print("Diciplina salva com sucesso!") 
        except Exception as e:
            print(f"Ocorreu um erro ao salvar a Disciplina: {e}")

    def editar_disciplina(self, id, nova_descricao=None, novo_segmento=None, novo_professorTitular=None):
        try:
            linhas = []
            encontrado = False

            # Ler o arquivo e atualizar o estudante correspondente ao RA fornecido
            with open('disciplinas.txt', 'r') as arquivo:
                for linha in arquivo:
                    dados = linha.strip().split(';')
                    if len(dados) > 0 and dados[0] == str(id):  # O RA está na posição 8
                        encontrado = True
                        # Atualiza os dados conforme os novos valores fornecidos
                        if nova_descricao is not None:
                            dados[1] = nova_descricao
                        if novo_segmento is not None:
                            dados[2] = novo_segmento
                        if novo_professorTitular is not None:
                            dados[3] = novo_professorTitular
                        
                        # Adiciona a linha atualizada à lista
                        linhas.append(';'.join(dados))
                    else:
                        linhas.append(linha.strip())  # Mantém a linha original se não for o estudante editado

            if not encontrado:
                print("Erro: Disciplina com ID não encontrado.")
                return
            
            # Reescrever o arquivo com as linhas atualizadas
            with open('Disciplinas.txt', 'w') as arquivo:
                for linha in linhas:
                    arquivo.write(linha + '\n')
            
            print("Disciplina editada com sucesso!")

        except Exception as e:
            print(f"Ocorreu um erro ao editar o estudante: {e}")

    def desativar_disciplina(self, id):
        try:
            linhas = []
            encontrado = False

            # Ler o arquivo e atualizar o status do estudante correspondente ao RA fornecido
            with open('disciplinas.txt', 'r') as arquivo:
                for linha in arquivo:
                    dados = linha.strip().split(';')
                    if len(dados) > 0 and dados[0] == str(id):  # O RA está na posição 8
                        encontrado = True
                        if dados[4] == "True":
                            dados[4] = "False"
                            print("Disciplina desativada com sucesso!")

                        else:
                            dados[4] = "True"  # Atualiza o status para inativo (desativado)
                            print("Disciplina ativada com sucesso!")

                        linhas.append(';'.join(dados))
                    else:
                        linhas.append(linha.strip())  # Mantém a linha original se não for o estudante editado

            if not encontrado:
                print("Erro: Disciplina com ID não encontrado.")
                return
            
            # Reescrever o arquivo com as linhas atualizadas
            with open('disciplinas.txt', 'w') as arquivo:
                for linha in linhas:
                    arquivo.write(linha + '\n')

        except Exception as e:
            print(f"Ocorreu um erro ao desativar a disciplina: {e}")

    def deletar_disciplina(self, id):
        try:
            linhas = []
            encontrado = False
            
            # Ler o arquivo e manter apenas os estudantes que não correspondem ao RA fornecido
            with open('disciplinas.txt', 'r') as arquivo:
                for linha in arquivo:
                    dados = linha.strip().split(';')
                    if len(dados) > 0 and dados[0] != str(id):  # O RA está na posição 8
                        linhas.append(linha.strip())
                    else:
                        encontrado = True  # Se encontrar o RA, marca como encontrado
            
            if not encontrado:
                print("Erro: Disciplina com RA não encontrado.")
                return
            
            # Reescrever o arquivo com as linhas filtradas
            with open('disciplinas.txt', 'w') as arquivo:
                for linha in linhas:
                    arquivo.write(linha + '\n')
            
            print("Disciplina deletada com sucesso!")
        
        except Exception as e:
            print(f"Ocorreu um erro ao deletar a disciplina: {e}")

class Turma:
    def __init__(self, id, nome, segmento, curso, ano, alunos=None, professores = None, disciplinas=None ):
        self.id = id
        self.nome = nome
        self.segmento = segmento  
        self.curso = curso
        self.ano = ano
        self.alunos = alunos if alunos else []
        self.professores = professores if professores else []
        self.disciplinas = disciplinas if disciplinas else []
        self.ativo = "True"  

    def salvar_turma(self):
        try:
            if self.segmento=="EM" and len(self.alunos)<20:
                raise ValueError("Uma turma de ensino médio deve ter no minímo 20 alunos. ")
            elif self.segmento=="SUPERIOR" and len(self.alunos)<5:
                raise ValueError("Uma turma de ensino superior deve ter no minímo 5 alunos. ")
            else:
                with open('turmas.txt', 'r') as arquivo:
                    for linha in arquivo:
                        dados = linha.strip().split(';')
                        if dados[0] == str(self.id):
                            print("Erro: Já existe uma turma com este ID.")
                            return
                
                with open('turmas.txt', 'a') as arquivo:
                    arquivo.write(f"{self.id};{self.nome};{self.segmento};{self.curso};{self.ano};{self.alunos};{self.professores};{self.disciplinas};{self.ativo}\n")
                print("Turma salva com sucesso!") 
        except Exception as e:
                print(f"Ocorreu um erro ao salvar a turma: {e}")

    def editar_turma(self, id, novo_nome=None, novo_segmento=None, novo_curso=None, novo_ano=None,  novo_aluno = None, novo_professor = None,nova_disciplina = None):
        try:
            linhas = []
            encontrado = False
            
            with open('turmas.txt', 'r') as arquivo:
                for linha in arquivo:
                    dados = linha.strip().split(';')
                    if dados[0] == str(id):
                        encontrado = True
                        if novo_nome is not None:
                            dados[1] = novo_nome
                        if novo_segmento is not None:
                            dados[2] = novo_segmento
                        if novo_curso is not None:
                            dados[3] = novo_curso
                        if novo_ano is not None:
                            dados[4] = novo_ano
                        if novo_aluno is not None:
                            dados[5] = novo_aluno
                        if novo_professor is not None:
                            dados[6] = novo_professor
                        if nova_disciplina is not None:
                            dados[7] = nova_disciplina
                        
                        linhas.append(';'.join(dados))
                    else:
                        linhas.append(linha.strip())
            
            if not encontrado:
                print("Erro: Turma com ID não encontrado.")
                return
            
            with open('turmas.txt', 'w') as arquivo:
                for linha in linhas:
                    arquivo.write(linha + '\n')
            
            print("Turma editada com sucesso!")
        except Exception as e:
            print(f"Ocorreu um erro ao editar a turma: {e}")

    def imprimir_turma(self, id):
        try:
            with open('turmas.txt', 'r') as arquivo:
                for linha in arquivo:
                    dados = linha.strip().split(';')
                    if dados[0] == str(id):
                        print( f"""
                        {linha}
                        """)
        except Exception as e:
            print(f"Ocorreu um erro ao imprimir a turma: {e}")


    def desativar_turma(self, id):
        try:
            linhas = []
            encontrado = "False"
            
            with open('turmas.txt', 'r') as arquivo:
                for linha in arquivo:
                    dados = linha.strip().split(';')
                    if dados[0] == str(id):
                        encontrado = "True"
                        dados[7] = "False" if dados[7] == "True" else "True"
                        print("Turma desativada com sucesso!" if dados[7] == "False" else "Turma ativada com sucesso!")
                        linhas.append(','.join(dados))
                    else:
                        linhas.append(linha.strip())
            
            if not encontrado:
                print("Erro: Turma com ID não encontrado.")
                return
            
            with open('turmas.txt', 'w') as arquivo:
                for linha in linhas:
                    arquivo.write(linha + '\n')
        except Exception as e:
            print(f"Ocorreu um erro ao desativar a turma: {e}")

    def deletar_turma(self, id):
        try:
            linhas = []
            encontrado = False
            
            with open('turmas.txt', 'r') as arquivo:
                for linha in arquivo:
                    dados = linha.strip().split(';')
                    if dados[0] != str(id):
                        linhas.append(linha.strip())
                    else:
                        encontrado = True
            
            if not encontrado:
                print("Erro: Turma com ID não encontrado.")
                return
            
            with open('turmas.txt', 'w') as arquivo:
                for linha in linhas:
                    arquivo.write(linha + '\n')
            
            print("Turma deletada com sucesso!")
        except Exception as e:
            print(f"Ocorreu um erro ao deletar a turma: {e}")

def carregar_estudantes(arquivo="estudantes.txt"):
    estudantes = []  # Lista para armazenar os objetos Estudante
    try:
        with open(arquivo, "r") as f:
            for linha in f:
                dados = linha.strip().split(';')
                
                # Criação de um objeto Estudante
                estudante = Estudante(
                    ra=dados[0],  # RA deve ser único para identificação
                    primeiroNome=dados[1],
                    sobrenome=dados[2],
                    endereco=dados[3],
                    cpf=dados[4],
                    email=dados[5],
                    usuario=dados[6],
                    senha=dados[7],
                    filiacao=dados[8],
                    emailResponsavel=dados[9],
                    turma=dados[10],
                    curso=dados[11],
                    segmento=dados[12]
                )
                
                # Adiciona o objeto Estudante à lista
                estudantes.append(estudante)
                
    except FileNotFoundError:
        print("Arquivo não encontrado. ")
    except Exception as e:
        print(f"Erro ao carregar estudantes: {e}")
    
    return estudantes

def carregar_professor(arquivo="professores.txt"):
            professores = []  # Lista para armazenar os objetos Estudante
            try:
                with open(arquivo, "r") as f:
                    for linha in f:
                        dados = linha.strip().split(';')
                        
                        # Criação de um objeto Estudante
                        professor = Professor(
                            cpf=dados[0],  # RA deve ser único para identificação
                            primeiroNome=dados[1],
                            sobrenome=dados[2],
                            endereco=dados[3],
                            email=dados[4],
                            usuario=dados[5],
                            senha=dados[6],
                            formacao=dados[7],
                        )
                        
                        # Adiciona o objeto Estudante à lista
                        professores.append(professor)
                        
            except FileNotFoundError:
                print("Arquivo não encontrado. ")
            except Exception as e:
                print(f"Erro ao carregar professores: {e}")
            
            return professores

def carregar_disciplina(arquivo="disciplinas.txt"):
    disciplinas = []  # Lista para armazenar os objetos Disciplina
    try:
        with open(arquivo, "r") as f:
            for linha in f:
                dados = linha.strip().split(';')
                
                # Criação de um objeto Disciplina
                disciplina = Disciplina(
                    id=dados[0],  # ID único da disciplina
                    descricao=dados[1],
                    segmento=dados[2],
                    professorTitular=dados[3] if len(dados) > 3 else None,  # Professor titular, se existir
                )

                # Adiciona o objeto Disciplina à lista
                disciplinas.append(disciplina)
                
    except FileNotFoundError:
        print("Arquivo 'disciplinas.txt' não encontrado.")
    except Exception as e:
        print(f"Erro ao carregar disciplinas: {e}")
    
    return disciplinas

def carregar_turmas():
    turmas = []
    try:
        with open('turmas.txt', 'r') as arquivo:
            for linha in arquivo:
                dados = linha.strip().split(';')
                
                # Descompactando os dados do arquivo
                id = (dados[0])
                nome = dados[1]
                segmento = dados[2]
                curso = dados[3]
                ano = (dados[4])
                alunos = dados[5].split(',') if len(dados) > 5 and dados[5] else []
                professores = dados[6].split(',') if len(dados) > 6 and dados[6] else []
                disciplinas = dados[7].split(',') if len(dados) > 7 and dados[7] else []
                ativo = dados[8] == "True"
                
                # Criando a instância da turma
                turma = Turma(id, nome, segmento, curso, ano, alunos, professores, disciplinas)
                turma.ativo = ativo  # Garantindo o status correto
                
                turmas.append(turma)
        print(f"{len(turmas)} turma(s) carregadas com sucesso!")
    except FileNotFoundError:
        print("O arquivo 'turmas.txt' não foi encontrado. Nenhuma turma carregada.")
    except Exception as e:
        print(f"Ocorreu um erro ao carregar as turmas: {e}")
    return turmas

def verificar_cpf(cpf):

    if len(cpf) == 11 and cpf.isdigit():  

        if cpf == cpf[0] * 11:
            return False
        else:
            soma = 0
            mult = 10

            for digito in cpf[:9]: 
                soma += int(digito) * mult
                mult -= 1

            if soma % 11 >= 2:
                d1 = 11 - (soma % 11)
            else:
                d1 = 0

            soma = 0
            mult = 11

            for digito in cpf[:10]:  
                soma += int(digito) * mult
                mult -= 1

            if soma % 11 >= 2:
                d2 = 11 - (soma % 11)
            else:
                d2 = 0

            # Verifica se os dígitos calculados correspondem aos fornecidos
            if int(cpf[9]) == d1 and int(cpf[10]) == d2:
                return True
            else:
                raise ValueError("CPF inválido.")
    else:
        raise ValueError("CPF deve ter 11 dígitos numéricos.")