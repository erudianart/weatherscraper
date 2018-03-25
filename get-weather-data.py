import urllib2
from bs4 import BeautifulSoup

# What year?
year = 2011

# Create/open a file called wunder.txt
f = open('wunder-data-' + str(year) + '.txt', 'w')
f.write('datestamp,tmean,tmax,tmin,precip,dewpoint\n')

# Iterate through months and days
# for m in range(1, 13):
#	for d in range(1, 32):
for m in range(1, 2):
	for d in range(1, 2):

		# Check if already gone through month
		if (m == 2 and d > 28):
			break
		elif (m in [4, 6, 9, 11] and d > 30):
			break

		# Open wunderground.com url
		datestamp = str(year) + '-' + str(m) + '-' + str(d)
		print 'Getting data for ' + datestamp
		url = 'http://www.wunderground.com/history/airport/KBNA/' + str(year) + '/' + str(m) + '/' + str(d) + '/DailyHistory.html'
		print 'url ' + url
		page = urllib2.urlopen(url)

		# Get history table
		soup = BeautifulSoup(page, "html.parser")
		historyTable = soup.find('table', id='historyTable')
		spans = historyTable.find_all(attrs={'class':'wx-value'})

		# Get mean temperatures from page
		tmean = spans[0].string
		tmax = spans[2].string
		tmin = spans[5].string

		#Get precip from page
		precip = spans[9].string

		#Get dewpoint from page
		dewpoint = spans[8].string

 		# Format month for datestamp
 		if len(str(m)) < 2:
 			mStamp = '0' + str(m)
 		else:
 			mStamp = str(m)

 		# Format day for datestamp
 		if len(str(d)) < 2:
 			dStamp = '0' + str(d)
 		else:
 			dStamp = str(d)

 		# Build timestamp
		datestamp = str(year) + mStamp + dStamp

		# Write timestamp and temperature to file
		print tmean + ':' + tmax + ':' + tmax + ':' + precip + ':' + dewpoint
		f.write(datestamp + ',' + tmean + ',' + tmax + ',' + tmin + ',' + precip + ',' + dewpoint + '\n')

# Done getting data! Close file.
f.close()
