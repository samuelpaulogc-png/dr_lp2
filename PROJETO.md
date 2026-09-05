# Projeto — Landing Page Dr. Rafael Gallassini

> **Para o assistente:** leia este arquivo e `index.html` antes de qualquer alteração.
> Ele registra decisões, restrições e pendências que **não estão dedutíveis do código**.

> 📍 **O projeto mudou de lugar e agora tem git.**
> Pasta de trabalho: **`C:\Users\-User-\Documents\dr_lp2`**
> Remoto: **https://github.com/samuelpaulogc-png/dr_lp2** (público, por decisão do usuário)
> A pasta antiga (`D:\Meus Documentos\Downloads\RG - PAGE`) **está num disco com falha física
> e não deve mais ser usada** — ver "Incidente de disco" nas notas técnicas.

## Arquivos

| Arquivo | Papel |
|---|---|
| `index.html` | **A entrega.** Landing page completa, arquivo único (HTML + CSS em `<style>` + JS inline). |
| `COPY.md` | Copy original aprovada. Fonte da verdade do texto. (No disco o nome é maiúsculo — em deploy Linux isso importa.) |
| `design-system.html` | Design system (cores, tipografia, componentes). Fonte da verdade visual. |
| `index-dark.html` | **Só para avaliação.** A página inteira em tons escuros, dentro da paleta da marca. Gerado por `gerar-dark.py` — **não editar à mão**, senão a próxima geração sobrescreve. |
| `gerar-dark.py` | Regenera o `index-dark.html` a partir do `index.html`. Rodar sempre que o principal mudar. |
| `assets/Logos/` | 6 arquivos: `rg_hrz` (horizontal), `rg_vrt` (vertical), `rg_ico` (só o símbolo), cada um em `_light` (para fundo escuro) e `_dark` (para fundo claro). |
| `assets/Fontes/goldoni-webfont.woff2` | A serifada da marca. 24,5 KB. ⚠️ **Só tem caixa alta** — ver a ressalva na seção de tipografia. |
| `assets/Fundo/` | `Fundo.jpg` é o original de 1,5 MB; `fundo-1920.webp` (13 KB) e `fundo-1280.webp` (4,7 KB) são as versões de uso. **Ainda não estão aplicados em lugar nenhum da página.** |
| `.claude/launch.json` | Config do servidor local de preview (`landing`, **porta 5181**). Não faz parte da entrega. ⚠️ Era 5173; mudou em 05/09/2026 porque outra sessão tomou a porta e serviu outro projeto — ver as notas de preview. |
| `assets/Fotos/` | Imagens reais. Os 6 derivados da hero são versionados; `_candidatas/` está no `.gitignore`. |

Os comparativos temporários (`_variacoes-*.html`, `comparacao.html`, `secao7.html`) **ficaram na pasta antiga do `D:`** e estão no `.gitignore`. Dois deles corromperam no disco. Se precisar de algum, é mais rápido regenerar do que recuperar.

## Onde o projeto está agora

**A entrega é o `index.html`, e ele está funcionando.** Medido a 1180px de viewport:

| seção | altura |
|---|---|
| 1+2 · hero · barra de prova | 867px |
| 3 · Você se reconhece? | 1361px |
| **4 · A virada** | 1224px |
| 5 · Sobre | 712px |
| 6 · Diferenciais | 893px |
| 7 · O que inclui | 679px |
| 8 · Como funciona | 820px |
| 9 · Para quem é | 737px |
| 10 · Depoimentos | 559px |
| 11 · Dúvidas | 911px |
| 12 · CTA final | 1016px |

**Página inteira: ~10.330px**, medida a 1180px em **04/09/2026, já com a marca aplicada**. Sem erro de console, sem estouro horizontal. ⚠️ **As alturas mexeram com a troca de fonte e ainda não foram reconferidas em 900/560/375px.**

### 🚨 As decisões que dependem do usuário — em ordem de urgência

1. **CAIXA ALTA DOS TÍTULOS.** O arquivo da Goldoni não tem caixa baixa, então **todos os títulos da página renderizam em maiúsculas**. Isso contraria uma decisão registrada aqui ("título em caixa alta — testado e descartado"). Três saídas foram oferecidas e nenhuma escolhida. Ver "Tipografia" abaixo.
2. **Depoimentos** — três placeholders no ar e **sem nenhum aviso na tela**. Bloqueia a publicação.
3. **As 7 fotos** — continuam vazias. É a maior mudança visual disponível e nenhuma decisão fina de layout se sustenta antes delas.
4. **Ritmo de imagem** — seções 4 e 5 estruturalmente idênticas (vertical à direita nas duas). Correção sugerida abaixo, não aplicada.
5. **Seção 7** — duas perguntas abertas para o Dr. Rafael: o plano alimentar volta? Os retornos precisam aparecer?
6. **CTA final** — sugestão nº1 levantada e **não aplicada**: remover `max-width:44ch` do `.inner`. Ver "Seção 12" abaixo.

### ✅ Agora existe git — e ele já salvou o projeto uma vez

Até 03/09/2026 o histórico eram cópias em disco. Hoje:

- Repositório em `C:\Users\-User-\Documents\dr_lp2`, remoto no GitHub, branch `main`.
- **Commite a cada mudança fechada**, com o motivo escrito na mensagem. Foi assim que as mudanças de 04/09 foram feitas, e a mensagem de commit passou a carregar o "porquê" junto com o "o quê".
- ⚠️ **Commitar e empurrar são ações do usuário.** Não fazer por conta própria sem ele pedir.

**O git não é teórico aqui:** durante a sessão de 03/09 o `index.html` corrompeu no disco **enquanto trabalhávamos**, e foi restaurado inteiro com `git checkout`. Duas horas antes teria sido perda real.

## Sessão de 03/09/2026 — resumo para retomar

Tudo abaixo está detalhado nas seções seguintes; isto é só o índice do que mudou, em ordem.

1. **Barra de prova** — ícones de check removidos; itens trocados por dados concretos (5 → 7); marquee 34s → 46s.
2. **CRM preenchido** — `CRM/SC 21664` em 4 lugares; UF confirmada pelo usuário.
3. **Volume preenchido** — "Mais de 30 mil pacientes acompanhados".
4. **Congressos** — o vago "congressos internacionais" virou **"5 congressos internacionais"**, a partir de um print da página antiga enviado pelo usuário.
5. **Legenda do retrato removida** (seção "Sobre").
6. **P2 do "Sobre" reescrito** — eliminado o eco do parágrafo do Mecanismo (56 → 47 palavras).
7. **Eyebrows removidos** — os 10 rótulos acima dos títulos, mais o CSS.
8. **Botão flutuante do WhatsApp** — passa a aparecer só depois da hero.
9. **Seção "A virada" reestruturada** — três faixas e os fatores tipografados como lista (eram 7 à época; hoje são 6, ver item 12).
10. **Segunda rodada na "A virada"** (mesma data, mais tarde): o usuário mandou duas referências e o tratamento B foi refeito **três vezes**, em cima delas. Ver "Refazendo o B" abaixo.
11. **Tratamento E** — a pedido do usuário, o layout do **D** (foto vertical ao lado) unido ao **painel do B1** (células verticais, número em cima, nome na base). Painel a 2 colunas, porque a coluna de texto do D tem ~525px e não 1032px.
12. **"Tireoide" cortado da lista de fatores** (7 → 6), autorizado pelo usuário. **Terceira exceção à regra 1** — ver Regras invioláveis. Aplicado no `index.html`, nos tratamentos da comparação e anotado no `COPY.md`.
13. **Tratamento E aplicado no `index.html`** — a seção "A virada" foi fechada. ⚠️ Isso **mudou o sistema de imagem da página** e deixou uma regressão de ritmo em aberto. Ver o bloco logo abaixo.
14. **Aviso de compliance dos depoimentos removido da página**, a pedido do usuário. 🚨 A obrigação continua valendo e agora vive **só neste arquivo** — ver Regras invioláveis §2 e Próximos passos §4.
15. **Bug corrigido na seção "Para quem é"** — um `<strong>` dentro de um `<li>` flex quebrava a frase em três caixas lado a lado. **O bug era anterior a esta sessão.** Ver Notas técnicas.
16. **Botão do "Sobre" encurtado** (só removendo palavras) e **retrato horizontal no mobile** (16/10), ambos a pedido do usuário.

### 🎨 Sessão de 04/09/2026 — a marca entrou

A página nasceu numa paleta que não era da marca (marinho + verde-limão). Nesta sessão ela foi trocada pela oficial, em três passos deliberados.

**Passo 1 — tokenizar, sem mudar um pixel.** A paleta estava tokenizada mas não 100%: havia **12 hexadecimais cravados no CSS em 24 ocorrências**, 12 `rgba()` derivados e 5 SVG com cor no atributo. Trocar só o `:root` teria deixado a página meio migrada. Tudo virou token; a prova foi expandir todo `var()` dos dois lados e comparar: **240 regras antes, 240 depois, zero diferenças**. Tokens novos: a escala `--on-dark`…`--on-dark-5` (que existia de fato, espalhada em 12 lugares, sem nome) e os componentes `--navy-rgb`/`--gold-rgb`/`--white-rgb`, necessários porque `rgba()` não aceita `var()` de cor inteira sem *relative color syntax*.

**Passo 2 — a paleta.** Extraída do PDF do manual, amostrada dos próprios swatches:

| nome no manual | hex | papel na página |
|---|---|---|
| Azul Profundo | `#1C2747` | fundo escuro, tinta sobre claro |
| Dourado | `#BD9853` | acento, CTA, destaques |
| Taupe | `#9D9077` | superfície e fio (**nunca texto**) |
| Bege | `#EADEC3` | chip do check, acento claro |
| Creme | `#F3F4F0` | chão da página, texto sobre escuro |

🔑 **O achado que rege tudo: o Azul Profundo é a ÚNICA cor da marca que contrasta com as outras quatro.** Ouro × Creme = 2,44:1, Ouro × Bege = 2,02:1, Taupe × Creme = 2,84:1, Ouro × Taupe = 1,16:1. Ou seja: **toda hierarquia de texto se constrói sobre o Azul Profundo**, e ouro/taupe/bege só servem como superfície e acento. Isso não é preferência, é o que os números permitem.

Tokens renomeados porque o nome virou mentira: `--lime`→`--gold`, `--lime-600`→`--gold-600`, `--lime-200`→`--sand`, `--sh-lime`→`--sh-gold`.

**Passo 3 — fontes, logo e navbar.**
- **Montserrat** no conteúdo (Google Fonts). **Goldoni** nos títulos, arquivo real da marca — ver a ressalva abaixo.
- O **logo** substituiu o monograma "RG" em CSS. A 46px o "GALLASSINI" era ilegível; foi para **58px**, e a navbar subiu de 66 para 78px. **Em 04/09/2026 baixou para 52px** a pedido do usuário — ver abaixo.
- A **navbar** deixou de ser uma barra de acento e virou **azul (`--navy-900`)**, um degrau abaixo da hero, com um fio dourado embaixo. Links, CTA, anel de foco, botão do menu e painel mobile foram ajustados junto — todos assumiam barra clara.
- A **escala `on-dark` deixou de puxar amarelo.** Ela descia misturando creme com **taupe**, então quanto mais escuro o degrau, mais quente: `R-B` ia de +3 até +28. Sobre o azul isso lia como amarelo, e o usuário apontou. Agora desce para cinza neutro (`R-B` entre 0 e −5).

#### ✅ O H1 DA HERO VOLTOU A 5 LINHAS (04/09/2026)

O usuário mandou print e pediu para diminuir o título até caber em 5 linhas. **Teto do `clamp` do `.hero h1`: 64px → 60px.**

**A linha que manda não é o texto todo, é a 4ª: "MÉDICO INDIVIDUALIZADO".** Ela é a mais larga e não cabia nos **640px** da `.hero-copy`, então "MÉDICO" caía sozinho e abria a 6ª linha. Medido a 1358px, variando só o corpo:

| corpo | linhas | folga na linha mais larga |
|---|---|---|
| 64px (antes) | **6** | 33px |
| 63px | 5 | **2,4px** |
| 62px | 5 | 12,5px |
| **60px (aplicado)** | **5** | **32,7px** |
| 58px | 5 | 53px |

**Por que 60 e não 63.** A 63px já cabe, mas com 2,4px de sobra — 0,4% da coluna, margem que qualquer arredondamento de outro navegador consome e devolve as 6 linhas. A 60px sobram 32,7px, **exatamente a mesma folga que os 64px tinham na linha mais larga deles**. É o menor corte que não fica na corda bamba.

**Ganho de brinde:** "MÉDICO INDIVIDUALIZADO" passou a ler junto, em vez de "MÉDICO" órfão numa linha inteira. Altura do H1: 392px → **306px** (−86px); hero: 804 → **718px**.

⚠️ **Ao mexer no corpo do H1, no `letter-spacing` ou na largura da `.hero-copy`, remedir "MÉDICO INDIVIDUALIZADO"** — é ela que decide, não o comprimento total.

✅ **Conferido em 7 larguras, sem estouro horizontal:** 1600/1358/1143 → 5 linhas a 60px · 960 → 5 linhas a 53,8px · 768 → 4 linhas · 560 → 3 linhas · 375 → 5 linhas. Abaixo de 1071px o `clamp` já entregava menos que 60px, então **nada mudou no responsivo** — o corte só toca as telas largas. `text-wrap:balance` foi testado e **não estava influenciando**: com `normal` o resultado é idêntico.

#### ✅ O TEXTO DOS CTAs GRANDES PERDEU PESO (04/09/2026)

O usuário perguntou se dava para diminuir o tamanho **ou a grossura do texto** do botão da primeira dobra. **`.btn-lg` ganhou `font-weight:700`**, no lugar dos 800 herdados do `.btn`.

**Quatro variações renderizadas lado a lado, em escala 1:1**, isolando os dois eixos:

| | corpo | peso | largura do botão da hero |
|---|---|---|---|
| A · antes | 18px | 800 | 379px |
| **B · aplicada** | **18px** | **700** | **374px** |
| C | 16px | 800 | 345px |
| D | 16px | 700 | 340px |

**O eixo certo era o peso, não o corpo.** 800 é o Extrabold da Montserrat e, sobre o ouro, os traços engrossam a ponto de quase fechar os contraformas — o C mostra que encolher sem tirar peso mantém a mancha densa. O 700 tira a grossura e **quase não mexe na geometria** (379 → 374px de largura, altura idêntica), então a composição da dobra fica onde estava.

**Aplicado nos 4 `.btn-lg`** — hero, Sobre, Como funciona e CTA final — escolha do usuário. Mudar só o da hero o deixaria diferente dos outros três idênticos, o que leria como descuido em vez de decisão.

✅ **Contraste conferido antes de escolher: navy sobre ouro = 5,44:1.** ⚠️ Detalhe que decide isso: **18px ainda é "texto normal" pelo WCAG** — o limiar de texto grande é 24px, ou 18,66px com peso ≥700 —, então as quatro variações precisavam de **4,5:1**, não de 3:1. Todas passam. Se um dia o corpo do `.btn-lg` cair, o limiar continua o mesmo; o que não pode é a cor mudar.

⚠️ **A regra `.btn-lg` tem de continuar DEPOIS de `.btn` no CSS.** As duas têm especificidade (0,1,0) — quem vence é quem vem por último. Movendo `.btn-lg` para cima, o peso 800 volta sem aviso.

