# Observações Importantes

## Para facilitar o teste do projeto no VSCode, considere os **valores fictícios** que você pode usar para preencher os campos da interface gráfica. Esses valores são consistentes com o contexto de uma escola online de cursos, mentorias e bootcamps

### **Valores Fictícios para Entrada de Dados**

| Campo                              | Valor Fictício       |
|------------------------------------|----------------------|
| Quantidade de cursos:              | 50                   |
| Quantidade de bootcamps:           | 10                   |
| Quantidade de mentorias:           | 20                   |
| Alunos Premium:                    | 1000                 |
| Alunos Grátis:                     | 5000                 |
| Valor Assinatura Premium (R$):     | 100.00               |
| Valor Assinatura Grátis (R$):      | 0.00                 |
| Custos com Professores (R$):       | 50000.00             |
| Custos Fixos (R$):                 | 30000.00             |
| Receita Mensal (R$):               | 150000.00            |
| Alunos Cancelados:                 | 200                  |
| Custos de Marketing (R$):          | 20000.00             |
| Novos Alunos:                      | 300                  |
| Tempo Médio de Assinatura (meses): | 6                    |
| Alunos no Mês Anterior:            | 5800                 |
| Alunos no Mês Atual:               | 6000                 |

### **Explicação dos Valores**

1. **Quantidade de cursos, bootcamps e mentorias**:
   - Representam a oferta de produtos da escola.

2. **Alunos Premium e Grátis**:
   - Alunos premium pagam R$ 100,00 por mês, enquanto os grátis não geram receita direta.

3. **Custos com Professores e Custos Fixos**:
   - Custos operacionais da escola.

4. **Receita Mensal**:
   - Receita total gerada pelas assinaturas premium.

5. **Alunos Cancelados**:
   - Número de alunos que cancelaram suas assinaturas no período.

6. **Custos de Marketing**:
   - Investimento em marketing para atrair novos alunos.

7. **Novos Alunos**:
   - Número de alunos adquiridos no período.

8. **Tempo Médio de Assinatura**:
   - Duração média (em meses) que um aluno permanece assinante.

9. **Alunos no Mês Anterior e Mês Atual**:
   - Usados para calcular o crescimento mensal de alunos.

### **Como Testar no VSCode**

1. **Execute o arquivo `main.py`**:
   - No terminal do VSCode, navegue até a pasta do projeto e execute:

     python main.py

2. **Preencha os campos**:
   - Use os valores fictícios fornecidos acima para preencher cada campo da interface gráfica.

3. **Clique em "Gerar Relatório"**:
   - Após preencher os campos, clique no botão para gerar o relatório.

4. **Verifique o arquivo `relatorio_kpis.pdf`**:
   - O relatório será salvo na mesma pasta do projeto. Abra-o para visualizar os resultados e gráficos.

### **Resultados Esperados**

Com os valores fictícios fornecidos, o relatório gerado deve conter:

1. **KPIs Calculados**:
   - Lucro: R$ 50.000,00
   - Margem de Lucro: 33,33%
   - Taxa de Conversão: 20,00%
   - Churn Rate: 3,33%
   - LTV: R$ 600,00
   - CAC: R$ 66,67
   - Crescimento Mensal: 3,45%
   - NPS: Promotores 60%, Neutros 30%, Detratores 10%

2. **Gráficos**:
   - Distribuição de Alunos (Premium vs Grátis).
   - Comparação de Receita, Custos e Lucro.
   - Crescimento Mensal de Alunos.
   - Distribuição do NPS (Promotores, Neutros, Detratores).

### **Conclusão**

Com esses valores fictícios, você poderá testar o projeto no VSCode e verificar o funcionamento completo do simulador.😊
O sistema calcula as KPIs e gera um relatório em PDF com:

- Métricas detalhadas (lucro, margem de lucro, churn rate, LTV, CAC, NPS, etc.).

- Gráficos visuais (distribuição de alunos, receita vs custos, crescimento mensal, NPS).

