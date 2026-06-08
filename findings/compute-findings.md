# Compute Findings

Compute Engine is for the deployment of virtual machines and VPC networks. The GridWatch application is hosted on a VM but lacks proper segmentation and access controls. 

## Findings

### Compute - 01 - Publicly Accessible Application Exposure

- GridWatch application is accessible through the internet due to open network ports. And the /admin interface is reachable via the same pathway. 
- No access controls for user authorization. 

### Compute - 02 - Default configuration and Network weaknesses

- VPC network relies solely on default configurations and contains over-permissive firewall rules.
- No evidence of hierarchical policies or network flow logs. 
- Virtual machine is accessible via the Shared-Services account. 

## Risk Impact

Unauthorized access to the application exposes sensitive metadata and provides the means for lateral movement via credential enumeration. Additionally, the VM can be used as a persistence point. Business operations could experience downtime due to identity-centric environment compromise. 
