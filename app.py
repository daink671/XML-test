# pip install --upgrade lxml

import xml.etree.ElementTree as ET
tree = ET.parse('example.xml')
root = tree.getroot()
#xmlstr = ElementTree.tostring(ET, encoding='utf8', method='xml')
print(root.findall('.//MARK'))

for i in root.findall("./ASSESSMENTS/STUDENT/MARK"):
    print(i)

    