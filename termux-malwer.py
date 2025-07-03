import os
import platform
import socket
import requests
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress
import time
import random

console = Console()


BANNER = """
[red]┌─────────────────────────────────────────────────────┐
│ [blink]▓▓▓▓▓▓  MALWARE ANALYZER PRO v9.1  ▓▓▓▓▓▓[/blink]  │
├─────────────────────────────────────────────────────┤
│ [white]ATENÇÃO: Sistema de varredura de vulnerabilidades[/white] │
│ [white]Este software é apenas para fins educacionais[/white]     │
└─────────────────────────────────────────────────────┘[/red]
"""

def get_ip_info():
    """Obtém informações de IP (apenas para demonstração)"""
    try:
        ip = requests.get('https://api.ipify.org').text
        response = requests.get(f'http://ip-api.com/json/{ip}').json()
        return {
            'IP': ip,
            'ISP': response.get('isp', 'Desconhecido'),
            'País': response.get('country', 'Desconhecido'),
            'Região': response.get('regionName', 'Desconhecida'),
            'Cidade': response.get('city', 'Desconhecida'),
            'Provedor': response.get('org', 'Desconhecido')
        }
    except:
        return {'Erro': 'Não foi possível obter informações'}

def get_system_info():
   
    return {
        'Sistema': platform.system(),
        'Nome do PC': platform.node(),
        'Usuário': os.getlogin(),
        'Processador': platform.processor(),
        'Diretório': os.getcwd()
    }

def show_scary_animation():
    
    with Progress() as progress:
        task = progress.add_task("[red]Varrendo sistema...", total=100)
        
        for i in range(100):
            progress.update(task, advance=1, 
                         description=f"[red]Analisando setor {random.randint(1, 256)}...")
            time.sleep(0.03)

def show_scary_message():
   
    messages = [
        "BACKDOOR ENCONTRADO NO SEU SISTEMA!",
        "SEUS DADOS ESTÃO SENDO EXFILTRADOS!",
        "CONEXÃO COM SERVIDOR C2 ESTABELECIDA!",
        "KEYLOGGER ATIVO - TODAS TECLAS MONITORADAS!",
        "RANSOMWARE DETECTADO - SEUS ARQUIVOS SERÃO CRIPTOGRAFADOS!"
    ]
    
    for _ in range(3):
        msg = random.choice(messages)
        console.print(Panel.fit(f"[blink red]{msg}[/blink red]", 
                      border_style="red",
                      title="⚠️ ALERTA DE SEGURANÇA ⚠️"))
        time.sleep(1)

def fake_webcam_capture():
  
    console.print("\n[red]Acessando dispositivos de mídia...[/red]")
    time.sleep(2)
    console.print("[green]Webcam encontrada: [/green]USB2.0 HD UVC WebCam")
    time.sleep(1)
    console.print("[red]Capturando imagem...[/red]")
    time.sleep(2)
    console.print(Panel.fit("[yellow]IMAGEM CAPTURADA COM SUCESSO![/yellow]",
                  border_style="yellow",
                  title="⚠️ WEBCAM ATIVADA ⚠️"))

def main():
    console.print(BANNER)
    time.sleep(2)
    
   
    console.print(Panel.fit("[bold white]INFORMAÇÕES DO SISTEMA[/bold white]"))
    for k, v in get_system_info().items():
        console.print(f"[cyan]{k}:[/cyan] [white]{v}[/white]")
    
    time.sleep(3)
    
   
    console.print("\n[bold white]COLETANDO DADOS DE LOCALIZAÇÃO...[/bold white]")
    show_scary_animation()
    
    ip_info = get_ip_info()
    console.print(Panel.fit("[bold white]DADOS DE LOCALIZAÇÃO[/bold white]"))
    for k, v in ip_info.items():
        console.print(f"[cyan]{k}:[/cyan] [white]{v}[/white]")
    
    time.sleep(3)
    
   
    show_scary_message()
    fake_webcam_capture()
    
 
    console.print(Panel.fit("""
    [blink red]SEU SISTEMA ESTÁ COMPROMETIDO![/blink red]
    
    [white]Este foi apenas um teste de conscientização sobre segurança digital.
    Nenhum dado real foi coletado ou armazenado.[/white]
    """

if __name__ == "__main__":
    main()
