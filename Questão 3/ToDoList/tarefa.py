from datetime import datetime

class Tarefa:
    def __init__(self, titulo, prazo):
        self.titulo = titulo
        self.status = "A Fazer"
        self.prazo = prazo