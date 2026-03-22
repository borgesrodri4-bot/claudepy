# Skill: Interface Design System

Baseado em: https://github.com/Dammyjay93/interface-design

Quando este skill for ativado, aplique o método de design system estruturado abaixo para criar interfaces consistentes e bem fundamentadas.

---

## Método: Como definir um Design System

Sempre comece definindo as **3 diretrizes** antes de escrever qualquer código de UI:

### 1. Personalidade (escolha uma)
| Opção | Uso ideal |
|-------|-----------|
| **Precision & Density** | Dashboards, admin, ferramentas de dados |
| **Warmth & Approachability** | Apps colaborativos, consumidor |
| **Sophistication & Trust** | Fintech, saúde, corporativo |
| **Boldness & Clarity** | Marketing, landing pages |
| **Utility & Function** | Dev tools, CLIs visuais |
| **Data & Analysis** | Analytics, BI, relatórios |

### 2. Fundação de cor
- `warm` → tons de stone/amber
- `cool` → tons de slate/blue
- `neutral` → cinza puro
- `tinted` → fundo com leve saturação

### 3. Profundidade
- `borders-only` → sem sombras, alta densidade
- `subtle-shadows` → sombras leves (1-3px)
- `layered-shadows` → hierarquia visual com múltiplas sombras

---

## Tokens padrão

### Espaçamento
- Base 4px: `4, 8, 12, 16, 24, 32` (denso/técnico)
- Base 8px: `8, 16, 24, 32, 48, 64` (generoso/amigável)

### Tipografia
- Escala densa: `11, 12, 13, 14, 16, 18`
- Escala padrão: `13, 14, 15, 16, 18, 20, 24`
- Pesos: `400 (normal), 500 (médio), 600 (semibold)`

### Radius
- Sharp (técnico): `4px, 6px, 8px`
- Soft (amigável): `8px, 12px, 16px`

---

## Exemplos de sistemas prontos

### Sistema: Precisão & Densidade (dashboards/admin)
```
Personalidade: Precision & Density
Fundação: Cool (slate)
Profundidade: Borders-only

Cores:
  --foreground: slate-900
  --secondary: slate-600
  --muted: slate-400
  --faint: slate-200
  --border: rgba(0, 0, 0, 0.08)
  --accent: blue-600

Botão: h-32px, padding 8px 12px, radius 4px, 13px/500
Card: border 0.5px solid faint, padding 12px, radius 6px, sem sombra
Tabela: cell padding 8px 12px, 13px tabular-nums, border-bottom faint
```

### Sistema: Calor & Acolhimento (apps colaborativos)
```
Personalidade: Warmth & Approachability
Fundação: Warm (stone)
Profundidade: Subtle shadows

Cores:
  --foreground: stone-900
  --secondary: stone-600
  --muted: stone-400
  --accent: orange-500
  --shadow: 0 1px 3px rgba(0, 0, 0, 0.08)

Botão: h-40px, padding 12px 20px, radius 8px, 15px/500, sombra sutil
Card: sem borda, padding 20px, radius 12px, sombra 1-3px
Input: h-44px, padding 12px 16px, radius 8px, border 1.5px faint
```

---

## Template para novo projeto

Ao criar uma nova interface, preencha:

```
# Meu Design System

## Direção
Personalidade: [escolha acima]
Fundação: [warm | cool | neutral | tinted]
Profundidade: [borders-only | subtle-shadows | layered-shadows]

## Tokens
Espaçamento base: [4px | 8px]
Cores: (defina --foreground, --secondary, --muted, --accent)
Radius: [sharp | soft]
Fonte: [system-ui | Inter | Geist]

## Decisões
| Decisão | Justificativa |
|---------|---------------|
| ...     | ...           |
```

---

## Integração com o projeto Agência Esteira

O projeto usa **Precision & Density** com **fundação tinted** (preto/dourado):
- Veja o skill `/frontend-design` para as classes Tailwind específicas do projeto
- Combine este método com as cores da brand (black/gold) ao criar novos componentes
