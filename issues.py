import requests, json, csv
from requests.auth import HTTPBasicAuth

logfile = 'issues.csv'

y = requests.get('https://api.github.com/repos/usnationalarchives/OPAProd/issues?milestone=1&per_page=100', auth=HTTPBasicAuth('<user>', '<password>'))
parsed = json.loads(y.text)

total = parsed[0]['milestone']['open_issues']
print '* ' + str(total) + 'issues found. *'

# For getting comments, not currently supported:
# requests.get('https://api.github.com/repos/usnationalarchives/OPAProd/issues/36/comments', auth=HTTPBasicAuth('', ''))

n = 0
with open(logfile, 'w') as log :
	writelog = csv.writer(log, delimiter= '\t', quoting=csv.QUOTE_ALL)
	writelog.writerow( ('Number', 'URL', 'Title', 'Time created', 'Text') )
	log.close()
	
while total > n :
	print str(n + 1) + ': Issue ' + str(parsed[n]['number'])
	with open(logfile, 'a') as log :
		writelog = csv.writer(log, delimiter= '\t', quoting=csv.QUOTE_ALL)
		writelog.writerow( (str(parsed[n]['number']), str(parsed[n]['html_url']), parsed[n]['title'].encode('utf-8'), str(parsed[n]['created_at']), parsed[n]['body'].encode('utf-8')) )
		log.close()
	n = n + 1
