#Read the file and make a DOM tree
import xml.dom.minidom
from xml.dom.minidom import parse
DOM= xml.dom.minidom.parse("go_obo.xml")
collection = DOM.documentElement
terms = collection.getElementsByTagName('term')

#Define a function that count the number of childNodes associated with 'a'
def countnumber(a):
    count=0
    for term in terms:                                   #Get the element 'term'
        defstr=term.getElementsByTagName('defstr')       #From term get element 'defstr'
        if a in defstr[0].firstChild.data:
            subclass=term.getElementsByTagName('is_a')   # If 'a' exists in 'defstr', then read the 'is_a' of it
            for is_a in subclass:
                count= count+ 1
    print('The childnode number of '+a+' is '+ str(count)+'.')
    return count
#reports the number of childNodes associated with ‘DNA’, ‘RNA’, and ‘protein’.
DNA=countnumber('DNA')
RNA=countnumber('RNA')
Protein=countnumber('protein')
Carbohydrate=countnumber('carbohydrate')        # I choose carbohydrate macromolecule that I am interested in

import matplotlib.pyplot as plt
dic={'DNA':DNA,'RNA':RNA,'Protein':Protein,'carbohydrate':Carbohydrate}

#calculate the sum of all cases
sum= dic['DNA']+dic['RNA']+dic['Protein']+dic['carbohydrate']

#set the image
labels='DNA','RNA','Protein','carbohydrate'
#count the percentage of cases
sizes=[100*dic['DNA']/sum,100*dic['RNA']/sum,100*dic['Protein']/sum,100*dic['carbohydrate']/sum]
explode=(0,0.1,0,0.1)
plt.pie(sizes,explode=explode,labels=labels,autopct='%1.1f%%',shadow=False,startangle=90)
plt.axis('equal')
plt.title('the number of childNodes associated with each of these terms')
plt.show()        