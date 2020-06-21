import os
import re
import sys
import locale
from datetime import datetime
from xml2html_tools import read_file, add_new_article

def set_feed_info(xml, html, xml_file):
    PY_RSSLINK = 'https://feed.yohan.world/'+re.search('(\w+\.xml)$', xml_file).group(1)
    PY_LOGO = re.search('image><url>(.*)</url>', xml).group(1)
    PY_TITLE = re.search('<title>(.*?)</title>', xml).group(1)
    PY_SUBTITLE = re.search('<description>(.*?)</description>', xml).group(1)

    html = html.replace('PY_RSSLINK', PY_RSSLINK).replace('PY_LOGO', PY_LOGO).replace('PY_TITLE', PY_TITLE).replace('PY_SUBTITLE', PY_SUBTITLE)
    return(html)

def set_feed_articles(items, html):
    for item in items:
        href = re.search('<link>(.*?)</link>', item).group(1)
        title = re.search('<title>(.*?)</title>', item).group(1)

        xml_time = re.search('<pubDate>(.*?)</pubDate>', item).group(1)
        locale.setlocale(locale.LC_TIME, 'en_US.utf8')
        obj_time = datetime.strptime(xml_time[5:-6], '%d %b %Y %H:%M:%S')
        locale.setlocale(locale.LC_TIME, 'fr_FR.utf8')
        time = obj_time.strftime('%A %d %B %Y à %Hh%M')

        body = re.search('<content:encoded>(.*?)</content:encoded>', item, re.DOTALL | re.MULTILINE).group(1)
        body = body.replace('&lt;', '<').replace('&gt;', '>')

        html = add_new_article(html).replace('PY_A_HREF', href).replace('PY_A_TITLE', title).replace('PY_A_TIME', time).replace('PY_A_BODY', body)

    html = html.replace('PY_ARTICLE', '')
    return(html)


def xml_to_html(xml_file):
    xml = read_file(xml_file)
    html = read_file('./feed.html')

    html = set_feed_info(xml, html, xml_file)

    items = re.findall('<item>(.*?)</item>', xml, re.DOTALL | re.MULTILINE)
    html = set_feed_articles(items, html)
    return(html)

html = xml_to_html(sys.argv[1])
name = re.search('(\w+)\.xml$', sys.argv[1]).group(1)
with open(f'{name}.html', 'w+') as f:
    f.write(html)