### **Estrutura do Anexo**

O anexo será dividido em duas partes:

1. **Explicação das Fórmulas das KPIs**.
2. **Explicação dos Gráficos**.

#### **1. Fórmulas das KPIs**

| KPI                  | Fórmula                                                                 |
|----------------------|-------------------------------------------------------------------------|
| Receita Total        | `(Alunos Premium * Valor Premium) + (Alunos Grátis * Valor Grátis)`     |
| Custos Totais        | `Custos com Professores + Custos Fixos + Custos de Marketing`           |
| Lucro                | `Receita Total - Custos Totais`                                         |
| Margem de Lucro      | `(Lucro / Receita Total) * 100`                                         |
| Taxa de Conversão    | `(Alunos Premium / Alunos Grátis) * 100`                                |
| Custo por Aluno      | `Custos Totais / Total de Alunos`                                       |
| Receita por Aluno    | `Receita Total / Total de Alunos`                                       |
| ROI                  | `(Lucro / Custos Totais) * 100`                                         |
| Churn Rate           | `(Alunos Cancelados / Total de Alunos) * 100`                           |
| LTV                  | `(Receita Total / Total de Alunos) * Tempo Médio de Assinatura`         |
| CAC                  | `Custos de Marketing / Novos Alunos`                                    |
| Crescimento Mensal   | `((Alunos Mês Atual - Alunos Mês Anterior) / Alunos Mês Anterior) * 100`|
| NPS                  | `Métrica de satisfação dos alunos (Promotores, Neutros, Detratores)`    |

#### **2. Explicação dos Gráficos**

| Gráfico                              | Explicação                                                                 |
|--------------------------------------|-----------------------------------------------------------------------------|
| Distribuição de Alunos (Premium vs Grátis) | Mostra a proporção de alunos premium e grátis. Útil para entender a base de clientes. |
| Receita, Custos e Lucro              | Compara a receita total, os custos totais e o lucro. Mostra a saúde financeira do negócio. |
| Crescimento Mensal de Alunos         | Mostra o crescimento do número de alunos de um mês para o outro. Indicador de expansão. |
| NPS (Net Promoter Score)             | Mostra a satisfação dos alunos, dividida em promotores, neutros e detratores. |

### **Exemplo de Saída no Anexo**

ANEXO: Explicação das Fórmulas e Gráficos

1. Fórmulas das KPIs
   - Receita Total: (Alunos Premium *Valor Premium) + (Alunos Grátis* Valor Grátis)
   - Custos Totais: Custos com Professores + Custos Fixos + Custos de Marketing
   - Lucro: Receita Total - Custos Totais
   - Margem de Lucro: (Lucro / Receita Total) * 100
   - Taxa de Conversão: (Alunos Premium / Alunos Grátis) * 100
   - Custo por Aluno: Custos Totais / Total de Alunos
   - Receita por Aluno: Receita Total / Total de Alunos
   - ROI: (Lucro / Custos Totais) * 100
   - Churn Rate: (Alunos Cancelados / Total de Alunos) * 100
   - LTV: (Receita Total / Total de Alunos) * Tempo Médio de Assinatura
   - CAC: Custos de Marketing / Novos Alunos
   - Crescimento Mensal: ((Alunos Mês Atual - Alunos Mês Anterior) / Alunos Mês Anterior) * 100
   - NPS: Métrica de satisfação dos alunos (Promotores, Neutros, Detratores)

2. Explicação dos Gráficos
   - Distribuição de Alunos (Premium vs Grátis): Gráfico de pizza que mostra a proporção de alunos premium e grátis.
   - Receita, Custos e Lucro: Gráfico de barras que compara a receita total, os custos totais e o lucro.
   - Crescimento Mensal de Alunos: Gráfico de linhas que mostra o crescimento do número de alunos de um mês para o outro.
   - NPS (Net Promoter Score): Gráfico de barras que mostra a distribuição de promotores, neutros e detratores.
