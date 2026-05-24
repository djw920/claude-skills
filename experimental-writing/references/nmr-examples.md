# NMR Examples — Annotated ACS Format

## 1. Standard medicinal compound (¹H + ¹³C + ¹⁹F + HRMS)

**4-Fluoro-*N*-methylbenzamide (1).**
Prepared according to General Procedure A from 4-fluorobenzoic acid (140 mg, 1.00 mmol). Purification by flash chromatography on silica gel (0→50% EtOAc/hexanes) afforded **1** as a white solid (109 mg, 0.71 mmol, 71%).
mp 156–158 °C.
IR (ATR) νmax 3320, 1638, 1606, 1545, 1505, 1234 cm⁻¹.
¹H NMR (400 MHz, DMSO-*d*₆) δ 8.45 (br q, *J* = 4.5 Hz, 1H), 7.89 (dd, *J* = 8.8, 5.5 Hz, 2H), 7.27 (t, *J* = 8.9 Hz, 2H), 2.78 (d, *J* = 4.5 Hz, 3H).
¹³C NMR (101 MHz, DMSO-*d*₆) δ 165.5, 163.7 (d, *J*CF = 248.0 Hz), 131.4 (d, *J*CF = 2.9 Hz), 130.2 (d, *J*CF = 9.0 Hz), 115.4 (d, *J*CF = 21.7 Hz), 26.3.
¹⁹F NMR (376 MHz, DMSO-*d*₆) δ −110.6.
HRMS (ESI-TOF) *m/z* [M + H]⁺ calcd for C₈H₉FNO 154.0668, found 154.0670.

**Annotation notes:**
- ¹³C shows C–F coupling constants (*J*CF) — required when ¹H-decoupled ¹³C shows coupling to other magnetically active nuclei
- DMSO-*d*₆ solvent — d italicized, 6 subscripted
- [M + H]⁺ formula: C₈H₉FNO is the protonated molecule (add one H to neutral formula)
- br q for NHCH₃ — exchange-broadened but still shows coupling to the methyl protons

---

## 2. Chiral compound with optical rotation and chiral HPLC

**Methyl (*S*)-2-(benzyloxy)propanoate (12).**
Prepared according to General Procedure C. Purification by flash chromatography on silica gel (5% EtOAc/hexanes) afforded **12** as a colorless oil (310 mg, 1.49 mmol, 85%).
IR (ATR) νmax 2985, 1735, 1454, 1128 cm⁻¹.
¹H NMR (500 MHz, CDCl₃) δ 7.38–7.28 (m, 5H), 4.71 (d, *J* = 11.6 Hz, 1H), 4.56 (d, *J* = 11.6 Hz, 1H), 3.98 (q, *J* = 6.9 Hz, 1H), 3.74 (s, 3H), 1.40 (d, *J* = 6.9 Hz, 3H).
¹³C NMR (126 MHz, CDCl₃) δ 174.1, 137.8, 128.5, 127.9, 127.8, 74.6, 72.0, 52.2, 18.6.
HRMS (ESI-TOF) *m/z* [M + Na]⁺ calcd for C₁₁H₁₄O₃Na 229.0835, found 229.0833.
[α]²⁵D −42.1 (*c* 1.05, CHCl₃). Enantiomeric ratio 97:3, determined by chiral HPLC (Chiralpak IA column, 99:1 hexanes/2-propanol, 1.0 mL/min, 210 nm); *t*R (minor) = 8.4 min, *t*R (major) = 11.2 min.

**Annotation notes:**
- (*S*) in italic parentheses in compound name
- [M + Na]⁺ adduct: formula adds Na, subtracts H: C₁₁H₁₄O₃ + Na − e⁻ → C₁₁H₁₃O₃Na (no, for [M + Na]⁺, add Na to neutral: C₁₁H₁₄O₃ + Na = C₁₁H₁₄NaO₃)
- Chiral HPLC: column, mobile phase ratio, flow rate, wavelength, both retention times with minor/major assignment

---

