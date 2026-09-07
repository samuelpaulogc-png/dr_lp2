# -*- coding: utf-8 -*-
"""Gera index.html a partir de index-white.html, convertendo a pagina para tons
escuros sem sair da paleta da marca. Troca o :root e acrescenta os poucos
ajustes que dependem de contexto (coisas que assumiam fundo claro)."""
import io, os, re

BASE = os.path.dirname(os.path.abspath(__file__))
s = io.open(os.path.join(BASE, 'index-white.html'), encoding='utf-8').read()


def hx(h):
    h = h.lstrip('#'); return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def lum(c):
    def f(v):
        v /= 255.0
        return v / 12.92 if v <= .03928 else ((v + .055) / 1.055) ** 2.4
    r, g, b = [f(x) for x in c]
    return .2126 * r + .7152 * g + .0722 * b


def ct(a, b):
    la, lb = lum(hx(a)), lum(hx(b))
    return round((max(la, lb) + .05) / (min(la, lb) + .05), 2)


# ---------------------------------------------------------------- escala escura
# ⚠️ --off e SOBRECARREGADO no CSS de origem: e cor de TEXTO em 18 lugares e
# fundo em 1 (o body). Na versao clara isso funciona porque o creme faz os dois
# papeis. Aqui eles se separam: --off continua creme e o chao vira --bg.
T = {
    'navy-900': '#0B111F',   # barra de prova e rodape — o degrau mais fundo
    'bg':       '#0F1729',   # chao da pagina (token novo, so nesta versao)
    'surface':  '#16203A',   # faixa secundaria (onde antes era cinza claro)
    'navy':     '#1C2747',   # faixa escura — o Azul Profundo da marca
    'white':    '#1E2A4B',   # superficie de cartao (era branco)
    'navy-700': '#26314F',   # cartoes dentro das faixas escuras
    'navy-500': '#3A4463',   # bordas sobre escuro
    'line':     '#2E3A5A',   # fios
    'gold':     '#BD9853', 'gold-600': '#9F8046', 'sand': '#EADEC3',
    'off':      '#F3F4F0',   # creme — segue sendo COR DE TEXTO
    # ⚠️ ESTA ESCALA DESCE PARA CINZA NEUTRO, E ISSO NAO E ESTETICA — E CORRECAO.
    # Ela descia misturando creme com TAUPE, entao quanto mais escuro o degrau,
    # mais quente ficava: ink-2 tinha R-B=+21 e ink-3 R-B=+25. Sobre o azul isso
    # le como AMARELO, e o usuario apontou (05/09/2026) na secao "Sobre", que usa
    # ink-2 nos dois paragrafos. E o MESMO defeito ja corrigido na escala on-dark
    # do index-white.html em 04/09 — a correcao de la nunca foi trazida para ca.
    # Regra: manter R-B entre 0 e -13. Ao mexer nestes hex, conferir R menos B.
    #
    # ⚠️ ink-2 = on-dark-3 DE PROPOSITO (05/09/2026). Nao alinhar os dois de novo
    # sem entender o porque: na pagina CLARA as duas escalas fazem trabalhos
    # opostos — `ink` e tinta escura sobre papel claro, `on-dark` e texto claro
    # sobre marinho. Na pagina ESCURA as duas pintam A MESMA COISA: texto claro
    # sobre fundo escuro. Ficaram rodando juntas com valores diferentes, e o
    # ink-2 era #C7CACF, que e EXATAMENTE o on-dark-4 — um degrau inteiro mais
    # apagado. Resultado: o corpo das secoes que nasceram claras (Voce se
    # reconhece?, Sobre, Diferenciais, O que inclui, FAQ) saia mais escuro que o
    # das que nasceram escuras (A virada, Como funciona), e o usuario apontou na
    # secao 7, que fica logo acima da 8 e deixa a diferenca lado a lado.
    # Pior: o degrau mais apagado caia justo nos fundos MAIS ESCUROS (bg e
    # surface), ou seja, o contraste andava ao contrario do que devia.
    # E a mesma familia de divida que o PROJETO.md ja registra para --off e para
    # color:var(--navy) — token que presumia papel claro sobrevivendo a inversao.
    'ink':      '#F3F4F0', 'ink-2': '#DADCDF', 'ink-3': '#A5A9B2',
    'on-dark':  '#F3F4F0', 'on-dark-2': '#E8E9EA', 'on-dark-3': '#DADCDF',
    'on-dark-4': '#C7CACF', 'on-dark-5': '#A5A9B2',
    'ph-dark-a': '#1A2440', 'ph-dark-b': '#232F52', 'ph-light-b': '#1A2440',
    'navy-rgb': '11,17,31', 'navy-900-rgb': '5,8,16',
    'gold-rgb': '189,152,83', 'white-rgb': '255,255,255',
    # ---- O CHIP DE ICONE (06/09/2026) ----
    # Mesma forma, mesma medida, mesmo traco de icone da versao clara — muda so
    # DE QUE LADO DA ESCALA VEM A TINTA. No claro o chip e uma tinta do azul
    # sobre o cartao branco; aqui e uma tinta do creme sobre o cartao azul.
    # E por isso que os quatro valores sao rgba() e nao hex: o chip precisa
    # deixar a superficie do cartao aparecer por baixo, senao vira selo — que e
    # exatamente o defeito do chip de ouro solido que saiu em 05/09.
    # ⚠️ Aqui o brilho e FORTE (a referencia usa .95) porque ele pinta em
    # `screen` e sobre o azul ha o que clarear. No arquivo-fonte claro ele fica
    # em .30 de proposito — ver a nota no :root de la.
    'chip-bg': ('linear-gradient(155deg,rgba(var(--white-rgb),.16) 0%,'
                'rgba(var(--white-rgb),.04) 45%,rgba(var(--white-rgb),.09) 100%)'),
    'chip-border': 'rgba(var(--white-rgb),.26)',
    'chip-ink': 'var(--off)',
    'chip-inset': 'inset 0 1px 0 rgba(var(--white-rgb),.20)',
    'chip-sheen': ('linear-gradient(115deg,rgba(var(--white-rgb),.95) 0%,'
                   'rgba(var(--white-rgb),.35) 20%,rgba(var(--white-rgb),0) 46%)'),
}

