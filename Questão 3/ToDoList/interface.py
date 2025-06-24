import ttkbootstrap as ttkb
from ttkbootstrap.constants import *
from tkinter import messagebox
from tarefa import Tarefa
from datetime import datetime

class AppToDo:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tarefas")
        self.root.geometry("550x500")
        self.tarefas = []
        self.setup_ui()

    def setup_ui(self):
        ttkb.Label(self.root, text="Título da Tarefa:", font=('Segoe UI', 12, 'bold')).pack(pady=5)
        self.entrada = ttkb.Entry(self.root, width=50, font=('Segoe UI', 12), bootstyle="info")
        self.entrada.pack(pady=5)

        ttkb.Label(self.root, text="Prazo (dd/mm/aaaa):", font=('Segoe UI', 12, 'bold')).pack(pady=5)
        self.prazo = ttkb.Entry(self.root, width=20, font=('Segoe UI', 12), bootstyle="info")
        self.prazo.pack(pady=5)

        ttkb.Button(self.root, text="Adicionar", command=self.adicionar_tarefa, bootstyle="success-outline").pack(pady=5)

        self.tree = ttkb.Treeview(self.root, columns=("Título", "Status", "Prazo"), show="headings", bootstyle="info")
        self.tree.heading("Título", text="Título")
        self.tree.heading("Status", text="Status")
        self.tree.heading("Prazo", text="Prazo")
        self.tree.column("Título", width=250)
        self.tree.column("Status", width=100)
        self.tree.column("Prazo", width=120)
        self.tree.pack(pady=10)

        frame_botoes = ttkb.Frame(self.root)
        frame_botoes.pack(pady=5)

        ttkb.Button(frame_botoes, text="Executando", command=lambda: self.mudar_status("Executando"), bootstyle="warning-outline").pack(side=LEFT, padx=5)
        ttkb.Button(frame_botoes, text="Pronta", command=lambda: self.mudar_status("Pronta"), bootstyle="success-outline").pack(side=LEFT, padx=5)
        ttkb.Button(frame_botoes, text="Excluir", command=self.excluir_tarefa, bootstyle="danger-outline").pack(side=LEFT, padx=5)

    def adicionar_tarefa(self):
        titulo = self.entrada.get().strip()
        prazo_str = self.prazo.get().strip()

        if not titulo:
            messagebox.showwarning("Aviso", "O título da tarefa não pode estar vazio.")
            return
        if len(titulo) > 80:
            messagebox.showwarning("Aviso", "O título não pode exceder 80 caracteres.")
            return
        try:
            datetime.strptime(prazo_str, "%d/%m/%Y")
        except ValueError:
            messagebox.showwarning("Aviso", "Formato de data inválido. Use dd/mm/aaaa.")
            return

        tarefa = Tarefa(titulo, prazo_str)
        self.tarefas.append(tarefa)
        self.tree.insert("", ttkb.END, values=(tarefa.titulo, tarefa.status, tarefa.prazo))
        self.entrada.delete(0, ttkb.END)
        self.prazo.delete(0, ttkb.END)

    def contar_executando(self):
        return sum(1 for t in self.tarefas if t.status == "Executando")

    def mudar_status(self, novo_status):
        selecionado = self.tree.selection()
        if not selecionado:
            messagebox.showwarning("Aviso", "Selecione uma tarefa para mudar o status.")
            return

        for item in selecionado:
            titulo, _, prazo = self.tree.item(item, "values")
            tarefa = next((t for t in self.tarefas if t.titulo == titulo and t.prazo == prazo), None)
            if tarefa:
                if novo_status == "Executando" and tarefa.status != "Executando":
                    if self.contar_executando() >= 10:
                        messagebox.showwarning("Aviso", "Limite de 10 tarefas em 'Executando' atingido.")
                        return
                tarefa.status = novo_status
                self.tree.item(item, values=(tarefa.titulo, tarefa.status, tarefa.prazo))

    def excluir_tarefa(self):
        selecionado = self.tree.selection()
        if not selecionado:
            messagebox.showwarning("Aviso", "Selecione uma tarefa para excluir.")
            return

        for item in selecionado:
            titulo, _, prazo = self.tree.item(item, "values")
            self.tarefas = [t for t in self.tarefas if not (t.titulo == titulo and t.prazo == prazo)]
            self.tree.delete(item)