## 3. Compound with rotamers

**(*S*)-*tert*-Butyl 4-(hydroxymethyl)-2,2-dimethyloxazolidine-3-carboxylate (18).**
Purification by flash chromatography on silica gel (20% EtOAc/hexanes) afforded **18** as a colorless oil (142 mg, 0.61 mmol, 78%). The compound exists as a mixture of rotamers at ambient temperature; signals are reported for the major rotamer unless otherwise noted.
¹H NMR (400 MHz, CDCl₃) δ 4.15–3.55 (m, 3H), 3.52–3.40 (m, 2H), 1.62 (s, 3H), 1.59 (s, 3H), 1.47 (s, 9H). [Selected signals for minor rotamer: δ 1.55 (s, 3H), 1.43 (s, 9H).]
¹³C NMR (101 MHz, CDCl₃) δ 154.3, 94.8, 80.6, 67.4, 63.8, 62.0, 28.4, 26.4, 24.8. [Selected carbons for minor rotamer: δ 94.2, 27.2.]
HRMS (ESI-TOF) *m/z* [M + Na]⁺ calcd for C₁₁H₂₁NO₄Na 254.1368, found 254.1365.

**Annotation notes:**
- Rotamers disclosed explicitly; not hidden behind ambiguous multiplets
- *tert*- italic, *S* italic in parentheses

---

## 4. Organometallic / ³¹P-containing compound

**(η⁵-Cp)Pd(PPh₃)Cl (22).**
¹H NMR (400 MHz, CDCl₃) δ 7.55–7.45 (m, 6H), 7.42–7.33 (m, 9H), 5.72 (s, 5H).
³¹P NMR (162 MHz, CDCl₃) δ 22.4 (s).
HRMS (ESI) *m/z* [M − Cl]⁺ calcd for C₂₃H₂₀PPd 449.0288, found 449.0290.

---

## 5. 2D-assigned natural product fragment

When 2D NMR data (HSQC, HMBC, NOESY) are collected, peak assignments must be provided:

¹H NMR (600 MHz, CDCl₃) δ 6.42 (1H, d, *J* = 1.8 Hz, H-5), 6.26 (1H, d, *J* = 1.7 Hz, H-7), 5.01 (1H, d, *J* = 6.6 Hz, H-1), 3.86 (3H, s, OCH₃-8).
¹³C NMR (150 MHz, CDCl₃) δ 170.6 (s, C-2ʺ), 160.6 (s, C-4a), 93.9 (d, C-7), 92.9 (d, C-5), 79.7 (d, C-1).

**Annotation notes:**
- Peak identity required when 2D experiments collected (ACS NMR guidelines §1.6)
- Multiplicity in ¹³C (s = quaternary, d = CH, t = CH₂, q = CH₃) reported when DEPT data collected

---

## 6. Multiplet reporting conventions

| Pattern | Correct notation |
|---------|-----------------|
| Clean doublet | d, *J* = 8.2 Hz |
| Doublet of doublets | dd, *J* = 12.4, 4.8 Hz |
| Doublet of triplets | dt, *J* = 11.2, 6.6 Hz |
| Triplet of doublets | td, *J* = 8.4, 2.0 Hz |
| Unresolvable complex pattern | m |
| Range for multiplet | 3.22–3.15 (m, 2H) |
| Broad singlet | br s |
| Broad doublet | br d, *J* = 9.6 Hz |

---

## 7. Solvent reference table (¹H residual solvent peaks)

| Solvent formula | Residual ¹H δ (ppm) | ¹³C δ (ppm) |
|----------------|---------------------|-------------|
| CDCl₃ | 7.26 | 77.0 |
| DMSO-*d*₆ | 2.50 | 39.5 |
| CD₃OD | 3.31 | 49.0 |
| D₂O | 4.79 | — |
| C₆D₆ | 7.16 | 128.1 |
| CD₂Cl₂ | 5.32 | 54.0 |
| acetone-*d*₆ | 2.05 | 29.8, 206.3 |
