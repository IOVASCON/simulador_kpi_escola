from fpdf import FPDF
import matplotlib.pyplot as plt
import locale

# Configurar o locale para o padrão brasileiro
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

def gerar_relatorio_pdf(kpis):
    # Criar gráficos
    plt.figure(figsize=(15, 10))

    # Gráfico de Pizza: Distribuição de Alunos (Premium vs Grátis)
    plt.subplot(2, 2, 1)
    labels = ["Premium", "Grátis"]
    sizes = [kpis["alunos_premium"], kpis["alunos_gratis"]]
    plt.pie(sizes, labels=labels, autopct="%1.1f%%", colors=["green", "blue"])
    plt.title("Distribuição de Alunos (Premium vs Grátis)")

    # Gráfico de Barras: Receita, Custos e Lucro
    plt.subplot(2, 2, 2)
    categorias = ["Receita", "Custos", "Lucro"]
    valores = [kpis["receita_total"], kpis["custos_totais"], kpis["lucro"]]
    plt.bar(categorias, valores, color=["green", "red", "blue"])
    plt.title("Receita, Custos e Lucro")

    # Gráfico de Linhas: Crescimento Mensal de Alunos
    plt.subplot(2, 2, 3)
    meses = ["Mês Anterior", "Mês Atual"]
    alunos = [kpis["alunos_mes_anterior"], kpis["alunos_mes_atual"]]
    plt.plot(meses, alunos, marker="o", color="purple")
    plt.title("Crescimento Mensal de Alunos")

    # Gráfico de Barras: NPS (Promotores, Neutros, Detratores)
    plt.subplot(2, 2, 4)
    nps_categorias = ["Promotores", "Neutros", "Detratores"]
    nps_valores = [kpis["nps_promotores"], kpis["nps_neutros"], kpis["nps_detratores"]]
    plt.bar(nps_categorias, nps_valores, color=["green", "yellow", "red"])
    plt.title("NPS (Net Promoter Score)")

    plt.tight_layout()
    plt.savefig("graficos.png")

    # Gerar PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Título do Relatório
    pdf.cell(200, 10, txt="Relatório de KPIs - Escola Online", ln=True, align="C")
    pdf.ln(10)

    # Adicionar KPIs ao PDF (formatados em R$)
    pdf.cell(200, 10, txt=f"Total de Alunos: {kpis['total_alunos']}", ln=True)
    pdf.cell(200, 10, txt=f"Receita Total: {locale.currency(kpis['receita_total'], grouping=True)}", ln=True)
    pdf.cell(200, 10, txt=f"Custos Totais: {locale.currency(kpis['custos_totais'], grouping=True)}", ln=True)
    pdf.cell(200, 10, txt=f"Lucro: {locale.currency(kpis['lucro'], grouping=True)}", ln=True)
    pdf.cell(200, 10, txt=f"Margem de Lucro: {kpis['margem_lucro']:.2f}%", ln=True)
    pdf.cell(200, 10, txt=f"Taxa de Conversão: {kpis['taxa_conversao']:.2f}%", ln=True)
    pdf.cell(200, 10, txt=f"Custo por Aluno: {locale.currency(kpis['custo_por_aluno'], grouping=True)}", ln=True)
    pdf.cell(200, 10, txt=f"Receita por Aluno: {locale.currency(kpis['receita_por_aluno'], grouping=True)}", ln=True)
    pdf.cell(200, 10, txt=f"ROI: {kpis['roi']:.2f}%", ln=True)
    pdf.cell(200, 10, txt=f"Churn Rate: {kpis['churn_rate']:.2f}%", ln=True)
    pdf.cell(200, 10, txt=f"LTV: {locale.currency(kpis['ltv'], grouping=True)}", ln=True)
    pdf.cell(200, 10, txt=f"CAC: {locale.currency(kpis['cac'], grouping=True)}", ln=True)
    pdf.cell(200, 10, txt=f"Crescimento Mensal: {kpis['crescimento_mensal']:.2f}%", ln=True)
    pdf.cell(200, 10, txt=f"NPS: Promotores {kpis['nps_promotores']}%, Neutros {kpis['nps_neutros']}%, Detratores {kpis['nps_detratores']}%", ln=True)
    pdf.ln(10)

    # Adicionar gráficos ao PDF
    pdf.image("graficos.png", x=10, y=pdf.get_y(), w=180)

    # Adicionar Anexo com Explicações Dinâmicas
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="ANEXO: Explicação das Fórmulas e Análise dos Resultados", ln=True, align="C")
    pdf.ln(10)

    # Explicação das Fórmulas e Análise dos Resultados
    pdf.set_font("Arial", size=12, style="B")
    pdf.cell(200, 10, txt="1. Explicação das Fórmulas e Resultados", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, txt=f"""
    - Receita Total: A receita total foi de {locale.currency(kpis['receita_total'], grouping=True)}, sendo {locale.currency(kpis['alunos_premium'] * kpis['valor_premium'], grouping=True)} proveniente dos alunos premium e {locale.currency(kpis['alunos_gratis'] * kpis['valor_gratis'], grouping=True)} dos alunos grátis. Isso indica que a escola depende principalmente dos alunos premium para gerar receita.

    - Custos Totais: Os custos totais foram de {locale.currency(kpis['custos_totais'], grouping=True)}, incluindo {locale.currency(kpis['custos_professores'], grouping=True)} com professores, {locale.currency(kpis['custos_fixos'], grouping=True)} com custos fixos e {locale.currency(kpis['custos_marketing'], grouping=True)} com marketing. A escola deve avaliar a eficiência desses custos.

    - Lucro: O lucro foi de {locale.currency(kpis['lucro'], grouping=True)}, resultante da diferença entre a receita total e os custos totais. {"Um lucro positivo indica que a escola está operando com eficiência financeira." if kpis['lucro'] >= 0 else "Um lucro negativo indica que a escola está operando com prejuízo, o que é preocupante."}

    - Margem de Lucro: A margem de lucro foi de {kpis['margem_lucro']:.2f}%. {"Isso é considerado saudável, mas há espaço para melhorias, como a redução de custos ou o aumento da receita." if kpis['margem_lucro'] >= 0 else "Uma margem de lucro negativa indica que a escola está gastando mais do que arrecada, o que é insustentável a longo prazo."}

    - Taxa de Conversão: A taxa de conversão foi de {kpis['taxa_conversao']:.2f}%, indicando que, para cada 5 alunos grátis, 1 se torna premium. A escola pode melhorar essa taxa com estratégias de marketing mais eficazes.

    - Custo por Aluno: O custo por aluno foi de {locale.currency(kpis['custo_por_aluno'], grouping=True)}, o que é {"razoável, mas pode ser otimizado." if kpis['custo_por_aluno'] <= 50 else "alto, indicando que a escola precisa reduzir custos para se tornar mais eficiente."}

    - Receita por Aluno: A receita por aluno foi de {locale.currency(kpis['receita_por_aluno'], grouping=True)}, um valor {"baixo devido ao grande número de alunos grátis. A escola deve focar em aumentar a base de alunos premium." if kpis['receita_por_aluno'] <= 50 else "adequado, mas ainda pode ser melhorado com estratégias de upsell."}

    - ROI: O ROI foi de {kpis['roi']:.2f}%, indicando que a escola está {"gerando um retorno positivo sobre seus investimentos." if kpis['roi'] >= 0 else "operando com um retorno negativo, o que é preocupante."}

    - Churn Rate: O Churn Rate foi de {kpis['churn_rate']:.2f}%, {"considerado baixo. Isso sugere que a maioria dos alunos está satisfeita com os serviços da escola." if kpis['churn_rate'] <= 5 else "considerado alto. Isso sugere que muitos alunos estão cancelando suas assinaturas, o que pode ser um sinal de insatisfação."}

    - LTV: O LTV foi de {locale.currency(kpis['ltv'], grouping=True)}, indicando o valor médio que um aluno gera durante todo o tempo de assinatura. A escola pode aumentar esse valor com estratégias de retenção.

    - CAC: O CAC foi de {locale.currency(kpis['cac'], grouping=True)}, o que é {"aceitável, mas pode ser reduzido com estratégias de marketing mais eficientes." if kpis['cac'] <= 100 else "alto, indicando que a escola está gastando muito para adquirir novos alunos."}

    - Crescimento Mensal: O crescimento mensal foi de {kpis['crescimento_mensal']:.2f}%, indicando uma {"expansão constante da base de alunos." if kpis['crescimento_mensal'] >= 0 else "redução na base de alunos, o que é preocupante."}

    - NPS: O NPS foi de {kpis['nps_promotores'] - kpis['nps_detratores']}, com {kpis['nps_promotores']}% de promotores, {kpis['nps_neutros']}% de neutros e {kpis['nps_detratores']}% de detratores. Isso indica que a maioria dos alunos está satisfeita com a escola.
    """)

    # Parecer Geral do Analista
    pdf.set_font("Arial", size=12, style="B")
    pdf.cell(200, 10, txt="2. Parecer Geral do Analista", ln=True)
    pdf.set_font("Arial", size=12)

    if kpis['lucro'] < 0:
        parecer = f"""
        A escola online está operando com prejuízo de {locale.currency(kpis['lucro'], grouping=True)} e uma margem de lucro negativa de {kpis['margem_lucro']:.2f}%. Isso indica que os custos estão muito altos em relação à receita gerada. Além disso, o Churn Rate de {kpis['churn_rate']:.2f}% sugere que muitos alunos estão cancelando suas assinaturas, o que pode ser um sinal de insatisfação.

        Recomenda-se:
        - Reduzir drasticamente os custos, especialmente com professores e marketing.
        - Revisar a estratégia de preços para aumentar a receita.
        - Implementar programas de retenção para reduzir o Churn Rate.
        - Avaliar a eficácia das campanhas de marketing, já que o CAC está alto em relação ao LTV.

        A situação atual é crítica, e ações imediatas são necessárias para evitar prejuízos maiores.
        """
    else:
        parecer = f"""
        A escola online apresenta um desempenho financeiro {"satisfatório" if kpis['lucro'] > 0 else "neutro"}, com um lucro de {locale.currency(kpis['lucro'], grouping=True)} e uma margem de lucro de {kpis['margem_lucro']:.2f}%. No entanto, há oportunidades de melhoria, como:
        - Aumentar a taxa de conversão de alunos grátis para premium.
        - Reduzir os custos de marketing para melhorar o ROI.
        - Implementar estratégias de retenção para aumentar o LTV.
        - Acelerar o crescimento mensal de alunos com campanhas mais eficientes.

        No geral, a escola está no caminho certo, mas pode alcançar resultados ainda melhores com ajustes estratégicos.
        """

    pdf.multi_cell(0, 10, txt=parecer)

    pdf.output("relatorio_kpis.pdf")
    print("Relatório gerado com sucesso: relatorio_kpis.pdf")
    