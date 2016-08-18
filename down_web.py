from urllib import request

url = 'http://pinyin.sogou.com/linux/download.php?f=linux&bit=32'

def download_url(file_url):
    response = request.urlopen(file_url)
    file = response.read()
    file_str = str(file)
    lines = file_str.split('\\n')
    dest_url = r'1.txt' #file directory
    svt = open(dest_url,'w')
    for line in lines:
        svt.write(line)
        svt.close()
download_url(url)