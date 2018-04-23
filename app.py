import sys
import pythonwhois


try:
    data = pythonwhois.get_whois(sys.argv[1])
    del data['raw']
    print(data)
except pythonwhois.shared.WhoisException:
    print({'error': 'domain ' + sys.argv[1] + ' not found.'})
    exit(1)
except IndexError:
    print({'error': 'must specify a domain.'})
    exit(1)
