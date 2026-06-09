
nome_missao = "Nova Frontier X1"
nome_equipe = "AstroTech"


dados_missao = [
    [22, 95, 91, 98, 93],  
    [26, 83, 76, 95, 88],  
    [33, 61, 54, 92, 67],  
    [38, 40, 35, 85, 48],  
    [41, 22, 15, 76, 30],  
    [35, 50, 28, 81, 45],  
]

areas_monitoradas = [
    "Temperatura interna",
    "Comunicacao com a base",
    "Sistema de energia",
    "Suporte de oxigenio",
    "Estabilidade operacional",
]



def analisar_temperatura(valor):

    if valor < 18:
        return "ATENCAO", "Temperatura baixa", 1
    elif valor <= 30:
        return "NORMAL", "Temperatura estavel", 0
    elif valor <= 35:
        return "ATENCAO", "Temperatura elevada", 1
    else:
        return "CRITICO", "Risco de superaquecimento", 2


def analisar_comunicacao(valor):

    if valor < 30:
        return "CRITICO", "Comunicacao com a base em nivel critico", 2
    elif valor < 60:
        return "ATENCAO", "Comunicacao instavel", 1
    else:
        return "NORMAL", "Comunicacao estavel", 0


def analisar_bateria(valor):

    if valor < 20:
        return "CRITICO", "Bateria em nivel critico", 2
    elif valor < 50:
        return "ATENCAO", "Bateria abaixo do recomendado", 1
    else:
        return "NORMAL", "Energia estavel", 0


def analisar_oxigenio(valor):

    if valor < 80:
        return "CRITICO", "Oxigenio em nivel critico", 2
    elif valor < 90:
        return "ATENCAO", "Oxigenio abaixo do ideal", 1
    else:
        return "NORMAL", "Oxigenio adequado", 0


def analisar_estabilidade(valor):
  
    if valor < 40:
        return "CRITICO", "Estabilidade operacional critica", 2
    elif valor < 70:
        return "ATENCAO", "Estabilidade operacional reduzida", 1
    else:
        return "NORMAL", "Estabilidade operacional adequada", 0


def classificar_ciclo(pontuacao):
    
    if pontuacao <= 2:
        return "MISSAO ESTAVEL"
    elif pontuacao <= 5:
        return "MISSAO EM ATENCAO"
    else:
        return "MISSAO CRITICA"


def gerar_recomendacao(pontuacao, resultados):
 
    _, _, _, _, _, p_temp, p_com, p_bat, p_oxi, p_est = resultados

    if pontuacao == 0:
        return "Manter operacao normal e continuar monitoramento."
    elif p_bat == 2 and p_com == 2:
        return "Ativar modo de economia de energia e tentar restabelecer contato com a base."
    elif pontuacao >= 6:
        return "Ativar modo de seguranca e priorizar suporte a vida, energia e comunicacao."
    elif p_temp == 2:
        return "Verificar controle termico da missao."
    elif p_com == 2:
        return "Tentar restabelecer contato com a base."
    elif p_bat == 2:
        return "Ativar modo de economia de energia."
    elif p_oxi == 2:
        return "Acionar protocolo de suporte a vida."
    elif p_est == 2:
        return "Reduzir operacoes nao essenciais."
    else:
        return "Monitorar sistemas em atencao e preparar plano de contingencia."


def analisar_tendencia(riscos):
  
    if riscos[-1] > riscos[0]:
        return "A missao apresentou tendencia de piora."
    elif riscos[-1] < riscos[0]:
        return "A missao apresentou tendencia de melhora."
    else:
        return "A missao permaneceu estavel em relacao ao inicio."


def identificar_area_mais_afetada(pontuacao_areas):
    
    maior_pontuacao = max(pontuacao_areas)
    indice = pontuacao_areas.index(maior_pontuacao)
    return areas_monitoradas[indice], maior_pontuacao


