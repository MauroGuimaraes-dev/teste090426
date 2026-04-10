"""
Robô de teste — verifica a home da Claro (HTTP 200) e depois permanece ativo por 5 minutos.

O Agent clona este repositório e executa este arquivo (stdlib apenas).
timeout_segundos no agendamento deve ser >= 360 (ex.: 3600).
"""
from __future__ import annotations

import sys
import time
import urllib.error
import urllib.request

# URL de teste (home institucional)
URL_CLARO = "https://www.claro.com.br/"

# Fase extra: manter o processo vivo para testar timeout / logs no dashboard
DURACAO_EXTRA_SEG = 5 * 60  # 5 minutos
INTERVALO_LOG_SEG = 30    # a cada 30s um print (aparece nos logs da execução)


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
    print(
        f"Iniciando espera de {DURACAO_EXTRA_SEG // 60} minutos "
        f"(logs a cada {INTERVALO_LOG_SEG}s). Ajuste DURACAO_EXTRA_SEG no código se quiser."
    )

    fim = time.monotonic() + DURACAO_EXTRA_SEG
    passo = 0
    while time.monotonic() < fim:
        dormir = min(INTERVALO_LOG_SEG, fim - time.monotonic())
        if dormir <= 0:
            break
        time.sleep(dormir)
        passo += 1
        restante = max(0, int(fim - time.monotonic()))
        print(f"Ainda em execução… passo {passo} — ~{restante}s restantes")

    print("Espera de 5 minutos concluída. Encerrando com sucesso.")
    sys.exit(0)


if __name__ == "__main__":
    main()
