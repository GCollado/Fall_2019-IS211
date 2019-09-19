
from datetime import datetime
import argparse
import csv
import urllib.request
import re

parser = argparse.ArgumentParser(description='Downloads a web log')
parser.add_argument('url', help='Web File location Address')
args = parser.parse_args()

#Downloads the file, decodes to utf-8, and returns its data.
def download_web_log(url):
    content = urllib.request.urlopen(url)
    data = content.read()
    return data.decode('utf-8')

#Reads and processes the CSV file.
def process_file(data):
    file = download_web_log(data)
    csv_file = []
    file = csv.reader(file.splitlines()) #splits file and converts to csv
    for row in file:
        row[1] = datetime.strptime(row[1], "%Y-%m-%d %H:%M:%S")
        csv_file.append(row)
    return csv_file

#Calculates the number of image file hits and displays its percentage.
def image_search_hits(file):
    file_content = process_file(file)
    file_type =r'\.jpg$|\.gif$|\.png$'
    pattern = re.compile( file_type, re.I)
    hit_total = 0
    image_hit_total = 0
    for item in file_content:
        matches = pattern.finditer(item[0])
        for match in matches:
            image_hit_total +=1
        hit_total +=1
    percentage = image_hit_total/hit_total * 100.0
    print("Image requests account for {}% of all requests.".format(percentage))

#Calculates each used browser's total and displays the most popular browser.
def popular_browser(file):
    file_content = process_file(file)
    user_agent = r'Firefox/.{1,}$|Chrome/.{1,}/$|Trident/.{1,}$|Safari/.{1,}$'
    browser = ''
    ff, chrome, ie, safari = 0,0,0,0
    pattern = re.compile(user_agent, re.I)
    for item in file_content:
        matches = pattern.finditer(item[2])
        for match in matches:
            if 'Firefox' in item[2]:
                ff +=1
            elif 'Chrome' in item[2]:
                chrome += 1
            elif 'Trident' in item[2]:
                ie += 1
            elif 'Safari' in item[2]:
                safari += 1
    browsers = [ff, chrome, ie, safari]
    most_used = max(browsers)
    if most_used == ff:
        pop_browser = "Firefox"
    elif most_used == chrome:
        pop_browser = "Chrome"
    elif most_used == ie:
        pop_browser = "Internet Explorer"
    elif most_used == safari:
        pop_browser = "Safari"
    print("The most popular brower is {}.".format(pop_browser))

#Calculates the number of hits per hour.
def hits_per_hour(file):
    file_content = process_file(file)
    hours = [hour for hour in range(24)]
    hit_count = 0
    for hour in hours:
        for item in file_content:
            if item[1].hour == hour:
                hit_count += 1
        print("Hour {} has {} hits.".format(hour, hit_count))
        hit_count=0

#Displays image hits total, the most popular browser and the number of
# hits per hour.
def main():
    image_search_hits(args.url)
    popular_browser(args.url)
    hits_per_hour(args.url)


main()