def gerar_relatorio_final(riscos, pontuacao_areas, medias):
 
    media_temp, media_com, media_bat, media_oxi, media_est = medias
    ciclo_critico = riscos.index(max(riscos)) + 1
    maior_risco = max(riscos)
    risco_medio = sum(riscos) / len(riscos)
    ciclos_criticos = sum(1 for r in riscos if r >= 6)
    tendencia = analisar_tendencia(riscos)
    area_afetada, _ = identificar_area_mais_afetada(pontuacao_areas)

  
    classificacao_final = classificar_ciclo(round(risco_medio))

    print("=" * 60)
    print("RELATORIO FINAL DA MISSAO")
    print("=" * 60)
    print(f"Missao: {nome_missao}")
    print(f"Equipe: {nome_equipe}")
    print(f"Quantidade de ciclos analisados: {len(dados_missao)}")
    print()
    print(f"Media de temperatura: {media_temp:.2f} C")
    print(f"Media de comunicacao: {media_com:.2f}%")
    print(f"Media de bateria: {media_bat:.2f}%")
    print(f"Media de oxigenio: {media_oxi:.2f}%")
    print(f"Media de estabilidade: {media_est:.2f}%")
    print()
    print(f"Ciclo mais critico: Ciclo {ciclo_critico}")
    print(f"Maior pontuacao de risco: {maior_risco}")
    print(f"Risco medio da missao: {risco_medio:.2f}")
    print(f"Quantidade de ciclos criticos: {ciclos_criticos}")
    print()
    print("Tendencia da missao:")
    print(f"  {tendencia}")
    print()
    print("Pontuacao acumulada por area:")
    for i, area in enumerate(areas_monitoradas):
        print(f"  {area}: {pontuacao_areas[i]} pontos")
    print()
    print("Area mais afetada:")
    print(f"  {area_afetada}")
    print()
    print("Classificacao final da missao:")
    print(f"  {classificacao_final}")
    print()
    print("Conclusao:")

    if classificacao_final == "MISSAO CRITICA":
        print("  A missao atingiu nivel critico durante a operacao.")
        print("  E necessario acionar todos os protocolos de emergencia imediatamente.")
    elif classificacao_final == "MISSAO EM ATENCAO":
        print("  A missao apresentou instabilidade relevante durante a operacao.")
        print("  Apesar da tentativa de recuperacao, ainda existem sistemas em atencao.")
        print("  A equipe deve manter o plano de contingencia ativo.")
    else:
        print("  A missao transcorreu dentro dos parametros normais.")
        print("  Todos os sistemas operaram de forma estavel.")




def main():
    print("=" * 60)
    print("MISSION CONTROL AI")
    print("=" * 60)
    print(f"Missao: {nome_missao}")
    print(f"Equipe: {nome_equipe}")
    print(f"Quantidade de ciclos analisados: {len(dados_missao)}")
    print("=" * 60)

    riscos = []
    pontuacao_areas = [0, 0, 0, 0, 0]
    soma_temp = soma_com = soma_bat = soma_oxi = soma_est = 0

    for i, ciclo in enumerate(dados_missao):
        temperatura, comunicacao, bateria, oxigenio, estabilidade = ciclo

     
        soma_temp += temperatura
        soma_com += comunicacao
        soma_bat += bateria
        soma_oxi += oxigenio
        soma_est += estabilidade

      
        s_temp, m_temp, p_temp = analisar_temperatura(temperatura)
        s_com,  m_com,  p_com  = analisar_comunicacao(comunicacao)
        s_bat,  m_bat,  p_bat  = analisar_bateria(bateria)
        s_oxi,  m_oxi,  p_oxi  = analisar_oxigenio(oxigenio)
        s_est,  m_est,  p_est  = analisar_estabilidade(estabilidade)

        pontuacao = p_temp + p_com + p_bat + p_oxi + p_est
        riscos.append(pontuacao)

      
        pontuacao_areas[0] += p_temp
        pontuacao_areas[1] += p_com
        pontuacao_areas[2] += p_bat
        pontuacao_areas[3] += p_oxi
        pontuacao_areas[4] += p_est

        classificacao = classificar_ciclo(pontuacao)

     
        resultados = (
            s_temp, s_com, s_bat, s_oxi, s_est,
            p_temp, p_com, p_bat, p_oxi, p_est
        )
        recomendacao = gerar_recomendacao(pontuacao, resultados)

        
        print(f"\nCICLO {i + 1}")
        print("-" * 60)
        print(f"Temperatura:  {str(temperatura) + ' C':<9} | {s_temp:<7} | {m_temp}")
        print(f"Comunicacao:  {str(comunicacao) + '%':<9} | {s_com:<7} | {m_com}")
        print(f"Bateria:      {str(bateria) + '%':<9} | {s_bat:<7} | {m_bat}")
        print(f"Oxigenio:     {str(oxigenio) + '%':<9} | {s_oxi:<7} | {m_oxi}")
        print(f"Estabilidade: {str(estabilidade) + '%':<9} | {s_est:<7} | {m_est}")
        print()
        print(f"Pontuacao de risco do ciclo: {pontuacao}")
        print(f"Classificacao do ciclo: {classificacao}")
        print(f"Recomendacao: {recomendacao}")

    
    n = len(dados_missao)
    medias = (
        soma_temp / n,
        soma_com / n,
        soma_bat / n,
        soma_oxi / n,
        soma_est / n,
    )

  
    print()
    gerar_relatorio_final(riscos, pontuacao_areas, medias)


if __name__ == "__main__":
    main()