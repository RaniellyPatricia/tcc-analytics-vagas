# TCC — Analytics Acadêmico com Vagas, Egressos e Aderência Curricular

Projeto de Trabalho de Conclusão de Curso voltado ao desenvolvimento de uma proposta de Analytics Acadêmico para apoiar a coordenação do curso de Sistemas de Informação.

A proposta geral é analisar a relação entre:

* competências exigidas pelo mercado de trabalho;
* trajetória profissional dos egressos;
* competências previstas no Projeto Pedagógico do Curso e na matriz curricular.

O projeto está sendo desenvolvido em etapas. A fase atual concentra-se na coleta, organização, validação e análise de anúncios de vagas de tecnologia publicados no Brasil.

---

## Objetivo do projeto

Desenvolver um estudo aplicado capaz de comparar as demandas do mercado de trabalho com a formação acadêmica e a trajetória profissional dos egressos.

Os resultados deverão apoiar a coordenação do curso por meio de indicadores relacionados a:

* áreas profissionais mais demandadas;
* competências técnicas;
* competências comportamentais;
* tecnologias mencionadas nas vagas;
* trajetória dos egressos;
* aderência entre currículo e mercado;
* possíveis oportunidades de atualização curricular.

---

## Resultados esperados

Entre os resultados previstos estão:

* base estruturada de vagas de tecnologia;
* análise exploratória dos anúncios;
* classificação das vagas por área de atuação;
* extração de competências;
* análise de dados públicos de egressos;
* análise das competências previstas no currículo;
* comparação entre mercado, formação e trajetória profissional;
* dashboard em Power BI.

---

## Escopo atual

A primeira etapa prática está focada na análise de vagas de tecnologia.

As atividades desta fase incluem:

1. testar uma fonte de vagas;
2. coletar anúncios com descrição completa;
3. estruturar os dados;
4. validar os campos extraídos;
5. limpar e preparar os textos;
6. definir categorias de classificação;
7. criar uma estratégia de rotulagem manual;
8. testar métodos simples de classificação;
9. avaliar métricas;
10. extrair competências dos anúncios.

O uso de Machine Learning será realizado somente após a construção de uma base rotulada com quantidade e qualidade suficientes para uma avaliação minimamente defensável.

---

## Fonte de dados testada

A primeira fonte utilizada foi a ProgramaThor:

`https://www.programathor.com.br/jobs`

A coleta foi realizada por meio de scripts em Python, utilizando requisições HTTP e extração de informações do HTML.

Até o momento, foram analisadas as três primeiras páginas da listagem.

A quantidade total de páginas disponíveis na plataforma ainda não foi determinada.

---

## Resultados da coleta-piloto

A coleta das três primeiras páginas apresentou os seguintes resultados:

| Indicador                        | Resultado |
| -------------------------------- | --------: |
| Páginas analisadas               |         3 |
| URLs encontradas                 |        45 |
| Vagas coletadas com sucesso      |        42 |
| Vagas indisponíveis              |         3 |
| URLs duplicadas                  |         0 |
| Taxa de sucesso                  |    93,33% |
| Salários não especificados       |        20 |
| Percentual sem salário divulgado |    47,62% |

As três vagas indisponíveis retornaram erro HTTP 500.

As respectivas URLs também foram testadas manualmente no navegador e permaneceram inacessíveis, indicando falha na própria fonte.

Os resultados representam apenas a amostra coletada e não devem ser generalizados para todo o mercado brasileiro de tecnologia.

---

## Validação da coleta

A qualidade da coleta foi avaliada em duas etapas.

### Validação estrutural

Foram verificados:

* quantidade de registros;
* quantidade de colunas;
* valores vazios;
* URLs duplicadas;
* mensagens de erro;
* tamanho dos textos;
* salários não especificados;
* taxa de sucesso.

Nas 42 vagas válidas não foram identificados problemas estruturais.

### Validação qualitativa

Foi selecionada uma amostra reproduzível de oito vagas utilizando `random_state=42`.

Os campos armazenados foram comparados manualmente com as páginas originais dos anúncios.

Foram conferidos:

* título;
* empresa;
* contrato;
* modalidade;
* localização;
* senioridade;
* skills;
* atividades;
* requisitos.

Não foram observadas divergências relevantes na amostra conferida.

A coluna `skills` representa somente as etiquetas disponibilizadas pela plataforma. Outras competências presentes nos textos serão extraídas em uma etapa posterior.

---

## Campos coletados

Cada anúncio pode conter os seguintes campos:

