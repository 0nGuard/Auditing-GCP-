# SCOPING MODEL

This document defines the systems, services, and operational areas included within the audit scope.

---

# 1. AUDIT OBJECTIVE

## Primary Goal
- Investigate and review the NuCore environment for misconfigurations leading to vulnerable security posture.

## Environment Type
- Google Cloud Platform set up for a startup company.

## Business Context
- Small and medium sized enterprise. Develops digital solutions for monitoring Energy Sector infrastructure.

---

# 2. IN-SCOPE RESOURCES

## Identity & Access Management
- Shared-Services service account

## Compute / Networking
- Virtual Private Cloud and Virtual Machine for application hosting

## Storage
- Two storage buckets for user uploads and business operations data

## Logging & Monitoring
- Unalert audit logs

## Backup & Recovery
- No evident backup systems or disaster recovery policy

## Application Layer
- The GridWatch Lite application for monitoring energy production

---

# 3. PRIORITY REVIEW AREAS

## High-Risk Areas
- Identity Access Management
- Networking and Compute Engine
- Virtual Machine instance hosting GridWatch

## Critical Assets
- GridWatch Lite monitoring application
- Storage bucket containing sensitive operational data
- Finance Department project

## External Exposure Points
- GridWatch application
- /admin interface for GridWatch
- VPC Network (overly-permissive)

---

# 4. OUT-OF-SCOPE ITEMS

- Backup/Recovery systems and Post-incident response plan
- Workload and Workforce Identity Federation
- Security Command Center

---

# 5. AUDIT ASSUMPTIONS

- IAM roles were over-permissioned and had Cross-project access
- The GridWatch Lite application was exposed and public-facing
- Environment relied on weak firewall rules

---

# 6. SCOPING SUMMARY

## Primary Focus
- Review the high-risk areas of the environment, document findings, and recommend or implement simple, high-impact fixes without disrupting operations.

## Primary Risk Theme
- Lack of Identity access controls and network segmentation leaves the environment vulnerable to external unauthorized access yo business critical assets and data.

## Expected Audit Outcome
- Low audit score due to the combination of various misconfigurations stemming from rapid cloud setup, over-reliance on default settings, and no governance policies.
