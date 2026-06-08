# Storage Bucket configuration

The storage bucket was one of the most vulnerable assets due to rapid deployment without security controls or a governance policy in place. 

- 2 buckets - user-uploads and Financials
- Not publicly accessible but Public Access Prevention was not enabled
- The user-uploads bucket was empty but the Financials bucket contained sensitive business operations data
- The Financials bucket content could be accessed by pdf download and copying and pasting the authenticated URL
- Some identities with excessive permissions had access to the Financials bucket
