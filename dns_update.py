import boto3
import json
import urllib
import argparse


class AWSDynDns(object):
    def __init__(self):
        self.ip_service = "http://httpbin.org/ip"

    def get_external_ip(self):
        try:
            self.external_ip_request = urllib.urlopen(self.ip_service).read()
            self.external_ip = json.loads(self.external_ip_request)['origin']
            print "Found external IP: {0}".format(self.external_ip)
        except Exception as e:
            raise "error getting external IP"

    def update_record(self, region, domain, subdomain, hosted_zone_id):
        self.get_external_ip()
        client = boto3.client('route53')
        response = client.change_resource_record_sets(
            HostedZoneId=hosted_zone_id,
            ChangeBatch={
                'Comment': 'string',
                'Changes': [
                    {
                        'Action': 'UPSERT',
                        'ResourceRecordSet': {
                            'Name': '{0}.{1}'.format(subdomain, domain),
                            'Type': 'A',
                            'TTL': 123,
                            'ResourceRecords': [
                                {
                                    'Value': self.external_ip
                                },
                            ],
                        }
                    },
                ]
            }
        )
        print response



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Update an AWS route53 DNS record with your external IP")

    parser.add_argument(
        "--region", "-r",
        default="eu-west-1",
        help="AWS region to connect to",
        required=False
    )

    parser.add_argument(
        "--domain", "-d",
        help="Domain to modify",
        required=True
    )

    parser.add_argument(
        "--subdomain", "-s",
        help="subdomain to modify",
        required=True
    )
    
    parser.add_argument(
        "--zone", "-z",
        help="AWS hosted zone id",
        required=True
    )

    args = parser.parse_args()

    run = AWSDynDns()
    run.update_record(args.region, args.domain, args.subdomain, args.zone)