**A navbar não foi tocada e nem precisava:** o "Agendar" já renderiza em **600**, não em 800, porque `.nav-links a` (0,1,1) vence `.btn` (0,1,0) e impõe o próprio peso. É o mesmo detalhe de especificidade já registrado nas notas técnicas para a *cor* daquele botão.

#### ✅ CTAs EM UMA LINHA NO CELULAR (04/09/2026) — e o CTA final que não fecha

O usuário mandou print do celular: o botão da hero quebrava em duas linhas. **Medido a 375px, os quatro quebravam** — e o do rodapé em **três**.

| botão | espaço | precisa de | antes |
|---|---|---|---|
| hero | 339px | 374px | 2 linhas |
| Sobre | 327px | 377px | 2 linhas |
| Como funciona | 327px | 389px | 2 linhas |
| **CTA final** | **259px** | 434px | **3 linhas** |

**O botão não estava grande demais — o padding é que era de desktop.** Os `18px 34px` do `.btn-lg` comem 68px dos 339 disponíveis num telefone.

**Correção aplicada** (dentro do `@media(max-width:768px)`): `width:100%` + `max-width:420px` + `padding:16px 12px` + `font-size:clamp(14px,4.45vw,18px)`.

🔑 **O achado que destravou o tamanho: largura cheia.** O usuário mandou de referência um print de landing de moto (`ablocacoesdeveiculos.com`) e pediu o botão "nesse sentido de tamanho e largura". O que aquela página faz e a nossa não fazia: **o CTA ocupa a coluna inteira**, texto centralizado. O nosso encolhia até o tamanho do texto — 302px numa coluna de 339 —, e era isso, não o corpo da fonte, que o fazia parecer pequeno.
- **E largura cheia financia corpo maior.** Com `width:100%` o padding horizontal deixa de definir a largura do botão e vira só o recuo mínimo do texto, então pode encolher para 12px sem parecer apertado — o botão não está mais colado no texto. Isso devolveu espaço e o corpo subiu de novo.
- **O `max-width:420px` existe para o tablet:** a regra vale até 768px, onde 100% de uma coluna de 705px viraria uma faixa atravessando a tela.

⚠️ **Por que o corpo é FLUIDO e não um número fixo.** Foram varridos 5 paddings × 6 corpos em 6 larguras: **nenhum par fixo sobrevive à faixa inteira**. A largura que o texto pede cresce com a tela, então qualquer valor que caiba a 360px fica pequeno demais a 430px — e o melhor candidato fixo (pad 20 / 15,5px) ainda estourava o "Como funciona" por 5px a 360px. A `4.45vw` acompanha o aparelho e devolve os 18px cheios a partir de ~405px.

🔎 **Os números são TETO MEDIDO, não chute.** Foram três rodadas com o usuário, cada uma pedindo mais tamanho. Varreduras de padding × corpo × largura em cada uma; o valor final é o maior corpo que mantém folga sadia na **largura crítica, que é 360px**. Evolução do corpo a 375px: **18px (quebrava em 2 linhas) → 15,4 → 16,1 → 16,7px**, e a largura do botão de 302 → **339px (coluna cheia)**. A partir de 405px ele já roda nos 18px cheios do desktop.

✅ **Conferido: 1 linha em 360 · 375 · 390 · 414 · 430 · 768px, sem estouro horizontal.** Larguras do botão da hero: 324 · 339 · 354 · 394 · 420px (o teto). Altura estável em 57–60px (quem manda é o `min-height:56px`, não o padding). **Desktop intacto** — a regra vive dentro do breakpoint, e a 1358px os quatro seguem 18px / padding 18px 34px. Em telas muito estreitas o piso de 14px não basta e volta a quebrar — comportamento aceito, aparelho de 320px é residual.

💡 **Onde ainda há corpo sobrando, se um dia quiserem:** o teto é do **"Como funciona"**, não da hero. A hero tem container mais largo (a `.hero .wrap` usa 18px de padding, não 24) e label mais curto, então **sozinha ela aguentaria mais**. Para aproveitar isso seria preciso ou deixar os CTAs com corpos diferentes — o usuário já optou por **consistência entre os quatro** quando o assunto foi o peso — ou encurtar o label "Quero dar o primeiro passo agora".

📌 **A referência trazia mais duas coisas que NÃO foram aplicadas** (não foram pedidas, e uma delas mexe em decisão já fechada): (a) um **segundo botão de WhatsApp em verde logo abaixo do CTA**, empilhado — aqui o WhatsApp vive no botão flutuante, e o ícone dentro dos CTAs está na lista de rejeitados; (b) **texto do botão em caixa alta**. Se o assunto voltar, vale lembrar que a caixa alta do botão é decisão independente da caixa alta dos títulos (que segue pendente).

⚠️ **Quem dita esses números é o botão do "Como funciona"** ("Quero dar o primeiro passo agora"), o label mais longo dos três. **Ao mexer em qualquer texto de CTA, remedir por ele.**

🚨 **PENDENTE — o CTA final não fecha em uma linha, e não é problema de tipografia.** Ele melhorou de 3 para 2 linhas, mas o gargalo é o **container**: o `.finalcta .box` tem `padding:clamp(34px,6vw,64px)`, então a 375px sobram só **259px úteis** — 21% da largura da tela vira padding do cartão. Contas medidas:
- Só encolhendo o corpo: precisaria de **~9,4px**. Fora de cogitação.
- Só abrindo o box (34 → 20px no celular): precisaria de ~12px. Ainda não.
- **Só as duas coisas juntas resolvem:** abrir o box para ~20px **e** tirar a palavra "agora" do label (que o deixaria idêntico ao da hero) dão ~15px — aí fecha.
- ⚠️ Tirar "agora" é o **método de remoção de palavras já autorizado** para botões (hero e Sobre), não uma exceção nova. Mas mexe na copy do CTA final e no visual da seção 12, **então é decisão do usuário** — não foi feito.
- 💡 Vale notar que a sugestão nº1 já registrada para a seção 12 (remover o `max-width:44ch` do `.inner`) é de desktop e **não ajuda aqui** — no celular o `.inner` já perde o `max-width` pelo breakpoint de 960px.

#### ✅ LOGO DA NAVBAR: 58px → 52px (04/09/2026)

O usuário pediu a logo "um pouco menor". **`.brand img{height:52px}`** — a largura vem sozinha da proporção do arquivo (747×285), então caiu de **152 para 136px**.

⚠️ **Existe um piso, e ele é de legibilidade, não de gosto.** O subtítulo "GALLASSINI" é tracejado e de traço fino. Renderizados 58 · 52 · 48 · 44px em escala 1:1 sobre o azul: **a 44px o subtítulo degrada visivelmente**, o que confirma o registro antigo dos 46px. **52px foi o menor degrau que passou limpo.** Não descer daqui sem olhar o resultado renderizado — medir não resolve, tem de ver.

**Onde isso mais pesa é no celular, não no desktop:** a 375px a logo ocupava **40% da largura da tela**; agora ocupa 36%. No desktop são 10%.

⚠️ **A barra continua em `min-height:78px` e o header em 79px** — o pedido foi a logo, não a barra. Com 52px de logo mais os 16px de padding do `.nav`, o conteúdo dá 68px, então quem manda na altura continua sendo o `min-height`. **Se um dia a barra encolher junto, o `scroll-padding-top` do `<html>` e o `scroll-margin-top` das seções (hoje 84px, os dois) têm de cair na mesma medida** — senão cada âncora do menu passa a parar deixando um vão sob o cabeçalho.

#### ✅ RODAPÉ: SÍMBOLO DA MARCA NO LUGAR DO MONOGRAMA (04/09/2026)

O `<div class="mark">RG</div>` — quadrado de 40×40 com as letras em CSS, último resto do monograma que a navbar já tinha aposentado — deu lugar ao **`rg_ico_light.png`**, o símbolo sozinho, a **64px de altura** (largura 36px, vem da proporção 317×557 do arquivo).

🔑 **Só o símbolo, sem o nome — e o usuário levantou isso sozinho, com razão.** A linha imediatamente abaixo já diz "Dr. Rafael Gallassini · Médico" em texto. O logo horizontal imprimiria o nome **duas vezes, a 16px de distância**. É o mesmo tipo de eco que este arquivo já registra em outros pontos da página.
- **Pelo mesmo motivo a imagem é decorativa** (`alt=""` + `aria-hidden`): o leitor de tela não deve ouvir o nome duplicado. O monograma anterior também era `aria-hidden`, então nada mudou de semântica.
- **Tamanho: 52px — o mesmo do logo da navbar**, a pedido do usuário ("para ficar harmônico"). Passou por 64px numa primeira rodada (escolhido vendo, contra o bloco de texto do rodapé) antes de o usuário pedir o pareamento.
- 🔑 **E o pareamento é real, não só o número igual — isso foi medido nos arquivos.** A dúvida legítima era: a navbar exibe o **conjunto** (símbolo + letreiro, 747×285) e o rodapé exibe **só o símbolo** (317×557), então `height` igual poderia não significar símbolo do mesmo tamanho. **Medido: o símbolo ocupa 100% da altura do lockup horizontal** (162×285) e 100% da altura do arquivo do ícone, e as proporções batem (**0,5684 vs 0,5691**). Logo, os dois a 52px renderizam **idênticos: 52×30px**. Confirmado no DOM.
- ⚠️ **POR ISSO OS DOIS ANDAM JUNTOS.** Se a altura do `.brand img` mudar, **mudar a do `.foot-brand .mark` na mesma medida** — senão a harmonia se perde e ninguém descobre de onde veio. Há comentário no CSS nos dois lugares.
- ✅ **O monograma "RG" sumiu do rodapé.** O que resta na página é o `.portrait .mono`, que é o **placeholder do Slot 3** e sai quando a foto do Dr. Rafael entrar.

**Removido junto, a pedido:** o parágrafo do **"Aviso legal"** no `.foot-legal`. Sobrou só a linha de copyright. 🚨 **Isso é compliance, não layout** — ver Regras invioláveis §2, onde ficou registrado o que a página perdeu.

#### ✅ SISTEMA TIPOGRÁFICO UNIFICADO (04/09/2026) — a partir de ablocacoesdeveiculos.com

O usuário mandou a landing de motos como referência de harmonia e pediu a análise antes da aplicação; depois delegou as três decisões em aberto ("faça da forma que achar melhor, se eu não gostar a gente volta").

**O que a referência faz, medido no DOM dela:** 24 títulos, **uma** entrelinha (1,08), **um** peso (800), tracking como **razão constante** (−0,02em; só o H1 a −0,03em), H2 de **46px em todas as seções**, subtítulo em **duas** definições (20px sob H1, 18px sob H2, ambos 400/1,55), e **título e subtítulo na mesma medida** (614px). Padding de seção 96px e entrelinha de corpo 1,55 — **iguais aos nossos já**.

**O diagnóstico:** o ritmo base da nossa página já estava certo. A desarmonia era só excesso de exceção no sistema de títulos.

| | antes | depois |
|---|---|---|
| entrelinhas de título | **3** (1,02 · 1,08 · 1,12) | **1** (1,08) |
| corpos de H2 | **3** (48 · 40 · 44) | **1** (46) |
| razões de tracking | **3** (−0,035 · −0,025 · −0,01) | **2** (−0,03 no H1, −0,02 no resto) |
| definições de subtítulo | **4** | **2** (19px sob H1 · 18px sob H2) |
| medida título vs subtítulo | 511 vs 675px | **640px nos dois** |

**Página: 10.231 → 9.935px (−296px).** Sem estouro horizontal em 1358 · 960 · 768 · 375px.

⚠️ **O nível 1 dos subtítulos foi de 20 para 19px em 04/09/2026**, a pedido do usuário ("diminua um pouquinho" o subtítulo da hero). **19 é o piso:** o nível 2 (`.lead`/`.intro`/`.mech-intro`, sob os H2) está em **18px**, então a 18 os dois níveis viram um só e a hierarquia título/subtítulo da hero deixa de existir. Não descer daqui sem decidir que o sistema passa a ter **um** nível de subtítulo, e não dois.
- **É decisão de presença, não de layout:** de 17 a 20px o texto fica em **3 linhas** de qualquer jeito. A hero encolheu de 736 para 732px.
- Contraste no pixel refeito (o bloco encolheu e ele fica sobre a foto no desktop): **H1 8,56 · subheadline 6,60 · microcopy 8,93**. Todos aprovados.

⚠️ **A subheadline da hero tem medida PRÓPRIA de 560px**, menor que a coluna de 640px — o usuário pediu para puxar a borda **direita** para dentro só nela, em 04/09/2026.
- **Os `52ch` anteriores eram INERTES:** davam ~688px e a coluna de 640 já limitava antes. Trocado por **px**, que é o que realmente morde.
- **560 é escolhido, não arredondado:** a **540px o texto ainda cabe em 3 linhas e a 520 quebra para 4**; os 560 deixam 20px de folga antes desse degrau. É também onde o rio da direita fica mais parelho — as duas primeiras linhas quase iguais e a terceira em dois terços, contra a terceira com só 226px quando a medida era 640.
- ⚠️ **É inerte no celular de propósito:** lá a coluna tem 339px, então 560 nunca morde. O ajuste vale só onde há largura sobrando (≥ ~608px de viewport).

⚠️ **NÃO confundir com `--maxw`.** Numa rodada anterior eu interpretei "diminuir a largura do desktop" como o container da página e baixei o `--maxw` de 1080 para 1040 — **estava errado e foi revertido**. Aquele token governa o `.wrap` de **todas** as seções e a `.nav`; encolhê-lo estreita as **grades** (os cartões passaram a quebrar em mais linhas, +112px de página) e **não toca** no título nem no subtítulo, que estão presos ao `--measure`. São três larguras independentes: `--maxw` (página), `--measure` (título e subtítulo de seção) e o `max-width` próprio da subheadline da hero.

🔑 **Token novo `--measure:640px`** — a medida que título e subtítulo dividem. Casa com o `max-width` da `.hero-copy`, então a página passou a ter **uma medida só**.
- ⚠️ **EM PX, NUNCA EM `ch`.** Descoberto medindo: `24ch` dá **614px no título** (Goldoni) e **270px na intro** (Montserrat), porque `ch` é a largura do "0" **da fonte do elemento**. Com duas famílias, `ch` nunca produz medida compartilhada. Foi a armadilha central desta rodada.

**A exceção de 40px do Mecanismo morreu.** Ela existia porque a 48px o título virava torre de 6 linhas na coluna de 523px. **A 46px ele cabe em 5** — medido. Custo: +32px naquela seção, pago com folga pelo resto.

**O `.lead` manteve o peso 600 — é a única exceção do sistema, e é deliberada.** Ele aparece **uma vez só na página** (a linha de posicionamento sob o nome do médico, na seção "Sobre") e faz um trabalho que nenhum outro subtítulo faz: separar o nome dos dois parágrafos densos. Sem o peso, título/posicionamento/corpo viram dois níveis em vez de três. O **corpo** dele foi unificado em 18px.
- ⚠️ **Cuidado de especificidade:** `.about-body p` (0,1,1) vence `.lead` (0,1,0) e estava impondo 17px por cima do sistema. O `font-size` está repetido em `.about-body .lead` de propósito.

**Duas regras mortas removidas** (mesmo critério dos eyebrows): `.sec-head` (0 usos no HTML) e `.sec-dark .lead` (o único `.lead` da página vive em seção clara, então a regra nunca era aplicada).

#### 🚨 CTA FINAL: a "sugestão nº1" registrada aqui ESTAVA ERRADA — corrigida

