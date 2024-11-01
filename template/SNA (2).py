


from pyvis.network import Network


# Dados da relação 'To' e 'From'
relations = [
    ("Químico Analítico", "Filosofia"),
    ("Químico Analítico", "Aspectos Estruturais e Funcionais do Tecido Humano"),
    ("Químico Analítico", "Genética Estrutural e Herança"),
    ("Engenheiro de Processos", "Estrutura, Composição e Propriedades da Matéria"),
    ("Engenheiro de Processos", "Sistemas do Corpo Humano"),
    ("Engenheiro de Processos", "Genômica"),
    ("Controle de Qualidade", "Aspectos Estruturais e Funcionais do Tecido Humano"),
    ("Cientista de formulação", "Estrutura, Composição e Propriedades da Matéria"),
    ("Analista de Dados Biotecnológicos", "Genética Estrutural e Herança"),
    ("Consultor em Análise Estatística Biotecnológica", "Análise de Dados Biotecnológicos"),
    ("Indústria Farmacêutica", "Vida e Sociedade na Era da Biotecnologia"),
    ("Desenvolvimento de Polímeros", "Projeto Interprofissional: Bioética e Direitos Humanos"),
    ("Produção de especiarias finas e cosméticos", "Sistemas do Corpo Humano"),
    ("Microbiologia", "Estrutura e Propriedades dos Compostos de Carbono"),
    ("Genética Molecular", "Microrganismos de Importância Biotecnológica"),
]

# Descrições para os nós da coluna "From"
descriptions = {
    "Filosofia": """Esta matéria é classificada como obrigatória em todos os cursos...""",
    "Aspectos Estruturais e Funcionais do Tecido Humano": """# Descrição da Matéria..."""
}

# Cria a rede
net = Network(height='750px', width='100%', bgcolor='#222222', font_color='white')

# Adiciona nós e arestas, ajustando o tamanho dos nós
for to, from_ in relations:
    # Tamanho dos nós
    net.add_node(to, title=to, size=50)  # Nós da coluna 'To' com tamanho maior
    
    # Adiciona nós da coluna 'From' com descrição se existir
    description = descriptions.get(from_, from_)  # Usa a descrição se disponível
    net.add_node(from_, title=description, size=15)  # Nós da coluna 'From' com tamanho menor
    
    # Adiciona aresta
    net.add_edge(from_, to)

# Customizações da rede
net.set_options(""" 
var options = {
  "nodes": {
    "borderWidth": 2,
    "color": {
      "border": "#ffffff",
      "background": "#007bff"
    },
    "font": {
      "color": "#ffffff"
    }
  },
  "edges": {
    "color": {
      "color": "#ffffff"
    }
  },
  "interaction": {
    "hover": true
  },
  "physics": {
    "enabled": true
  }
}
""")

# Salva o HTML diretamente
net.write_html('network.html')

print("Arquivo HTML gerado com sucesso como 'network.html'. Abra esse arquivo no seu navegador.")
