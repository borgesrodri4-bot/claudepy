




# Kolhey Design Prompt — Referência Rápida

Prompt condensado com toda a identidade visual da Kolhey para uso como referência no Claude Code.

---

## Design Tokens (CSS Variables)

```css
:root {
  /* Cores primárias */
  --navy:        #0f2f48;
  --navy-soft:   #1a3d54;
  --navy-card:   #235475;
  --navy-hover:  #2a4a66;

  /* Cores de destaque */
  --orange:      #f28933;
  --orange-light:#f5a55c;
  --orange-dark: #c96e1a;
  --orange-muted:rgba(242,137,51,0.15);

  /* Complementar */
  --terra:       #c79982;
  --white:       #ffffff;

  /* Status */
  --ok:          #22C55E;
  --warning:     #F59E0B;
  --danger:      #EF4444;
  --paused:      #6B7280;

  /* Gradientes */
  --orange-gradient: linear-gradient(135deg, #f28933 0%, #f5a55c 50%, #c96e1a 100%);
  --navy-gradient:   linear-gradient(180deg, #0f2f48 0%, #1a3d54 100%);

  /* Sombras */
  --shadow-orange:    0 0 0 1px rgba(242,137,51,0.3);
  --shadow-orange-lg: 0 4px 24px rgba(242,137,51,0.15);

  /* Tipografia */
  --font-display: 'Cinzel', serif;
  --font-body:    'Montserrat', system-ui, sans-serif;

  /* Espaçamento */
  --space-unit: 8px;
}
```

---

## Direção Criativa

- **Estilo:** Premium corporativo — sofisticado, confiante, sem ser formal demais
- **Referências de mercado:** Framer.com, Linear.app, Stripe
- **Tom visual:** Dark mode navy com destaque em laranja vibrante
- **Mascote:** Onça-pintada como watermark decorativo (branco, 7–15% opacidade, canto direito, grande)
- **Personalidade:** Agência do Tocantins com força e precisão de jaguar

---

## Tipografia

| Uso | Fonte | Peso | Tamanho |
|---|---|---|---|
| Logo / Display H1 | **Cinzel** | 600–700 | 2rem–5rem |
| Subtítulo / Slogan | Montserrat | 300 italic | 0.875rem–1rem |
| Corpo / Labels | Montserrat | 300–700 | 0.75rem–1rem |

**Regras:**
- Cinzel SOMENTE para KOLHEY wordmark e números grandes de fase
- Montserrat para TODO texto de interface
- "Resultados que se cultivam" sempre em Montserrat italic weight-300
- NUNCA: Inter, Roboto, Arial como fonte principal

**Google Fonts import:**
```css
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600;700&family=Montserrat:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400&display=swap');
```

---

## Hierarquia de Cores

1. **Fundo principal:** navy `#0f2f48` — NUNCA preto puro
2. **Superfícies secundárias:** navy-soft `#1a3d54` (sidebar, header)
3. **Cards / painéis:** navy-card `#235475`
4. **Destaque / CTAs:** orange `#f28933` — NUNCA dourado
5. **Textos:** branco sobre navy
6. **Bordas sutis:** `rgba(255,255,255,0.08–0.10)`
7. **Bordas de destaque:** `rgba(242,137,51,0.20–0.30)`

**Proibido:**
- Preto puro `#000` ou `#1a1a1a` como fundo
- Dourado/gold `#C9A84C` (substituído pelo laranja Kolhey)
- Roxo, azul elétrico, verde limão
- Gradiente roxo sobre branco (clichê de IA)

---

## Logo Kolhey

```tsx
// Símbolo K
<div className="w-11 h-11 bg-orange-gradient rounded-xl flex items-center justify-center shadow-orange-lg">
  <span className="font-display text-white font-bold text-xl">K</span>
</div>

// Wordmark — O sempre laranja
<p className="font-display text-white font-bold tracking-widest">
  K<span className="text-brand-orange">O</span>LHEY
</p>

// Slogan
<p className="font-sans text-white/40 text-xs italic font-light tracking-wide">
  Resultados que se cultivam
</p>
```

---

## Animações Obrigatórias

```css
/* 1. Page load — stagger fadeIn */
@keyframes fadeIn {
  from { opacity: 0; transform: translateY(12px); }
  to   { opacity: 1; transform: translateY(0); }
}
.animate-fadeIn { animation: fadeIn 0.4s ease forwards; }

/* 2. Hover elevation */
.card:hover { transform: translateY(-2px); transition: all 0.3s ease; }

/* 3. CTA pulse (laranja) */
@keyframes pulse-orange {
  0%, 100% { box-shadow: 0 0 0 0 rgba(242,137,51,0.4); }
  50%       { box-shadow: 0 0 0 8px rgba(242,137,51,0); }
}
.btn-primary:focus { animation: pulse-orange 1.5s infinite; }
```

