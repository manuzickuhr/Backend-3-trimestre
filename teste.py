from classes import *

estudantes = []
professores = []
disciplinas = []
turmas = []

def menu_principal():
    while True:
        print("\nBem-vindo ao sistema")
        print("1 - Sair")
        print("2 - Alunos")
        print("3 - Professores")
        print("4 - Disciplinas")
        print("5 - Turmas")
        escolha_principal = int(input("Digite o número da opção desejada: "))

        if escolha_principal == 1:
            print("Saindo do sistema.")
            break
        elif escolha_principal == 2:
            menu_alunos()
        elif escolha_principal == 3:
            menu_professores()
        elif escolha_principal == 4:
             menu_disciplinas()
        elif escolha_principal == 5:
             menu_turmas() 
        else:
            print("Opção inválida. Tente novamente.")
     
def menu_alunos():
    while True:
        print("\nMenu Alunos:")
        print("1 - Voltar")
        print("2 - Cadastrar aluno")
        print("3 - Editar aluno")
        print("4 - Trocar curso do aluno")
        print("5 - Desativar aluno")
        print('6 - Deletar aluno')
        escolha_alunos = int(input("Digite o número da opção desejada: "))

        if escolha_alunos == 1:
            break
        elif escolha_alunos == 2:
            salvar_aluno()
        elif escolha_alunos == 3:
            editar_aluno()
        elif escolha_alunos == 4:
            trocar_curso_aluno()
        elif escolha_alunos == 5:
            desativar_aluno()
        elif escolha_alunos == 6:
            deletar_aluno()
        else:
            print("Opção inválida. Tente novamente.")
        
def salvar_aluno():
            print("\nCadastro de Aluno:")
            primeiroNome = input('Digite o primeiro nome do aluno: ')
            sobrenome = input("Digite o sobrenome do aluno: ")
            endereco = input("Digite o endereço do aluno :")
            while True:
                    try:
                        cpf = input('Digite o CPF: ')
                        verificar_cpf(cpf)  # Verifica se o CPF é válido
                        print("CPF válido!")  # Se o CPF for válido, sai do laço
                        break  # Encerra o laço e segue para o restante do cadastro
                    except ValueError as e:
                        print(f"Erro: {e}. Tente novamente.")

            email = input("Digite o email do aluno :")
            usuario = input("Digite o usuario do aluno :")
            senha = input("Digite a senha do aluno :")
            filiacao = input("Digite a filiacao do aluno :")
            emailResponsavel = input("Digite o email do responsável do aluno :")
            ra = input("Digite o ra do aluno(deve ser unico):")
            turma = input("Digite a(s) turma(s) do aluno :")
            segmento = input("Segmento da turma (EM ou Superior): ").upper()

            if segmento not in ["EM", "SUPERIOR"]:
                print("Segmento inválido. Por favor, escolha entre 'EM' (Ensino Médio) ou 'Superior'.")
                return

            curso = None
            if segmento == "EM":
                print("Cursos disponíveis para Ensino Médio: Mecatrônica, Eletromecânica, Informática")
                curso = input("Digite o curso do aluno: ").capitalize()
                if curso not in ["Mecatrônica", "Eletromecânica", "Informática"]:
                    print("Curso inválido para Ensino Médio. Operação cancelada.")
                    return

            elif segmento == "SUPERIOR":
                print("Cursos disponíveis para Superior: Ciências da Computação, Pedagogia")
                curso = input("Digite o(s) curso(s) do aluno: ").capitalize()
                if curso not in ["Ciências da Computação", "Pedagogia"]:
                    print("Curso inválido para Superior. Operação cancelada.")
                    return

            estudante = Estudante(ra, primeiroNome, sobrenome, endereco, cpf, email, usuario, senha, filiacao, emailResponsavel, turma, curso, segmento)
            estudante.salvar_estudante()

