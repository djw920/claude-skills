# Chemistry-Aware (Non-Overclaiming) Flags

This skill is a *visual* reviewer. It looks at rendered ChemDraw output. It does **not** verify chemistry. But certain visual symptoms are reliable hints that the *drawing* of the chemistry has a problem worth a chemist's second look — and a senior chemist (the user or a student fixing the figure) wants those flagged.

Every flag in this file uses **conditional language**. Never write "this is wrong." Write "this looks like X — please verify." The reason is twofold: (1) you cannot rule out that what looks like an error is in fact deliberate, and (2) you cannot adjudicate chemistry from a 2D depiction alone.

---

## How to phrase a chemistry flag

Use this template:

> *"[Specific visual observation]. Looks like [the underlying chemistry concern] — please verify."*

Examples of acceptable phrasing:

- *"Compound 3a in Scheme 3.2 is drawn with a methyl wedge; the same compound in Scheme 3.4 is drawn with a methyl hash. **Looks like a stereochemistry inconsistency — please verify which is intended.**"*
- *"The product of step 2 has one fewer carbon than the substrate, with no byproduct labeled on the arrow. **Looks like an apparent atom-count change — please verify the structures or label the lost fragment.**"*
- *"There is a single wedge bond at C5 with no corresponding hash. **Looks like an incomplete stereochemistry depiction — please verify whether a hash is intended.**"*

Examples of phrasing to **avoid**:

- ❌ "C5 is the wrong stereochemistry."
- ❌ "This mechanism is incorrect."
- ❌ "The product structure cannot arise from the substrate."

The first set says *check this drawing*. The second set adjudicates chemistry. Stay in the first set.

---

## The catalogue of visual symptoms

Each entry: what to look for → what it might mean → exact phrasing.

### CF-1. Dangling bond / free valence

**Look for:** a bond that ends in empty space, with no atom label and no implicit-carbon vertex. Also: a vertex where one of the expected bonds appears to be missing.

**Might mean:** an unintentional drawing error, or a deliberate `R` group whose label was deleted.

**Phrase as:**
> *"There appears to be a bond ending in empty space at [position]. Looks like a dangling valence or a missing R-group label — please verify."*

### CF-2. Wedge/hash imbalance at a chiral center

**Look for:** a carbon with one wedge bond (or one hash bond) and no complementary hash (or wedge) — particularly in contexts where both are usually drawn (e.g., explicit α-stereochemistry in natural-product synthesis).

**Might mean:** incomplete stereochemistry, or — sometimes — a deliberate omission because the second stereobond is implicit.

**Phrase as:**
> *"At [position] there is a [wedge/hash] bond with no matching [hash/wedge]. Looks like a stereochemistry that is partially drawn — please verify whether the omission is intentional."*

### CF-3. Sequential stereocenters drawn off a ring

**Look for:** two adjacent stereocenters off a ring, both drawn with stereobonds. The Stoltz handout calls this out specifically: it is hard to read and prone to ambiguity.

**Might mean:** the convention says to indicate one center with stereobonds and the other through a heteroatom or ring connection.

**Phrase as:**
> *"Two adjacent stereocenters are both drawn with stereobonds at [position]. Per the group style guide, sequential stereobonds off a ring should be avoided — consider using a heteroatom or ring connection to indicate the second center."*

### CF-4. Apparent atom-count drift across an arrow

**Look for:** a substrate and product whose carbon counts (or heteroatom counts) appear different by a recognizable fragment, with no labeled byproduct on the arrow.

**Might mean:** a deliberate transformation that loses a fragment (e.g., loss of `H2O`, `HX`, `CO2`) that should be shown over the arrow as a byproduct, OR a drawing error in either substrate or product.

**Phrase as:**
> *"The product at [position] appears to have [N fewer / N more] carbons than the substrate, and no byproduct is labeled on the arrow. Looks like either a missed byproduct annotation or an atom-count drift — please verify."*

### CF-5. Same compound number, different structures

**Look for:** compound `5` drawn one way in Scheme 3 and a *visibly different* way in Scheme 5 (different connectivity, different stereochemistry, different functional groups).

**Might mean:** numbering reused by accident, or two structures that should have different numbers.

**Phrase as:**
> *"Compound **5** in Scheme 3 (p. 12) and compound **5** in Scheme 5 (p. 18) appear to be different structures. Looks like a numbering collision — please verify."*

### CF-6. Numbering gap or duplicate within a scheme

**Look for:** compound numbers `1, 2, 3, 5, 6` (where is `4`?) or `1, 2, 2, 3` (duplicate).

**Might mean:** a deleted intermediate that was not renumbered, or a copy-paste mistake.

**Phrase as:**
> *"Compound numbering in [scheme] runs [observed sequence] — looks like a [gap / duplicate]. Please verify the numbering scheme."*

### CF-7. Reagent over an arrow with no equivalents

**Look for:** an arrow with reagent text but no `(N equiv)` annotation, AND no obvious indicator that the reagent is the solvent.

