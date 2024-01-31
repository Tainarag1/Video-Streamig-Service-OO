
class Usuario:
    def __init__(self, id, email, senha):
        self.id = id
        self.email = email
        self.senha = senha


class Aula:
    def __init__(self, id, url_aula, titulo):
        self.id = id
        self.url_aula = url_aula
        self.titulo = titulo


class Plano:
    def __init__(self, id, valor, titulo, descricao):
        self.id = id
        self.valor = valor
        self.titulo = titulo
        self.descricao = descricao


class Categoria:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome


class Aula_Categoria:
    def __init__(self, Categoria_id, Aula_id):
        self.Categoria_id = Categoria_id
        self.Aula_id = Aula_id


class Usuario_aula:
    def __init__(self, usuario_id, aula_id):
        self.usuario_id = usuario_id
        self.aula_id = aula_id

class Categoria_plano:
    def __init__(self, plano_id, categoria_id):
        self.plano_id = plano_id
        self.categoria_id = categoria_id


class Usuario_plano:
    def __init__(self, id_plano, id_usuario):
        self.id_plano = id_plano
        self.id_usuario = id_usuario