O `PROJETO.md` registrava que remover o `max-width:44ch` do `.finalcta .inner` derrubaria o título de 5 para 4 linhas, "custo zero". **Medido hoje: sozinho ele é inerte.** O `44ch` dá ~449px na Montserrat de 16px e a coluna do grid já limitava em **447px** — quem manda é o grid, não o `max-width`.

Também estava errado o diagnóstico da altura: o título **já caía em 6 linhas antes**, com o corpo em 44px (285px). A unificação em 46px custou 13px, **não uma linha**.

**A alavanca real é o grid:** `.finalcta .grid` de `1.05fr .95fr` → **`1.25fr .75fr`**. A coluna de texto vai de 447 para **533px**, o título fecha em **4 linhas** (298 → 199px) e a caixa inteira cai de **827 para 671px**. A foto do Slot 7 fica em 320×427, ainda 3:4 confortável.
- ⚠️ **O `max-width:44ch` tinha de sair junto** — senão reimporia a largura antiga e a mudança do grid não faria efeito nenhum. Saiu também a regra órfã `.finalcta .inner{max-width:none}` do breakpoint de 960px.
- Este era **o único H2 da página que não recebia a medida**. Agora os 533px dele são o mais perto que a composição em duas colunas permite dos 640 do resto.

⚠️ **Ponto de retorno desta rodada:** cópia verificada por md5 em `scratchpad/antes-tipografia/` (`index.html`, `index-dark.html`, `PROJETO.md`). Foi feita porque havia **seis mudanças não commitadas** — um `git checkout` teria descartado a sessão inteira, não só esta.

#### ✅ A HERO GANHOU FOTO — fundo cheio (04/09/2026)

O usuário mandou o Drive com **28 fotos** do ensaio de 10/2024 (`Rede Social - Cor`, numeradas 01–30 sem a 12 e a 24; 14 horizontais 3:2 e 14 verticais 2:3, 2048px no maior lado). Escolhida a **09**, como **fundo cobrindo a hero inteira** — o caminho (a) que este arquivo registrava como opção.

**Arquivos:** `assets/Fotos/dr-rafael-hero-{1100,1600}.{avif,webp,jpg}`. O AVIF de 1600px pesa **45 KB**; o JPG é fallback.

🔑 **A LIÇÃO GEOMÉTRICA, e ela custou duas rodadas erradas.** A hero tem ~1,85:1 e as fotos são 3:2 (1,50). Com `object-fit:cover`, **a escala é pela LARGURA — a imagem inteira aparece na horizontal e `object-position` no eixo X NÃO FAZ NADA.** O corte é só vertical. Logo:
- **Não dá para "empurrar" o médico para a direita pelo CSS.** O arquivo tem de vir recortado.
- O que está no ar é um recorte de **1406×762 de um original 2048×1365**, calculado para pôr o rosto a **83% da largura**. **Ao trocar a foto, refazer o recorte; mexer no `object-position` não resolve.**
- **Como se chegou a 83%, em duas rodadas.** A 74% o corpo dele ficava parcialmente sob o painel de cor — o usuário pediu para levar mais à direita "para o corpo ficar mais evidente". Comparados 74 · 80 · 86% renderizados com o painel: a **80%** o torso, as mãos entrelaçadas e o relógio ficam inteiramente fora do painel; a **86%** ele cresce demais e o enquadramento aperta embaixo. O usuário pediu mais um empurrão e ficou em **83%** — o teto útil antes do aperto do 86%. **Empurrar para a direita = recorte MAIS ESTREITO** (1577 → 1459px), porque o recorte sempre começa na borda esquerda e o que se corta é o lado direito do original. Arquivos ficaram em 1440/1080px de largura. ⚠️ A 83% o recorte nativo é 1406px, então o de 1440 tem 2,4% de upscale — imperceptível, mas **se for além de 83% vale baixar as saídas junto**, senão o upscale cresce.
- **Contraste refeito a cada rodada** (o fundo sob o texto muda junto): a 80% deu H1 10,22 · sub 5,43 · micro 8,93; a **83%** deu **H1 8,54 · sub 6,76 · micro 8,93**. Todos aprovados. ⚠️ Note que o H1 caiu e a subheadline subiu — mover a foto **troca** qual bloco fica sobre a parte clara, então não dá para supor a direção: tem de medir.

⚠️ **As verticais não servem para fundo cheio.** A 10 foi a escolhida enquanto o plano era um card 4:5 à direita (e era ótima ali); em tela cheia o médico centralizado cai atrás do H1. Formato e tratamento andam juntos.

🚨 **NÃO CONFIAR EM DETECÇÃO DE PELE NESTE ENSAIO.** Escrevi um localizador de rosto por faixa YCbCr e ele apontou 62% onde o rosto estava a 37%: **as molduras douradas e a madeira caem na mesma faixa de tom que pele**. As posições que valem foram lidas no olho, com grade de porcentagem sobreposta — método barato e confiável, vale repetir. Posições reais medidas assim: 09 → 57% · 05 → 57% · 22 → 53% · 20 → 42% · 26 → 40%.

**O véu não é enfeite.** São duas camadas: um degradê horizontal (97% de opacidade à esquerda, onde vive o texto → 30% à direita, onde está o médico) e um escurecimento geral de 34%. É o que segura o contraste sem lavar a foto inteira.

✅ **TRATAMENTO FINAL (04/09/2026): PAINEL DE COR + FOTO**, no padrão da referência `ablocacoesdeveiculos.com`, que o usuário trouxe.

**Não é um véu sobre a foto inteira.** A esquerda é **azul chapado** (a foto não aparece ali), a direita é a foto em **força total, sem escurecimento nenhum**, e entre as duas há uma transição suave. Um único degradê horizontal resolve:

```
var(--navy) 0% → 52%  ·  rgba(navy,.55) 63%  ·  rgba(navy,0) 72%
```

**Os dois números que governam tudo — 52% e 72%.** O 52% precisa passar do fim do bloco de texto (~59% da largura) o bastante para o degradê ainda cobrir, mas **não tanto que engula o médico, que está a 74%**. É um corredor estreito entre duas restrições.

🔧 **Contraste medido no pixel, e ele MELHOROU em relação ao véu anterior:**

| elemento | véu antigo | **painel** | limiar |
|---|---|---|---|
| H1 | 9,59 | **13,03** | 3,0 |
| subheadline | 7,36 | **5,63** | 4,5 |
| microcopy | 8,51 | **8,93** | 4,5 |

**A foto ficou mais viva E o texto mais legível ao mesmo tempo** — porque a cor deixou de ser um filtro sobre tudo e virou um bloco onde o texto realmente vive.

**O caminho até aqui, para não repetir:** (1) véu em degradê sobre a foto inteira + 34% de escurecimento geral — funcionava, mas lavava a imagem; (2) sem véu nenhum, a pedido do usuário, só para ver — a foto ganhou muito, mas **reprovava** (H1 1,34 · sub 1,00 · micro 1,96), quebrando nas **arandelas acesas** atrás do H1 e no **braço iluminado** atrás da subheadline; (3) o painel, que é a referência e resolve os dois lados.

#### ✅ A HERO NO ESTREITO: TEXTO EM CIMA, FOTO EM BLOCO EMBAIXO (04/09/2026)

O usuário mandou o print do mobile da mesma referência e pediu esse arranjo. **Até 960px a foto deixa de ser fundo e vira um bloco cheio abaixo do texto, sem véu nenhum.**

**Por que o tratamento do desktop não sobrevive aqui:** no largo, o painel de cor cobre a esquerda e a foto ocupa a direita. No estreito o texto passa a ocupar a largura toda — **não sobra lado nenhum para a foto respirar**. A saída é parar de sobrepor.

**Como foi feito:**
- `.hero` vira `display:flex;flex-direction:column`. A `<figure>` vem **antes** do `.wrap` no DOM (ela precisa disso para funcionar como fundo no desktop), então quem inverte a ordem visual é o **`order`** — a ordem do DOM continua a mesma para o leitor de tela.
- `.hero-bg` volta ao fluxo com `position:relative;inset:auto`, largura total e `height:clamp(280px,86vw,560px)`. O teto de 560px existe porque a 4/5 puro um tablet de 900px daria **1125px só de foto**.
- ✅ **Menos mesa (04/09/2026, 3ª rodada).** O usuário pediu para aparar o rodapé — mostrar menos tampo — **sem mexer no topo**, que já estava certo. **Não foi preciso recorte novo:** bastou baixar a altura do bloco de `105vw` para **`86vw`**. Com o bloco mais largo que alto, o `cover` passa a escalar pela largura e sobra corte vertical; como o `object-position` está preso a **12%**, **todo esse corte sai do rodapé**. No celular: bloco de 394 → **323px**, com **53px de mesa a menos** e a cabeça exatamente onde estava.
- ⚠️ **É esse par (`altura` + `object-position:12%`) que decide o que se perde.** Altura menor com enquadramento no topo = corta mesa; enquadramento mais alto em % = cortaria a cabeça. Tablet não muda: a 768 e 900px o teto de 560px já governa.
- `.hero::before{display:none}` — **sem véu sobre a foto**, como na referência. O texto fica sobre o azul chapado da própria `.hero`.
- ✅ **Transição no topo da foto (04/09/2026, 2ª rodada).** O usuário apontou dois pontos: a foto estava baixa demais e encostava no azul numa **aresta dura**. Duas correções:
  - **O bloco subiu:** `margin-top` de `clamp(28px,6vw,44px)` para `clamp(8px,2vw,16px)`. O vão entre a microcopy e a foto caiu de ~48 para **22px**.
  - 🚨 **Mas o pedido era outro, e eu errei na 1ª tentativa: ele queria o CONTEÚDO subir, não o bloco.** Havia muito teto/parede acima da cabeça dentro da foto. **`object-position` não resolvia:** a fonte é 1:1 num bloco de 0,95:1, então no celular **não sobra folga vertical nenhuma** para deslocar — o valor é inerte ali. Foi preciso **refazer o recorte**.
  - **Topo da cabeça de 27% para 12% do bloco** (medido com grade horizontal sobre o recorte). Recorte novo: **1132×1132**, cortando 237px do topo do original. No celular a cabeça passou de ~128px para **69px** abaixo do último texto.
  - ⚠️ **Recorte e transição são acoplados.** A transição de 128px cobriria a cabeça inteira no recorte novo — caiu para **64px**. **Ao mexer num, remedir o outro.**
  - ⚠️ **`object-position` foi para `50% 12%`** por causa do TABLET: lá o bloco fica 1,58:1 e aí sim sobra corte vertical. A 38% a cabeça saía fora da moldura.
  - **`.hero-bg::after` com degradê vertical** — opaco no topo, transparente a 64px. **É o mesmo gesto do painel do desktop, girado 90°:** lá a cor é opaca à esquerda e some à direita; aqui é opaca em cima e some descendo. Sem ele a foto começa numa aresta.
  - ⚠️ **As paradas são em PX, não em %.** A altura do bloco varia de 300 a 560px; em `%` a transição encolheria junto na tela pequena, que é justamente onde ela mais precisa aparecer. Em px ela ocupa 17% do bloco a 360px e 11% a 900px — mais forte onde a aresta seria mais visível.
  - ⚠️ **Os 128px param ANTES do rosto.** Com `object-position:50% 38%` ele cai por volta dos 150px do topo do bloco. **Ao mexer num dos dois, conferir o outro.**
- `padding-bottom:0` na `.hero`, para a foto encostar na seção seguinte em vez de sobrar uma faixa de azul.

🔑 **O ARQUIVO É OUTRO, e isso é a mesma lição de sempre: formato e tratamento andam juntos.** O recorte do desktop é uma faixa **1,85:1 com o médico a 83%** — num bloco vertical ele ficaria minúsculo e encostado na borda. Foi gerado um recorte **1:1 centrado nele** (`dr-rafael-hero-mob-*`, 640 e 900px), servido por `<source media="(max-width:960px)">`. ⚠️ **As `<source>` com `media` têm de vir PRIMEIRO** no `<picture>`: o navegador usa a primeira que casar.

✅ **Conferido em 360 · 375 · 430 · 768 · 900 · 1358px, sem estouro** (transição incluída; a 1358 ela é `none` e o painel do desktop segue ativo). A foto fica em ~0,95:1 no celular (375×394) e abre para 1,58:1 no tablet — a composição aguenta, com ele à esquerda e as telas preenchendo a direita.

✅ **Ganho de brinde:** no estreito o texto voltou a ficar **sobre cor chapada**, então **a auditoria de contraste do projeto volta a cobrir a hero ali**. Ela só é cega onde o texto está sobre a foto, que agora é só o desktop.

⚠️ **Ao medir `currentSrc` depois de redimensionar sem recarregar, o valor mente:** o navegador mantém o candidato já baixado e o desktop aparece "servindo" a imagem do mobile. **Recarregar antes de concluir.** Confirmado com carga limpa: desktop serve `dr-rafael-hero-1440.avif`, estreito serve `dr-rafael-hero-mob-900.avif`.

**Estado:** desktop conferido a 1358px, sem estouro, hero em 736px e H1 em 5 linhas. **Mobile e tablet fechados.**

#### 📸 O ENSAIO — o que ele cobre e o que não cobre

- ⚠️ **A direção de arte escrita neste arquivo está DESATUALIZADA.** Ela pede "luz natural neutra/fria, baixa saturação, fundos limpos, muito espaço negativo". O ensaio é o oposto: **luz quente de tungstênio, alto contraste, fundo ornamentado** (painéis azul-petróleo, molduras douradas, Chesterfield, tapete persa). **Mas ele combina com a marca melhor do que a direção escrita** — aquela direção é de quando a página era marinho + limão. O azul-petróleo da parede e o ouro das molduras são quase o Azul Profundo e o Dourado do manual. **Reescrever a direção a partir deste ensaio, não rejeitar as fotos.**
- 🚨 **O ensaio NÃO tem imagem clínica nenhuma.** Não há consultório, exames, atendimento nem equipe. **Os slots 4, 5 e 6 (os três passos do "Como funciona") continuam sem material** e precisam de produção. O ensaio cobre a hero, o Slot 3 (retrato do "Sobre") e provavelmente o Slot 7.
- ✅ **Compliance:** todas as 28 são retratos do médico, vestido. Nenhuma foto de corpo, nenhum antes-e-depois.
- **A hero não é nenhum dos 7 slots numerados** — ela não tinha slot. É um oitavo, e a tabela dos 7 continua válida como está.
- ⚠️ **`assets/Fotos/` não está no `.gitignore` e o repositório é PÚBLICO.** Hoje só há os 6 arquivos derivados da hero. As 28 originais estão no scratchpad, fora do repositório.

#### 🎨 SLOT 1 — quatro rodadas de imagem gerada, e o que cada erro ensinou (05/09/2026)

O usuário pediu para **criar** a imagem do Slot 1 (seção "Você se reconhece?") com o Higgsfield, aprovando o cenário antes de gerar. **Nada foi instalado ainda** — a decisão está aberta.

📐 **PRIMEIRO ACHADO, e ele invalida a tabela dos 7 slots: o Slot 1 NÃO é 3:4 nem 4:5.** Medido, ele renderiza em **425×686 — proporção 0,619**, porque `.figure.fill` tem `height:100%` e estica para acompanhar a coluna de cartões. Como o `object-fit` é `cover`, **uma imagem 3:4 perde ~17% da largura no recorte**. Gerar em **2:3** (0,667) e compor com folga nas laterais. ⚠️ **A tabela dos 7 slots, mais abaixo, está desatualizada nesse ponto.**

🚨 **TRÊS DIREÇÕES ERRADAS ANTES DE ACERTAR O ENUNCIADO.** Registro porque o padrão do erro se repete e é caro:

