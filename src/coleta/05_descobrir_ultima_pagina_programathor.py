import re
import time
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup


# Endereço principal da plataforma.
BASE_URL = "https://www.programathor.com.br"

# Endereço da listagem de vagas.
LIST_URL = "https://www.programathor.com.br/jobs"

# Limite máximo de páginas que o script poderá testar.
# Essa configuração evita uma repetição infinita.
MAX_PAGINAS_TESTE = 50

# Pausa entre os acessos às páginas.
TEMPO_ENTRE_REQUISICOES = 2

# Identifica a requisição como proveniente de um navegador.
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/125.0 Safari/537.36"
    )
}


def montar_url_pagina(numero_pagina):
    """
    Monta o endereço correspondente ao número da página.

    A primeira página não precisa do parâmetro ?page=1.
    """

    if numero_pagina == 1:
        return LIST_URL

    return f"{LIST_URL}?page={numero_pagina}"


def baixar_html(url):
    """
    Acessa uma página e devolve seu conteúdo HTML.
    """

    response = requests.get(
        url,
        headers=HEADERS,
        timeout=30
    )

    # Gera uma exceção em respostas como 404 ou 500.
    response.raise_for_status()

    return response.text


def extrair_links_vagas(html):
    """
    Localiza os links únicos de vagas presentes no HTML.
    """

    # Transforma o HTML em uma estrutura pesquisável.
    soup = BeautifulSoup(
        html,
        "lxml"
    )

    # Procura todos os elementos de link que possuem href.
    elementos_link = soup.find_all(
        "a",
        href=True
    )

    links_vagas = []

    for elemento in elementos_link:
        # Obtém o endereço do link.
        href = elemento["href"]

        # Verifica se o endereço segue o padrão /jobs/número.
        if re.search(r"/jobs/\d+", href):
            # Converte um endereço relativo em endereço completo.
            url_completa = urljoin(
                BASE_URL,
                href
            )

            # Remove possíveis parâmetros existentes após ?.
            url_completa = url_completa.split("?")[0]

            links_vagas.append(url_completa)

    # Remove links duplicados e preserva a ordem original.
    links_vagas = list(
        dict.fromkeys(links_vagas)
    )

    return links_vagas


def main():
    """
    Percorre as páginas até encontrar uma página sem vagas novas.
    """

    # O set armazena URLs únicas e não aceita repetições.
    links_vistos = set()

    # Guarda o número da última página que apresentou vagas novas.
    ultima_pagina_valida = 0

    # Testa as páginas de 1 até o limite configurado.
    for pagina in range(
        1,
        MAX_PAGINAS_TESTE + 1
    ):
        url_pagina = montar_url_pagina(
            pagina
        )

        print("\n" + "=" * 60)
        print("Testando página:", pagina)
        print("URL:", url_pagina)

        try:
            html = baixar_html(
                url_pagina
            )

            links_pagina = extrair_links_vagas(
                html
            )

        except requests.RequestException as erro:
            print("Erro ao acessar a página:")
            print(erro)

            print("A busca será encerrada.")
            break

        quantidade_links = len(
            links_pagina
        )

        # Converte os links atuais para set e remove os já vistos.
        links_novos = (
            set(links_pagina)
            - links_vistos
        )

        print(
            "Links encontrados:",
            quantidade_links
        )

        print(
            "Links novos:",
            len(links_novos)
        )

        # Para quando a página não possui links de vagas.
        if quantidade_links == 0:
            print("A página não possui vagas.")
            print("A busca será encerrada.")
            break

        # Para quando a página repete somente vagas já encontradas.
        if len(links_novos) == 0:
            print(
                "A página não apresentou vagas novas."
            )
            print(
                "A paginação provavelmente terminou."
            )
            break

        # Esta página apresentou pelo menos uma vaga nova.
        ultima_pagina_valida = pagina

        # Adiciona os links atuais ao conjunto geral.
        links_vistos.update(
            links_pagina
        )

        print(
            "Total de links únicos acumulados:",
            len(links_vistos)
        )

        # Aguarda antes de acessar a próxima página.
        time.sleep(
            TEMPO_ENTRE_REQUISICOES
        )

    print("\n" + "=" * 60)
    print("RESUMO DO TESTE")
    print("=" * 60)

    print(
        "Última página válida encontrada:",
        ultima_pagina_valida
    )

    print(
        "Total de URLs únicas encontradas:",
        len(links_vistos)
    )


if __name__ == "__main__":
    main()