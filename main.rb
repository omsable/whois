require 'whois'
$stdout.print Whois.whois(ARGV[0])
