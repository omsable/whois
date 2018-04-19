import sys
import json
import whois

try:
    domain = whois.query(sys.argv[1])
    if domain.creation_date:
        domain.creation_date = str(domain.creation_date)
    if domain.expiration_date:
        domain.expiration_date = str(domain.expiration_date)
    if domain.last_updated:
        domain.last_updated = str(domain.last_updated)
    if domain.name_servers:
        domain.name_servers = list(domain.name_servers)
    sys.stdout.write(json.dumps(domain.__dict__, indent=4))
except Exception as e:
    sys.stdout.write(json.dumps({'error': str(e)}, indent=4))