**Regras:**
- Duração: 150–300ms para micro-interações, 400ms para page load
- Sem exagero — movimento suave e profissional
- `transition-all duration-200` como padrão
- Stagger nos cards: delay de 50ms por item

---

## Estrutura de Seções (Landing Page)

### 1. Navbar
- Fundo: navy-soft com `backdrop-blur`
- Logo K + KOLHEY à esquerda
- Nav links ao centro
- CTA "Falar com a Kolhey" à direita (btn-primary)
- Sticky com `border-b border-white/5` ao scrollar

### 2. Hero
- Fundo: navy com glow laranja top-center
- Headline em Cinzel bold `text-5xl md:text-7xl`
- Subtítulo em Montserrat italic
- CTA primário + secundário
- Onça-pintada watermark à direita (opacidade 10%)
- Badge "Agência do Tocantins" pill

### 3. Sobre
- Grid 2 colunas: texto + stats
- Stats em cards navy-card com número grande em Cinzel laranja
- Exemplo: `47` clientes, `7` fases, `98%` satisfação

### 4. Diferencial
- Bento grid 3 colunas (mobile: 1 col)
- Cards com PhaseIcon + título + descrição
- Card de destaque maior com `card-gold` (borda laranja)

### 5. CTA Final
- Fundo: orange-gradient
- Texto branco, CTA invertido (fundo branco, texto laranja)
- Slogan em Cinzel

### 6. Footer
- Fundo: navy-soft
- Logo + slogan italic
- Links organizados em colunas
- Bordas `border-t border-white/5`
- "By Kolhey" + ano

---

## Classes Tailwind do Projeto

```
/* Cores */
bg-brand-navy          → #0f2f48
bg-brand-navy-soft     → #1a3d54
bg-brand-navy-card     → #235475
bg-brand-navy-hover    → #2a4a66
bg-brand-orange        → #f28933
bg-brand-orange-muted  → rgba(242,137,51,0.15)
text-brand-orange      → laranja nos textos
text-brand-terra       → #c79982 terracota

/* Gradientes */
bg-orange-gradient     → gradiente laranja
bg-navy-gradient       → gradiente navy

/* Sombras */
shadow-orange          → borda sutil laranja
shadow-orange-lg       → sombra laranja difusa

/* Tipografia */
font-display           → Cinzel
font-sans              → Montserrat
```

---

## Componentes Padrão

```css
.btn-primary   → bg-brand-orange text-white rounded-lg px-4 py-2 font-semibold
.btn-ghost     → border border-brand-orange text-brand-orange rounded-lg px-4 py-2
.card          → bg-brand-navy-card border border-white/10 rounded-xl p-4
.card-gold     → bg-brand-navy-card border border-brand-orange/30 shadow-orange rounded-xl p-4
.input         → bg-brand-navy-soft border border-white/10 rounded-lg px-3 py-2 focus:border-brand-orange
.label         → text-white/60 text-xs uppercase tracking-wide mb-1
```

---

## Ícones

- **Usar:** SVG inline, `currentColor`, NUNCA emojis
- **Tamanhos:** `w-4 h-4` (inline), `w-5 h-5` (botões), `w-6 h-6` (cards)
- **Onça SVG:** `components/icons/JaguarSVG.tsx` — watermark, branca, baixa opacidade
- **Fases SVG:** `components/icons/PhaseIcon.tsx` — SVGs das 7 fases

---

## Regras de Qualidade

- HTML semântico (`section`, `article`, `nav`, `header`, `main`, `footer`)
- CSS variables para tokens (nunca hex hardcoded)
- Mobile-first (`md:`, `lg:` breakpoints)
- Espaçamento múltiplos de 8px (`p-2`=8px, `p-4`=16px, `p-6`=24px...)
- SVG inline para todos os ícones
- Contraste mínimo 4.5:1 para acessibilidade
- `focus:ring-2 focus:ring-brand-orange` para todos os interativos
- Imagens em WebP com `alt` descritivo
- Skeletons animados no lugar de "Carregando..."
- Mobile: botões mínimo 44px de altura, bottom nav 56px

---

## Checklist antes de entregar

- [ ] Fundo navy `#0f2f48`, nunca preto
- [ ] Destaques em laranja `#f28933`, nunca dourado
- [ ] Cinzel só em logo/display
- [ ] Montserrat no corpo
- [ ] "O" do KOLHEY em laranja
- [ ] Ícones sempre SVG, nunca emoji
- [ ] Botão primário: laranja com texto branco
- [ ] Cards com borda white/10 ou orange/30
- [ ] Animações 150–300ms, sem exagero
- [ ] Focus rings em laranja
- [ ] Skeletons no lugar de "Carregando..."
- [ ] Testado em mobile (min 375px)
