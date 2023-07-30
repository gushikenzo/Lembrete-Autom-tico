import os
import time
import pyautogui
from datetime import datetime, timedelta, timezone


def horario_brasilia():
    # Obtém o horário atual em Brasília
    agora = datetime.now(timezone(timedelta(hours=-3)))
    return agora


def abrir_bloco_de_notas():
    # Verifica se o sistema operacional é Windows 10 ou 11
    if os.name == 'nt':
        # Caminho para o executável do Bloco de Notas
        bloco_de_notas_path = "C:\\Windows\\System32\\notepad.exe"
        # Abre o Bloco de Notas
        os.startfile(bloco_de_notas_path)
        time.sleep(1)  # espera 1seg
    else:
        print("Este programa suporta apenas Windows 10 e 11.")
        return False


def escrever_no_bloco_de_notas():
    # Escreve o texto no Bloco de Notas usando o pyautogui
    pyautogui.write("AVALIAR AULA")


def verificar_horario_alvo(horario_alvo):
    # Obtém o horário atual em Brasília (UTC-3)
    horario_atual = datetime.utcnow() - timedelta(hours=3)

    # Formata o horário atual para o mesmo formato do horário alvo (HH:MM)
    horario_atual_str = horario_atual.strftime("%H:%M")

    # Verifica se o horário atual é igual ao horário alvo
    if horario_atual_str == horario_alvo:
        return True
    else:
        return False


print(f"Programa iniciado às {horario_brasilia()}")


# Lista de horários desejados para execução (Você pode modificar os horários)
horarios_desejados = ["07:40", "08:25", "09:00", "10:25", "11:10", "11:55", "12:30", "14:10", "14:45", "16:10", "16:45"]

# Pega o dia da semana atual
dia_da_semana = datetime.now().weekday()

while True:
    # Obtém o horário atual em Brasília
    horario_atual = horario_brasilia().strftime("%H:%M")

    '''Verifica se o horário atual está presente na lista de horários desejados. Aqui, você pode modificar os dias em que o lembrete aparecerá utilizando AND, OR ou NOT'''
    if horario_atual in horarios_desejados and (dia_da_semana != 0 and horario_atual != "16:45") and (dia_da_semana != 5 and dia_da_semana != 6):
        abrir_bloco_de_notas()
        escrever_no_bloco_de_notas()

    # Intervalo de espera de 1 minuto (ou o valor desejado)
    time.sleep(60)
