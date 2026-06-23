# TCC — Analytics Acadêmico com Vagas, Egressos e Aderência Curricular

Projeto de Trabalho de Conclusão de Curso voltado ao desenvolvimento de uma proposta de Analytics Acadêmico para apoiar a coordenação do curso de Sistemas de Informação.

A proposta geral é analisar a relação entre:

* competências exigidas pelo mercado de trabalho;
* trajetória profissional dos egressos;
* competências previstas no Projeto Pedagógico do Curso e na matriz curricular.

O projeto está sendo desenvolvido em etapas. A fase atual concentra-se na coleta, organização, validação, preparação textual e classificação de anúncios de vagas de tecnologia publicados no Brasil.

---

## Objetivo do projeto

Desenvolver um estudo aplicado capaz de comparar as demandas do mercado de trabalho com a formação acadêmica e a trajetória profissional dos egressos.

Os resultados deverão apoiar a coordenação do curso por meio de indicadores relacionados a:

* áreas profissionais mais demandadas;
* competências técnicas;
* competências comportamentais;
* tecnologias mencionadas nas vagas;
* trajetória profissional dos egressos;
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

O uso de Machine Learning será realizado somente após a construção de uma base rotulada com quantidade, diversidade e qualidade suficientes para uma avaliação minimamente defensável.

---

## Fonte de dados testada

A primeira fonte utilizada foi a ProgramaThor:

`https://www.programathor.com.br/jobs`

A coleta foi realizada por meio de scripts em Python, utilizando requisições HTTP e extração de informações do HTML.

Inicialmente, foram analisadas as três primeiras páginas da listagem para validar:

* acesso à plataforma;
* funcionamento da paginação;
* extração dos campos;
* tratamento de erros;
* armazenamento em CSV;
* qualidade estrutural dos dados.

Posteriormente, foi realizado um teste de extensão da paginação nas primeiras 50 páginas.

Esse teste identificou 748 URLs únicas. Como a página 50 ainda apresentava anúncios novos, a última página real da plataforma não foi determinada.

Por questão de escopo e viabilidade, a coleta detalhada foi ampliada de forma controlada para as primeiras 20 páginas.

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

A coleta-piloto foi utilizada para validar o fluxo completo antes da ampliação da base.

---

## Teste de extensão da paginação

Foi realizado um teste nas primeiras 50 páginas da ProgramaThor para avaliar o volume de anúncios disponível.

| Indicador                        | Resultado |
| -------------------------------- | --------: |
| Páginas testadas                 |        50 |
| URLs únicas encontradas          |       748 |
| Página 50 apresentou vagas novas |       Sim |
| Última página real identificada  |       Não |

O teste foi encerrado pelo limite de segurança definido no script, e não pela ausência de novos anúncios.

Portanto, é possível afirmar apenas que, no momento do teste, a plataforma possuía pelo menos 50 páginas acessíveis e 748 URLs únicas nas páginas examinadas.

Esse resultado representa um recorte temporal, pois os anúncios podem ser publicados, alterados ou removidos ao longo do tempo.

---

## Coleta ampliada de 20 páginas

Após a validação da coleta-piloto, foi realizada uma coleta detalhada das primeiras 20 páginas da ProgramaThor.

| Indicador                        | Resultado |
| -------------------------------- | --------: |
| Páginas percorridas              |        20 |
| URLs únicas encontradas          |       298 |
| Vagas coletadas com sucesso      |       296 |
| Vagas indisponíveis              |         2 |
| URLs duplicadas                  |         0 |
| Taxa de sucesso                  |    99,33% |
| Salários não especificados       |       173 |
| Percentual sem salário informado |    58,45% |

As duas vagas indisponíveis retornaram erro HTTP 500 da própria plataforma.

As ocorrências foram preservadas no arquivo original contendo:

* URL;
* data de coleta;
* fonte;
* mensagem de erro.

Os demais campos permaneceram vazios porque o conteúdo dos anúncios não estava disponível.

Os registros com erro não foram utilizados na base processada.

---

## Validação da coleta

A qualidade da coleta foi avaliada por meio de validação estrutural e conferência manual.

### Validação estrutural da coleta-piloto

Foram verificados:

* quantidade de registros;
* quantidade de colunas;
* valores vazios;
* URLs duplicadas;
* mensagens de erro;
* tamanho dos textos;
* salários não especificados;
* taxa de sucesso.

Nas 42 vagas válidas da coleta-piloto não foram identificados problemas estruturais.

### Validação qualitativa da coleta-piloto

Foi selecionada uma amostra reproduzível de oito vagas utilizando:

`random_state=42`

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

A coluna `skills` representa apenas as etiquetas disponibilizadas pela plataforma. Outras competências aparecem nos textos de atividades e requisitos.

