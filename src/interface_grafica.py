import tkinter as tk
from tkinter import messagebox
from src.simulacao import calcular_kpis
from gerar_relatorio import gerar_relatorio_pdf
import locale

# Configurar o locale para o padrão brasileiro
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

def coletar_dados():
    def gerar_relatorio():
        try:
            # Coletar dados dos campos
            cursos = int(entry_cursos.get())
            bootcamps = int(entry_bootcamps.get())
            mentorias = int(entry_mentorias.get())
            alunos_premium = int(entry_alunos_premium.get())
            alunos_gratis = int(entry_alunos_gratis.get())
            valor_premium = float(entry_valor_premium.get())
            valor_gratis = float(entry_valor_gratis.get())
            custos_professores = float(entry_custos_professores.get())
            custos_fixos = float(entry_custos_fixos.get())
            receita_mensal = float(entry_receita_mensal.get())
            alunos_cancelados = int(entry_alunos_cancelados.get())
            custos_marketing = float(entry_custos_marketing.get())
            novos_alunos = int(entry_novos_alunos.get())
            tempo_medio_assinatura = float(entry_tempo_medio_assinatura.get())
            alunos_mes_anterior = int(entry_alunos_mes_anterior.get())
            alunos_mes_atual = int(entry_alunos_mes_atual.get())

            # Calcular KPIs
            kpis = calcular_kpis(
                cursos, bootcamps, mentorias, alunos_premium, alunos_gratis,
                valor_premium, valor_gratis, custos_professores, custos_fixos,
                receita_mensal, alunos_cancelados, custos_marketing, novos_alunos,
                tempo_medio_assinatura, alunos_mes_anterior, alunos_mes_atual
            )

            # Gerar relatório
            gerar_relatorio_pdf(kpis)
            messagebox.showinfo("Sucesso", "Relatório gerado com sucesso: relatorio_kpis.pdf")
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira valores válidos.")

    # Configuração da interface gráfica
    root = tk.Tk()
    root.title("Simulador de KPIs - Escola Online")

    # Campos de entrada
    campos = [
        ("Quantidade de cursos:", 0),
        ("Quantidade de bootcamps:", 1),
        ("Quantidade de mentorias:", 2),
        ("Alunos Premium:", 3),
        ("Alunos Grátis:", 4),
        ("Valor Assinatura Premium (R$):", 5),
        ("Valor Assinatura Grátis (R$):", 6),
        ("Custos com Professores (R$):", 7),
        ("Custos Fixos (R$):", 8),
        ("Receita Mensal (R$):", 9),
        ("Alunos Cancelados:", 10),
        ("Custos de Marketing (R$):", 11),
        ("Novos Alunos:", 12),
        ("Tempo Médio de Assinatura (meses):", 13),
        ("Alunos no Mês Anterior:", 14),
        ("Alunos no Mês Atual:", 15)
    ]

    entries = []
    for label_text, row in campos:
        tk.Label(root, text=label_text).grid(row=row, column=0, sticky="w")
        entry = tk.Entry(root)
        entry.grid(row=row, column=1)
        entries.append(entry)

    # Atribuir cada campo a uma variável
    (
        entry_cursos, entry_bootcamps, entry_mentorias, entry_alunos_premium,
        entry_alunos_gratis, entry_valor_premium, entry_valor_gratis,
        entry_custos_professores, entry_custos_fixos, entry_receita_mensal,
        entry_alunos_cancelados, entry_custos_marketing, entry_novos_alunos,
        entry_tempo_medio_assinatura, entry_alunos_mes_anterior, entry_alunos_mes_atual
    ) = entries

    # Botão para gerar relatório
    tk.Button(root, text="Gerar Relatório", command=gerar_relatorio).grid(row=16, column=0, columnspan=2, pady=10)

    # Encerrar o programa corretamente ao fechar a janela
    root.protocol("WM_DELETE_WINDOW", root.quit)
    
    root.mainloop()

if __name__ == "__main__":
    coletar_dados()
