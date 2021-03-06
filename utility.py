import urllib
from bs4 import BeautifulSoup
import re
import codecs
from datetime import datetime
import os
import urllib.request

# UTILITY FUNCTION
def check_contain_filter(topic, contain_filter):
    '''
    function
    --------
    check if topic satisfiy contain_filters in format "a,b,c ; x,y,z" means (a or b or c) and (x or y or z)
    :input:
        topic (string|list): string|list to search
    '''
    if isinstance(topic, list):
        content_string = [x.lower() for x in topic]
    else:
        content_string = topic.lower()
    search_string = contain_filter.lower()

    and_terms_satisfy = True
    for and_terms in search_string.split(';'):
        or_term_satisfy = False
        for or_term in and_terms.split(','):
            if or_term.strip() in content_string: # current or_term is in search_string
                or_term_satisfy = True
                break
        if not or_term_satisfy: # some and_term doesn't in search_string
            and_terms_satisfy = False
            break

    if and_terms_satisfy:
        return True
    else:
        return False

def get_os_name():
    if os.name == "posix":
        return "linux"
    else:
        return "windows"

def get_os_linefeed():
    if get_os_name == "linux":
        return '\n'
    else:
        return '\r\n'

def get_independent_os_path(path_list):
    path = ""
    for item in path_list:
        path = os.path.join(path, item)
    return path

def open_utf8_file_to_read(filename):
    try: 
        return codecs.open(filename, "r", "utf-8")
    except:
        return None

def open_utf8_file_to_write(filename):
    try:
        return codecs.open(filename, "w+", "utf-8")
    except:
        return None


def open_binary_file_to_write(filename):
    try:
        return open(filename, "wb+")
    except:
        return None


def open_binary_file_to_read(filename):
    try:
        return open(filename, "rb")
    except:
        return None


def read_url_source_as_html(url):  # return page as soup of BeautifulSoup
    hdr = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'none',
        'Accept-Language': 'en-US,en;q=0.8',
        'Connection': 'keep-alive'}
    try:
        req = urllib.request.Request(
            url,
            data=None,
            headers=hdr)
        f = urllib.request.urlopen(req)
        return f.read().decode('utf-8')
    except:
        print("Can't open %s " % url)
        return None


def get_date(s_date): #date la dang string, tra ve datetime
    date_patterns = ["%d/%m/%Y","%Y-%m-%d", "%d/%m/%y", "%d-%m-%Y", "%d-%m-%y" , "%d/%m.%Y"]
    for pattern in date_patterns:
        try:
            return datetime.strptime(s_date, pattern)
        except:
            pass

def get_fullurl(weburl, articleurl):
    if re.compile("(http|https)://").search(articleurl):
        return articleurl
    else:
        return weburl + articleurl
