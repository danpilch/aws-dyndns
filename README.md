# aws-dyndns
Manage a dynamic home IP address with an AWS hosted route53 domain

```
usage: dns_update.py [-h] [--region REGION] --domain DOMAIN --subdomain
                     SUBDOMAIN --zone ZONE

Update an AWS route53 DNS record with your external IP

optional arguments:
  -h, --help            show this help message and exit
  --region REGION, -r REGION
                        AWS region to connect to
  --domain DOMAIN, -d DOMAIN
                        Domain to modify
  --subdomain SUBDOMAIN, -s SUBDOMAIN
                        subdomain to modify
  --zone ZONE, -z ZONE  AWS hosted zone id
```
