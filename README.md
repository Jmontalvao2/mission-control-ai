# Mission Control AI 

Sistema Inteligente de Monitoramento de Missão Espacial desenvolvido em Python.

---

## Sobre o Projeto

O **Mission Control AI** simula o monitoramento de uma missão espacial experimental chamada **Nova Frontier X1**, desenvolvida pela **Equipe Nebula**.

O sistema analisa 6 ciclos de monitoramento da missão, verificando automaticamente os dados de cada ciclo, gerando alertas, calculando o nível de risco e exibindo um relatório final completo no terminal.

---

## Integrantes

| Nome | RM |
|------|----|
| Laura Pícari dos Santos Costa | RM: 569914 |
| Gabriela Caetano Campos| RM: 572738 |
| João Victor Montalvão Correia | RM: 571630 |

---

## Dados da Missão

| Campo | Valor |
|-------|-------|
| Nome da missão | Nova Frontier X1 |
| Nome da equipe | AstroTech |
| Ciclos analisados | 6 |

---

## Áreas Monitoradas

Cada ciclo analisa 5 áreas da missão, nesta ordem:

| Posição | Área | Unidade |
|---------|------|---------|
| 0 | Temperatura interna | °C |
| 1 | Comunicação com a base | % |
| 2 | Sistema de energia (Bateria) | % |
| 3 | Suporte de oxigênio | % |
| 4 | Estabilidade operacional | % |

---

## Regras de Alerta

### Temperatura
| Condição | Classificação |
|----------|---------------|
| Menor que 18 °C | ATENÇÃO |
| De 18 °C até 30 °C | NORMAL |
| De 31 °C até 35 °C | ATENÇÃO |
| Maior que 35 °C | CRÍTICO |

### Comunicação
| Condição | Classificação |
|----------|---------------|
| Menor que 30% | CRÍTICO |
| De 30% até 59% | ATENÇÃO |
| 60% ou mais | NORMAL |

### Bateria
| Condição | Classificação |
|----------|---------------|
| Menor que 20% | CRÍTICO |
| De 20% até 49% | ATENÇÃO |
| 50% ou mais | NORMAL |

### Oxigênio
| Condição | Classificação |
|----------|---------------|
| Menor que 80% | CRÍTICO |
| De 80% até 89% | ATENÇÃO |
| 90% ou mais | NORMAL |

### Estabilidade
| Condição | Classificação |
|----------|---------------|
| Menor que 40% | CRÍTICO |
| De 40% até 69% | ATENÇÃO |
| 70% ou mais | NORMAL |

---

## Pontuação de Risco

| Classificação | Pontos |
|---------------|--------|
| NORMAL | 0 ponto |
| ATENÇÃO | 1 ponto |
| CRÍTICO | 2 pontos |

### Classificação do Ciclo

| Pontuação total | Classificação |
|-----------------|---------------|
| 0 a 2 pontos | MISSÃO ESTÁVEL |
| 3 a 5 pontos | MISSÃO EM ATENÇÃO |
| 6 a 10 pontos | MISSÃO CRÍTICA |

---

## Funções do Sistema

O sistema possui 10 funções:

- `analisar_temperatura()` — analisa a temperatura do módulo
- `analisar_comunicacao()` — analisa a qualidade do sinal
- `analisar_bateria()` — analisa o nível de bateria
- `analisar_oxigenio()` — analisa o nível de oxigênio
- `analisar_estabilidade()` — analisa a estabilidade dos sistemas
- `classificar_ciclo()` — classifica o ciclo com base na pontuação
- `gerar_recomendacao()` — gera recomendação automática para o ciclo
- `analisar_tendencia()` — compara o primeiro e último ciclo para identificar tendência
- `identificar_area_mais_afetada()` — identifica a área com maior risco acumulado
- `gerar_relatorio_final()` — exibe o relatório completo da missão

---

##  Como executar

1. Certifique-se de ter o **Python 3** instalado
2. Clone este repositório ou baixe o arquivo `mission_control.py`
3. No terminal, execute:

```bash
python mission_control.py
```

4. O sistema irá analisar automaticamente os 6 ciclos da missão e exibir o relatório final.

---


---

## Informações Acadêmicas

- **Curso:** Ciências da computação — FIAP
- **Disciplina:** Pensamento Computacional e Automação com Python
- **Semestre:** 1º Semestre — 2026
