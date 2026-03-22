---
name: kolhey-brand
description: Manual de marca completo da Kolhey — agência de marketing do Tocantins. Usar SEMPRE que trabalhar no projeto agencia-esteira ou qualquer material visual da Kolhey. Contém paleta, tipografia, identidade, regras de uso e classes Tailwind do projeto.
type: reference
---

# Kolhey Brand — Manual de Referência Completo

## Identidade da Marca

- **Nome:** Kolhey
- **Segmento:** Agência de marketing digital
- **Localização:** Tocantins, Brasil
- **Slogan:** "Resultados que se cultivam"
- **Mascote:** Onça-pintada (jaguar) — símbolo do Tocantins, força e precisão
- **Tom:** Profissional, confiante, sofisticado — sem ser formal demais

---

## Paleta de Cores

| Nome | Hex | Uso |
|---|---|---|
| Navy profundo (primária) | `#0f2f48` | Fundo principal, backgrounds |
| Navy médio | `#1a3d54` | Sidebar, header, superfícies secundárias |
| Navy card | `#235475` | Cards, painéis internos |
| Navy hover | `#2a4a66` | Estados hover de elementos navy |
| Laranja vibrante (destaque) | `#f28933` | CTAs, destaques, logo letra O |
| Laranja claro | `#f5a55c` | Hover de botões, gradiente laranja |
| Laranja escuro | `#c96e1a` | Sombra do gradiente laranja |
| Terracota (complementar) | `#c79982` | Elementos decorativos sutis |
| Branco | `#ffffff` | Textos, ícones, elementos sobre navy |

### Gradientes
- **Laranja:** `linear-gradient(135deg, #f28933 0%, #f5a55c 50%, #c96e1a 100%)`
- **Navy:** `linear-gradient(180deg, #0f2f48 0%, #1a3d54 100%)`

### NUNCA usar
- Preto puro como fundo (`#000` ou `#1a1a1a`) — usar navy
- Dourado/gold (`#C9A84C`) — foi substituído pelo laranja Kolhey
- Roxo, azul elétrico, verde limão — fora da identidade
- Gradiente roxo sobre branco — genérico de IA, proibido

---

## Tipografia

| Função | Fonte | Peso | Uso |
|---|---|---|---|
| Display / Logo | **Cinzel** | 600–700 | Nome KOLHEY, números de fase, títulos de seção |
| Corpo | **Montserrat** | 300–700 | Todo texto de interface, parágrafos, labels |
| Slogan | Montserrat | 300 italic | "Resultados que se cultivam" sempre em itálico |

**Import Google Fonts:**
```css
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600;700&family=Montserrat:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400&display=swap');
```

### NUNCA usar
- Inter, Roboto, Arial, System UI como fonte principal
- Cinzel para textos longos (só display/logo)
- Montserrat bold em tamanhos menores que 10px

---

## Logo e Wordmark

### Regra principal
O "O" de KOLHEY é **sempre laranja** (`#f28933`). As demais letras são brancas.

```tsx
// Correto
<p className="font-display text-white font-bold tracking-widest">
  K<span className="text-brand-orange">O</span>LHEY
</p>

// Errado — nunca todo branco ou todo laranja
```

### Símbolo "K"
- Fundo: gradiente laranja (`bg-orange-gradient`)
- Letra: branco, fonte Cinzel bold
- Forma: `rounded-lg` ou `rounded-xl`
- Sombra: `shadow-orange` ou `shadow-orange-lg`

### Onça-pintada
- Usada como watermark/mascote decorativo
- Cor: branco com baixa opacidade (7–15%) sobre navy
- Nunca colorida, nunca como ícone pequeno
- Posição preferida: canto direito, grande, como elemento de fundo
- Arquivo: `components/icons/JaguarSVG.tsx`

---

## Classes Tailwind do Projeto

