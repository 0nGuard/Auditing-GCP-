## Top 3 Attack Chains   

These attack paths are some of the most realistic scenarios of compromise based on the following: IAM weaknesses, networking flaws, lack of application security, and metadata exposure.

They demonstrate how several low-severity misconfigurations combine into high-impact exploitation routes.

1. Public Application -> VM Compromise -> Finance Data Access

Path

- Using internet scanning, the exposed GridWatch application is discovered.
- Internal system details and operational information are exposed by the /admin endpoint.
- Application or VM layer is leveraged to gain further system access plus command execution capabilities.
- Service account credentials are retrieved once the metadata service is queried.
- The Shared - Services account is used to access the finance storage bucket.
- Sensitive financial reports are download and exfiltrated.

Impact

The exposure and loss of financial and strategic business data can lead to regulatory and reputational damage. And a loss of confidentiality across internal business operations.


2. Shared Service Account Abuse -> Cross - project Access

Path

- Shared - Services credentials are obtained via the VM or metadata access.
- Multiple projects are enumerated due to over - permissive IAM roles.
- Attacker infiltrates Finance and operational environments.
- Sensitive resources are accessed or modified across projects.
- Activity detection is delayed due to limited monitoring.

Impact

The cross - project compromise destabilizes business operations and puts data integrity at risk. Thus, expanding the blast radius from a single compromised credential.


3. Internet Exposure -> Network Access -> Persistent Foothold

Path

- The attacker scans and identifies exposed services (SSH, RDP, port 8080).
- Default VPC and permissive firewall rules enable direct targeting.
- Initial access is gained by brute force or vulnerability exploitation.
- Persistence is established within the VM environment.
- Minimal monitoring and lack of flow logs delays detection.

Impact

Persistent unauthorized access creates a space for lateral movement and privilege escalation. Increasing risk of the business being ransomed or attacked destructively.


# Summary

The risk is not isolated misconfigurations, but the combination of exposed application surfaces, excessive IAM trust relationships, and limited monitoring visibility.

These vulnerabilities create real - world attack paths from public exposure to sensitive financial data compromise.
