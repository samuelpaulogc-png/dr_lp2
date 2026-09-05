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
    'ink':      '#F3F4F0', 'ink-2': '#C7CACF', 'ink-3': '#A5A9B2',
    'on-dark':  '#F3F4F0', 'on-dark-2': '#E8E9EA', 'on-dark-3': '#DADCDF',
    'on-dark-4': '#C7CACF', 'on-dark-5': '#A5A9B2',
    'ph-dark-a': '#1A2440', 'ph-dark-b': '#232F52', 'ph-light-b': '#1A2440',
    'navy-rgb': '11,17,31', 'navy-900-rgb': '5,8,16',
    'gold-rgb': '189,152,83', 'white-rgb': '255,255,255',
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
    ('tick: check sobre bege',    'navy', 'sand', 4.5),
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
.card:hover{box-shadow:none;border-color:var(--gold)}
.finalcta .box{box-shadow:none}

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
</style>"""
s = s.replace('</style>', AJUSTES, 1)

s = s.replace('<meta name="theme-color" content="#1C2747">',
              '<meta name="theme-color" content="#0F1729">', 1)
s = s.replace('<title>', '<title>[ESCURA] ', 1)

io.open(os.path.join(BASE, 'index.html'), 'w', encoding='utf-8').write(s)
print("gerado: index.html  (%d bytes)" % len(s))
