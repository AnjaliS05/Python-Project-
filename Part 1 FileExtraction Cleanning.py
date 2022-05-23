#File Extraction

import PyPDF2

import re



a=PyPDF2.PdfFileReader('Head First Python.pdf')

#print(a.documentInfo)


#print(a.getNumPages())


#print(a.getPage(2))


#print(a.getPage(3).extractText())


#Extract data

str = ""

for i in range(1,624):
    str +=a.getPage(i).extractText()


with open("text1.txt","w",encoding='utf-8') as f:
    text=f.write(str)

# Clean data -remove punctuations
new_str=re.sub('[^a-zA-Z0-9\n]', ' ',str)
open('output1.txt','w').write(new_str)


#split data in such a way that every words is isolated 
result=new_str.split()
print(result)







