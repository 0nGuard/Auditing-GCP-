# IAM FINDINGS

The identity layer represents the primary control plane for the environment. Current configuration indicates a highly centralized administrative model.

---

## FINDINGS

### IAM-01 — Excessive Privilege Concentration

- Single OWNER-level account controls all resources

- No separation of duties or least privilege enforcement

### IAM-02 — Lack of Delegated Roles

- No service-level role segmentation observed

- Compute and storage access inherited through broad permissions

---

## RISK IMPACT

Compromise of a single identity results in full environment compromise, including compute, storage, and backup layers.
