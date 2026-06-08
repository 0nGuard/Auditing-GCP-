# Audit Framework

1. Environment Reconnaissance

  Document:

• Projects

• VMs

• Service accounts

• Buckets

• Firewall rules

• Public exposure


2. IAM Review

Focus on:

• Primitive roles (Owner, Editor)

• Shared service account reuse

• Cross-project permissions

• Default SA usage

• Excessive Finance access


3. Network Exposure

Document:

• 0.0.0.0/0

• Open port 8080

• Public IP exposure

• Lack of segmentation


4. Application Security Review

Analyze:

• No authentication

• /admin exposure

• Sensitive operational info leakage

• No TLS

• Weak deployment controls


5. Metadata & Identity Risk

Test/document:

curl "http://metadata.google.internal/computeMetadata/v1/" \\

-H "Metadata-Flavor: Google"

Then evaluate:

• Accessible tokens

• Attached SA privileges

• Pivot opportunities


6. Data Exposure Review

Finance bucket:

• Who can access it?

• Is it public?

• Cross-project access?

• Sensitive report contents?