def editar_aluno():
        print("\nEdição de Aluno:")
        ra_aluno = input("Digite o RA do aluno que deseja editar: ")
        print("Deixe os campos vazios caso não queira alterá-los.")
                
        estudantes = carregar_estudantes()

            
        aluno_encontrado = None
        for aluno in estudantes:  
                if aluno.ra == ra_aluno:
                    aluno_encontrado = aluno
                    break
            
        if aluno_encontrado !=None:
                
                novo_primeiroNome = input("Digite o novo primeiro nome do aluno: (enter caso não mude) ")
                if novo_primeiroNome == "":
                    novo_primeiroNome = None

                novo_sobrenome = input("Digite o novo sobrenome do aluno: (enter caso não mude) ")
                if novo_sobrenome == "":
                    novo_sobrenome = None

                novo_endereco = input("Digite o novo endereço do aluno: (enter caso não mude) ")
                if novo_endereco == "":
                    novo_endereco = None

                novo_email = input("Digite o novo email do aluno: (enter caso não mude) ")
                if novo_email == "":
                    novo_email = None

                novo_usuario = input("Digite o novo usuário do aluno: (enter caso não mude) ")
                if novo_usuario == "":
                    novo_usuario = None

                nova_senha = input("Digite a nova senha do aluno: (enter caso não mude) ")
                if nova_senha == "":
                    nova_senha = None

                nova_filiacao = input("Digite a nova filiação do aluno: (enter caso não mude) ")
                if nova_filiacao == "":
                    nova_filiacao = None

                novo_emailResponsavel = input("Digite o novo email do responsável do aluno: (enter caso não mude) ")
                if novo_emailResponsavel == "":
                    novo_emailResponsavel = None

                nova_turma = input("Digite a(s) nova(s) turma(s) do aluno: (enter caso não mude) ")
                if nova_turma == "":
                    turmas = None

                else:
                    nova_turma = nova_turma.strip().split(",")
                    turmas = f"['{nova_turma[0]}'"
                    for i in range(len(nova_turma)-1):
                        turmas += f",'{nova_turma[i+1]}'"
                    turmas += ']'


                novo_segmento = input("Digite o novo segmento do aluno: (enter caso não mude) ")
                if novo_segmento == "":
                    novo_segmento = None

                # Editar o aluno
                aluno_encontrado.editar_estudante(ra_aluno, novo_primeiroNome, novo_sobrenome, novo_endereco, novo_email, novo_usuario, nova_senha, nova_filiacao, novo_emailResponsavel, turmas, None, novo_segmento)

def trocar_curso_aluno():
    print("\nTroca de curso de Aluno:")
    ra_aluno = input("Digite o RA do aluno que deseja trocar de curso: ")

    estudantes = carregar_estudantes()

            
    aluno_encontrado = None
    for aluno in estudantes:  
        if aluno.ra == ra_aluno:
            aluno_encontrado = aluno
            break

    if aluno_encontrado !=None:
        novo_curso = input("Digite o(s) novo(s) curso(s) do aluno: ")
        novo_curso = novo_curso.strip().split(",")
        cursos = f"['{novo_curso[0]}'"
        for i in range(len(novo_curso)-1):
            cursos += f",'{novo_curso[i+1]}'"
        cursos += ']'


        aluno_encontrado.editar_estudante(ra_aluno,novo_curso = cursos)


def desativar_aluno():
    print("\nDesativar Aluno:")
    ra_aluno = input("Digite o RA do aluno que deseja desativar: ")
    estudantes = carregar_estudantes()  # Certifique-se de que essa função retorna uma lista de objetos Estudante
    
    # Procurar pelo aluno
    aluno_encontrado = None
    for aluno in estudantes:
        if aluno.ra == ra_aluno:
            aluno_encontrado = aluno
            break

    # Verificar se o aluno foi encontrado
    if aluno_encontrado:
        aluno_encontrado.desativar_estudante(ra_aluno)  # Chamar o método desativar_estudante no objeto
        print(f"O aluno com RA {ra_aluno} foi desativado com sucesso.")
    else:
        print(f"Aluno com RA {ra_aluno} não encontrado.")

