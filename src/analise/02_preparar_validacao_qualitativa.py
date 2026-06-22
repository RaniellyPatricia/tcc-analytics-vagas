import pandas as pd
from pathlib import Path


PASTA_PROJETO = Path(__file__).resolve().parents[2]

CAMINHO_ENTRADA = (
    PASTA_PROJETO
    / "data"
    / "samples"
    / "programathor_amostra_45_vagas.csv"
)

df = pd.read_csv(CAMINHO_ENTRADA)

print("Base carregada com sucesso!")
print("Quantidade de linhas:", len(df))
print("Quantidade de colunas:", len(df.columns))

#vagas sem erro 
df_validas = df[df['erro'].isna()].copy()

#vgasd indisponiveis

df_com_erro = df[df['erro'].notna()].copy()

print("\nSeparação da base:") 
print("Vagas válidas:", len(df_validas)) 
print("Vagas com erro:", len(df_com_erro))

quantidade_amostra = 8

amostra = df_validas.sample(n=quantidade_amostra, random_state=42).copy()

print("\nAmostra selecionada:")
print("quantidade de vagas na amostra:", len(amostra))
print(amostra[['titulo', 'empresa', 'url']].to_string(index=False))

# Mantém apenas os campos que serão conferidos manualmente.
colunas_validacao = [
    "titulo",
    "empresa",
    "contrato",
    "modalidade",
    "localizacao",
    "senioridade",
    "skills",
    "atividades",
    "requisitos",
    "url",
]

amostra = amostra[colunas_validacao].reset_index(drop=True)

# Cria um identificador simples para cada vaga.
amostra.insert(
    0,
    "id_validacao",
    range(1, len(amostra) + 1)
)

print("\nTabela preparada para validação:")

print(
    amostra[
        [
            "id_validacao",
            "titulo",
            "empresa",
            "modalidade",
            "senioridade",
        ]
    ].to_string(index=False)
)

# Cria as colunas de conferência manual.
amostra["titulo_confere"] = ""
amostra["empresa_confere"] = ""
amostra["contrato_confere"] = ""
amostra["modalidade_confere"] = ""
amostra["localizacao_confere"] = ""
amostra["senioridade_confere"] = ""
amostra["skills_conferem"] = ""
amostra["atividades_conferem"] = ""
amostra["requisitos_conferem"] = ""
amostra["observacoes"] = ""

CAMINHO_SAIDA = (
    PASTA_PROJETO
    / "data"
    / "samples"
    / "validacao_qualitativa_8_vagas.csv"
)

CAMINHO_SAIDA = (
    PASTA_PROJETO
    / "data"
    / "samples"
    / "validacao_qualitativa_8_vagas.csv"
)
amostra.to_csv(
    CAMINHO_SAIDA,
    index=False,
    encoding="utf-8-sig"
)

print("\nArquivo de validação criado com sucesso!")
print("Arquivo salvo em:")
print(CAMINHO_SAIDA)