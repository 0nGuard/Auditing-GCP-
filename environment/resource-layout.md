# RESOURCE LAYOUT — GRIDWATCH LITE AUDIT ENVIRONMENT

This document represents the authoritative inventory of cloud resources observed within the scoped environment. It is structured to support audit traceability, findings correlation, and remediation planning.

---

## 1. IDENTITY & ACCESS MANAGEMENT (IAM)

### Primary Identity

- Principal: NuCore Founder

- Account Type: Shared Services / Root-Level Administrative Identity

- Role Assignment: OWNER

- Scope: Full project-level control

### Key IAM Constructs

- Service Accounts: (Implicit / Not explicitly separated)

  - Default compute service account (attached to VM workload)

- Privilege Model:

  - Flat administrative structure

  - No enforced least-privilege segmentation observed

- Authentication Controls:

  - MFA enforcement: Evident but assumed inconsistent in startup configuration

  - Role separation: Absent (single owner authority model)

### Audit Exposure Points

- Excessive privilege concentration in single identity

- Lack of delegated administration boundaries

- Potential for credential-based full environment compromise

---

## 2. COMPUTE ENGINE & NETWORKING

### Compute Resources

- Instance Name: GridWatch Lite VM

- Type: Compute Engine Virtual Machine

- Purpose: Application hosting (GridWatch Lite service)

- Workload Type: Lightweight cloud application / monitoring utility

### Network Configuration

- VPC: Default Startup VPC Network

- Subnet Model: Implicit default segmentation

- External Connectivity: Enabled (assumed for application accessibility)

### Security Characteristics

- Firewall posture: Likely permissive / minimally segmented

- Network isolation: Limited (default VPC reliance)

- Ingress exposure: Application-level entry point assumed

### Audit Exposure Points

- Flat network topology increases lateral movement risk

- VM likely exposed via broad ingress rules

- No evidence of micro-segmentation or zero-trust boundaries

---

## 3. STORAGE LAYER

### Cloud Storage Assets

- Bucket Name: Startup Records Bucket (logical grouping)

- Data Categories:

  - Client Records

  - Client Proposals

  - Operational Documents (assumed mixed sensitivity)

### Access Model

- Likely IAM-bound access via OWNER role

- Potential public access misconfiguration risk (not explicitly confirmed)

### Data Classification

- Sensitive Business Data:

  - Client proposals (confidential)

  - Operational records (internal use)

### Audit Exposure Points

- Over-broad IAM access to sensitive data

- Lack of explicit data classification enforcement

- Potential absence of object-level access controls

---

## 4. LOGGING & MONITORING

### Logging Infrastructure

- Central Logging System: Enabled (Google Cloud Logging equivalent)

- Log Types:

  - Application logs (GridWatch Lite)

  - System events (VM-level)

  - IAM activity logs (assumed enabled but not validated)

### Monitoring Scope

- Basic operational monitoring present

- Security event correlation: Not confirmed / likely minimal

### Visibility Gaps

- No evidence of alerting rules defined

- No SIEM integration observed

- Limited behavioral anomaly detection

### Audit Exposure Points

- Logging exists but may lack actionable detection capability

- Possible blind spots in identity-based events

- No evidence of threat detection pipeline

---

## 5. BACKUP & RECOVERY

### Backup Resources

- Database Snapshot System (logical representation)

- Recovery Storage Location: Backup datastore / snapshot repository

### Coverage

- Application state backups: Assumed

- Data persistence layer: Present (database-backed system implied)

### Recovery Characteristics

- Recovery strategy: Unverified (likely manual or semi-automated)

- RPO/RTO definitions: Not documented

- Versioning strategy: Unknown / not explicitly defined

### Audit Exposure Points

- Recovery process not formally defined

- Potential mismatch between backup existence and restoration readiness

- No evidence of tested disaster recovery procedure

---

## 6. CROSS-RESOURCE RELATIONSHIPS

### IAM Dependency Model

- All resources implicitly controlled via OWNER-level identity

- No delegated role hierarchy observed

### Compute ↔ Storage Relationship

- VM likely reads/writes to Storage Bucket directly

- No intermediate access mediation layer identified

### Logging Dependency Model

- Central logging dependent on VM and cloud-native services

- No independent log archival or immutability layer observed

### Backup Dependency Model

- Backup system likely tied to database or compute snapshots

- No externalized resilience layer identified

---

## 7. SUMMARY OF ARCHITECTURAL RISK CHARACTERISTICS

- Flat IAM structure with excessive privilege concentration

- Default network configuration with minimal segmentation

- Mixed-sensitivity storage without explicit governance controls

- Logging present but potentially non-operational from a detection standpoint

- Backup systems exist but lack verified recovery governance

---

END OF RESOURCE LAYOUT
