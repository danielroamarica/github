file1 = open('text.txt','w')
file1.write('hey guys,this is my first file creating by I/O')
file1.write('<html>hi I am a web</html>')
file1.close()

fr = open('text.txt','r')
text = fr.read()
print (text)
fr.close()