1. **Natureza-morta na sala do ensaio** (cadernos e fita métrica na mesa do médico). Bonita e coerente com a hero — **mas ancorada no mundo do MÉDICO.** A seção fala do **leitor**: as tentativas que falharam aconteceram na cozinha dela, não numa biblioteca de painéis com molduras douradas. *O que compartilhar com o ensaio é o TOM, não o LUGAR.*
2. **Geladeira na madrugada / beira da cama.** A geladeira saiu com a pessoa **sem camisa** — pele exposta, exatamente o que a regra de compliance proíbe — e com uma cozinha degradada, que lê como julgamento e não como identificação. A beira da cama funcionava, mas **dramatiza angústia**, o que é ruim para Ads (ver abaixo).
3. **Mãos na xícara de café.** O usuário matou com uma frase: *"uma mão na xícara de café não diz nada."* Estava certo — **eu estava perseguindo clima em vez de significado.**

🔑 **O ENUNCIADO CERTO: a seção é sobre REPETIÇÃO, não sobre cansaço.** O que os quatro cartões têm em comum está na própria copy — *"já perdeu a conta de quantas vezes recomeçou do zero"*, *"cada tentativa que não durou"*. A imagem certa mostra o **rastro acumulado de tentativas que não pegaram**, no mundo dela. Foi só depois disso que as gerações passaram a servir.

⚠️ **RESTRIÇÕES QUE O USUÁRIO TROUXE E QUE VALEM PARA QUALQUER IMAGEM FUTURA DA PÁGINA:**
- **O público é majoritariamente feminino.**
- **A página vai ser destino de anúncio no Google Ads.** Emagrecimento é categoria sensível: **imagem que dramatiza sofrimento ou insatisfação com o corpo atrai revisão.** Preferir cotidiano neutro. Isso **desqualificou a cena da beira da cama**, que eu havia recomendado.
- **"Não inventar muito"** — nada conceitual demais.
- **Nada de comprimido, cápsula ou frasco de remédio**, mesmo a copy citando "remédio por conta própria". Medicação numa página médica de emagrecimento é o que mais atrai revisão.

🔧 **Higgsfield — o que funciona e o que engana:**
- Modelo **`nano_banana_pro`**, `aspect_ratio: "2:3"`, `resolution: "2k"` → sai 1696×2528. **2 créditos por imagem** (confirmado com `get_cost`).
- 🚨 **"Out of credits" pode ser MENTIRA.** Um lote falhou com *"Out of credits on plus (monthly) plan"* e eu repassei isso ao usuário como fato. **O saldo era 100 e a imagem custa 2.** Reenviado como envio único, passou na hora. **Conferir `balance` antes de anunciar falta de crédito.**
- ⚠️ **O modelo escreve texto mesmo com "no lettering" no prompt.** A melhor bancada saiu com **"THE DIET PLAN" e "HERBAL TEA" em inglês**, legível no tamanho de exibição — inaceitável numa página em português.
- ⚠️ **E o remédio tem efeito colateral:** ao exigir tudo sem rótulo, os objetos viraram um **jogo bege combinando, cara de catálogo** — e sumiu justamente o que dava sentido à cena, que era serem coisas **de fases diferentes que não combinam**. Se for refazer, pedir rótulos **em português**, não rótulo nenhum.

📁 **As 12 candidatas estão em `assets/Fotos/_candidatas/`, fora do versionamento** (entrada nova no `.gitignore`). A recomendação atual é a **`09-GAVETA-A.png`**: vista de cima de uma gaveta com fita métrica, caderninho, colheres medidoras, sachês, balança e uma folha impressa — bagunçada de verdade, objetos de origens diferentes, sem pessoa, sem corpo, sem texto legível. Cobre os quatro cartões porque cada objeto é uma tentativa distinta.
- ⚠️ **Duas ressalvas sobre ela, ainda não resolvidas:** é **vista de cima**, ângulo que nenhuma outra imagem da página usa; e a madeira clara é mais fria que o ensaio — na seção creme funciona, na versão escura vai puxar atenção.
- ⚠️ **Elas ficaram fora do scratchpad de propósito: o scratchpad foi limpo DUAS VEZES nesta sessão**, levando junto tudo que estava baixado. As URLs do Higgsfield sobreviveram e permitiram recuperar — **guardar sempre a URL de resultado, não só o arquivo.**

#### 🚨 O SERVIDOR DE PREVIEW SERVIU OUTRO PROJETO (05/09/2026)

A porta **5173** foi tomada por um `python.exe` de **outra sessão**, servindo **outra pasta**. O preview parecia normal, mas o DOM trazia classes que não existem aqui (`recognition-layout`, `section-heading`) e **o Slot 1 nem existia**.

**Como pegar:** comparar o que o servidor entrega com o arquivo em disco — **48 KB servidos contra 86 KB em disco**. O `.claude/launch.json` foi movido para a **porta 5181**.

⚠️ **É a terceira vez que o preview engana nesta sessão.** As outras duas: `currentSrc` mentindo depois de redimensionar sem recarregar (o navegador mantém o candidato já baixado), e prints saindo com a foto em branco porque a captura acontece antes da pintura. **Regra: antes de concluir qualquer coisa sobre a página, confirmar que o servidor é o certo, recarregar, e repetir o print se vier estranho.**

#### 🚨 A GOLDONI SÓ TEM CAIXA ALTA — decisão pendente

Medido no navegador: `"a"` e `"A"` têm a mesma largura (65px), `"g"` e `"G"` também (56px), `"emagrecer"` e `"EMAGRECER"` idem (519px). **Os slots de minúscula contêm desenho de maiúscula.**

Resultado: **todos os títulos da página estão em caixa alta**, e o H1 da hero passou de 5 para **6 linhas**. ✅ **As 6 linhas foram resolvidas em 04/09/2026** baixando o teto do `clamp` para 60px — ver o bloco logo acima. **A decisão sobre a caixa alta continua aberta.**

Isso contradiz uma decisão registrada neste arquivo — *"título em caixa alta: testado (variações A–E) e descartado; escolhida a variação B, caixa mista"*. **Mas o contexto mudou:** a marca inteira é caixa alta, o logo é caixa alta, e o que foi rejeitado era caixa alta na tipografia antiga. Pode ser que agora funcione.

Três saídas oferecidas, **nenhuma escolhida**:
1. Aceitar — é a natureza de uma fonte de titulação e combina com o logo.
2. Goldoni só nos títulos de seção, Playfair no H1 da hero (que é o mais longo).
3. Pedir a quem fez a marca o corte de texto da Goldoni, se existir.

`@font-face` está declarado com `font-weight:100 900` de propósito: o arquivo tem um peso só, e o range impede o navegador de fabricar falso-negrito, que borraria uma serifada de alto contraste. Playfair Display fica de reserva na mesma declaração.

#### ✅ Auditoria de contraste — ferramenta nova, vale reusar

Verificar pares "a mão" não bastou: foi assim que os placeholders escaparam na versão escura. Foi escrita uma **auditoria que percorre o DOM**, calcula o fundo efetivo de cada elemento de texto (subindo a árvore até achar fundo opaco) e mede o contraste real.

Ela achou coisas que a lista manual não achou, inclusive **um defeito que estava no ar desde antes da troca de paleta**: o texto legal do rodapé a **2,93:1**, porque usava `--ink-3` — a tinta da paleta *clara* — sobre o rodapé escuro.

**Estado: 164 elementos auditados, 0 reprovados** (clara e escura).

⚠️ **Limitação conhecida:** a auditoria lê `background-color` e **não enxerga gradiente**. O "RG" do retrato aparece reprovado, mas está sobre o degradê azul. Falso positivo.

#### A versão escura (`index-dark.html`)

Pedida pelo usuário só para avaliação. **É gerada, não editada** — `python gerar-dark.py`. Rodar sempre que o `index.html` mudar.

Ela é quase só um `:root` diferente, o que só foi possível por causa do passo 1. Cinco degraus de fundo: `#0B111F` (prova/rodapé) < `#0F1729` (chão) < `#16203A` (faixa secundária) < `#1C2747` (faixa escura) < `#1E2A4B`/`#26314F` (cartões). A alternância clara/escura da página sobrevive, invertida.

⚠️ **Ela expôs dois defeitos de token que existem também no arquivo principal** — ver "Notas técnicas": `--off` sobrecarregado e `color:var(--navy)` assumindo fundo claro.

### ✅ Sessão de 03/09/2026 (tarde) — seções 4 e 7

**1. Fecho da seção 4 reancorado.** A frase "Sem cardápio de gaveta…" estava `text-align:center`, 537px, começando em **x=364** — enquanto título, painel e corpo começam em **x=117**. Terceiro eixo de alinhamento: o mesmo defeito que as rodadas do B já tinham corrigido no resto da seção. Era também o texto mais apagado dali (`#C7CBD8`, contra `#D6D9E4` do corpo) e repetia o gesto da `.turn`, que fecha a **seção 3** também em serif centralizada, na versão forte. **Cinco tratamentos comparados; o usuário escolheu o D:** à esquerda, na medida do bloco (1032px), `clamp(21px,3.4vw,26px)`, `#E4E7F0`, `border-top:1px solid var(--navy-500)` + 30px de respiro. A frase saiu do segundo `<div class="wrap">` e foi para **dentro do `.wrap.reveal`** — corrigiu a animação (ela aparecia de imediato enquanto o bloco acima entrava) e virou o rodapé do bloco também na estrutura. ❌ Descartada a variante em duas colunas: cai na armadilha do B9 — metades alinhadas pelo topo leem como paralelas, não como sequência.

**2. Parágrafo do mecanismo quebrado em dois.** Eram 73 palavras em 8 linhas, com **frase 1 de 17 e frase 2 de 56** — seis das oito linhas eram uma frase só. Viraram dois `<p class="mech-body">`, mesma tipografia. O intervalo é `.mech-body+.mech-body{margin-top:…}` — **este é o botão de ajuste.** Passou por `1.55em` → `0` (o usuário pediu para tirar, para avaliar a estrutura) → **`1.55em` de novo, depois do corte N2**. `1.55em` = exatamente uma entrelinha; medido em 26,34px = 1,00 linha, igual no desktop e no mobile. ⚠️ Foi oferecida e **recusada** a variante de dois níveis (afirmação 21px off-white + explicação apagada): ela resolveria também o fato de `.mech-intro` e `.mech-body` terem **a mesma cor exata** (`#D6D9E4`), o que **continua em aberto**. ❌ Testado e rejeitado: `<strong>antes</strong>` em limão — cai logo abaixo da célula limão do painel e vira limão demais num trecho vertical curto.

**3. Seção 4 encurtada — 4ª exceção à regra 1.** O usuário pediu versão resumida; era pendência antiga deste arquivo. **Método: só remoção de palavras**, o mesmo da hero e do botão do "Sobre". Três níveis oferecidos, aplicado o **N2**: 92 → **68 palavras** (intro + parágrafos). Saíram `A partir da sua história, dos seus exames e da avaliação da sua composição corporal,` · `metas realistas,` · `(alimentação, comportamento e, quando indicado clinicamente, medicação)`; o `é` virou `É` — caixa, não palavra nova. **Nada se perdeu na página:** o trio história/exames/composição corporal segue no card 1 dos Diferenciais; a medicação sob indicação clínica segue na seção 7 e na 3ª pergunta do FAQ. **Preservado de propósito:** `investiga esse conjunto **antes**`, `se sustente` e `em vez de virar mais um ciclo de perder e recuperar` — este último, depois da reescrita do "Sobre", só existe aqui. ❌ **Recusado o N3** (apagaria a linha de intro): contraria o achado já registrado de que a sequência é **situação → agitação → virada**, e essa linha é a agitação.
- ✅ **A validação é automática e vale reusar:** o script testa se o texto novo é **subsequência** do original (palavra a palavra, ignorando caixa e pontuação) e aborta se alguma palavra tiver sido inventada. É a forma barata de garantir a regra 1 em qualquer corte futuro.
- **Saldo da seção 4:** 1166px → 1210px (fecho D) → 1131px (N2) → **1157px** (linha pulada). Terminou **abaixo de onde começou**, com o fio de fechamento e a frase maior de brinde.

**4. Seção 7 — dois itens removidos, a pedido do usuário.** Saíram **"Plano alimentar individualizado"** e a **nota interna** *"(Nota: revisar a lista com o Dr. Rafael…)"* — esta era lembrete de produção e nunca deveria ir ao ar. A regra `.note-inline` ficou sem uso e saiu junto (mesmo critério dos eyebrows). Depois, para fechar a grade, saiu também **"Acompanhamento contínuo"**. **Lista: 8 → 7 → 6 itens. Seção: 918 → 826 → 695px. Grade fechada em 3×2**, sem cartão órfão — com 7 ficava 3/3/1, o mesmo "problema de 3+1" que os Diferenciais já resolveram virando 2×2.
- **Critério do segundo corte:** o que já está dito em outro lugar. "Acompanhamento contínuo" repete a mesma promessa em **8 outros pontos**, quase palavra por palavra nas **duas seções vizinhas** — card 3 dos Diferenciais (logo antes) e passo 3 do "Como funciona" (logo depois).
- **Vice-campeão: "Suporte da equipe"** — item mais fraco da lista (único que não é ato médico), mas "equipe" aparece 7 vezes **sempre sobre contato e agendamento**, então o suporte *entre* as consultas é a única informação exclusiva dele. Por isso perdeu.
- ❌ **Não cortar destes 6:** "Solicitação e interpretação de exames" e "Tratamento medicamentoso quando indicado" — juntos são a resposta da 1ª pergunta do FAQ e a razão de procurar um *médico* e não um nutricionista. Mesma lógica que protegeu "Uso de medicações".

**5. Seção 7 — a lista perdeu as caixas.** Depois de comparar quatro tratamentos com as seções 4, 5 e 6 na sequência real, o usuário escolheu o **2**: mesma grade `auto-fit`, mas cada item sem fundo, sem borda, sem sombra e sem raio — só um **fio de 1px acima**. Motivo: era o terceiro bloco de cartões seguido (3, 6, 7, 8 e 9 são todas grades de caixa), e nenhum outro bloco da página é uma lista sem moldura. **Seção: 695px → 679px.**
- ⚠️ **O `gap` subiu de 16px para `34px 44px`, e isso não é enfeite.** Sem a moldura, é o vão que separa as colunas. A 16px os fios de colunas vizinhas quase se encostam e a linha lê como uma régua quebrada em vez de três colunas independentes. **Se mexer no número de colunas, remedir o vão.**
- ✅ **A grade fecha em todos os breakpoints:** 1180px → 3 colunas (3/3) · 900px → 2 colunas (3/3) · 375px → 1 coluna. Com 6 itens isso é automático; **com 7 volta a quebrar** (ver pendências abaixo).
- ❌ **Descartados os tratamentos 3 e 4**, ambos vindos de `agent.humanacademy.ai`. O **3** (coluna fixa + lista numerada 01–06) duplicaria as duas assinaturas da seção 4 — cujo painel nasceu dessa mesma referência — e a página só tem dois `position:sticky` no total (cabeçalho e a foto da seção 4). O **4** (quadro único com fios internos) é melhor que o 3, porque larga a numeração e o sticky, mas custava **+242px** (937px) e perdia os checks limão. **Argumento decisivo contra o 3:** o que dá vida à referência — a pílula "RESULTADO" e o hover com seta — não é transferível (eyebrow banido; os itens não são links), e o que é transferível é justamente o que colide com a seção 4.
- 📄 O comparativo dos quatro está em `_variacoes-secao7.html`, com as seções 4/5/6 acima para julgar a duplicação. **Vale guardar até a seção 7 fechar de vez.**

