from lxml import etree

root_element = etree.parse('./sample.xml').getroot()

book = root_element.xpath('//book[@id="bk101"]')[0]

multi = book.xpath('./multi[@id="m1"]')[0]
for tag in list(multi.xpath('./thread[@id="th1"]/descendant::tag[3]')):
    print('tag3:{}'.format(tag.attrib['id']))
    print('tag3の前方タスク：　%s' % [x.attrib['id'] for x in tag.xpath('./preceding::tag')])
    print('tag3の子供： %s' % [x.tag for x in tag])

print('-------------------------------------------')
for tag in list(multi.xpath('./thread/descendant::tag[1]')):
    print('thread内の先頭タスク： {}'.format(tag.attrib['id']))
    print('thread内の先頭タスクの子供：%s' % [x.tag for x in tag])
    print('thread内の先頭タスクのtext：%s' % tag.text)