PARES = [
    ('titulo sobre o chao',       'ink', 'bg', 4.5),
    ('corpo sobre o chao',        'ink-2', 'bg', 4.5),
    ('terciario sobre o chao',    'ink-3', 'bg', 4.5),
    ('ouro sobre o chao',         'gold', 'bg', 4.5),
    ('titulo sobre surface',      'ink', 'surface', 4.5),
    ('corpo sobre surface',       'ink-2', 'surface', 4.5),
    ('titulo sobre faixa escura', 'on-dark', 'navy', 4.5),
    ('corpo sobre faixa escura',  'on-dark-2', 'navy', 4.5),
    ('apoio sobre faixa escura',  'on-dark-3', 'navy', 4.5),
    ('microcopy sobre faixa',     'on-dark-4', 'navy', 4.5),
    ('ouro sobre faixa escura',   'gold', 'navy', 4.5),
    ('titulo dentro do cartao',   'ink', 'white', 4.5),
    ('corpo dentro do cartao',    'ink-2', 'white', 4.5),
    ('corpo no cartao escuro',    'on-dark-3', 'navy-700', 4.5),
    ('navbar: azul sobre ouro',   'navy', 'gold', 4.5),
    # O chip do .includes passou de bege para ouro em 05/09/2026 — a auditoria
    # tem de medir o par que existe na pagina, senao aprova uma combinacao morta.
    ('tick: check sobre ouro',    'navy', 'gold', 4.5),
    ('rodape sobre o mais fundo', 'ink-2', 'navy-900', 4.5),
    ('placeholder sobre escuro',  'on-dark-5', 'navy', 3.0),
]
print("=== contraste da versao escura ===")
falhas = 0
for nome, a, b, alvo in PARES:
    v = ct(T[a], T[b]); ok = v >= alvo
    falhas += 0 if ok else 1
    print("  %-28s %5.2f:1  alvo %.1f  %s" % (nome, v, alvo, 'OK' if ok else '<<< FALHA'))
print("  %s\n" % ("todos passam" if not falhas else "%d FALHA(S)" % falhas))

# ---------------------------------------------------------------- :root
root = re.search(r':root\{(.*?)\n\}', s, re.S).group(1)
novo = root.replace('  --maxw:1080px;', '  --bg:#0F1729;  /* chao da versao escura */\n  --maxw:1080px;')
for k, v in T.items():
    if k == 'bg':
        continue
    novo, c = re.subn(r'(--%s\s*:\s*)[^;]+' % re.escape(k), lambda m: m.group(1) + v, novo)
    if c == 0:
        print("  ! token nao encontrado:", k)