🚨 **DUAS PENDÊNCIAS ABERTAS NA SEÇÃO 7 — decidir com o Dr. Rafael:**
1. **A página não diz mais que existe plano alimentar.** Aquele item era a **única afirmação positiva** sobre isso. O que restou é tudo pela negativa: *"Sem cardápio de gaveta"* (seção 4), *"Nada de cardápio pronto no primeiro dia"* (Diferenciais 1), *"dietas genéricas não funcionam"* (seção 3). **Agravou com o corte N2**, que tirou `(alimentação, …)` da seção 4. A página nega três vezes a dieta genérica e nunca afirma o que entrega no lugar.
2. **Os retornos sumiram da lista de entregáveis.** Se a oferta for "consulta + X retornos", isso precisa aparecer em algum lugar.
- ⚠️ **As duas estão amarradas:** se o plano alimentar voltar, a lista vai a 7 e o 3/3/1 reaparece. A seção fecha bem com **6** ou **8**, e mal com **7**.

💡 **IDEIA NÃO APLICADA, a melhor da seção — agrupar os 6 itens em dois blocos.** Os itens já se dividem 3/3 por natureza: **investigação** (avaliação médica · exames · composição corporal) e **tratamento e acompanhamento** (medicamentoso · estilo de vida · suporte). Essa estrutura está na copy e hoje é invisível. Torná-la visível daria à seção a hierarquia que nenhum dos quatro tratamentos deu, e **ecoaria o posicionamento da página** — "investigar antes de prescrever", que é a regra declarada do Dr. Rafael na seção "Sobre". ⚠️ **Custo: exige dois rótulos novos**, ou seja, palavras que não existem no `COPY.md` — seria a **5ª exceção à regra 1**, e a primeira que *inventa* texto em vez de remover. Por isso não foi feita. Se for adiante, os rótulos têm de vir do Dr. Rafael, não de mim.

### ✅ RESOLVIDO — a seção "A virada" foi fechada

**O usuário escolheu o tratamento "E" e ele está aplicado no `index.html`** (03/09/2026), depois de 12 tratamentos comparados. Minha recomendação era o B10 (o mais completo e o único mais curto que o A); o usuário preferiu o E. Decisão dele, registrada.

**O que o E é:** texto à esquerda (título, intro, painel de fatores, desenvolvimento) e o Slot 2 como foto **vertical 3:4 à direita, grudada no scroll** (`position:sticky;top:96px`). Os fatores viraram um painel indexado de 2 colunas, células verticais (número em cima, nome na base), com a célula limão de fechamento ocupando a linha inteira.

**Medido a 1180px:** coluna de texto 525px · foto 448×597 · painel 525px com células de 261px em linhas 2/2/2/1 · **seção 1474px → 1166px (−308px)**. Página inteira: 10.470px. Sem erro de console, sem estouro horizontal, `.reveal` todos ativos.

#### ⚠️ O E MUDOU O SISTEMA DE IMAGEM DA PÁGINA — leia antes de mexer

**A faixa full-bleed 21:9 não existe mais.** Era o gesto visual mais forte da landing e a única imagem que sangrava de borda a borda. Com ela saíram, como CSS morto: `.figure.bleed`, `.figure.r-21`, o overlay `.figure.bleed:has(img)::after` e as regras responsivas de 16/9 e 4/3. Também morreram e saíram `.factors`, `.mech-claim` e `.mech .span`; a lista de stagger do `.reveal` passou a mirar `.panel` no lugar de `.factors`.

**⚠️ O Slot 2 mudou de formato: era 21:9 (~2100×900), agora é 3:4 vertical (~900×1200).** Se a foto já tiver sido produzida no formato antigo, **ela não serve** — o recorte é outro. A tabela das 7 imagens, mais abaixo, já está corrigida.

**⚠️ Ritmo de imagem quebrado — pendência real.** O `PROJETO.md` registra como regra da referência klearmindclinics que *nenhum tratamento se repete em seções vizinhas*, e era isso que evitava a cara de template. Com o E:

| seção | slot | tratamento |
|---|---|---|
| 3 · Você se reconhece? | 1 | vertical à **esquerda** |
| 4 · A virada | 2 | vertical à **direita** |
| 5 · Sobre | 3 | retrato à **direita** |

**As seções 4 e 5 ficaram idênticas em estrutura:** texto à esquerda, imagem vertical à direita, uma atrás da outra. É exatamente o que a regra existia para impedir.

**Correção sugerida (não aplicada, precisa da sua decisão):** inverter as duas pontas — Slot 1 vai para a **direita** na seção 3 e Slot 2 para a **esquerda** na seção 4. O ritmo vira direita → esquerda → direita, alternando. Mexe na seção 3, que não foi pedida, por isso não fiz.

### ⏳ Por onde retomar

Em ordem. Os três primeiros dependem de decisão do usuário e travam o resto.

1. **Caixa alta dos títulos.** A Goldoni só tem maiúsculas e a página inteira virou caixa alta. Três saídas oferecidas, nenhuma escolhida. **Nada de tipografia fina antes disso**, porque qualquer escolha muda a quebra de linha de todos os títulos. (O H1 da hero já voltou a 5 linhas — mas isso resolveu o *sintoma* naquele título, não a decisão.)
2. **Reconferir o responsivo.** As alturas mudaram com a troca de fonte e **só foram medidas a 1180px**. ✅ **A hero foi conferida em 04/09** (1600/1358/1143/960/768/560/375, sem estouro); **falta o resto da página** nessas larguras.
3. **Aplicar o fundo.** `assets/Fundo/fundo-1920.webp` (13 KB) está pronto e não está em uso. Onde entra é decisão em aberto — a hero é o candidato óbvio, mas o `PROJETO.md` registra que um degradê de "luz ambiente" na hero já foi rejeitado uma vez (no contexto do limão, que não existe mais).
4. ✅ **CTA final resolvido em 04/09/2026** — mas **não como estava escrito aqui**: remover o `max-width:44ch` sozinho é inerte (quem limitava era a coluna do grid). A alavanca foi `.finalcta .grid` → `1.25fr .75fr`, que derrubou o título de 6 para 4 linhas e a caixa de 827 para 671px. Ver o bloco no topo.
5. **As 7 fotos.** Maior mudança visual disponível. ⚠️ **Reajustar o `object-position:50% 25%` do `.portrait` quando a foto do Slot 3 chegar.**
6. **Depoimentos e compliance** antes de publicar.
7. **`design-system.html`** está desatualizado (ainda marinho + limão). Decidir se atualiza ou aposenta.
8. **Dívida técnica de token**, quando der: separar `--off` em `--bg` e `--on-invert` (18 substituições mecânicas) e resolver os `color:var(--navy)` que assumem fundo claro. Ver Notas técnicas.

### Refazendo o B — o que as referências ensinaram

O usuário mandou **`agent.humanacademy.ai`** e **`medgenius.com`** e pediu um insight sobre como organizar a seção. Tudo abaixo é **medido no DOM das próprias referências**, não impressão.

#### O que as duas fazem igual

| | Human Academy | MedGenius |
|---|---|---|
| Painel | container único 1040×293, raio 16px, borda `1px rgba(0,0,0,.06)` | células com fundo próprio, um degrau tonal mínimo (`#E9EADB` sobre `#F7F8F2`) |
| Células | 9 itens, grade `346px ×3`, gap 0, cada uma 346×97 | 5 itens de 256px |
| Item | chip **redondo de 32px** com o número sobre **8%** da cor de destaque, nome 16px/600 ao lado, chevron à direita — **linha horizontal, centrada** | rótulo de status em cima, nome **28px na cor de destaque**, dado pequeno embaixo |
| Fundo | **branco** | **off-white quente** |

**Regra que as duas seguem:** uma lista longa é composta como **um objeto só com grade interna** — a borda é do container, não de cada item — e cada item ganha uma **segunda camada de rótulo**. Aqui a única forma de fazer isso sem inventar palavra (regra 1) é a **numeração 01–07**.

#### Cabeçalho: título e intro pertencem a um sistema só

- **MedGenius**, idêntico nas quatro seções: duas colunas **iguais** de 663px (gutter 16px), título à esquerda, intro à direita, **alinhados pelo topo**. O título é pequeno (21px) e a intro 18px — quase o mesmo corpo, por isso não sobra vão.
- **Human Academy**: ou empilha título e intro numa coluna estreita com o **mesmo `max-width`** (380px / 384px), ou centraliza o cabeçalho na largura toda.

Em nenhuma delas o título tem uma medida e a intro outra, em alturas diferentes.

#### Os três erros que cometi, em ordem

Registro porque cada um parecia certo na medição e só apareceu ao ver renderizado.

1. **Copiei a grade e inventei o miolo da célula.** Pus o número no topo e o nome na base com `margin-top:auto`. Nenhuma das referências faz isso — e é o que abre o vazio no meio: célula de 104px para ~40px de conteúdo preso nos cantos. **A célula é uma linha horizontal centrada.** Corrigido: chip 32px + nome ao lado, célula de 76px, e o painel caiu de 316px para 242px.
2. **Mudei o buraco de lugar em vez de eliminá-lo.** Recuei o parágrafo do rodapé para as colunas 2–3 para alinhá-lo com a célula limão: elegante no papel, abriu **344×158px** de marinho morto à esquerda. Recuo assim funciona no MedGenius porque lá o chão é claro e arejado; **sobre marinho chapado, vão fechado vira buraco.** Corrigido: parágrafo em largura total, `columns:2`.
3. **Deixei quatro blocos de texto com três medidas e três margens esquerdas** (título 561px em x=177 · intro 415px em x=794, ainda centrada na vertical · corpo 488+488 em x=177 e x=721). Nada alinhava com nada — era isso que o usuário chamou de "não tá harmônico". Corrigido com **1032 = 488 + 56 + 488**: cabeçalho e rodapé na mesma grade.

#### A seção que eu não tinha olhado — "Todo mundo está construindo com IA"

Terceira ida à Human Academy, agora **vendo** e não só medindo. A seção 3 daquela página é o análogo **retórico** desta aqui (problema → virada), e é a mais útil das que analisei. Escala de tipo medida:

| | corpo | peso | entrelinha | cor |
|---|---|---|---|---|
| Situação (título) | **57,6px** | **500** | 1,05 | preto |
| Agitação | 18px | 400 | **1,56** | preto a **55%** |
| **A virada** | **38,4px** | 500 | 1,15 | **cor de destaque** |
| Rótulos | 10–11px | 600–700 | — | 30–55% de opacidade |

**O achado:** a virada não é um parágrafo comum — é um **terceiro nível tipográfico**, entre o título e o corpo, e é a **única coisa colorida** do bloco. As duas colunas também não são "título | intro": são **problema | resolução**, e o grande/pequeno se inverte de uma coluna para a outra.

Outras diferenças de sistema, para referência (não aplicadas):
- Padding vertical das seções: **160px** lá, contra `--s9: 96px` aqui. É a maior diferença de "respiro" entre as duas páginas. Mudar isso é decisão de página inteira, não de seção.
- Título com **peso 500**; o nosso design system pede 700–800, então esse não dá para copiar.
- Razão título:corpo de **3,2×** lá (57,6 / 18) contra 2,5× aqui (42 / 17).

**A ordem também importa, e a nossa estava trocada.** Geometria medida na seção da referência (viewport 1280): situação `top 180→361`, agitação `top 393` (**32px** depois), virada `top 292→469` (**40px** depois do texto pequeno da coluna direita). A sequência é **situação → agitação → virada**: o texto pequeno fica *entre* as duas coisas grandes e é ele que justifica a virada. Em **todos** os nossos tratamentos até o B7 a agitação vinha **depois** da virada — a explicação chegando depois da conclusão. Corrigido no **B8**, que é o B7 com a ordem certa.
- Implementado com `display:contents` no `<h2>` + `order` no grid: **a ordem do DOM continua a da copy original** (o `<h2>` inteiro, depois o parágrafo), só a posição visual muda. O leitor de tela ouve a frase completa e depois a explicação; o olho recebe o argumento na ordem da referência. `display:contents` em cabeçalho é seguro em Chrome 89+/Firefox 87+/Safari 15+.
- Ganho real: a intro deixa de flutuar sozinha embaixo de uma virada de largura total, com vão à direita. Ensanduichada entre dois blocos grandes, ela lê como o tecido conectivo que é.

**Aplicado no tratamento B7:** a nossa copy já traz o par pronto dentro do próprio título — "Emagrecer **não é** sobre comer menos." / "**É sobre** entender por que o seu corpo não está deixando você emagrecer." Os dois foram apenas **tipografados em níveis diferentes**, dentro de um único `<h2>`, com as mesmas palavras na mesma ordem. **Não abre exceção à regra 1** — é a mesma natureza da decisão que virou a frase dos fatores em lista. O limão saiu da faixa de fechamento e foi para a virada, o que rima com o `<em>` limão do H1 da hero.

⚠️ **Duas armadilhas que só apareceram renderizadas, e a correção de cada uma:**
- **A negação a 27px lia como eyebrow** — rótulo pequeno e apagado acima de um título grande. Eyebrow é exatamente o que foi banido da página ("cara de IA"). Subiu para **36px**, aí lê como a primeira metade de uma frase. **Quem carrega a ênfase é a cor, não o tamanho** — é assim na referência e é assim no H1 da hero.
- **Fechamento marinho dentro do painel branco** virava uma barra escura colada no rodapé do cartão. Passou a um degrau claro (`--surface`), que é o que o MedGenius faz: fundo levemente distinto, não de outra família.

#### B9 — a composição da referência trazida inteira

O usuário mandou print da seção e pediu uma versão inspirada nela. O que ela tem que o B7/B8 não tinham: são **duas colunas de verdade, dentro de um cartão**, com um texto pequeno em cada uma. Eu tinha achatado isso numa coluna só.

- **Cartão** `--navy-700` com borda `--navy-500`, raio `--r-xl`, padding `clamp(28px,4.4vw,56px)`. Na referência é um cartão cinza-claro sobre branco; aqui é um degrau escuro sobre o marinho.
- **Esquerda:** negação 40px off-white + agitação 18px, **32px** abaixo (mesmo intervalo medido na referência).
- **Direita:** a virada em limão, `align-self:end`. **Sem isso ela começa na mesma linha da negação e as duas lem como colunas paralelas.** Descida, a base dela alinha com a base da agitação e o olho faz negação → agitação → virada **em diagonal** — a ordem do argumento. Deslocamento medido: 57px (na referência, 112px).
- **A virada é MENOR que a negação** (33px contra 40px), igual à referência (38,4 contra 57,6). Quem carrega a ênfase é a cor. Ênfase dupla, de tamanho *e* cor, fica gritada — foi a lição do B7.
- Empilhado (≤960px) o `align-self` é resetado e a ordem volta a ser negação → agitação → virada. Conferido a 900px e 560px, sem estouro.

⚠️ **A referência tem QUATRO blocos de texto no cabeçalho; a nossa copy tem TRÊS.** Falta o pequeno do alto da direita ("Parece mágica. Parece complicado."). O lugar ficou **vazio de propósito** — inventar essa frase violaria a regra 1. Se um dia quiserem preencher, tem de vir do Dr. Rafael ou do `COPY.md`.

❌ **Não trazido da referência:** os grafismos flutuantes dos cantos (asterisco, círculo, blob) e a **borda serrilhada** do cartão. Grafismo sobre o fundo está na lista de rejeitados, e o serrilhado é da mesma família.