```
// Cores
bg-brand-navy          → #0f2f48 (fundo principal)
bg-brand-navy-soft     → #1a3d54 (sidebar/header)
bg-brand-navy-card     → #235475 (cards)
bg-brand-navy-hover    → #2a4a66 (hover)
bg-brand-orange        → #f28933 (botão primário)
bg-brand-orange-muted  → rgba(242,137,51,0.15) (fundo sutil laranja)
text-brand-orange      → laranja nos textos
text-brand-terra       → #c79982 terracota

// Gradientes
bg-orange-gradient     → gradiente laranja (logo, botões especiais)
bg-navy-gradient       → gradiente navy

// Sombras
shadow-orange          → borda sutil laranja
shadow-orange-lg       → sombra laranja difusa

// Utilitários
font-display           → Cinzel
font-sans              → Montserrat
```

---

## Componentes Padrão (globals.css)

```css
.btn-primary   → bg-brand-orange, texto branco
.btn-ghost     → borda + texto brand-orange
.card          → bg-brand-navy-card, borda branca/10
.card-gold     → bg-brand-navy-card, borda laranja/30, shadow-orange
.input         → bg-brand-navy-soft, focus laranja
.phase-done    → bg-brand-orange, texto branco
.phase-active  → bg-brand-orange-muted, borda laranja
.phase-pending → bg-brand-navy-soft, texto branco/30
```

---

## Ícones

- **Usar:** SVG inline, nunca emojis
- **Arquivo de ícones de fase:** `components/icons/PhaseIcon.tsx`
- **Onça SVG:** `components/icons/JaguarSVG.tsx`
- **Tamanhos padrão:** `w-4 h-4` (inline), `w-5 h-5` (botões), `w-6 h-6` (cards)
- **Cor:** herdar do pai via `currentColor`

---

## Estrutura do Projeto

```
agencia-esteira/              ← raiz
├── app/
│   ├── (auth)/login/         ← tela de login Kolhey
│   ├── (app)/
│   │   ├── dashboard/        ← painel principal
│   │   ├── clientes/         ← listagem + detalhe + checklist
│   │   └── esteira/          ← documento de referência das 7 fases
│   ├── globals.css           ← fonte, cores base, utilitários
│   └── layout.tsx            ← metadata "Agência Kolhey"
├── components/
│   ├── layout/Sidebar.tsx    ← logo Kolhey + nav SVG
│   ├── layout/Header.tsx     ← avatar laranja
│   ├── clients/
│   │   ├── ClientCard.tsx    ← card com progresso e fase
│   │   └── PhaseProgressBar.tsx
│   ├── dashboard/StatsBar.tsx
│   ├── checklist/ChecklistItem.tsx
│   └── icons/
│       ├── PhaseIcon.tsx     ← SVGs das 7 fases
│       └── JaguarSVG.tsx     ← mascote onça watermark
├── hooks/
│   ├── useClients.ts         ← CRUD clientes + advancePhase + regressPhase + deleteClient
│   └── useChecklist.ts
├── lib/
│   ├── phases.ts             ← 7 fases com slug, SLA, checklist, KPIs
│   └── types.ts
└── tailwind.config.ts        ← paleta navy/orange completa
```

---

## Stack Técnico

- **Framework:** Next.js 14 (App Router) + TypeScript
- **Estilo:** Tailwind CSS com paleta customizada
- **Banco:** Supabase (PostgreSQL + Auth)
- **Deploy:** Vercel → agencia-esteira.vercel.app
- **Repo:** github.com/borgesrodri4-bot/agencia-esteira

---

## Regras de Design — Checklist antes de entregar

- [ ] Fundo navy (`#0f2f48`), nunca preto
- [ ] Destaques em laranja (`#f28933`), nunca dourado
- [ ] Fonte Cinzel só em display/logo
- [ ] Montserrat no corpo
- [ ] "O" do KOLHEY em laranja no logo
- [ ] Ícones sempre SVG, nunca emoji
- [ ] Botão primário: laranja com texto branco
- [ ] Cards com borda sutil branca/10 ou laranja/30
- [ ] Animações suaves (150–300ms), sem exagero
- [ ] Mobile: bottom nav com 56px de altura mínima
- [ ] Focus rings em laranja para acessibilidade
- [ ] Skeletons animados no lugar de texto "Carregando..."