novo = novo.replace('/* ---- Paleta oficial',
                    '/* ---- VERSAO ESCURA, gerada por _gerar_dark.py ----\n'
                    '     Mesmas 5 cores da marca; muda so qual degrau cada papel ocupa.\n'
                    '     Cinco degraus de fundo: navy-900 < bg < surface < navy < white/navy-700\n'
                    '     Paleta oficial', 1)
s = s.replace(root, novo, 1)

# ---------------------------------------------------------------- ajustes
AJUSTES = """
/* ================= AJUSTES DA VERSAO ESCURA =================
   O resto da pagina ficou escuro so trocando o :root. As regras abaixo existem
   porque assumiam explicitamente um fundo claro.

   O chao vem de --bg, e nao de --off: --off e usado como COR DE TEXTO em 18
   lugares do CSS e como fundo em apenas 1. Reaproveita-lo aqui apagaria os 18. */
body{background:var(--bg)}

/* A sombra e azul sobre claro; sobre escuro ela desaparece. Quem separa as
   superficies passa a ser a borda. */
.card,.includes li,blockquote.quote,.faq details{box-shadow:none}
.finalcta .box{box-shadow:none}

/* ---- O CARTAO ESCURO GANHOU MATERIAL (06/09/2026) ----
   Vem de aurumclinic.org, e conserta um buraco que a regra logo acima abria:
   na versao clara o cartao se separa do chao por SOMBRA (--sh-sm); sobre escuro
   sombra azul nao existe, entao ela era zerada e sobrava um fio de 1px chapado.
   O cartao ficava sem material — e era ele que ia receber o chip de icone.
   🔑 SOBRE FUNDO ESCURO NAO SE USA SOMBRA POR BAIXO, SE USA LUZ POR CIMA.
   Sao tres camadas, todas medidas no DOM da referencia:
   1) `--ring` — a borda vira um DEGRADE vertical: 22% na aresta de cima, 5% ja
      aos 6% da altura, 3% no miolo e 8% na de baixo. E a quina superior pegando
      luz. Um fio de opacidade constante nao faz isso: ele desenha o contorno
      inteiro e le como caixa, nao como superficie iluminada.
   2) o fio interno de 1px no topo (`inset`), que e o reflexo na propria quina.
   3) a sombra de contato preta embaixo — preta, e nao azul: ela e ausencia de
      luz, e sobre um chao ja azul a sombra azul nao escurece nada.
   ⚠️ O TRUQUE E DE DUAS CAIXAS DE FUNDO: `padding-box` pinta a superficie e
   `border-box` pinta a faixa da borda. Para isso a borda precisa existir com
   largura e ser TRANSPARENTE — `border-color:transparent`, nunca `border:none`.
   Sem largura declarada nao ha faixa de border-box para o degrade ocupar.
   ⚠️ E POR ISSO QUE CADA FAMILIA DE CARTAO APARECE SEPARADA ABAIXO: o primeiro
   plano de `background` tem de ser a cor daquele cartao (--white nos claros de
   origem, --navy-700 nos que ja nasceram escuros). Nao da para unificar numa
   regra so sem achatar os dois degraus de superficie que a pagina tem. */
:root{--ring:linear-gradient(180deg,rgba(var(--white-rgb),.22) 0%,rgba(var(--white-rgb),.05) 6%,rgba(var(--white-rgb),.03) 94%,rgba(var(--white-rgb),.08) 100%);
  --card-lift:inset 0 1px 0 rgba(var(--white-rgb),.07),0 10px 30px rgba(0,0,0,.26)}
/* ⚠️ A SUPERFICIE VAI COMO GRADIENTE, NAO COMO COR — e nao e estilo, e sintaxe.
   No atalho `background` com varias camadas, a COR so pode aparecer na ULTIMA.
   Escrito como `var(--white) padding-box,var(--ring) border-box` o navegador
   descarta o plano de cor inteiro: medido, o cartao voltou `background-color:
   rgba(0,0,0,0)` e sumiu contra o chao. `linear-gradient(cor,cor)` e a mesma
   cor chapada expressa como IMAGEM, que pode ocupar a primeira camada. */
.card{border-color:transparent;
  background:linear-gradient(var(--white),var(--white)) padding-box,var(--ring) border-box;
  box-shadow:var(--card-lift)}
.step{border-color:transparent;
  background:linear-gradient(var(--navy-700),var(--navy-700)) padding-box,var(--ring) border-box;
  box-shadow:var(--card-lift)}
/* No hover a luz sobe junto com o cartao, em vez de sumir. O ouro entra so no
   fio — o mesmo gesto do chip la dentro, que tambem acende a borda e nao o
   fundo. ⚠️ `border-color` opaco cobre o degrade de border-box: e o que faz o
   contorno virar ouro inteiro no hover, e e o efeito desejado. */
.card:hover{border-color:rgba(var(--gold-rgb),.55);
  box-shadow:inset 0 1px 0 rgba(var(--white-rgb),.10),0 16px 40px rgba(0,0,0,.34)}

/* Borda de 2px em azul sobre cartao azul e invisivel: passa a ouro. */
.aud-yes{border-color:var(--gold)}

/* O botao secundario era azul sobre claro; sobre escuro sumia no fundo.
   Vira contorno em ouro — o gesto discreto que a marca pede. Dentro da navbar
   (que e dourada) ele continua solido em azul, senao ouro sobre ouro sumiria. */
.btn-secondary{background:transparent;color:var(--gold);box-shadow:inset 0 0 0 1.5px var(--gold)}
.btn-secondary:hover{background:var(--gold);color:var(--navy)}
.nav-links a.btn-secondary{background:var(--navy);color:var(--off);box-shadow:none}
.nav-links a.btn-secondary:hover{background:var(--navy-900);color:var(--off)}

/* Texto em azul que assumia fundo claro. Sobre escuro cai para ~1.1:1.
   Sao os unicos casos em que color:var(--navy) NAO fica sobre ouro ou bege. */
.turn{color:var(--on-dark)}
.faq summary{color:var(--on-dark)}
blockquote.quote cite{color:var(--gold)}
.btn-outline{color:var(--gold);box-shadow:inset 0 0 0 2px var(--gold)}
.btn-outline:hover{background:var(--gold);color:var(--navy)}

/* O chevron do FAQ em ouro escuro ficava apagado sobre o cartao. */
.faq summary .chev{color:var(--gold)}

/* O retrato era um degrade claro->escuro; sobre escuro precisa de degraus
   proprios para nao virar um buraco. */
.portrait{background:linear-gradient(160deg,var(--navy-700),var(--navy-900))}

/* 🚨 O ANEL DE FOCO ERA INVISIVEL NA PAGINA INTEIRA (corrigido em 05/09/2026).
   `--focus` vale `var(--navy)` no arquivo-fonte, e la esta certo: azul sobre papel
   claro. Aqui o azul e FUNDO, entao o anel desenhava a mesma cor por baixo dele:
   1,00:1 sobre a faixa navy (identico), 1,10 sobre surface, 1,14 sobre cartao,
   1,22 sobre o chao. O minimo do WCAG para indicador de foco e 3,0:1 — ou seja,
   quem navega por teclado nao via onde estava em NENHUM botao, link ou pergunta
   do FAQ. So o cabecalho escapava, porque ja tinha um override proprio em ouro.
   Em ouro o anel da 6,62:1 sobre o chao.
   ⚠️ E o QUINTO caso da divida "color:var(--navy) assumindo fundo claro" que o
   PROJETO.md registra. Os outros quatro (.turn, .faq summary, cite, .btn-outline)
   foram corrigidos; este passou porque a auditoria do script mede TEXTO, e anel de
   foco nao e texto. Ao acrescentar tokens de cor aqui, perguntar sempre: este
   valor assume papel claro? */
:root{--focus:var(--gold)}
</style>"""
s = s.replace('</style>', AJUSTES, 1)

s = s.replace('<meta name="theme-color" content="#1C2747">',
              '<meta name="theme-color" content="#0F1729">', 1)

# ⚠️ AQUI EXISTIA UM `s.replace('<title>', '<title>[ESCURA] ')`. FOI REMOVIDO EM
# 05/09/2026 e NAO DEVE VOLTAR. Ele era util quando a escura era so uma versao de
# avaliacao e convinha distinguir as duas abas. Depois da inversao o index.html
# virou A PAGINA PUBLICADA, e o prefixo passou a ir para a aba do navegador e para
# o resultado do Google. Ficou no ar por dias exatamente por isso: o nome deste
# script ainda sugere que ele gera um arquivo auxiliar, e nao a entrega.

io.open(os.path.join(BASE, 'index.html'), 'w', encoding='utf-8').write(s)
print("gerado: index.html  (%d bytes)" % len(s))