* fonte;
* data da coleta;
* título;
* empresa;
* tamanho da empresa;
* contrato;
* modalidade;
* localização;
* salário;
* senioridade;
* skills;
* descrição da empresa;
* atividades;
* requisitos;
* texto completo;
* URL;
* mensagem de erro.

---

## Estrutura do projeto

```text
TCC-analytics-vagas/
├── data/
│   ├── processed/
│   ├── raw/
│   └── samples/
│       ├── programathor_amostra_15_vagas.csv
│       ├── programathor_amostra_45_vagas.csv
│       └── validacao_qualitativa_8_vagas.csv
├── docs/
│   └── diario_coleta.md
├── notebooks/
├── outputs/
│   ├── graficos/
│   └── tabelas/
├── src/
│   ├── analise/
│   │   ├── 01_validar_base_programathor.py
│   │   └── 02_preparar_validacao_qualitativa.py
│   ├── coleta/
│   │   ├── 01_teste_acesso_programathor.py
│   │   ├── 02_coletar_amostra_programathor.py
│   │   ├── 03_teste_paginacao_programathor.py
│   │   └── 04_coletar_multiplas_paginas_programathor.py
│   └── limpeza/
├── .gitignore
├── README.md
└── requirements.txt
```

As pastas `data/processed`, `data/raw`, `notebooks`, `outputs` e `src/limpeza` ainda poderão estar vazias enquanto suas respectivas etapas não forem iniciadas.

---

## Descrição dos scripts

### `01_teste_acesso_programathor.py`

Testa o acesso à página principal da ProgramaThor.

Apresenta:

* código HTTP;
* tamanho do HTML recebido.

---

### `02_coletar_amostra_programathor.py`

Coleta uma amostra inicial de 15 vagas presentes na primeira página da plataforma.

A amostra foi utilizada para testar:

* estrutura dos anúncios;
* campos disponíveis;
* regras de extração;
* exportação para CSV.

---

### `03_teste_paginacao_programathor.py`

Testa as páginas 1, 2 e 3 da listagem.

Verifica:

* quantidade de links encontrados;
* diferença entre as páginas;
* existência de URLs repetidas;
* funcionamento do parâmetro de paginação.

---

### `04_coletar_multiplas_paginas_programathor.py`

Percorre as três primeiras páginas, reúne os links únicos e coleta os dados individuais dos anúncios.

O script:

* remove URLs duplicadas;
* mantém intervalo entre requisições;
* registra mensagens de erro;
* preserva URLs indisponíveis;
* exporta os dados para CSV.

---

### `01_validar_base_programathor.py`

Realiza a validação estrutural da base ampliada.

Verifica:

* quantidade de registros;
* quantidade de colunas;
* valores vazios;
* URLs duplicadas;
* salários não especificados;
* tamanho dos textos;
* vagas indisponíveis;
* taxa de sucesso.

---

### `02_preparar_validacao_qualitativa.py`

Seleciona uma amostra reproduzível de oito vagas válidas e gera uma tabela para conferência manual.

A comparação considera:

* título;
* empresa;
* contrato;
* modalidade;
* localização;
* senioridade;
* skills;
* atividades;
* requisitos.

---

## Preparação do ambiente

### 1. Clonar o repositório

```powershell
git clone https://github.com/RaniellyPatricia/tcc-analytics-vagas.git
```

### 2. Entrar na pasta do projeto

```powershell
cd tcc-analytics-vagas
```

### 3. Criar o ambiente virtual

```powershell
python -m venv venv
```

### 4. Ativar o ambiente virtual

```powershell
.\venv\Scripts\Activate.ps1
```

Quando o ambiente estiver ativo, o terminal deverá apresentar:

```text
(venv)
```

### 5. Instalar as dependências

```powershell
python -m pip install -r requirements.txt
```

---

## Execução dos scripts

Os comandos devem ser executados a partir da pasta principal do projeto.

### Testar o acesso

```powershell
python src/coleta/01_teste_acesso_programathor.py
```

### Coletar a amostra inicial

```powershell
python src/coleta/02_coletar_amostra_programathor.py
```

### Testar a paginação

```powershell
python src/coleta/03_teste_paginacao_programathor.py
```

### Coletar múltiplas páginas

```powershell
python src/coleta/04_coletar_multiplas_paginas_programathor.py
```

### Validar a base coletada

```powershell
python src/analise/01_validar_base_programathor.py
```

### Preparar a validação qualitativa

```powershell
python src/analise/02_preparar_validacao_qualitativa.py
```

