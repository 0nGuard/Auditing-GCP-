# EVIDENCE COLLECTION

This document summarizes the evidence gathered during the audit process and the artifacts used to validate the highest-priority findings.

---

# 1. EVIDENCE TYPES

## Configuration Evidence
- IAM role assignments
- Firewall configurations
- Storage permissions
- VM/network settings

## Log Evidence
- Authentication events
- System activity logs
- Application runtime logs
- Monitoring alerts/events

## Application Evidence
- Source code review
- Runtime observations
- Deployment characteristics

## Infrastructure Evidence
- Resource inventory
- Network relationships
- Service exposure mapping

---

# 2. EVIDENCE COLLECTED — TOP PRIORITY FINDINGS

## Finding 1 — Overly broad permissions for IAM roles

### Evidence Sources
- Role assignments
- System activity logs
- Token issuance history

### Key Observations
- The NuCore founder and the Shared-Services account had Owner-level privileges.
- The Shared-Services account was left enabled and the service account key remained active.
- No indication of tags and labels used for tracking and managing resources.

### Impact Area
- Identity Access Management and the authentication and authorization layer.

---

## Finding 2 — Unsegmented network and Weak Compute infrastructure

### Evidence Sources
- Firewall rule configurations
- Network activity logs
- Network relationships

### Key Observations
- Firewall rules were overly-permissive and relied on default configurations.
- No hierarchial policies were present.
- The Shared-Services account had permission to access a VM instance.

### Impact Area
- Networking and compute + VPC and VM deployment

---

## Finding 3 — VM hosted application publicly accessible

### Evidence Sources
- System audit logs
- Source code review
- Deployment characteristics

### Key Observations
- A lack of security controls to restrict unauthorized access
- The /admin interface was accessible by external actors
- Metadata related to the environment and sensitive business material was available

### Impact Area
- Application security and network accessibility

---

# 3. FINAL SUMMARY

## Audit Visibility
- Minimal visibility due to activity logs from Logging and Monitoring but imbalanced as a result of no alert policies, usage logs, and flow logs.

## Primary Risk Areas
- Identity and Privileged access management
- Networking and Compute Infrastructure
- The public facing GridWatch Lite Application

## Overall Assessment
- Environment is disorganized.There is a lack of identity-based policies, conditional access controls, network segmentation, and visibility.

## Recommended Next Steps
- Create custom IAM roles and strict conditional access policies.
- Segment the network and disable access to or from over-privileged service accounts.
- Change firewall configurations for compute and virtual environments hosting company assets.