def deletar_aluno():
    print("\nDeletar Aluno:")
    ra_aluno = input("Digite o RA do aluno que deseja deletar: ")
    estudantes = carregar_estudantes()  # Certifique-se de que essa função retorna uma lista de objetos Estudante
    
    # Procurar pelo aluno
    aluno_encontrado = None
    for aluno in estudantes:
        if aluno.ra == ra_aluno:
            aluno_encontrado = aluno
            break

    # Verificar se o aluno foi encontrado
    if aluno_encontrado:
         aluno_encontrado.deletar_estudante(ra_aluno)
    
def menu_professores():
     while True:
        print("\nMenu Professores:")
        print("1 - Voltar")
        print("2 - Cadastrar professor")
        print("3 - Editar professor")
        print("4 - Desativar professor")
        print("5 - Deletar professor")
        escolha_professores = int(input("Digite o número da opção desejada: "))

        if escolha_professores == 1:
            break
        elif escolha_professores == 2:
            salvar_professor() 
        elif escolha_professores == 3:
            editar_professor() 
        elif escolha_professores == 4:
            desativar_professor()
        elif escolha_professores == 5:
            deletar_professor()
        else:
            print("Opção inválida. Tente novamente.")
        
def salvar_professor():
     print("\nCadastro de Professor:")
     nome = input('Digite o primeiro nome do professor: ')
     sobrenome = input('Digite o sobrenome do professor: ')
     endereco = input('Digite o endereço: ')
     while True:
        try:
            cpf = input('Digite o CPF: ')
            verificar_cpf(cpf)  # Verifica se o CPF é válido
            print("CPF válido!")  # Se o CPF for válido, sai do laço
            break  # Encerra o laço e segue para o restante do cadastro
        except ValueError as e:
            print(f"Erro: {e}. Tente novamente.")

     email = input('Digite um email válido: ')
     usuario = input('Digite o usuário: ')
     senha = input('Digite a senha: ')
     formacao = input('Digite a formação')

     professor = Professor(cpf, nome, sobrenome, endereco, email, usuario, senha, formacao)
     professor.salvar_professor()

def editar_professor():
     print("\nEdição de Professor: ")
     cpf_professor= input("Digite o CPF do professor que deseja editar: ")
     print("Deixe os campos vazios caso não queira alterá-los.")

     professores = carregar_professor()
            
     professor_encontrado = None
     for professor in professores:
        if professor.cpf == cpf_professor:
            professor_encontrado = professor
            break  # Interrompe o laço ao encontrar o professor

     if professor_encontrado:
                novo_primeiroNome = input("Digite o novo primeiro nome do professor: (enter caso não mude) ")
                if novo_primeiroNome == "":
                    novo_primeiroNome = None

                novo_sobrenome = input("Digite o novo sobrenome do professor: (enter caso não mude) ")
                if novo_sobrenome == "":
                    novo_sobrenome = None

                novo_endereco = input("Digite o novo endereço do professor: (enter caso não mude) ")
                if novo_endereco == "":
                    novo_endereco = None

                novo_email = input("Digite o novo email do professor: (enter caso não mude) ")
                if novo_email == "":
                    novo_email = None

                novo_usuario = input("Digite o novo usuário do professor: (enter caso não mude) ")
                if novo_usuario == "":
                    novo_usuario = None

                nova_senha = input("Digite a nova senha do professor: (enter caso não mude) ")
                if nova_senha == "":
                    nova_senha = None

                nova_filiacao = input("Digite a nova formação do professor: (enter caso não mude) ")
                if nova_filiacao == "":
                    nova_filiacao = None
                
                professor_encontrado.editar_professor(cpf_professor, novo_primeiroNome, novo_sobrenome, novo_endereco, novo_email, novo_usuario, nova_senha, nova_filiacao)