### Atenção

O script de preparação da validação qualitativa recria o arquivo:

`data/samples/validacao_qualitativa_8_vagas.csv`

Após o preenchimento manual, ele não deve ser executado novamente sem que seja criada uma cópia de segurança, pois as respostas poderão ser substituídas.

Os anúncios disponíveis na plataforma podem mudar ao longo do tempo. Dessa forma, novas execuções podem produzir resultados diferentes da amostra armazenada.

---

## Dependências atuais

As principais bibliotecas utilizadas diretamente são:

* `beautifulsoup4`;
* `lxml`;
* `pandas`;
* `requests`.

As demais dependências estão registradas em:

`requirements.txt`

Para atualizar o arquivo após a instalação de uma nova biblioteca:

```powershell
python -m pip freeze > requirements.txt
```

---

## Tecnologias utilizadas

* Python;
* pandas;
* requests;
* Beautiful Soup;
* lxml;
* Git;
* GitHub;
* Visual Studio Code.

Tecnologias que poderão ser incorporadas posteriormente:

* scikit-learn;
* TF-IDF;
* matplotlib;
* Power BI;
* técnicas de mineração de texto.

---

## Categorias iniciais de classificação

As categorias preliminares consideradas são:

* Desenvolvimento;
* Dados, BI e Analytics;
* Sistemas, Negócios e Produto;
* Infraestrutura, Cloud e DevOps;
* QA e Testes;
* Segurança da Informação;
* Suporte Técnico;
* Outros ou Indefinido.

Essas categorias ainda deverão ser transformadas em um protocolo de rotulagem contendo:

* definição de cada categoria;
* critérios de inclusão;
* critérios de exclusão;
* palavras indicativas;
* exemplos;
* regras para casos ambíguos.

---

## Estratégia prevista para competências

A coluna `skills` contém somente as etiquetas apresentadas pela ProgramaThor.

A extração completa de competências deverá considerar:

* título;
* skills da plataforma;
* atividades;
* requisitos.

Posteriormente poderá ser criado um campo como:

```text
texto_analise = titulo + skills + atividades + requisitos
```

Esse texto poderá ser utilizado em:

* análise de frequência;
* dicionário de competências;
* mineração de texto;
* TF-IDF;
* classificação de vagas.

---

## Limitações atuais

A etapa atual possui as seguintes limitações:

* coleta restrita às três primeiras páginas;
* utilização de uma única plataforma;
* quantidade total de páginas ainda desconhecida;
* amostra pequena para treinamento de Machine Learning;
* possibilidade de alteração ou remoção dos anúncios;
* existência de páginas listadas, mas indisponíveis;
* possível viés relacionado ao perfil da ProgramaThor;
* validação qualitativa restrita a oito vagas;
* ausência de uma base rotulada manualmente;
* competências textuais ainda não extraídas;
* ausência de integração com dados de egressos e currículo.

---

## Cuidados metodológicos

Os resultados devem ser interpretados como um recorte da fonte e do período de coleta.

A coleta deve:

* respeitar os limites técnicos da plataforma;
* evitar excesso de requisições;
* registrar datas;
* preservar falhas;
* manter rastreabilidade;
* evitar o preenchimento artificial de dados ausentes.

Nas etapas envolvendo egressos deverão ser considerados:

* princípios éticos;
* finalidade acadêmica;
* utilização responsável de dados públicos;
* minimização de dados pessoais;
* Lei Geral de Proteção de Dados.

---

## Atividades concluídas

* configuração do ambiente;
* organização das pastas;
* criação do repositório Git;
* publicação no GitHub;
* teste de acesso à ProgramaThor;
* coleta inicial de 15 vagas;
* teste de paginação;
* coleta ampliada de 45 URLs;
* identificação de 42 vagas válidas;
* registro de três páginas indisponíveis;
* validação estrutural;
* validação qualitativa de oito vagas;
* criação do diário de coleta;
* documentação dos scripts.

---

## Próximas etapas

* resumir automaticamente a validação qualitativa;
* identificar a última página válida da plataforma;
* verificar duplicidades entre todas as páginas;
* criar uma base processada somente com vagas válidas;
* preparar os textos para análise;
* criar o campo `texto_analise`;
* definir as categorias finais;
* elaborar o guia de rotulagem;
* rotular manualmente uma amostra;
* analisar a distribuição das categorias;
* extrair competências;
* avaliar a viabilidade de um modelo simples;
* integrar posteriormente dados de egressos e currículo.
