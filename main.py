import tkinter as tk
from process_manager import ProcessManager
from disk_emulator import DiskEmulator
from mmu import MMU
from cpu import CPU
import random

manager = ProcessManager()
disk_emulator = DiskEmulator(1000)
mmu = MMU(256)
cpu = CPU(8)

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
        file_size = random.randint(1, disk_emulator.disk_space)  # Valor aleatório dentro do espaço total do disco
        if file_size > disk_emulator.available_space:
            listbox.insert(tk.END, f'Erro: Processo {process.id} de prioridade {process.priority} não pode ser executado. Tamanho do arquivo ({file_size}) excede o espaço disponível no disco ({disk_emulator.available_space}).')
        else:
            process.use_disk(disk_emulator, file_size)
            process.use_mmu(mmu, random.randint(0, mmu.memory_capacity))
            process.use_cpu(cpu)
            listbox.insert(tk.END, '')
            listbox.insert(tk.END, f'Processo {process.id} de prioridade {process.priority} iniciado.')
            listbox.insert(tk.END, f'Processo {process.id} de prioridade {process.priority} concluído.')
            listbox.insert(tk.END, f'Métrica de Disco: {process.disk_usage}')
            listbox.insert(tk.END, f'Métrica de MMU: {process.mmu_usage}')
            listbox.insert(tk.END, f'Métrica de CPU: {process.cpu_usage}')
    else:
        listbox.insert(tk.END, '')
        listbox.insert(tk.END, 'Nenhum processo na fila para execução.')


def execute_all_processes():
    process = manager.execute_process()
    while process:
        file_size = random.randint(1, disk_emulator.disk_space)  # Valor aleatório dentro do espaço total do disco
        if file_size > disk_emulator.available_space:
            listbox.insert(tk.END, f'Erro: Processo {process.id} de prioridade {process.priority} não pode ser executado. Tamanho do arquivo ({file_size}) excede o espaço disponível no disco ({disk_emulator.available_space}).')
        else:
            process.use_disk(disk_emulator, file_size)
            process.use_mmu(mmu, random.randint(0, mmu.memory_capacity))
            process.use_cpu(cpu)
            listbox.insert(tk.END, '')
            listbox.insert(tk.END, f'Processo {process.id} de prioridade {process.priority} iniciado.')
            listbox.insert(tk.END, f'Processo {process.id} de prioridade {process.priority} concluído.')
            listbox.insert(tk.END, f'Métrica de Disco: {process.disk_usage}')
            listbox.insert(tk.END, f'Métrica de MMU: {process.mmu_usage}')
            listbox.insert(tk.END, f'Métrica de CPU: {process.cpu_usage}')

        process = manager.execute_process()



window = tk.Tk()
window.title("Simulação de Gerenciamento de Processos")

window.geometry("800x600")

priority_label = tk.Label(window, text="Prioridade:", font=('Arial', 14))
priority_label.pack(pady=10)
priority_entry = tk.Entry(window, font=('Arial', 14))
priority_entry.pack(pady=10)

add_button = tk.Button(window, text="Criar Processo", command=create_process, height=2, width=30,
                       font=('Arial', 14))
add_button.pack(pady=10)

execute_button = tk.Button(window, text="Executar Processo", command=execute_process, height=2, width=30,
                           font=('Arial', 14))
execute_button.pack(pady=10)

execute_all_button = tk.Button(window, text="Executar Todos", command=execute_all_processes, height=2, width=30,
                               font=('Arial', 14))
execute_all_button.pack(pady=10)

listbox = tk.Listbox(window, width=100, height=20, font=('Arial', 14))
listbox.pack(pady=10)

window.mainloop()