def desativar_professor():
     print("\nDesativar Professor: ")
     cpf_professor= input("Digite o CPF do professor que deseja desativar: ")

     professores = carregar_professor()
            
     professor_encontrado = None
     for professor in professores:
        if professor.cpf == cpf_professor:
            professor_encontrado = professor

        if professor_encontrado !=None:
            professor_encontrado.desativar_professor(cpf_professor)
            break

def deletar_professor():
     print('\n Deletar Professor: ')
     cpf_professor= input("Digite o CPF do professor que deseja deletar: ")

     professores = carregar_professor()
            
     professor_encontrado = None
     for professor in professores:
        if professor.cpf == cpf_professor:
            professor_encontrado = professor
             

        if professor_encontrado:
             professor_encontrado.deletar_professor(cpf_professor)
             break 
     
def menu_disciplinas():
    while True:
        print("\nMenu Disciplinas:")
        print("1 - Voltar")
        print("2 - Cadastrar disciplinas")
        print("3 - Editar disciplina")
        print("4 - Desativar disciplina")
        print("5 - Deletar disciplina")
        escolha_disciplinas = int(input("Digite o número da opção desejada: "))

        if escolha_disciplinas == 1:
            break
        elif escolha_disciplinas == 2:
            salvar_disciplina() 
        elif escolha_disciplinas == 3:
            editar_disciplina()
        
        elif escolha_disciplinas == 4:
            desativar_disciplina()
            
        elif escolha_disciplinas == 5:
            deletar_disciplina()
        else:
            print("Opção inválida. Tente novamente.") 

def salvar_disciplina():
    print("\nCadastro de Disciplina:")
    id = input('Digite o id da disciplina: ')
    descricao = input("Digite a descrição da disciplina: ")
    segmento = input('Segmento da disciplina (EM ou ES): ')
    professorTitular = input("Digite o cpf do professor titular(já deve estar cadastrado): ")

    professores = carregar_professor()
            
    professor_encontrado = None
    for professor in professores:
        if professor.cpf == professorTitular:
            professor_encontrado = professor
            break  # Interrompe o laço ao encontrar o professor

    if professor_encontrado:
        disciplina = Disciplina(id, descricao, segmento, professorTitular)
        disciplina.salvar_disciplina()
    else:
        print("O professor titular não foi encontrado. ")

def editar_disciplina():
    print("\nEdição de Disciplina:")
    id_disciplina = input("Digite o ID da disciplina que deseja editar: ")
    print("Deixe os campos vazios caso não queira alterá-los.")

    # Carregar a lista de disciplinas
    disciplinas = carregar_disciplina()  # Certifique-se de que essa função está implementada corretamente

    # Procurar a disciplina com o ID fornecido
    disciplina_encontrada = None
    for disciplina in disciplinas:
        print(disciplina)
        if disciplina.id == id_disciplina:
            disciplina_encontrada = disciplina
            break  # Interrompe o laço ao encontrar a disciplina

    if disciplina_encontrada:
        # Permitir ao usuário editar os campos desejados
        nova_descricao = input("Digite a nova descrição da disciplina: (enter caso não mude) ")
        if nova_descricao == "":
            nova_descricao = None

        novo_segmento = input("Digite o novo segmento da disciplina (EM ou ES): (enter caso não mude) ")
        if novo_segmento == "":
            novo_segmento = None

        novo_professorTitular = input("Digite o CPF do novo professor titular (deve estar cadastrado): (enter caso não mude) ")
        if novo_professorTitular == "":
            novo_professorTitular = None
        else:
            # Validar se o professor existe
            professores = carregar_professor()  # Certifique-se de que essa função retorna uma lista de professores
            professor_encontrado = None
            for professor in professores:
                if professor.cpf == novo_professorTitular:
                    professor_encontrado = professor
                    break

            if not professor_encontrado:
                print("O professor titular com o CPF informado não foi encontrado.")
                return

        # Atualizar os atributos da disciplina
        disciplina_encontrada.editar_disciplina(
            id_disciplina, 
            nova_descricao=nova_descricao,
            novo_segmento=novo_segmento,
            novo_professorTitular =novo_professorTitular
        )

