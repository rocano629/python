import xml.etree.ElementTree as ET 
tree = ET.parse("report.xml")
root = tree.getroot()


for child in root:
    for c in child:
        for a in c:
            for b in a:
                for z in b:
                    for y in z:
                        for u in y:
                            for w in u.findall('{http://schemas.microsoft.com/sqlserver/reporting/2016/01/reportdefinition}TablixRow'):
                                #print(w.tag,w.attrib)
                                for w1 in w.findall('{http://schemas.microsoft.com/sqlserver/reporting/2016/01/reportdefinition}TablixCells'):
                                    print(w1.tag,w1.attrib)
                                

#print(root)
for actor in root.findall('{http://schemas.microsoft.com/sqlserver/reporting/2016/01/reportdefinition}TablixRow'):
    print(actor.attrib)


#rint(elem)
#elems = tree.findall('Report')
#elems = root.find('Value')
#print('elems', elems)
#for elem in elems:
#    elem.text = 'A'
#tree.write("output.xml")
#print(root)