### Validação estrutural da coleta ampliada

A base de 298 URLs também foi submetida à validação estrutural.

Resultados:

* 296 vagas válidas;
* 2 vagas indisponíveis;
* 0 URLs duplicadas;
* 0 campos obrigatórios vazios nas vagas válidas;
* taxa de sucesso de 99,33%;
* 173 vagas sem salário especificado.

Quatro anúncios apresentaram requisitos com menos de 50 caracteres.

As páginas originais foram verificadas manualmente e confirmou-se que os textos eram realmente curtos. Portanto, esses registros foram mantidos como válidos.

O limite de 50 caracteres foi utilizado apenas como alerta para conferência, e não como regra automática de exclusão.

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

## Base textual processada

As 296 vagas válidas da coleta ampliada foram preparadas para as etapas de análise, extração de competências e classificação.

O processamento incluiu:

* remoção dos registros com erro;
* verificação de URLs duplicadas;
* padronização de espaços;
* padronização de quebras de linha e tabulações;
* criação da coluna `skills_plataforma`;
* criação da coluna `texto_analise`;
* criação da coluna `tamanho_texto_analise`;
* remoção das colunas redundantes `skills` e `erro`;
* reorganização do índice.

O campo `texto_analise` foi formado pela combinação de:

```text
titulo + skills_plataforma + atividades + requisitos
```

Resultados da base processada:

| Indicador              |                        Resultado |
| ---------------------- | -------------------------------: |
| Vagas processadas      |                              296 |
| Colunas                |                               18 |
| URLs duplicadas        |                                0 |
| Menor texto de análise |                   151 caracteres |
| Tamanho médio          | aproximadamente 1.533 caracteres |
| Maior texto de análise |                 4.954 caracteres |

Arquivo gerado:

`data/processed/programathor_vagas_processadas_20_paginas.csv`

---

## Estrutura do projeto

```text
TCC-analytics-vagas/
├── data/
│   ├── processed/
│   │   ├── programathor_vagas_processadas.csv
│   │   └── programathor_vagas_processadas_20_paginas.csv
│   ├── raw/
│   └── samples/
│       ├── programathor_amostra_15_vagas.csv
│       ├── programathor_amostra_45_vagas.csv
│       ├── programathor_coleta_20_paginas.csv
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
│   │   ├── 02_preparar_validacao_qualitativa.py
│   │   └── 03_validar_coleta_ampliada_programathor.py
│   ├── coleta/
│   │   ├── 01_teste_acesso_programathor.py
│   │   ├── 02_coletar_amostra_programathor.py
│   │   ├── 03_teste_paginacao_programathor.py
│   │   ├── 04_coletar_multiplas_paginas_programathor.py
│   │   ├── 05_descobrir_ultima_pagina_programathor.py
│   │   └── 06_coletar_amostra_ampliada_programathor.py
│   └── limpeza/
│       ├── 01_preparar_base_textual.py
│       └── 02_preparar_base_ampliada.py
├── .gitignore
├── README.md
└── requirements.txt
```

As pastas `data/raw`, `notebooks` e `outputs` poderão permanecer vazias enquanto suas respectivas etapas não forem iniciadas.

As pastas `data/processed` e `src/limpeza` já são utilizadas na preparação das bases textuais.

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

### `05_descobrir_ultima_pagina_programathor.py`

Percorre sucessivamente as páginas da listagem e compara os links encontrados com as URLs já identificadas.

O script é encerrado quando:

* uma página não apresenta vagas;
* uma página contém apenas URLs já vistas;
* ocorre um erro de acesso;
* o limite de segurança é alcançado.

No teste realizado, foram percorridas 50 páginas e identificadas 748 URLs únicas.

A última página real da plataforma não foi alcançada.

---

### `06_coletar_amostra_ampliada_programathor.py`

Realiza a coleta detalhada das primeiras 20 páginas da ProgramaThor.

O script:

* reúne os links das páginas;
* remove URLs repetidas;
* acessa cada anúncio;
* extrai os campos estruturados;
* registra falhas;
* mantém intervalo entre as requisições;
* salva a base ampliada em CSV.

---

### `01_validar_base_programathor.py`

Realiza a validação estrutural da coleta-piloto.

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

### `03_validar_coleta_ampliada_programathor.py`

Valida a base de 298 URLs da coleta ampliada.

Verifica:

* quantidade de vagas válidas;
* registros indisponíveis;
* valores vazios;
* URLs duplicadas;
* salários não especificados;
* requisitos curtos;
* taxa de sucesso.

---

### `01_preparar_base_textual.py`

Prepara a base-piloto de 42 vagas válidas.

O script:

