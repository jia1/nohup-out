import xml.etree.ElementTree as ET

tree = ET.parse('english-lexical-sample.train.xml')
root = tree.getroot()

with open('english-lexical-sample.train.key', 'w') as k:
    for lexelt in root:
        lexelt_item = lexelt.attrib['item']
        for instance in lexelt:
            instance_id = instance.attrib['id']
            for answer in instance.findall('answer'):
                sense_id = answer.attrib['senseid']
                k.write('{0} {1} {2}\n'.format(lexelt_item, instance_id, sense_id))

