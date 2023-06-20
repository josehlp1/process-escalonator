import tkinter as tk
from process_manager import ProcessManager
from disk_emulator import DiskEmulator
from mmu import MMU
from cpu import CPU
import random
import threading

ESPACO_MAXIMO_FILE_SIZE = 100
manager = ProcessManager()
disk_emulator = DiskEmulator(1000)
mmu = MMU(256)
cpu = CPU(8)
waiting_queue = []


def create_process():
    try:
        priority = int(priority_entry.get())
    except ValueError:
        priority = random.randint(1, 10)

    priority_entry.delete(0, tk.END)
    process_id = manager.create_process(priority)
    listbox.insert(tk.END, f'Processo {process_id} de prioridade {priority} criado.')


def execute_process_thread():
    execute_button.config(state='disabled', text='Executando')
    threading.Thread(target=execute_process).start()


def execute_process():
    try:
        process = manager.execute_process()
        if process:
            file_size = random.randint(1, ESPACO_MAXIMO_FILE_SIZE)
            if file_size > disk_emulator.available_space:
                listbox.insert(tk.END,
                               f'Erro: Processo {process.id} de prioridade {process.priority} não pode ser executado. Tamanho do arquivo ({file_size}) excede o espaço disponível no disco ({disk_emulator.available_space}).')
                waiting_queue.append(process)
            else:
                process.use_disk(disk_emulator, file_size)
                process.use_mmu(mmu, random.randint(0, mmu.memory_capacity))
                process.use_cpu(cpu)
                listbox.insert(tk.END, '')
                listbox.insert(tk.END, f'Processo {process.id} de prioridade {process.priority} iniciado. Tamanho: {file_size}')
                listbox.insert(tk.END, f'Processo {process.id} de prioridade {process.priority} concluído.')
                listbox.insert(tk.END, f'Métrica de Disco: {process.disk_usage}')
                listbox.insert(tk.END, f'Métrica de MMU: {process.mmu_usage}')
                listbox.insert(tk.END, f'Métrica de CPU: {process.cpu_usage}')
        else:
            listbox.insert(tk.END, '')
            listbox.insert(tk.END, 'Nenhum processo na fila para execução.')

        execute_waiting_processes()
    finally:
        enable_execute_buttons()


def execute_all_processes_thread():
    execute_all_button.config(state='disabled', text='Executando')
    threading.Thread(target=execute_all_processes).start()


def execute_all_processes():
    try:
        process = manager.execute_process()
        while process:
            file_size = random.randint(1, ESPACO_MAXIMO_FILE_SIZE)
            if file_size > disk_emulator.available_space:
                listbox.insert(tk.END,
                               f'Erro: Processo {process.id} de prioridade {process.priority} não pode ser executado. Tamanho do arquivo ({file_size}) excede o espaço disponível no disco ({disk_emulator.available_space}).')
                waiting_queue.append(process)
            else:
                process.use_disk(disk_emulator, file_size)
                process.use_mmu(mmu, random.randint(0, mmu.memory_capacity))
                process.use_cpu(cpu)
                listbox.insert(tk.END, '')
                listbox.insert(tk.END, f'Processo {process.id} de prioridade {process.priority} iniciado. Tamanho: {file_size}')
                listbox.insert(tk.END, f'Processo {process.id} de prioridade {process.priority} concluído.')
                listbox.insert(tk.END, f'Métrica de Disco: {process.disk_usage}')
                listbox.insert(tk.END, f'Métrica de MMU: {process.mmu_usage}')
                listbox.insert(tk.END, f'Métrica de CPU: {process.cpu_usage}')

            process = manager.execute_process()

        execute_waiting_processes()
    finally:
        enable_execute_buttons()


def get_available_space():
    space_label[
        'text'] = f"Espaço disponível no disco: {disk_emulator.get_available_space()}/{disk_emulator.disk_space}"


def clean_disk():
    disk_emulator.clean_disk()
    space_label[
        'text'] = f"Espaço disponível no disco: {disk_emulator.get_available_space()}/{disk_emulator.disk_space}"
    listbox.insert(tk.END, "Disco limpo. Todo o espaço está disponível novamente.")
    execute_waiting_processes()


def execute_waiting_processes():
    while waiting_queue:
        process = waiting_queue.pop(0)
        file_size = random.randint(1, ESPACO_MAXIMO_FILE_SIZE)
        if file_size > disk_emulator.available_space:
            listbox.insert(tk.END,
                           f'Erro: Processo {process.id} de prioridade {process.priority} não pode ser executado. Tamanho do arquivo ({file_size}) excede o espaço disponível no disco ({disk_emulator.available_space}).')
            waiting_queue.append(process)
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

    space_label[
        'text'] = f"Espaço disponível no disco: {disk_emulator.get_available_space()}/{disk_emulator.disk_space}"


def enable_execute_buttons():
    execute_button.config(state='normal', text='Executar Processo')
    execute_all_button.config(state='normal', text='Executar Todos')


window = tk.Tk()
window.title("Simulação de Gerenciamento de Processos")

window.geometry("1000x800")

priority_label = tk.Label(window, text="Prioridade:", font=('Arial', 14))
priority_label.pack(pady=10)
priority_entry = tk.Entry(window, font=('Arial', 14))
priority_entry.pack(pady=10)

add_button = tk.Button(window, text="Criar Processo", command=create_process, height=2, width=30,
                       font=('Arial', 14))
add_button.pack(pady=10)

execute_button = tk.Button(window, text="Executar Processo", command=execute_process_thread, height=2, width=30,
                           font=('Arial', 14))
execute_button.pack(pady=10)

execute_all_button = tk.Button(window, text="Executar Todos", command=execute_all_processes, height=2, width=30,
                               font=('Arial', 14))
execute_all_button.pack(pady=10)

space_label = tk.Label(window, text="Espaço disponível no disco: {}/{}".format(disk_emulator.get_available_space(),
                                                                               disk_emulator.disk_space),
                       font=('Arial', 14))
space_label.pack(pady=10)

get_space_button = tk.Button(window, text="Ver Espaço Disponível", command=get_available_space, height=2, width=30,
                             font=('Arial', 14))
get_space_button.pack(pady=10)

clean_disk_button = tk.Button(window, text="Limpar Disco", command=clean_disk, height=2, width=30,
                              font=('Arial', 14))
clean_disk_button.pack(pady=10)

listbox = tk.Listbox(window, width=100, height=20, font=('Arial', 14))
listbox.pack(pady=10)

window.mainloop()
