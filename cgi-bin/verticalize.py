#!/usr/bin/env python
# coding: utf-8

import cgi
form=cgi.FieldStorage()
html_body = u"""
<html>
<head>
<meta http-equiv="content-type" content="text/html;charset=utf-8"> </head>
<body>
TEST
%s
</body>
</html>"""
body_line=[]
body=form.getvalue('body', '')
body=unicode(body,'utf-8', 'ignore') #(1)
for cnt in range(0, len(body), 10):
    line=body[:10]
    line+=''.join([u'□' for i in range(len(line), 10)])    # (2)
    body_line.append(line)
    body=body[10:]
body_line_v=[u' '.join(reversed(x)) for x in zip(*body_line)]  # (3)

print ("Content-type: text/html¥n")
print ("(html_body % '<br />'.join(body_line_v)).encode('utf-8')")"