**Might mean:** missing stoichiometry, or a solvent listed where equivalents are not appropriate.

**Phrase as:**
> *"The arrow at [position] shows '[reagent]' with no equivalents annotation. If this is the stoichiometric reagent, please add `(N equiv)` per template; if it is the solvent, please move it below the arrow."*

### CF-8. Mass-balance asymmetry

**Look for:** a stoichiometric arrow where a small molecule byproduct is structurally expected (e.g., loss of HX in an elimination, loss of H2O in a condensation, evolution of N2 in a Curtius-like step) but no byproduct is shown above or below the arrow.

**Might mean:** missing labeling of evolved byproducts, which downstream readers will miss.

**Phrase as:**
> *"Step [N] involves [observed transformation, e.g. an apparent dehydration] but no byproduct is labeled. Please verify whether [H2O / HX / CO2 / N2] should be shown over the arrow."*

### CF-9. Reaction arrow used for a retrosynthesis

**Look for:** in a clearly retrosynthetic figure (target structure on the left, simpler precursors on the right with discrete disconnections), a normal solid reaction arrow is used.

**Might mean:** the wrong arrow type — should be the open-ended retrosynthetic arrow.

**Phrase as:**
> *"This figure reads as a retrosynthesis but uses standard reaction arrows. Per group style, retrosynthetic disconnections should use the open-ended retrosynthetic arrow."*

### CF-10. Resonance arrow between tautomers (or vice versa)

**Look for:** a double-headed straight arrow connecting two structures that differ in proton/atom positions (i.e., tautomers, not resonance forms).

**Might mean:** a common conceptual mix-up. Tautomers are *equilibrium*, not *resonance*.

**Phrase as:**
> *"The arrow between [structure X] and [structure Y] is a resonance arrow, but the two structures appear to be tautomers (proton in different positions). Tautomers should be related by equilibrium arrows, not a resonance arrow."*

### CF-11. Curved arrow ending in empty space (mechanism)

**Look for:** in a mechanism figure, a curved arrow that does not terminate at an atom, a bond center, or a lone pair.

**Might mean:** a drawing imprecision, or a real mechanism error — but you do not adjudicate.

**Phrase as:**
> *"The curved arrow at [position] does not appear to terminate at an atom, bond, or lone pair. Looks like an incomplete mechanism arrow — please verify the intended endpoint."*

### CF-12. Fishhook used for two-electron movement (or curved used for one)

**Look for:** half-headed (fishhook) arrows in a clearly polar mechanism, or full-headed curved arrows in a clearly radical mechanism.

**Might mean:** wrong arrow style for the mechanism class.

**Phrase as:**
> *"Mechanism arrows in this figure mix fishhook (single-electron) and standard curved (two-electron) styles. Please verify the mechanism class and use one consistent arrow type."*

### CF-13. Stereochemistry indicated from the wrong atom

**Look for:** a wedge or hash drawn from a sp²-hybridized carbon (e.g., a carbonyl carbon), or from any atom that cannot be a stereocenter.

**Might mean:** the stereobond should originate from the adjacent stereocenter, not the achiral atom.

**Phrase as:**
> *"The stereobond at [position] is drawn from what appears to be an achiral atom (e.g., a carbonyl carbon). Per the group style guide, indicate stereochemistry from the actual stereocenter — please verify and redraw."*

### CF-14. Functional-group mismatch between substrate and product

**Look for:** a clear functional-group transformation depicted by the structures themselves (e.g., alcohol → ketone, ester → amide) but the reagent shown over the arrow is implausible for that transformation.

**Might mean:** a copy-paste error, or a complex multi-step that should be condensed differently.

**Phrase as (carefully):**
> *"The transformation [substrate → product] depicts [observed change], but the reagent shown is [reagent]. Please verify whether the reagent is correct for this transformation, or whether intermediate steps have been collapsed."*

### CF-15. Catalytic-cycle direction reversed

**Look for:** in a catalytic cycle drawn as curved arrows around a central catalyst, the sequence runs in the wrong rotation (clockwise where intermediates demand counter-clockwise, or vice versa).

**Phrase as:**
> *"The catalytic cycle at [position] reads [clockwise/counter-clockwise], but the sequence of intermediates suggests the opposite direction. Please verify."*

---

## What this skill never claims

- That a structure is "wrong."
- That a mechanism is "right" or "wrong."
- That a stereochemistry assignment is correct.
- That a yield is plausible.
- That a transformation is feasible.

Every observation in this catalogue ends with *please verify*. That is not weakness — that is the contract.

## When to escalate vs. flag silently

If a single figure has **three or more** chemistry flags from this catalogue, mention in the document-level summary that the figure may need a substantive chemistry review, not just a style pass. Suggest the user have a chemist (themselves, or the student's mentor) walk through it before the next round.

If the document is a manuscript headed for submission and has **any** Critical chemistry flag (CF-1, CF-2, CF-4, CF-5, CF-13), explicitly recommend resolving it before submission.