⚠️ **A altura cresceu a cada refinamento:** B6 1489 → B7 1564 → B8 1594 → B9 1619px. Cada melhoria de hierarquia custou altura. **O B10 reverteu isso** (ver abaixo).

#### B10 — tudo num bloco só

A pedido do usuário ("tudo compacto, junto"). Até o B9 a seção era uma **pilha de objetos**: cartão do cabeçalho + painel dos fatores + parágrafo, cada um com sua borda e um vão entre eles. No B10 o cabeçalho e os fatores dividem **a mesma superfície**, separados só por um fio, e o fechamento vira o rodapé do bloco. Some um vão inteiro, somem duas bordas, e as células caem de 76px para 62px porque dentro de um bloco fechado não precisam mais se defender sozinhas.

| | B9 | B10 |
|---|---|---|
| Bloco de texto | 738px | **586px** |
| Seção | 1619px | **1468px** |

**É o primeiro tratamento B mais curto que o A que está no ar** (1474px), e ainda assim é o que carrega todas as correções acumuladas: grade fechada, célula composta como linha horizontal, entorno numa medida só, virada em dois níveis, ordem retórica da referência e composição em duas colunas.

✅ **A virada voltou a 36px de graça.** Medido a 1180px de viewport, variando só o corpo dela:

| virada | linhas | bloco | seção |
|---|---|---|---|
| 29,5px | 3 | 422px | 1468px |
| 32px | 3 | 422px | 1468px |
| **36px** | **3** | **422px** | **1468px** |
| 40px | 4 | 466px | 1511px |

Até 36px ela continua em **3 linhas** e a altura do bloco não muda — quem dita a altura é a coluna da esquerda (negação + agitação), não ela. São 22% mais presença sem custo nenhum. **A 40px ela quebra para 4 linhas, passa a mandar na altura e cobra 43px.** Aplicado: `clamp(20px,3vw,36px)`.

Efeito colateral: a virada (35,4px) ficou praticamente do mesmo tamanho da negação (34px). Isso é o dispositivo do H1 da hero — **um corpo só, com a cor marcando o trecho** — e evita tanto a ênfase dupla do B7 quanto a virada subordinada da referência.

⚠️ **O que sobra de trade-off:** o bloco inteiro é `--navy-700`, então não existe mais elemento claro na seção. Ficou mais contido; se bater como "apagado", o caminho é devolver o painel claro, aceitando a altura de volta.

⚠️ **A partir daqui, a alavanca de altura não é mais o texto: é a imagem.** Na seção do B10, o Slot 2 ocupa **499px + 128px de margem = 627px, 43% da seção**, contra 586px (40%) de todo o texto. Nenhum ajuste tipográfico compete com isso. Encurtar de verdade exige mexer na faixa 21:9 — e o `PROJETO.md` registra essa faixa como o gesto visual mais forte da página.

#### ⚠️ A torre de título — o defeito que sobra em quase tudo

Com as colunas de volta a 488px, o `<h2>` vira **5 linhas / 217px**, quebrando em `entender por que o` — artigo solto no fim da linha. (Nos tratamentos B o título é `clamp(26px,3.4vw,42px)`; o `index.html` está em 40px. A diferença não muda o diagnóstico — o problema é a **largura da coluna**, não o corpo.) **É o mesmo problema que a nota do Mecanismo já registrava** ("a 48px numa coluna de 460px ele quebrava a cada 3 palavras"), e eu o reintroduzi ao consertar o alinhamento.

**Em largura total (1032px) o mesmo texto cai em 2 linhas / 87px**, quebrando na fronteira da frase. É o que o **B6** faz, e é a maior diferença visual entre os sete tratamentos. Aí o título divide a medida com o painel (1032) e a intro com as colunas do corpo (488): duas medidas, ambas estruturais, uma margem esquerda só.

**Ao mexer em qualquer largura de coluna nesta seção, remedir o título — sempre.**

### ⚠️ Já tentado e revertido — não repetir sem pedir

Cheguei a **encurtar a seção "Sobre"**: cortei a linha de posicionamento (`.lead`), enxuguei o P2 (89 → 75 palavras) e centralizei o texto contra o retrato (`.about-body{align-self:center}`). **O usuário mandou voltar para a versão anterior, e voltei.** O estado atual é o de antes desse corte. Não refaça por conta própria — mas o diagnóstico que motivou continua válido e está registrado abaixo, se ele voltar ao assunto.

## Regras invioláveis

### 1. Copy é verbatim
O texto da página vem de `COPY.md` **palavra por palavra**. Não reescrever, não "melhorar", não inventar frases novas.

- Placeholders em `[colchetes]` são intencionais — o cliente preenche depois.
- **Exceção 1 — hero (autorizada):** a subheadline foi encurtada para caber em 3 linhas. O método foi **apenas remover palavras** da frase original (saiu "tira sua disposição e alimenta o efeito sanfona"), nunca escrever palavras novas. **Use esse mesmo método** se precisar encurtar outro texto.
- **Encurtamento de botão (03/09/2026):** o CTA da seção "Sobre" passou de "Quero começar minha avaliação com o Dr. Rafael" para **"Quero começar minha avaliação"**. **Não é uma nova exceção** — é o método de remoção de palavras já autorizado para a hero, sem nenhuma palavra nova. Largura do botão: 464px → 330px. Anotado no `COPY.md`.
- **Exceção 3 — corte do "tireoide" (autorizada em 03/09/2026):** o usuário perguntou qual dos 7 fatores da seção "A virada" eu removeria e autorizou o corte. Saiu **"Tireoide"** — o único item **inteiramente contido em outro da mesma lista**, já que a tireoide é uma glândula endócrina e portanto já cabe em "alterações hormonais". "Resistência à insulina" também é hormonal, mas é um mecanismo metabólico nomeado e sustenta o "saúde metabólica" do H1. **A lista agora tem 6 fatores.** Aplicado no `index.html` e nos 8 tratamentos da comparação; a frase original está preservada no `COPY.md` com a nota do corte ao lado. ⚠️ **Custo assumido:** "tireoide" era provavelmente a palavra de maior reconhecimento imediato da lista — se o Dr. Rafael atender muito caso de tireoide, vale reconsiderar. **Vice-campeão foi "Alterações hormonais"** (lógica oposta: específico ganha de genérico); **o que não se deve cortar é "Uso de medicações"**, porque é o item que mais justifica procurar um *médico* em vez de um nutricionista — que é o argumento da 1ª pergunta do FAQ e do posicionamento da página.
- **Exceção 2 — seção "Sobre" (autorizada em 03/09/2026):** o usuário pediu explicitamente a **reescrita** desta seção, por achar a copy original "enchendo linguiça". A nova versão foi montada cruzando **fatos da página antiga do próprio Dr. Rafael** (CRM, tempo de atuação, formação internacional, congressos) com o **mecanismo já presente na copy atual** (investigar antes do plano). Nada foi inventado — toda afirmação vem de uma dessas duas fontes. **Esta exceção vale só para a seção "Sobre".** O resto da página continua verbatim.

### 2. Compliance — publicidade médica (CFM)
Isto não é opcional e vale para qualquer texto ou imagem adicionada:

- ❌ **Nunca** usar "nutrólogo", "especialista em Nutrologia" ou exibir RQE. Ele tem **pós-graduação em Nutrologia**, não título de especialista. A forma correta é "médico" ou "médico com pós-graduação em Nutrologia".
- ❌ **Sem** promessa de resultado, de tempo ("emagreça em X dias") ou de quantidade de peso.
- ❌ **Sem** imagens ou descrições de "antes e depois" (vedado).
- ⚠️ Depoimentos de pacientes são **restritos pelo CFM**. A Seção 10 está com **três placeholders** (`[Depoimento real…]`, `[Nome]`). **Confirmar com o compliance antes de publicar.**
  - 🚨 **O aviso que existia na própria página foi REMOVIDO** a pedido do usuário em 03/09/2026 (o bloco `.compliance`, com o CSS junto). Ele era a única salvaguarda visível de que aquela seção não estava pronta. **Agora nada na página sinaliza isso** — o alerta vive só aqui. Antes de publicar: ou entram depoimentos reais com autorização de uso de imagem, ou a seção inteira sai do ar. Publicar os placeholders como estão seria divulgar depoimento inventado.
- Tom informativo, sem superlativos ("melhor médico").
- 🚨 **O "AVISO LEGAL" DO RODAPÉ FOI REMOVIDO** a pedido do usuário em 04/09/2026. Ele dizia: *"As informações desta página têm caráter informativo e não substituem uma consulta médica. Resultados variam de pessoa para pessoa, de acordo com a avaliação individual e a adesão ao tratamento."*
  - ⚠️ **A segunda frase era a única ressalva de resultado da página inteira.** Numa landing de emagrecimento, "resultados variam de pessoa para pessoa" é o texto padrão que equilibra as afirmações de resultado — e a página agora **não tem nenhum texto nesse sentido**. Conferido: a string "Aviso legal" não aparece mais em lugar nenhum.
  - **É a segunda salvaguarda visível retirada da página** (a primeira foi o aviso dos depoimentos, em 03/09). Padrão a observar: as duas obrigações continuam valendo e passaram a viver **só neste arquivo**.
  - **Antes de publicar, decidir com o compliance** se o aviso volta (no rodapé ou numa página de termos) — a remoção foi de exibição, não de obrigação.

### 3. Design system — **a paleta da marca, desde 04/09/2026**

- **Azul Profundo** `#1C2747` · **Dourado** `#BD9853` · **Taupe** `#9D9077` · **Bege** `#EADEC3` · **Creme** `#F3F4F0`
- Tipografia: **Goldoni** nos títulos (⚠️ só caixa alta) + **Montserrat** no conteúdo. Playfair Display fica de reserva da Goldoni e ainda serve as frases-âncora em itálico.
- Espaçamento base 4px (`--s1`…`--s9`), `--maxw: 1080px`
- 🔑 **A regra que rege a cor:** o Azul Profundo é a única cor que contrasta com as outras quatro. **Ouro, Taupe e Bege são superfície e acento — nunca texto sobre fundo claro.**
- ⚠️ **`design-system.html` está DESATUALIZADO** — ainda traz o marinho e o verde-limão. Ou é atualizado, ou deixa de ser a fonte da verdade. Hoje a fonte da verdade é o `:root` do `index.html`.
- ⚠️ **Antes de fechar qualquer mudança de cor, rodar a auditoria de contraste** (ver Notas técnicas). Verificação manual já deixou defeito passar duas vezes.

## Estado atual

Landing completa com as 13 seções da copy, responsiva (breakpoints 960px e 768px), acessível (HTML semântico, `aria-*`, foco visível, `prefers-reduced-motion` / `-transparency` / `-contrast`), **na paleta e nas fontes oficiais da marca**, com o logo na navbar e favicon.

Dependências externas: Google Fonts (Montserrat + Playfair Display) e os arquivos locais em `assets/`. A Goldoni é servida do próprio projeto.

**Sistema de imagem instalado (7 slots vazios).** A página está preparada para receber fotos sem retrabalho: existe um componente único `.figure` e os slots já estão posicionados, dimensionados e com o markup de inserção comentado ao lado de cada um. Enquanto as fotos não chegam, cada slot mostra um placeholder listrado (`.ph`) com o número do slot e o formato esperado.

### Decisões de design tomadas

- **Cidade:** `[CIDADE]` → **Florianópolis** em toda a página.
- **Navbar:** fundo **verde-limão sólido**, texto/links marinho, botão "Agendar" **marinho** (limão sobre limão sumiria). Anel de foco e skip link em marinho dentro do header — o limão padrão ficaria invisível ali.
- **H1:** `clamp(32px, 5.6vw, 64px)`, tracking `-.035em`, leading 1.02. Destaque em **lime no trecho "saúde metabólica"** (`.hero h1 em`).
- **Hero:** navy chapado, sem grafismos, padding simétrico (`var(--s8) 0`). Coluna de texto em 640px.
- **Barra de prova:** marquee horizontal em loop contínuo (46s), pausa no hover, estática em `prefers-reduced-motion`.
- **Barra de prova reescrita** (03/09/2026): **ícones de check removidos** (a pedido do usuário) e os itens trocados por **dados concretos**, no mesmo registro factual da seção "Sobre" — CRM, pós-graduação, tempo de atuação, formação internacional, congressos, volume de pacientes e áreas de foco. **Conteúdo final dos 7 itens:** Médico · CRM/SC 21664 — Pós-graduação em Nutrologia — Mais de 10 anos de atuação — Formação internacional — Participação em 5 congressos internacionais — Mais de 30 mil pacientes acompanhados — Emagrecimento, saúde metabólica e longevidade. Saíram os dois itens que descreviam o serviço em vez de credenciar ("Plano individualizado, sem dieta de gaveta" e "Presencial e online" — este último já aparece na microcopy da hero logo acima). **5 → 7 itens**, por isso a duração subiu de 34s para 46s: sem o ajuste a barra passaria ~35% mais rápida por item. Sem os checks a barra ficou **sem limão**, o que é coerente com a regra de moderação. Em `prefers-reduced-motion` a divisória vertical passou a ser mantida — sem ícone e sem borda os itens empilhados se colavam.
- **Seção "A virada / Mecanismo" reestruturada** (03/09/2026). O usuário achou a seção "simples e com quantidade exagerada de texto". **Diagnóstico medido:** o texto ocupava 614px de um `.wrap` de 1080px — **442px (41%) de campo marinho morto à direita** — com 127 palavras em dois blocos corridos. O "simples" e o "texto demais" eram o mesmo problema: uma fita estreita de texto sem nada para o olho fazer.
  - **A copy já continha uma lista disfarçada de frase:** "Alterações hormonais, resistência à insulina, tireoide, qualidade do sono, uso de medicações, histórico de dietas restritivas e até o seu nível de estresse" — 7 itens dentro de uma vírgula só. Foram **tipografados como lista** (`.factors`), não reescritos. Verificado palavra a palavra: **nenhuma palavra inventada e uma única removida — a conjunção "e"**, que a grade substitui. O predicado da frase continua logo abaixo, em `.mech-claim`. **Isto não abre exceção à regra 1**; é decisão de tipografia, não de copy.
  - **Layout em três faixas** (`.mech`): (1) título | intro, (2) os 7 fatores em largura total, (3) afirmação | desenvolvimento. A coluna esquerda passou a carregar as duas *afirmações* e a direita as duas *explicações* — é isso que dá coerência ao ritmo. Todas as faixas agora chegam à borda direita.
  - ⚠️ **O `<h2>` desta seção é 40px, não os 48px do resto da página.** Não é descuido: a 48px, numa coluna de 460px, ele quebrava a cada 3 palavras e virava uma torre de **6 linhas / 311px** — sozinho, 44% da altura do bloco. Testei 9 combinações de largura de coluna × corpo; a 40px são 5 linhas e o bloco cai de 708px para 613px. **Se mexer na largura das colunas, remedir o título.**
  - As pílulas são **de propósito diferentes** dos cartões retangulares do resto da página: aqui não são etapas nem benefícios, são variáveis de um conjunto. O ponto limão de 7px em cada uma é o que dá vida ao bloco sobre o marinho — 7 pontos agindo como um gesto só, não limão espalhado.
  - `.prose` **deixou de existir** na página (só era usado aqui) e foi substituído por `.mech*`. `.factors` entrou também na lista de stagger do `.reveal`.
  - ⚠️ **A seção não ficou mais curta:** 1525px → 1571px (+46px). O texto foi *reorganizado*, não reduzido — as 127 palavras continuam todas lá. **O único caminho que encurta de verdade é cortar copy**, e isso abriria uma terceira exceção à regra 1. Ficou em aberto com o usuário.
