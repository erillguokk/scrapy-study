from lxml import etree
text = "<div class=\"u-txt\"><a href=\"/user/others-23188314.html\" class=\"u-user-name\" target=\"_blank\">" \
       "浅笑微凉 </a><span class=\"u-time  f-ib f-fr\">2020-03-02 08:10:02</span></div>"
html = etree.HTML(text)
print(etree.tostring(html).decode())
print(html.xpath("//a/text()"))
#etree会自动补全,修正html