import tkinter as tk
from tkinter import font
import requests
import json

# --- Funções Lógicas ---

def get_weather():
    """
    Busca o clima para a cidade inserida e atualiza a interface.
    """
    # IMPORTANTE: Substitua "SUA_API_KEY_AQUI" pela sua chave de API do OpenWeatherMap
    API_KEY = "SUA_API_KEY_AQUI"
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

    city = city_entry.get()

    # Limpa labels de resultado e erro antes de uma nova busca
    clear_labels()

    if not city:
        error_label.config(text="Por favor, digite o nome de uma cidade.")
        return

    if API_KEY == "SUA_API_KEY_AQUI":
        error_label.config(text="Erro: Configure sua API_KEY no código.")
        return

    # Parâmetros da requisição
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric",  # Para Celsius
        "lang": "pt_br"     # Para descrições em português
    }

    try:
        # --- Faz a chamada à API ---
        response = requests.get(BASE_URL, params=params)

        # --- Processa a Resposta ---
        if response.status_code == 200:
            # Converte a resposta JSON em um dicionário Python
            data = response.json()
            
            # Extrai os dados que queremos
            city_name = data.get("name")
            temp = data.get("main", {}).get("temp")
            condition = data.get("weather", [{}])[0].get("description")
            feels_like = data.get("main", {}).get("feels_like")

            # Atualiza as labels na interface
            if city_name:
                location_label.config(text=f"Clima em: {city_name}")
            if temp is not None:
                temp_label.config(text=f"Temperatura: {temp:.1f}°C")
            if feels_like is not None:
                feels_like_label.config(text=f"Sensação: {feels_like:.1f}°C")
            if condition:
                condition_label.config(text=f"Condição: {condition.capitalize()}")

        elif response.status_code == 401:
            # Erro de autenticação (API key errada)
            error_label.config(text="Erro: Chave de API inválida.")
        elif response.status_code == 404:
            # Cidade não encontrada
            error_label.config(text="Cidade não encontrada.")
        else:
            # Outros erros
            error_label.config(text=f"Erro na API: {response.status_code}")

    except requests.exceptions.ConnectionError:
        error_label.config(text="Erro de conexão com a internet.")
    except Exception as e:
        error_label.config(text=f"Ocorreu um erro inesperado: {e}")

def clear_labels():
    """Limpa os textos das labels de resultado e erro."""
    location_label.config(text="")
    temp_label.config(text="")
    feels_like_label.config(text="")
    condition_label.config(text="")
    error_label.config(text="")

# --- Configuração da Interface Gráfica (Tkinter) ---

# Janela principal
root = tk.Tk()
root.title("App de Clima")
root.geometry("400x350") # Largura x Altura
root.configure(bg="#f0f0f0") # Cor de fundo leve

# Define fontes
default_font = font.Font(family="Arial", size=10)
title_font = font.Font(family="Arial", size=12, weight="bold")
result_font = font.Font(family="Arial", size=11, weight="bold")
error_font = font.Font(family="Arial", size=10, weight="bold")

# Frame principal para organizar os widgets
main_frame = tk.Frame(root, bg="#f0f0f0", padx=20, pady=20)
main_frame.pack(expand=True, fill=tk.BOTH)

# --- Seção de Entrada ---
input_frame = tk.Frame(main_frame, bg="#f0f0f0")
input_frame.pack(fill=tk.X, pady=10)

prompt_label = tk.Label(input_frame, text="Digite o nome da cidade:", font=title_font, bg="#f0f0f0")
prompt_label.pack()

city_entry = tk.Entry(input_frame, font=default_font, width=30, relief=tk.SOLID, borderwidth=1)
city_entry.pack(pady=5)

search_button = tk.Button(input_frame, text="Buscar Clima", font=default_font, command=get_weather, 
                          bg="#007bff", fg="white", relief=tk.FLAT, activebackground="#0056b3", activeforeground="white")
search_button.pack(pady=10)

# --- Seção de Resultado ---
result_frame = tk.Frame(main_frame, bg="#ffffff", relief=tk.SOLID, borderwidth=1, padx=15, pady=15)
result_frame.pack(fill=tk.X, pady=10)

location_label = tk.Label(result_frame, text="", font=result_font, bg="#ffffff", anchor="w")
location_label.pack(fill=tk.X, pady=4)

temp_label = tk.Label(result_frame, text="", font=result_font, bg="#ffffff", anchor="w")
temp_label.pack(fill=tk.X, pady=4)

feels_like_label = tk.Label(result_frame, text="", font=result_font, bg="#ffffff", anchor="w")
feels_like_label.pack(fill=tk.X, pady=4)

condition_label = tk.Label(result_frame, text="", font=result_font, bg="#ffffff", anchor="w")
condition_label.pack(fill=tk.X, pady=4)

# --- Label de Erro ---
error_label = tk.Label(main_frame, text="", font=error_font, bg="#f0f0f0", fg="red")
error_label.pack(pady=5)

# Inicia o loop principal da aplicação
root.mainloop()
