# QUESTION
'''given a list of emails and URLs , return a dictionary, where each key is a URL And the value is how many emails have the same domain, Note that the domains begin with www.. whereas the emails do not , and the emails with domains not in the list should be ignored.
Ex: email=['foo@a.com,'bar@a.com', 'baz@b.com', qux@d.com']
urls=['www.a.com', 'www.b.com', 'www.c.com']
Returns
{
    'www.a.com': 2,
    'www.b.com' : 1,
    'www.c.com': 0,
}'''



# SOLUTION
emails= ['foo@a.com','bar@a.com', 'baz@b.com', 'qux@d.com']
urls= ['www.a.com', 'www.b.com', 'www.c.com']

a0 = lambda a: ["www."+ i.partition("@")[2] for i in a]
a1 = lambda a: print({s:a0(a).count(s) for s in urls})
a1(emails)
