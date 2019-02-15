aws-dyndns
=====

Manage a dynamic home IP address with an AWS hosted route53 domain

# usage
```
usage: dns_update.py [-h] --domain DOMAIN [--subdomain SUBDOMAIN]
                     [--hostname HOSTNAME] [--zone ZONE]

Manage a dynamic home IP address with an AWS hosted route53 domain

optional arguments:
  -h, --help            show this help message and exit
  --domain DOMAIN, -d DOMAIN
                        Domain to modify
  --subdomain SUBDOMAIN, -s SUBDOMAIN
                        Subdomain to modify
  --hostname HOSTNAME   Hostname to modify
  --zone ZONE, -z ZONE  AWS hosted zone id
```
