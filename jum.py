from bs4 import BeautifulSoup
import urllib.request
import calendar
import csv
#link = "http://www.jamiat-ul-ulama.org/node/3971"
#content = str(urllib.request.urlopen(link).read().decode('utf8'))
#soup = BeautifulSoup(content,"html.parser")
#print(content)

verifiedNodes = []

genFile = open("JUM/gen.html","w+")
genFile.write("""<!DOCTYPE html>
<html>
<head>
<style>
.outer{border:5px solid black;}
.tag{color:orange;}
</style>
</head>
<body>""")

for node in range(3971):
    print(node, end=" ")
    try:
        print()
        link = "http://www.jamiat-ul-ulama.org/node/" + str(node)
        content = str(urllib.request.urlopen(link).read().decode('utf8'))
        if ("Home</a> » Q & A »" in content):
            genFile.write("<div class='outer'>")
            verifiedNodes.append(node)
            soup = BeautifulSoup(content,"html.parser")
            for I in soup.find_all("div", class_="field-item odd"):
                genFile.write(str(I))
                print("== I", I.text.strip())
                
            for N in soup.find_all("div", class_="question-asks"):
                genFile.write(str(N))
                print("N", N.text.replace("asks:","").strip())
                
            for Q in soup.find_all("div", class_="question-question"):
                genFile.write(str(Q))
                print("Q", Q.text.replace("Question","").strip())
                
            for A in soup.find_all("div", class_="question-answer"):
                genFile.write(str(A))
                print("A", A.text.replace("Answer","").strip())
                
            for D in soup.find_all("div", class_="breadcrumb"):
                tag = str(D.text.split("»")[2].strip())
                genFile.write('<div class="tag">'+tag+'</div>')
                print("D", D.text.split("»")[2].strip())
            genFile.write("</div>")
    except:
        print("aborted")
        pass

genFile.write("</body></html>")
genFile.flush()
genFile.close()
with open('JUM/nodes.csv', 'w') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerow(verifiedNodes)