* remove registros com erro;
* verifica duplicidades;
* padroniza os textos;
* cria `skills_plataforma`;
* cria `texto_analise`;
* calcula o tamanho dos textos;
* salva a base processada.

---

### `02_preparar_base_ampliada.py`

Prepara as 296 vagas válidas da coleta ampliada.

O script:

* remove registros com erro;
* remove possíveis duplicidades;
* padroniza os textos;
* cria `skills_plataforma`;
* cria `texto_analise`;
* calcula o tamanho dos textos;
* salva a base processada com 18 colunas.

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

### Testar a paginação inicial

```powershell
python src/coleta/03_teste_paginacao_programathor.py
```

### Coletar as três primeiras páginas

```powershell
python src/coleta/04_coletar_multiplas_paginas_programathor.py
```

### Testar a extensão da paginação

```powershell
python src/coleta/05_descobrir_ultima_pagina_programathor.py
```

### Realizar a coleta ampliada

```powershell
python src/coleta/06_coletar_amostra_ampliada_programathor.py
```

### Validar a coleta-piloto

```powershell
python src/analise/01_validar_base_programathor.py
```

### Preparar a validação qualitativa

```powershell
python src/analise/02_preparar_validacao_qualitativa.py
```

### Validar a coleta ampliada

```powershell
python src/analise/03_validar_coleta_ampliada_programathor.py
```

### Preparar a base-piloto

```powershell
python src/limpeza/01_preparar_base_textual.py
```

### Preparar a base ampliada

```powershell
python src/limpeza/02_preparar_base_ampliada.py
```

---

## Atenção sobre a reprodução dos dados

Os anúncios disponíveis na plataforma podem mudar ao longo do tempo.

Uma nova execução pode produzir resultados diferentes das bases armazenadas no projeto porque:

* novas vagas podem ser publicadas;
* anúncios podem ser removidos;
* anúncios podem mudar de posição entre as páginas;
* páginas individuais podem ficar indisponíveis;
* campos do site podem ser modificados.

O script de preparação da validação qualitativa recria o arquivo:

`data/samples/validacao_qualitativa_8_vagas.csv`

Após o preenchimento manual, ele não deve ser executado novamente sem a criação de uma cópia de segurança.

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

A coluna `skills_plataforma` contém apenas as etiquetas apresentadas pela ProgramaThor.

A extração completa de competências deverá considerar:

* título;
* skills da plataforma;
* atividades;
* requisitos.

Foi criado o campo:

```text
texto_analise = titulo + skills_plataforma + atividades + requisitos
```

Esse texto será utilizado em:

* análise de frequência;
* construção de um dicionário de competências;
* mineração de texto;
* TF-IDF;
* classificação de vagas.

---

## Limitações atuais

A etapa atual possui as seguintes limitações:

* utilização de uma única plataforma;
* coleta detalhada restrita às primeiras 20 páginas;
* última página real da ProgramaThor ainda não identificada;
* possibilidade de alteração ou remoção dos anúncios;
* existência de páginas listadas, mas indisponíveis;
* possível viés relacionado ao perfil de vagas da ProgramaThor;
* validação qualitativa restrita a oito vagas;
* ausência de uma base completamente rotulada;
* distribuição das categorias ainda não avaliada;
* competências textuais ainda não extraídas;
* viabilidade do Machine Learning ainda dependente da quantidade de exemplos por categoria;
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

Os resultados da ProgramaThor não representam automaticamente todo o mercado brasileiro de tecnologia.

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
* teste de paginação das três primeiras páginas;
* coleta-piloto de 45 URLs;
* identificação de 42 vagas válidas;
* validação estrutural da coleta-piloto;
* validação qualitativa de oito vagas;
* preparação da base textual de 42 vagas;
* teste de extensão em 50 páginas;
* identificação de 748 URLs únicas no teste de extensão;
* coleta detalhada das primeiras 20 páginas;
* coleta de 298 URLs únicas;
* identificação de 296 vagas válidas;
* validação estrutural da coleta ampliada;
* preparação da base textual ampliada;
* criação do campo `texto_analise`;
* atualização do diário de coleta;
* documentação dos scripts.

---

## Próximas etapas

* criar o guia de rotulagem das vagas;
* definir formalmente as categorias;
* selecionar uma amostra inicial para rotulagem manual;
* analisar casos ambíguos;
* avaliar a distribuição das categorias;
* decidir se as categorias possuem exemplos suficientes;
* extrair competências técnicas e comportamentais;
* construir um dicionário de competências;
* realizar análise exploratória;
* testar uma classificação simples por regras;
* avaliar posteriormente a viabilidade de um modelo supervisionado;
* integrar dados de egressos;
* analisar o PPC e a matriz curricular;
* desenvolver indicadores e dashboard em Power BI.
