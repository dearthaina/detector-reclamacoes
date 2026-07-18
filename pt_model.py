import sys
import subprocess
import spacy

try:
    # Tenta carregar o modelo normalmente
    spacy.load("pt_core_news_sm")
except OSError:
    # Se não encontrar, força a instalação diretamente via pip usando a URL do pacote pré-compilado
    print("Modelo 'pt_core_news_sm' não encontrado. Baixando...")
    subprocess.check_call([
        sys.executable, "-m", "pip", "install", 
        "https://github.com/explosion/spacy-models/releases/download/pt_core_news_sm-3.7.0/pt_core_news_sm-3.7.0-py3-none-any.whl"
    ])
    print("Modelo instalado com sucesso!")
