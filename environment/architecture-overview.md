ARCHITECTURE OVERVIEW — TRUST-BASED VIEW

[ INTERNET / EXTERNAL ACTORS ]

            │

            ▼

┌─────────────────────────────────────┐

│              CLOUD LAYER            │

└─────────────────────────────────────┘

            │

            ├───────────────────────────────────────────

            │

            ▼

IAM DOMAIN

- NuCore Founder (Primary Identity)

- Shared-Services Account

  → Role: OWNER (Full Privileges)

  → Risk: Single-point privilege concentration

            │

            ├───────────────────────────────────────────

            │

            ▼

COMPUTE & NETWORK ZONE

- VM: GridWatch Lite App

- VPC: Default Network

  → Attack Surface: Application + network exposure

            │

            ├───────────────────────────────────────────

            │

            ▼

DATA STORAGE ZONE

- Cloud Storage Bucket

  → Records

  → Client Proposals

  → Risk: Data exposure / misconfiguration impact

            │

            ├───────────────────────────────────────────

            │

            ▼

OBSERVABILITY ZONE

- Logging & Monitoring System

  → System logs

  → App telemetry

  → Security events visibility

            │

            └───────────────────────────────────────────

            ▼

RESILIENCE ZONE

- Backup & Recovery System

  → Database snapshots

  → Recovery artifacts

  → Business continuity layer

   * No indications of a full backup system present