- **Seção "Você se reconhece?":** split — imagem grande à esquerda + 4 cards em **2×2** à direita.
- **Seção "Diferenciais":** grid **2×2** (`.cardgrid.cols-2`), sem imagem — o fundo `--surface` é que dá o respiro. Resolve o antigo problema de 3+1.
- **Seção "Sobre":** duas colunas apenas — **texto à esquerda, retrato à direita**. O `<h2>` vive **dentro** da coluna de texto (não acima das duas): é isso que compacta a seção. O retrato estica com `align-items:stretch` + `height:100%`. Ganho medido na época: **1035px → 718px** (−31%).
  - **Retrato horizontal no mobile (03/09/2026, a pedido do usuário).** Abaixo de 960px o `.portrait` deixou de ser 4/5 limitado a 400px e passou a **16/10 em largura total**. Motivo: a 4/5 com 339px de largura ele virava um bloco de ~424px de altura que tomava a tela inteira; a 16/10 cai para ~204px num iPhone. É a mesma proporção que `.mech-figura` e `.finalcta .figure` já usam neste breakpoint, então o mobile ficou coerente. ⚠️ **A foto do Slot 3 é vertical (~1000×1500)** e, recortada em 16/10, o `cover` pegaria a faixa central e cortaria a cabeça — por isso entrou `object-position:50% 25%`. **Reajustar esse valor quando a foto real chegar.**
  - ⚠️ **Medição refeita em 03/09/2026, e o número mudou:** depois dos cortes de hoje (legenda, P2 reescrito, eyebrow) a linha do grid é de **520px**, imposta pelo `min-height` do `.portrait`, mas o texto só ocupa **451px** — ou seja, existem hoje **69px de vão abaixo do botão**. Não é regressão de nada que se tenha feito hoje; já era assim. **Se o texto do "Sobre" encurtar mais, esse vão cresce.** Baixar o `min-height` não resolve: a 420×520 o retrato está em 0,81 (≈4:5), a proporção pedida para o Slot 3, e encolher deixaria a moldura quase quadrada. A saída testada foi `.about-body{align-self:center}`, que divide a folga em cima e embaixo — foi revertida junto com o resto, mas funciona e está medida.
- **Copy da seção "Sobre" reescrita** (03/09/2026), no formato da referência drmariogomes.com.br: `<h2>` com o **nome** → uma linha de posicionamento (`.lead`) → dois parágrafos densos e factuais. (O eyebrow "Sobre o médico" que abria a seção foi removido depois, junto com os outros nove.) Saiu a narrativa em primeira pessoa ("Sou o Dr. Rafael... Me dediquei..."), entraram os fatos. **185 → 126 palavras**; a seção de referência tem 107.
- **Eyebrows removidos da página inteira** (03/09/2026), a pedido do usuário: "deixa a página com cara de IA". Saíram os **10** `<span class="eyebrow">` ("Você se reconhece?", "A virada", "Sobre o médico", "Diferenciais", "O acompanhamento", "Como funciona", "Para quem é", "Depoimentos", "Dúvidas frequentes", "Dê o primeiro passo") e o bloco CSS `.eyebrow` inteiro, que ficou morto. **O `<h2>` virou o primeiro elemento de cada seção**, então o respiro de topo que existia para o eyebrow foi zerado em dois lugares: `.h-sec` (`margin:14px 0 10px` → `0 0 10px`) e `.finalcta h2` (`16px 0 18px` → `0 0 18px`). Sem isso as seções ficariam com 14–16px de vão inexplicado no topo.
  - Nenhuma informação se perdeu: os eyebrows eram rótulos da própria seção, e no FAQ o rótulo era **idêntico** ao `<h2>` logo abaixo ("Dúvidas frequentes" duas vezes).
  - Efeito colateral desejável: saíram 10 barrinhas de limão da página, o que aproxima do "use com moderação" da regra 3. O limão continua na navbar, no `<em>` do H1, nos botões, nos ícones dos cards, no destaque da frase de virada, nos números dos passos e no chevron do FAQ.
  - O componente **continua definido em `design-system.html`** (intocado). Se um dia for reintroduzido, é de lá que se copia — mas veja a lista de rejeitados abaixo antes.
- **Botão flutuante do WhatsApp: só aparece depois da hero** (03/09/2026, a pedido do usuário — "a partir da segunda seção"). Regra implementada: entra quando `scrollY >= hero.offsetHeight`, ou seja, no instante em que a hero termina de sair. **Escolhi esse gatilho em vez de "quando a seção 2 entra no viewport"**: num desktop alto a barra de prova já está visível com a página no topo, e o botão apareceria de cara, sem gate nenhum. Da forma implementada a primeira dobra fica limpa em qualquer tela. Ele some de novo ao voltar para a hero.
  - **Sem `IntersectionObserver`, de propósito.** Foi fundido no listener de scroll que **já existia** para o `.scrolled` do header — nenhum listener novo, e a altura da hero é lida a cada evento, então continua correto depois de um resize.
  - Oculta com `opacity` + `visibility` (não `display`): `visibility:hidden` tira o botão da ordem de tabulação e do leitor de tela enquanto está fora. O `transition:visibility 0s linear .25s` atrasa só a *saída*, para o fade acontecer antes de sumir.
  - ⚠️ **A regra `.show` não define `transform` de propósito.** `.js .wa-float.show` (0,3,0) venceria `.wa-float:hover` (0,2,0) e mataria a animação de hover. Se algum dia quiser uma entrada deslizante, vai precisar subir a especificidade das regras de hover/active junto.
  - Sem JS o botão continua sempre visível (mesmo padrão do `.reveal`).
- **Legenda do retrato removida** (03/09/2026), a pedido do usuário. Saiu o `<figcaption>` "Dr. Rafael Gallassini · Médico · Pós-graduação em Nutrologia" e, com ele, a regra `.portrait figcaption` (era o único `<figcaption>` da página). **Nenhum sinal de confiança se perdeu:** o mesmo conteúdo já aparecia três vezes ali perto — no `<h2>` logo ao lado, na barra de prova e no rodapé. A foto agora entra sem tarja escura no rodapé, então a composição do retrato pode usar o quadro inteiro.
- **Segundo parágrafo da seção "Sobre" reescrito** (03/09/2026). O anterior era um **eco quase literal** do parágrafo do Mecanismo: os dois terminavam com a mesma frase ("para que o resultado se sustente, em vez de virar mais um ciclo de perder e recuperar") e repetiam o mesmo aposto de "alimentação, comportamento e, quando há indicação clínica, medicação". O trio "história, exames e composição corporal" chegava a aparecer **três vezes** na página (Mecanismo, Sobre e o card 1 dos Diferenciais). A versão nova troca a repetição do método por fatos que **só cabem aqui** — onde atende e em que volume — e resume a marca da prática em uma linha ("investigar antes de prescrever"). **56 → 47 palavras.** Nada inventado: consultório/teleconsulta vêm da copy, o volume é o número confirmado pelo usuário. **Ao editar o Mecanismo ou os Diferenciais, cuidado para não reintroduzir o eco.**
- **Quadro de credenciais na seção "Sobre" — removido** a pedido do usuário (02/09/2026). A seção agora é só "quem é" + a foto. Saíram da página com ele os placeholders `[Instituição]`, `[Graduação em Medicina, Instituição]`, `[Outras formações e cursos relevantes]` e `[mais de X anos de experiência]`. **CRM e pós-graduação continuam visíveis** na barra de prova, no P1 do "Sobre" e no rodapé — não se perdeu sinal de confiança. (A legenda do retrato também os trazia, mas foi removida em 03/09/2026.)
- Animações de reveal por `IntersectionObserver` são **progressive enhancement**: sem JS o conteúdo aparece normalmente (classe `.js` no `<html>`).

#### Sistema de imagem — referência: klearmindclinics.com

Análise feita em 02/09/2026. O que se aproveitou de lá e por quê:

- **Uma moldura só.** Raio `--r-xl` (32px) em **toda** foto da página. A repetição do mesmo raio é o que faz formatos diferentes lerem como um sistema — é a regra mais barata e mais eficaz da referência. **Não criar raios novos para imagem.**
- **Nenhum tratamento se repete em seções vizinhas.** O ritmo era: vertical à esquerda → faixa full-bleed → retrato à direita → (nada) → 3 horizontais em grid → (nada) → vertical à direita. Foi isso que evitou a cara de template no site de referência. ⚠️ **Com o tratamento E esta regra passou a ser violada** — a faixa full-bleed virou vertical à direita, ficando igual ao retrato da seção seguinte. Ver "O E mudou o sistema de imagem", no topo.
- **O bloco de cor é uma imagem.** Seções pesadas de texto (Diferenciais, Para quem é, FAQ) ficam **sem foto** de propósito: a troca de fundo (`--surface` / navy) dá o mesmo respiro com zero peso de download.
- **Imagem é clima, não documentação.** Poucas fotos, todas na mesma família de luz. Não encher a página.

#### Componente `.figure`

| Classe | Efeito |
|---|---|
| `.figure` | Moldura base: raio `--r-xl`, `overflow:hidden`, `object-fit:cover` (funciona com `<img>` e `<picture>`) |
| `.r-45` `.r-34` `.r-32` | Proporção 4:5 · 3:4 · 3:2 |
| `.fill` | Preenche a altura da linha do grid (usado no split da seção 3) |
| `.on-dark` | Moldura para fundo marinho (aplicada automaticamente dentro de `.sec-dark`) |
| `.ph` / `.ph.on-dark` | Placeholder listrado, versão clara e escura |

- ⚠️ **`.bleed`, `.r-21` e o overlay `.figure.bleed:has(img)::after` NÃO EXISTEM MAIS.** Saíram do `index.html` junto com a faixa full-bleed, quando o tratamento E foi aplicado. Ficam registrados aqui só porque a lógica do overlay era boa: ele entrava sozinho quando a foto real chegava, mantendo a unidade cromática com o bloco escuro em vez de "furar" o marinho. **Se um dia a faixa voltar, é de um backup que se recupera** — ver "Backups desta sessão", no topo.
- **O Slot 2 hoje usa `.mech-figura`**, não `.figure`: é a foto vertical 3:4 grudada no scroll ao lado do texto da seção 4.
- Nos passos de "Como funciona", a foto **sangra até a borda do card** (`.step-media` com margem negativa de -28px + `overflow:hidden` no `.step`) e o **número passou a viver sobre a foto** (`.step-media .num`, canto superior esquerdo).
- O CTA final virou **duas colunas** (`.finalcta .grid`): texto à esquerda, imagem 3:4 à direita. Em ≤960px vira uma coluna e a foto muda para 16:10.

### ❌ Rejeitado pelo usuário — NÃO sugerir de novo

- **Eyebrows / rótulos acima dos títulos de seção** — removidos da página em 03/09/2026 por darem "cara de IA". **Não reintroduzir**, nem como variação (kicker, tag, numeração de seção).
- **Glassmorphism** (cartão translúcido na hero) — não gostou.
- **Quadro de credenciais na hero** — removido por completo; o espaço é para imagem/vídeo.
- **Grafismos/ícones sobre o fundo** (sparkles, linhas curvas) na hero e no CTA final.
- **Degradê radial "luz ambiente"** na hero — removido (quebrava a harmonia com a navbar e atrapalharia a mídia de fundo).
- **Máscara de fade nas bordas** do marquee — deixava o branco do fundo vazar.
- **Ícone do WhatsApp dentro dos botões de CTA** — removido. (O botão flutuante mantém o ícone, porque ali o ícone *é* o botão.)
- **Borda arredondada** no fim da hero.
- Título em **caixa alta** — testado (variações A–E) e descartado; escolhida a **variação B** (maior, caixa mista).

## Pendências

### Preencher (dados reais)
`[DDD][NÚMERO]` WhatsApp (o link `wa.me` aparece em **7** lugares: nav, hero, Sobre, Como funciona, CTA final, rodapé e botão flutuante) · endereço · e-mail · `[@perfil]` · `[ANO]` · convênios · depoimentos reais.

**Preenchidos em 03/09/2026:** CRM (`CRM/SC 21664`, em 4 lugares) e volume de pacientes (`Mais de 30 mil pacientes acompanhados`, na barra de prova).

### Decidir / confirmar (seção "Sobre")

A página antiga do Dr. Rafael traz três afirmações que **não** foram para a nova copy, de propósito:

| Afirmação da página antiga | Por que ficou de fora |
|---|---|
| "Mais de 30.000 vidas transformadas" | ✅ **Resolvido (03/09/2026).** O usuário confirmou o número. Entrou na barra de prova na forma factual — "Mais de 30 mil pacientes acompanhados" — sem "vidas transformadas", que é alegação de resultado e cai na mesma vedação do antes-e-depois. |
| "Palestrante reconhecido na área" | "Reconhecido" é superlativo/autopromoção, restrito pelo CFM. Cabe "palestrante", sem o adjetivo. **Ainda não usado na página** — disponível se quiserem densidade extra de credencial. |
| "Médico com foco em emagrecimento saudável e **Medicina Integrativa**" · "**performance**" | ✅ Fatos disponíveis, **ainda não usados**. A página atual diz "Atua com foco em emagrecimento, saúde metabólica, prevenção e longevidade" — a página antiga acrescenta *Medicina Integrativa* e *performance*. Entram na copy se o Dr. Rafael confirmar que seguem sendo foco; é mudança de posicionamento, não só de dado, por isso não foram inseridos sozinhos. |
| "CONHEÇA O ESPECIALISTA" (eyebrow) | **Não usar.** Ele tem pós-graduação, não título de especialista com RQE. Ficou "Sobre o médico". |

Também pendente:

- ✅ **CRM resolvido (03/09/2026).** O usuário confirmou a UF: o registro é de Santa Catarina. Está na página como **`CRM/SC 21664`** — grafado no formato `CRM/UF nº` do CFM, e não "CRM 21664 SC". Aparece em **4 ocorrências**: as duas trilhas do marquee, o P1 da seção "Sobre" e o rodapé.
- ✅ **Congressos resolvido (03/09/2026).** O usuário enviou print da página antiga: **"Participação em 5 congressos internacionais"**. O número entrou na barra de prova e no P1 do Sobre, no lugar do vago "participação em congressos internacionais da área".
- ⚠️ **"formação internacional" continua sendo o único dado vago da página.** O print da página antiga **também** diz só "formação internacional", sem instituição nem ano — ou seja, a fonte não resolve. Para especificar é preciso perguntar ao Dr. Rafael. A referência ganha força citando as instituições pelo nome (FMTM, FHEMIG, APM, SANAR).
- **"mais de 10 anos de experiência"** vem da página antiga e **é o máximo de precisão que a fonte permite** — ela não dá o ano de formatura. Se quiserem "há 14 anos" ou similar, precisa vir do Dr. Rafael.

### As 7 imagens

Cada slot tem, no HTML, um comentário com o `<picture>` pronto para copiar. Basta apagar a `<div class="ph">` e colar no lugar.

| Slot | Seção | Formato | Tamanho sugerido |
|---|---|---|---|
| 1 | Você se reconhece? (esquerda) | ⚠️ **0,62, não 3:4** — medido em 425×686; gerar em **2:3** | ~1700×2530 |
| 2 | A virada — **ao lado do texto, grudada no scroll** | vertical **3:4** | ~900×1200 |
| 3 | Sobre — retrato do Dr. Rafael | vertical, **estica até a altura do texto** | ~1000×1500 (origem 4:5 ou 2:3) |
| 4·5·6 | Como funciona — um por passo | horizontal 3:2 | ~1200×800 |
| 7 | CTA final (direita) | vertical 3:4 | ~900×1200 |

