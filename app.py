import streamlit as block_st
import spacy

block_st.set_page_config(page_title="Detector de Reclamações", page_icon="🔍")

@block_st.cache_resource
def carregar_modelo():
    return spacy.load("pt_core_news_sm")

nlp = carregar_modelo()

# Lista de termos em minúsculo e sem pontuação
TERMOS_RECLAMACAO = {"ruim", "erro", "pessimo", "horrivel", "falha", "defeito", "pior", "problema"}

def limpar_e_verificar(mensagem):
    doc = nlp(mensagem.lower())
    
    # Filtra o texto removendo as pontuações e espaços extras
    palavras_limpas = [token.lemma_ for token in doc if not token.is_punct and not token.is_space]
    
    # Verifica se algum termo de reclamação está nas palavras limpas
    for palavra in palavras_limpas:
        if palavra in TERMOS_RECLAMACAO:
            return True, palavras_limpas
            
    return False, palavras_limpas

# --- INTERFACE DO STREAMLIT ---

block_st.title("🔍 Detector Automático de Reclamações")
block_st.markdown("Digite ou cole a mensagem do cliente abaixo para analisar se ela contém termos de reclamação.")

# Campo de texto para o usuário digitar
mensagem_cliente = block_st.text_area(
    "Mensagem do Cliente:", 
    placeholder="Ex: O produto... veio com um ERRO péssimo!!"
)

# Botão para executar a análise
if block_st.button("Analisar Mensagem"):
    if mensagem_cliente.strip() != "":
        e_reclamacao, _ = limpar_e_verificar(mensagem_cliente) # Ignora o retorno da lista usando '_'
        
        block_st.subheader("Resultados da Análise")
        
        # Exibe apenas o veredito com caixas coloridas
        if e_reclamacao:
            block_st.error("🚨 **Status:** Esta mensagem foi classificada como uma **Reclamação**!")
        else:
            block_st.success("✅ **Status:** Mensagem **Normal** (Nenhuma reclamação detectada).")
    else:
        block_st.warning("⚠️ Por favor, digite alguma mensagem antes de analisar.")
