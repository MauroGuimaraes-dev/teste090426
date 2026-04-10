"""
Robô de teste — verifica se a home da Claro responde HTTP 200.

O Agent clona este repositório e executa este ficheiro (stdlib apenas).
"""
from __future__ import annotations

import sys
import urllib.error
import urllib.request

# URL de teste (home institucional)
URL_CLARO = "https://www.claro.com.br/"


def main() -> None:
    # User-Agent: alguns sites bloqueiam pedido sem navegador “de verdade”
    pedido = urllib.request.Request(
        URL_CLARO,
        headers={"User-Agent": "OrquestradorClaro-RPA-Test/1.0"},
        method="GET",
    )
    try:
        with urllib.request.urlopen(pedido, timeout=30) as resposta:
            codigo = resposta.getcode()
    except urllib.error.HTTPError as e:
        print(f"ERRO HTTP: {e.code} — {e.reason}")
        sys.exit(1)
    except urllib.error.URLError as e:
        print(f"ERRO de rede/URL: {e.reason}")
        sys.exit(1)
    except OSError as e:
        print(f"ERRO ao acessar o site: {e}")
        sys.exit(1)

    if codigo != 200:
        print(f"ERRO: status inesperado {codigo}")
        sys.exit(1)

    print(f"OK — {URL_CLARO} respondeu HTTP 200")
    sys.exit(0)


if __name__ == "__main__":
    main()
