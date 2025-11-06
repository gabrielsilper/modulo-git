import re
"""
Desafio Módulo Git

Neste arquivo você encontrará funções **incompletas** que representam
tarefas relacionadas ao aprendizado de Git e GitHub.

Seu objetivo é:
- Criar uma issue para cada função.
- Implementar a função em uma branch específica.
- Fazer commit, criar tag e abrir Pull Request.
- Repetir o processo até concluir todas as funções.

Boa sorte e bons commits! 🚀
"""

def mostrar_mensagem_inicial():
    return "Bem-vindo ao Desafio de Git!"


def listar_comandos_git_basicos():
    return [
        "git init",
        "git add <file>",
        "git status",
        "git push -u origin <branch>",
        "git push",
        "git log",
        "git reflog",
        "git checkout <branch>",
        "git merge <branch>",
    ]


def criar_mensagem_commit(funcao_nome):
    return f"feat: Implementa função {funcao_nome}"


def verificar_tag_valida(tag):
    """
    Verifica se uma tag está no formato 'vX.Y.Z' (ex: v1.0.1, v2.1.23).
    Retorna True se o formato for válido, caso contrário False.
    """
    tag_pattern = re.compile(r"^v\d+\.\d+\.\d+$")
    return re.fullmatch(tag_pattern, tag) is not None


def gerar_relatorio_final(funcoes_concluidas):
    """
    Recebe uma lista com os nomes das funções implementadas
    e retorna uma mensagem final do desafio.

    Exemplo:
    gerar_relatorio_final(["mostrar_mensagem_inicial", "listar_comandos_git_basicos"])
    ->
    "Desafio concluído! 2 funções implementadas com sucesso."
    """
    return f"Desafio concluído! {len(funcoes_concluidas)} funções implementadas com sucesso."
