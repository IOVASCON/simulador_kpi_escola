def calcular_kpis(cursos, bootcamps, mentorias, alunos_premium, alunos_gratis, valor_premium, valor_gratis, custos_professores, custos_fixos, receita_mensal, alunos_cancelados, custos_marketing, novos_alunos, tempo_medio_assinatura, alunos_mes_anterior, alunos_mes_atual):
    # Cálculo de KPIs
    total_alunos = alunos_premium + alunos_gratis
    receita_total = (alunos_premium * valor_premium) + (alunos_gratis * valor_gratis)
    custos_totais = custos_professores + custos_fixos + custos_marketing
    lucro = receita_total - custos_totais
    margem_lucro = (lucro / receita_total) * 100 if receita_total != 0 else 0

    # Novas KPIs
    taxa_conversao = (alunos_premium / alunos_gratis) * 100 if alunos_gratis != 0 else 0
    custo_por_aluno = custos_totais / total_alunos if total_alunos != 0 else 0
    receita_por_aluno = receita_total / total_alunos if total_alunos != 0 else 0
    roi = (lucro / custos_totais) * 100 if custos_totais != 0 else 0
    churn_rate = (alunos_cancelados / total_alunos) * 100 if total_alunos != 0 else 0
    ltv = (receita_total / total_alunos) * tempo_medio_assinatura if total_alunos != 0 else 0
    cac = custos_marketing / novos_alunos if novos_alunos != 0 else 0
    crescimento_mensal = ((alunos_mes_atual - alunos_mes_anterior) / alunos_mes_anterior) * 100 if alunos_mes_anterior != 0 else 0

    # Simulação de NPS
    nps_promotores = 60  # 60% promotores
    nps_neutros = 30     # 30% neutros
    nps_detratores = 10  # 10% detratores

    kpis = {
        "total_alunos": total_alunos,
        "receita_total": receita_total,
        "custos_totais": custos_totais,
        "lucro": lucro,
        "margem_lucro": margem_lucro,
        "taxa_conversao": taxa_conversao,
        "custo_por_aluno": custo_por_aluno,
        "receita_por_aluno": receita_por_aluno,
        "roi": roi,
        "churn_rate": churn_rate,
        "ltv": ltv,
        "cac": cac,
        "crescimento_mensal": crescimento_mensal,
        "nps_promotores": nps_promotores,
        "nps_neutros": nps_neutros,
        "nps_detratores": nps_detratores,
        "cursos": cursos,
        "bootcamps": bootcamps,
        "mentorias": mentorias,
        "alunos_premium": alunos_premium,
        "alunos_gratis": alunos_gratis,
        "valor_premium": valor_premium,
        "valor_gratis": valor_gratis,
        "custos_professores": custos_professores,
        "custos_fixos": custos_fixos,
        "receita_mensal": receita_mensal,
        "alunos_cancelados": alunos_cancelados,
        "custos_marketing": custos_marketing,
        "novos_alunos": novos_alunos,
        "tempo_medio_assinatura": tempo_medio_assinatura,
        "alunos_mes_anterior": alunos_mes_anterior,
        "alunos_mes_atual": alunos_mes_atual
    }

    return kpis
