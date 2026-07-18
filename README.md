# 🔍 Detector Automático de Reclamações

## 📝 Introdução
Este é um aplicativo web interativo desenvolvido em Python que processa mensagens enviadas por clientes para triagem de atendimento. O sistema analisa o texto estrututuralmente de forma automatizada para descobrir se o consumidor está manifestando alguma insatisfação com o serviço ou produto oferecido.

## 🎯 Objetivo
O principal objetivo do projeto é automatizar a identificação de reclamações utilizando técnicas de Processamento de Linguagem Natural (PLN). Através da normalização do texto (remoção de pontuações, conversão para letras minúsculas) e análise de lematização (redução das palavras à sua forma base), o sistema consegue detectar com precisão termos negativos como "ruim", "erro", "péssimo" e variações associadas, simplificando o fluxo de monitoramento de suporte.

## 🛠️ Bibliotecas Utilizadas
* **Python** (Linguagem base do projeto)
* **Streamlit** (Criação e renderização da interface gráfica web do app)
* **spaCy** (Processamento de Linguagem Natural com o modelo pré-treinado em português `pt_core_news_sm`)

## 🚀 Como Executar o Projeto

### 1. Preparar os Arquivos
Certifique-se de que os arquivos do seu projeto estão na mesma pasta do seu computador:
* `app.py` (Código principal com o aplicativo Streamlit)
* `requirements.txt` (Arquivo contendo as dependências de instalação)

### 2. Instalar as Dependências
Abra o seu Terminal ou Prompt de Comando (CMD) dentro da pasta onde os arquivos estão salvos e execute o seguinte comando:
```bash
pip install -r requirements.txt
