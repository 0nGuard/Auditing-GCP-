# RISK RATING METHOD

This document defines the standardized method used to score and classify risk across all audit findings in this framework.

---

# 1. SCORING MODEL

Each finding is evaluated across three dimensions:

## Likelihood (L)
- How likely the issue is to be exploited or triggered in the current environment.

## Impact (I)
- The potential damage if the issue is exploited (data, availability, financial, operational).

## Exposure (E)
- How accessible the issue is from an attacker or misconfiguration perspective.

---

# 2. RISK SCORE CALCULATION

## Formula
Risk Score = L × I × E

Each dimension is scored on a scale:

- 1 = Low
- 2 = Medium
- 3 = High
- 4 = Critical
---

# 3. RISK LEVELS

## Low Risk
- Score: 1–3
- Limited exposure and minimal impact

## Medium Risk
- Score: 4–6
- Moderate exposure or impact, requires attention

## High Risk
- Score: 7–12
- High likelihood or significant impact

## Critical Risk
- Score: 13–27
- Immediate threat to system integrity, data, or access control

---

# 4. SCORING GUIDELINES

## Likelihood Indicators
- Public exposure increases likelihood
- Weak authentication increases likelihood
- Misconfigurations increase likelihood

## Impact Indicators
- Sensitive data exposure increases impact
- Full environment compromise increases impact
- Service downtime increases impact

## Exposure Indicators
- Internet-facing systems = high exposure
- Privileged IAM roles = high exposure
- Flat network design = high exposure

---

# 5. CONSISTENCY RULE

All findings must use this scoring model to ensure consistent prioritization across the audit lifecycle.