def desativar_disciplina():
    print("\nDesativar Disciplina:")
    id_disciplina = input("Digite o ID da disciplina que deseja desativar: ")
    print("Deixe os campos vazios caso não queira alterá-los.")

    # Carregar a lista de disciplinas
    disciplinas = carregar_disciplina()  # Certifique-se de que essa função está implementada corretamente

    # Procurar a disciplina com o ID fornecido
    disciplina_encontrada = None
    for disciplina in disciplinas:
        print(disciplina)
        if disciplina.id == id_disciplina:
            disciplina_encontrada = disciplina
            break  # Interrompe o laço ao encontrar a disciplina

    if disciplina_encontrada:
        disciplina_encontrada.desativar_disciplina(id_disciplina)

def deletar_disciplina():
    print("\nDeletar Disciplina:")
    id_disciplina = input("Digite o ID da disciplina que deseja desativar: ")
    print("Deixe os campos vazios caso não queira alterá-los.")

    # Carregar a lista de disciplinas
    disciplinas = carregar_disciplina()  # Certifique-se de que essa função está implementada corretamente

    # Procurar a disciplina com o ID fornecido
    disciplina_encontrada = None
    for disciplina in disciplinas:
        print(disciplina)
        if disciplina.id == id_disciplina:
            disciplina_encontrada = disciplina
            break  # Interrompe o laço ao encontrar a disciplina

    if disciplina_encontrada:
        disciplina_encontrada.deletar_disciplina(id_disciplina)

def menu_turmas():
    while True:
            print("\nMenu Turmas:")
            print("1 - Voltar")
            print("2 - Cadastrar turma")
            print("3 - Editar turma")
            print("4 - Desativar turma")
            print("5 - Deletar turma")
            print("6 - Imprimir turma")
            escolha_turmas = int(input("Digite o número da opção desejada: "))

            if escolha_turmas == 1:
                break
            elif escolha_turmas == 2:
                salvar_turma() 
            elif escolha_turmas == 3:
                editar_turma() 
            elif escolha_turmas == 4:
                desativar_turma()
            elif escolha_turmas == 5:
                deletar_turma()
            elif escolha_turmas == 7:
                imprimir_turma()
            else:
                print("Opção inválida. Tente novamente.")