⚠️ **Compliance de conteúdo:** em página de emagrecimento, **foto de corpo é promessa de resultado implícita** — cai na mesma vedação do antes-e-depois. As fotos devem ser de consultório, atendimento, exames, ambiente, alimento real ou o próprio médico. **Nunca corpo transformado.**

Direção de arte para as fotos não brigarem entre si: luz natural neutra/fria (combina com o marinho), baixa saturação, fundos limpos, muito espaço negativo. Exportar em AVIF + WebP + JPG de fallback.

### Próximos passos combinados
1. ✅ **Seção "A virada" fechada** — o usuário escolheu o **E** e ele está aplicado. Ver o bloco no topo do arquivo, incluindo a regressão de ritmo de imagem que ficou em aberto.
2. **Preencher os 7 slots de imagem** (tabela acima). ⚠️ **O Slot 2 mudou de 21:9 para 3:4 vertical** com o tratamento E — se já tiver sido produzido no formato antigo, refazer. Continua sendo o mais urgente: hoje é um retângulo listrado de 448×597 ocupando toda a coluna direita da seção.
3. ✅ **Hero resolvida em 04/09/2026**, desktop e mobile. No largo é painel de cor + foto; no estreito o texto fica em cima e a foto vira um bloco cheio embaixo, com arquivo recortado próprio. Ver os dois blocos no topo. O texto abaixo fica como registro da decisão original:
   ~~**Hero — decisão em aberto.** O usuário optou por **não mexer na hero** por enquanto.~~ Quando for mexer, há dois caminhos que **não se somam**: (a) imagem/vídeo de fundo com `min-height` em `svh` + overlay escuro de contraste — se vídeo, `autoplay muted loop playsinline` + `poster` + respeitar `prefers-reduced-motion`; ou (b) card 4:5 emoldurado à direita, no padrão da referência, mantendo o navy chapado. Perguntar antes de implementar.
4. **Depoimentos** — 🚨 **ponto de atenção antes de publicar.** Continua com os três placeholders, e o aviso de compliance que ficava na própria página **foi removido** em 03/09/2026 a pedido do usuário. Não há mais nada na tela lembrando que a seção não está pronta. Decidir: entram depoimentos reais (com autorização de uso de imagem e aval do compliance) ou a seção sai.
5. Revisão final de **compliance** antes de publicar. ⚠️ **Agora com dois itens concretos:** os depoimentos-placeholder e o **"Aviso legal" removido do rodapé** em 04/09/2026 — a página ficou sem nenhuma ressalva de que resultados variam.
6. Rastreamento: conversão de clique no WhatsApp (GA4 + Google Ads) e parâmetro `gclid`.
7. **Fechar o Slot 1.** 12 candidatas geradas em 05/09/2026 e nenhuma instalada — ver o bloco no topo. Recomendação atual: `_candidatas/09-GAVETA-A.png`. ⚠️ **A página é destino de anúncio no Google Ads**, e isso restringe toda imagem daqui para frente: nada que dramatize sofrimento ou insatisfação com o corpo, nada de medicação.

## Como o usuário trabalha

- Ele **decide melhor vendo do que lendo**. Perguntas conceituais ("qual direção prefere?") receberam "eu não sei, eu quero que fique bonito". Variações renderizadas lado a lado, com o mesmo texto, funcionaram.
- Ele **manda print da tela com setas** quando algo não agrada, e aponta muito bem em cima da imagem — mesmo sem conseguir nomear o problema em abstrato. Foi assim que saiu "os textos ao redor não estão harmônicos", que era exatamente o diagnóstico certo. **Renderize e mostre; não pergunte no vazio.** (Você também consegue tirar print sozinho — ver notas técnicas.)
- Ele **repete "melhorou, mas ainda não está do meu agrado"** por várias rodadas sem desistir. Isso não é rejeição do caminho: nas três rodadas da "A virada" cada iteração estava de fato mais perto. Continue iterando e mostrando.
- Ele **reverte sem cerimônia** ("volte para a versão anterior"). **Agora existe git** — commite a cada mudança fechada e o desfazer fica trivial. Antes de mudança grande sem commit, guarde as strings exatas que vai substituir.
- Quando ele pede um dado mais específico, a resposta certa quase sempre está na **página antiga dele** — foi de lá que vieram CRM, 10 anos, 5 congressos e os 30 mil. Peça o print antes de dizer que o dado não existe.

## Notas técnicas

- ✅ **DÁ para tirar print no preview — o problema é a rolagem, não a captura.** Descoberto em 03/09/2026, depois de três rodadas inteiras decididas só na base de medição por JS. **As capturas falham (voltam em branco) sempre que a página foi rolada; no topo do documento elas funcionam.** A saída é fazer o que se quer ver **cair no topo**:
  ```js
  var s=document.createElement('style');
  s.textContent='.doc,.tag{display:none!important} section{display:none!important}'
              + ' section.alvo{display:block!important} body{background:#283050}';
  document.head.appendChild(s);
  document.querySelectorAll('section')[N].classList.add('alvo');
  scrollTo(0,0);   // e só então tirar o print
  ```
  **Use isto antes de concluir qualquer coisa sobre aparência.** As medições diziam "título com 5 linhas, 217px" e eu tratei como dado neutro; renderizado, era a primeira coisa que saltava aos olhos e o defeito principal da seção. Medir não substitui ver.
  - Em abas fixadas num preview de arquivo (`file://`), o `location.reload()` **não** recarrega o disco — a aba serve um snapshot `data:`. Para ver o arquivo atualizado, edite com a ferramenta Edit (o hook abre uma aba nova) ou navegue numa aba nova.
  - Navegar para `http://localhost:5173` funciona em algumas abas e é recusado em outras. Se for recusado, use o caminho `file:///D:/...`.
- ⚠️ **O preview embutido não executa comportamento de scroll.** Descoberto em 03/09/2026, testando o botão flutuante. Três limitações confirmadas, todas do ambiente e não da página: (1) **`IntersectionObserver` nunca dispara** — um observer criado do zero no console também não é chamado, e as 10 seções `.reveal` ficam paradas; (2) **eventos de `scroll` não são entregues** — nem `scrollTo` programático nem rolagem de mouse disparam o handler, então o `.scrolled` do header e o botão flutuante parecem quebrados quando não estão; (3) **transições CSS não avançam**, então `opacity` fica congelado no valor inicial. **Como testar mesmo assim:** disparar `window.dispatchEvent(new Event('scroll'))` após posicionar com `scrollTo` (valida o JS), e ler o estilo computado com `el.style.transition='none'` (valida a cascata do CSS, sem depender de transição). **O comportamento final tem de ser conferido em navegador real.**
- **Para conferir layout, use o servidor local, não o snapshot.** Existe um `.claude/launch.json` com a config `landing` (`python -m http.server 5173`). No snapshot estático o `IntersectionObserver` não dispara (seções `.reveal` saem **em branco**) e `innerWidth` chega a medir **0**, o que torna qualquer medição de altura/coluna inútil. Servido em `http://localhost:5173` tudo mede corretamente. Dois detalhes ao medir por JS no preview: `html{scroll-behavior:smooth}` faz `scrollTo` ser **assíncrono** (medir logo depois devolve a posição antiga), e o marquee em loop infinito faz a captura de tela expirar — pausar com `document.getAnimations().forEach(a=>a.pause())` antes do screenshot.
- 🚨 **INCIDENTE DE DISCO — 03/09/2026. Leia antes de confiar em qualquer arquivo daqui.** O `PROJETO.md` foi encontrado **fisicamente corrompido**: `head` e `tail` liam, mas `grep`, `wc` e `md5sum` devolviam **Input/output error**. Varredura por blocos: **4 blocos de 4KB ilegíveis a partir do offset 8192**, e o conteúdo restante era uma **versão antiga do `index.html`** — clusters cruzados, corrupção de sistema de arquivos. **Não foi erro de edição:** nenhum script consegue gerar um arquivo que falha na leitura sequencial. O arquivo foi **reconstruído** a partir do backup no scratchpad mais a reaplicação dos registros do dia. `index.html`, `COPY.md` e `design-system.html` foram verificados por checksum na mesma hora e estavam íntegros.
  - ✅ **Resolvido mudando de disco.** O projeto foi clonado para `C:\Users\-User-\Documents\dr_lp2` e enviado ao GitHub. A pasta do `D:` está abandonada.
  - **Diagnóstico final (04/09):** o log do Windows registra **11.841 eventos "setor defeituoso"** no `\Device\Harddisk1\DR1` (o `D:`, um HD mecânico WDC WD5000AAKX), desde 30/08. **`chkdsk` não resolve** — já tinha rodado em 31/08 (existe uma pasta `found.000` de lá) e os erros continuaram. É falha física: o disco precisa ser substituído, não reparado.
  - **Lição operacional:** o scratchpad fica no `C:` e foi o que salvou. Copiar antes de mudança grande **e verificar com `md5sum` que a cópia lê inteira** — tamanho e `head` não detectam este defeito.
- ⚠️ **Cache atrapalha a conferência — no celular e no preview.** Em 03/09/2026 o usuário mandou print do iPhone com o retrato do "Sobre" no formato antigo. O arquivo e o servidor estavam corretos (medido: 327×204, 16/10); o Safari servia um snapshot antigo. O mesmo aconteceu no preview embutido depois de uma edição. **Sempre carregue com um parâmetro na URL (`?v=2`, `?v=3`)** — é outro endereço para o cache, então força a busca do zero.
  - Quem serve para o celular é o **Live Server do VS Code, na porta 5500** (`http://192.168.0.117:5500/...`) — o Safari esconde a porta na barra compacta. Ele manda `Cache-Control: public, max-age=0`, e abas suspensas do iOS reexibem sem perguntar ao servidor.
- 🔧 **AUDITORIA DE CONTRASTE — usar antes de fechar qualquer mudança de cor.** Verificação de pares "a mão" já deixou defeito passar duas vezes. O script percorre `document.querySelectorAll('body *')`, filtra os que têm texto próprio e são visíveis, sobe a árvore até achar um fundo opaco, calcula o contraste WCAG e reprova abaixo de 4.5:1 (ou 3:1 para texto grande: ≥24px, ou ≥18.66px com peso ≥700). Roda no console do navegador. Foi ela que achou o texto legal do rodapé a 2,93:1, que estava no ar havia dias.
  - ⚠️ **Limitação:** lê `background-color` e **não enxerga gradiente**. Elementos sobre degradê dão falso positivo — hoje só o `.mono` do retrato.
- ⚠️ **`color:var(--navy)` assumindo fundo claro — irmão do problema do `--off`.** São 14 usos no CSS. Dez estão corretos porque ficam sobre ouro ou bege (botão primário, navbar, chips numerados, célula de fechamento, tick). Os outros quatro assumem fundo claro e **quebram em qualquer variante escura**: `.turn` (1,22:1), `.faq summary` (1,04:1), `blockquote.quote cite`, `.btn-outline`. Corrigidos na `index-dark.html` pelo bloco de ajustes; **no arquivo principal continuam como estão** (lá o fundo é claro, então funcionam).
- ⚠️ **`--off` é um token SOBRECARREGADO.** Ele é usado como **cor de texto em 18 lugares** do CSS (H1 da hero, `.sec-dark`, `.btn-secondary`, `.panel .nm`, títulos do rodapé…) e como **fundo em apenas 1** (o `body`). Na paleta clara isso passa despercebido, porque o creme faz os dois papéis. **Qualquer variante que mude o fundo da página tem de separar os dois** — foi o que quebrou na primeira geração da versão escura: o H1 ficou da cor do próprio fundo. Na `index-dark.html` a solução foi manter `--off` como creme e criar `--bg` para o chão.
  - **Melhoria pendente no arquivo principal:** separar `--off` em `--bg` (fundo) e `--on-invert` (texto sobre escuro). São 18 substituições mecânicas, verificáveis pelo mesmo método da tokenização. Não foi feito para não misturar com a troca de paleta.
- ⚠️ **O servidor de preview e o cache atrapalharam a conferência várias vezes.** Depois de editar, o preview serviu o arquivo antigo em três tentativas seguidas, e chegou a servir a **pasta errada** depois da mudança de diretório. **Sempre carregar com parâmetro na URL (`?v=2`, `?v=3`)** e, se a medição vier estranha, conferir por HTTP o que o servidor está entregando antes de concluir qualquer coisa sobre a página:
  ```python
  import urllib.request
  h = urllib.request.urlopen('http://localhost:5173/index.html').read().decode()
  print('--navy' in h, 'Goldoni' in h)
  ```
- Cuidado com **especificidade CSS** em botões dentro da nav: `.nav-links a` (0,1,1) vence `.btn-secondary` (0,1,0) e sobrescreve a cor do texto. Já existe `.nav-links a.btn-secondary` para corrigir.
- **Corrigido:** três `<section>` tinham o atributo `class` **duplicado** (`class="sec-dark" ... class="reveal"`) em "Como funciona", "Dúvidas" e o CTA final. O HTML descarta o segundo, então essas três seções nunca recebiam `.reveal` e nunca animavam. Ao editar tags de seção, conferir que existe **um único** `class`.
- A ordem das regras de `.figure` importa: `.sec-dark .figure` (fundo/borda) precisa vir **antes** de `.figure.bleed` (que zera raio e bordas laterais). Mesma especificidade — quem vem depois vence.
- `.figure.bleed` só sangra corretamente porque é **filho direto da `<section>`**, fora do `.wrap`. Não usar `100vw` — isso reintroduz estouro horizontal por causa da barra de rolagem.
- ⚠️ **Num container `display:flex`, um `<strong>` solto no meio do texto QUEBRA a frase.** Cada filho vira um flex item, então `<li><svg><strong>` + texto vira três caixas lado a lado. Foi o que aconteceu na seção "Para quem é": o item `Você quer entender a <strong>causa</strong> do problema…` renderizava embaralhado — *"Você quer | causa | do problema, e não só"* na primeira linha e *"entender a | enxugar a balança."* na segunda. **O bug estava na página desde antes desta sessão** e só apareceu porque aquele era o único item da lista com `<strong>`.
  - **Correção (03/09/2026):** o texto de cada `<li>` foi envolvido num `<span>`, virando um flex item só; o `<strong>` volta a ser inline. Envolvi os **7 itens** das duas colunas, não só o quebrado, para o problema não voltar quando alguém adicionar ênfase em outro item. Há um comentário no CSS avisando disso.
  - **Regra geral:** em `.aud-card li`, `.includes li`, `.panel li` e `.faq summary` — todos flex — **o texto sempre vai dentro de um `<span>`**. As outras três já estavam certas; só a `.aud-card` não estava.
- ⚠️ **`<figure>` tem margem padrão do navegador: `margin: 1em 40px`.** Isso mordeu o `.portrait`, que ficava 80px mais estreito e 16px deslocado para baixo sem nenhuma regra explicando o porquê. **Todo `<figure>` novo precisa de `margin:0`** — `.figure` e `.portrait` já têm. Sintoma típico: imagem que "não preenche a coluna" e desalinha do topo do texto ao lado.
- Quando uma coluna de imagem precisar terminar junto com a coluna de texto, use `align-items:stretch` no grid e **remova o `aspect-ratio`** da imagem (os dois brigam). A proporção volta no breakpoint empilhado, junto com um `max-width`, senão a foto fica gigante no tablet.
