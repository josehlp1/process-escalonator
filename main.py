import tkinter as tk
from process_manager import ProcessManager
import random

# Inicializa o gerenciador de processos
manager = ProcessManager()

def create_process():
    try:
        priority = int(priority_entry.get())
    except ValueError:
        priority = random.randint(1, 10)

    priority_entry.delete(0, tk.END)
    process_id = manager.create_process(priority)
    listbox.insert(tk.END, f'Processo {process_id} de prioridade {priority} criado.')

def execute_process():
    process = manager.execute_process()
    if process:
        listbox.insert(tk.END, f'Processo {process.id} de prioridade {process.priority} iniciado.')
        listbox.insert(tk.END, f'Processo {process.id} de prioridade {process.priority} concluído.')
    else:
        listbox.insert(tk.END, 'Nenhum processo na fila para execução.')

def execute_all_processes():
    process = manager.execute_process()
    while process:
        listbox.insert(tk.END, f'Processo {process.id} de prioridade {process.priority} iniciado.')
        listbox.insert(tk.END, f'Processo {process.id} de prioridade {process.priority} concluído.')
        process = manager.execute_process()

# Cria a janela do Tk
window = tk.Tk()
window.title("Simulação de Gerenciamento de Processos")

# Define o tamanho da janela
window.geometry("800x600")

# Cria um campo de entrada para a prioridade do processo
priority_entry = tk.Entry(window, font = ('Arial', 14))
priority_entry.pack(pady=10)

# Cria um botão para adicionar processos
add_button = tk.Button(window, text="Criar Processo", command=create_process, height = 2, width = 30, font = ('Arial', 14))
add_button.pack(pady=10)

# Cria um botão para executar processos
execute_button = tk.Button(window, text="Executar Processo", command=execute_process, height = 2, width = 30, font = ('Arial', 14))
execute_button.pack(pady=10)

# Cria um botão para executar todos os processos
execute_all_button = tk.Button(window, text="Executar Todos", command=execute_all_processes, height = 2, width = 30, font = ('Arial', 14))
execute_all_button.pack(pady=10)

# Cria uma listbox para mostrar a atividade do processo
listbox = tk.Listbox(window, width = 100, height = 20, font = ('Arial', 14))
listbox.pack(pady=10)

# Inicia o loop da janela Tk
window.mainloop()