def salvar_turma():
    print("\nCadastro de Turma:")
    id = input('Digite o id da turma: ')
    nome = input("Digite o nome da turma: ")
    segmento = input("Segmento da turma (EM ou Superior): ").upper()


    if segmento not in ["EM", "SUPERIOR"]:
        print("Segmento inválido. Por favor, escolha entre 'EM' (Ensino Médio) ou 'Superior'.")
        return

    curso = None
    if segmento == "EM":
        print("Cursos disponíveis para Ensino Médio: Mecatrônica, Eletromecânica, Informática")
        curso = input("Digite o curso da turma: ").capitalize()
        if curso not in ["Mecatrônica", "Eletromecânica", "Informática"]:
            print("Curso inválido para Ensino Médio. Operação cancelada.")
            return

    elif segmento == "SUPERIOR":
        print("Cursos disponíveis para Superior: Ciências da Computação, Pedagogia")
        curso = input("Digite o curso da turma: ").capitalize()
        if curso not in ["Ciências da Computação", "Pedagogia"]:
            print("Curso inválido para Superior. Operação cancelada.")
            return

    ano_escolar = input("Digite o ano escolar da turma (ex: 2024, 2025): ")


    print("Informe os alunos da turma (Digite 'fim' para encerrar):")
    alunos = []
    while True:
        ra_aluno = input("Digite o RA do aluno: ")
        if ra_aluno.lower() == "fim":
            break
        
            # Ler o arquivo e atualizar o estudante correspondente ao RA fornecido
        with open('estudantes.txt', 'r') as arquivo:
            for linha in arquivo:
                dados = linha.strip().split(';')
                aluno_encontrado = False
                if len(dados) > 0 and dados[0] == str(ra_aluno):  # O RA está na posição 8
                    aluno_encontrado = True

                    if aluno_encontrado:
                        if dados[12].upper() != segmento.upper():
                            print(f"O aluno com RA {ra_aluno} não pertence ao segmento {segmento}.")
                        else:
                            alunos.append(dados[0])
                            print(f"Aluno foi adicionado.")
                    else: 
                        print(f"Aluno com RA {ra_aluno} não encontrado.")

    if segmento == "EM" and len(alunos) < 20:
        print("Erro: Uma turma do Ensino Médio deve ter no mínimo 20 alunos. Operação cancelada.")
        return
    elif segmento == "SUPERIOR" and len(alunos) < 5:
        print("Erro: Uma turma do Ensino Superior deve ter no mínimo 5 alunos. Operação cancelada.")
        return

    print("Informe os professores da turma (Digite 'fim' para encerrar):")
    professores = []
    while True:
        id_professor = input("Digite o ID do professor: ")
        if id_professor.lower() == "fim":
            break

        with open('professores.txt', 'r') as arquivo:
            for linha in arquivo:
                dados = linha.strip().split(';')
                professor_encontrado = False
                if len(dados) > 0 and dados[0] == str(id_professor):  
                    professor_encontrado = True
                
                    if professor_encontrado:
                        print(f"Professor adicionado.")
                        professores.append(dados[0])

                    else:
                        print(f"Professor com ID {id_professor} não encontrado.")

    if not professores:
        print("Erro: É necessário adicionar ao menos um professor para a turma. Operação cancelada.")
        return

    print("Informe as disciplinas da turma (Digite 'fim' para encerrar):")
    disciplinas = []
    while True:
        id_disciplina = input("Digite o ID da disciplina: ")
        if id_disciplina.lower() == "fim":
            break

        with open('disciplinas.txt', 'r') as arquivo:
            for linha in arquivo:
                dados = linha.strip().split(';')
                disciplina_encontrada = False

                if len(dados) > 0 and dados[0] == str(id_disciplina): 
                    disciplina_encontrada = True
                    

                    if disciplina_encontrada:
                        if dados[2].upper() != segmento.upper():
                            print(f"A disciplina {dados[0]} não pertence ao segmento {segmento}.")
                        else:
                            print(f"Disciplina adicionada.")
                            disciplinas.append(dados[0])

                    else:
                        print(f"Disciplina com ID {id_disciplina} não encontrada.")

    if not disciplinas:
        print("Erro: É necessário adicionar ao menos uma disciplina para a turma. Operação cancelada.")
        return

    # Criar a turma
    turma = Turma(id, nome, segmento, curso, ano_escolar, alunos, professores, disciplinas)
    turma.salvar_turma()
    print(f"Turma '{nome}' cadastrada com sucesso!")

