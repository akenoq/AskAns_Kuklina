#!/usr/bin/env python3

import cgi
import html
import sys
import codecs

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach());

form = cgi.FieldStorage();

t1 = form.getfirst("t1", "пусто");
t2 = form.getfirst("t2", "пусто");

t1 = html.escape(t1);
t2 = html.escape(t2);

a = int(t1);
b = int(t2);

answer = a + b;

print("Content-type: text/html\n");
print();
print(answer);
