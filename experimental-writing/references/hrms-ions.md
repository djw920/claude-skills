# HRMS Ion Type Selection Guide

## 1. Ion Types and When to Use Them

### Positive-ion ESI (ESI+) — most common for drug-like molecules

| Ion | Formula relationship | Use when |
|-----|---------------------|----------|
| [M + H]⁺ | Neutral + 1H, +1 charge | Basic N, most amides, hydroxamates, default choice |
| [M + Na]⁺ | Neutral + Na, +1 charge | Poor ionization as [M+H]⁺; ethers, esters, carbohydrates |
| [M + K]⁺ | Neutral + K, +1 charge | Rarely reported; confirm with spectrum |
| [M + NH₄]⁺ | Neutral + NH₄, +1 charge | Neutral polar compounds; common in ammonium acetate mobile phase |
| [M + 2H]²⁺ | Neutral + 2H, +2 charge | Large peptides, multiply basic compounds |

### Negative-ion ESI (ESI−)

| Ion | Formula relationship | Use when |
|-----|---------------------|----------|
| [M − H]⁻ | Neutral − 1H, −1 charge | Carboxylic acids, phosphonates, sulfonamides, phenols |
| [M + HCOO]⁻ | Neutral + formate | When [M−H]⁻ not observed; formate buffer in mobile phase |
| [M + Cl]⁻ | Neutral + Cl | Rarely primary choice |

### EI (electron ionization)

| Ion | Formula relationship | Use when |
|-----|---------------------|----------|
| [M]⁺• | Neutral, +1 charge (radical cation) | Volatile compounds; GC-MS samples |

### APCI

Used similarly to ESI for less polar compounds. Report as APCI+ or APCI−.

---

## 2. Formula Verification Rules

### For [M + H]⁺
- calcd formula = molecular formula + H (add 1 H to the neutral)
- Example: neutral C₁₃H₁₂N₄O₃ → ion C₁₃H₁₃N₄O₃ (calcd 273.0982)
- Charge is +1; monoisotopic mass used

### For [M + Na]⁺
- calcd formula includes Na
- Example: neutral C₁₁H₁₄O₃ → ion C₁₁H₁₄NaO₃ (calcd 229.0835)
- Do NOT subtract H — the sodium adduct retains all protons

### For [M − H]⁻
- calcd formula = molecular formula − H
- Example: neutral C₁₃H₁₂N₄O₃ → ion C₁₃H₁₁N₄O₃ (calcd 271.0831)

### For [M]⁺• (EI)
- calcd formula = molecular formula (no added or removed atoms)
- Monoisotopic mass

---

## 3. Mass Accuracy Thresholds

| Technique | Acceptable Δ |
|-----------|-------------|
| EI-sector | ≤5 ppm |
| ESI-TOF | ≤5–10 ppm |
| ESI-Orbitrap | ≤2–5 ppm |
| APCI | ≤10 ppm |

Always report the actual **found** mass, not just "within tolerance."

---

## 4. Common Errors

| Error | Correct practice |
|-------|-----------------|
| Using molecular formula instead of ion formula | Always add/subtract atoms for the specific ion |
| Reporting [M+H]⁺ for an acid (should be [M−H]⁻) | Match ion to ionization mode actually used |
| Omitting charge state designation | Always include ⁺ or ⁻ superscript |
| Reporting average mass instead of monoisotopic | HRMS always uses monoisotopic masses |
| Rounding found value to match calcd | Report actual instrument output |
| Formula inconsistent with structure drawn | Cross-check formula against ChemDraw or ChemDoodle atom count |

---

## 5. Standard Reporting Format

> HRMS ([ionization]-[analyzer]) *m/z* [ion designation] calcd for [ion formula including charge carrier atoms] [calcd value], found [found value].

Full examples:
> HRMS (ESI-TOF) *m/z* [M + H]⁺ calcd for C₁₃H₁₃N₄O₃ 273.0982, found 273.0980.
> HRMS (ESI-Orbitrap) *m/z* [M − H]⁻ calcd for C₁₃H₁₁N₄O₃ 271.0831, found 271.0829.
> HRMS (EI) *m/z* [M]⁺• calcd for C₁₂H₁₄O₂ 190.0994, found 190.0992.
> HRMS (APCI-TOF) *m/z* [M + Na]⁺ calcd for C₁₁H₁₄NaO₃ 229.0835, found 229.0837.