def editar_turma():
    print("\nEdição de Turma:")
    id_turma = input("Digite o ID da turma que deseja editar: ")
    
    
    turmas = carregar_turmas()
    
    turma_encontrada = None
    for turma in turmas:
        if turma.id == id_turma:
            turma_encontrada = turma
            break
            
    print("Deixe os campos vazios caso não queira alterá-los.")
    if turma_encontrada:
        novo_nome = input("Digite o novo nome da turma: (enter caso não mude) ")
        if novo_nome == "":
            novo_nome = None

        novo_segmento = input("Digite o novo segmento da turma (EM/SUPERIOR): (enter caso não mude) ")
        if novo_segmento == "":
            novo_segmento = None

        novo_curso = input("Digite o novo curso da turma: (enter caso não mude) ")
        if novo_curso == "":
            novo_curso = None

        novo_ano = input("Digite o novo ano da turma: (enter caso não mude) ")
        if novo_ano == "":
            novo_ano = None

        continuar = False
        while continuar != True:
            novos_alunos = input("Digite os novos IDs de alunos separados por vírgula: (enter caso não mude) ")
            if novos_alunos == "":
                alunos = None
                continuar = True
            else:
                estudantes = carregar_estudantes()
                novos_alunos = novos_alunos.strip().split(",")
                for aluno in novos_alunos:
                    if aluno not in estudantes:
                        print(f'Aluno com ID {aluno} não encontrado')
                        deuerrado = True
                        continue
                if deuerrado:
                    continue
                alunos = f"['{novos_alunos[0]}'"
                for i in range(len(novos_alunos)-1):
                    alunos += f",'{novos_alunos[i+1]}'"
                alunos += ']'
                if alunos:
                    continuar = True

        continuar = False
        while continuar != True:
            novo_professor = input("Digite os novos IDs de professores separados por vírgula: (enter caso não mude) ")
            if novo_professor == "":
                professores = None
                continuar = True
            else:
                profs = carregar_professor()
                novo_professor = novo_professor.strip().split(",")
                for prof in novo_professor:
                    if prof not in profs:
                        print(f'Professor com ID {prof} não encontrado')
                        deuerrado = True
                        continue
                if deuerrado:
                    continue
                professores = f"['{novo_professor[0]}'"
                for i in range(len(novo_professor)-1):
                    professores += f",'{novo_professor[i+1]}'"
                professores += ']'
                if professores:
                    continuar = True


        continuar = False
        while continuar != True:
            novas_disciplinas = input("Digite os novos IDs de disciplinas separados por vírgula: (enter caso não mude) ")
            if novas_disciplinas == "":
                disciplinas = None
                continuar = True
            else:
                materias = carregar_disciplina()
                novas_disciplinas = novas_disciplinas.strip().split(",")
                for materia in novas_disciplinas:
                    if materia not in materias:
                        print(f'Disciplina com ID {materia} não encontrado')
                        deuerrado = True
                        continue
                if deuerrado:
                    continue
                disciplinas = f"['{novas_disciplinas[0]}'"
                for i in range(len(novas_disciplinas) - 1):
                    disciplinas += f",'{novas_disciplinas[i+1]}'"
                disciplinas += ']'
                if disciplinas:
                    continuar = True


        turma_encontrada.editar_turma(turma.id,novo_nome, novo_segmento, novo_curso, novo_ano, alunos, professores,disciplinas)

def desativar_turma():
    print("\nDesativar Turma:")
    id_turma = input("Digite o ID da turma que deseja desativar: ")
    
    turmas = carregar_turmas()
    
    turma_encontrada = None
    for turma in turmas:
        if turma.id == id_turma:
            turma_encontrada = turma
            break

    if turma_encontrada:
        turma_encontrada.desativar_turma(id_turma)

def deletar_turma():
    print("\nDeletar Turma:")
    id_turma = input("Digite o ID da turma que deseja deletar: ")
    
    turmas = carregar_turmas()
    
    turma_encontrada = None
    for turma in turmas:
        if turma.id == id_turma:
            turma_encontrada = turma
            break

    if turma_encontrada:
        turma_encontrada.deletar_turma()

def imprimir_turma():
    print("\nImprimir Turma:")
    id_turma = input("Digite o ID da turma que deseja imprimir: ")
    
    turmas = carregar_turmas()
    
    turma_encontrada = None
    for turma in turmas:
        if turma.id == id_turma:
            turma_encontrada = turma
            break

    if turma_encontrada:
        turma_encontrada.imprimir_turma()

menu_principal()