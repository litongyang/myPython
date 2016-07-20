# __author__ = 'tongyang.li'

def test():
    for line in open("test.txt"):
        print line.encode('utf8')

test()
