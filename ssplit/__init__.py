#!/usr/bin/env python3
import pickle, os, regex, sys

mydir = os.path.dirname(__file__)
prefix_types = pickle.load(open("%s/prefix_types.dat"%mydir,'rb'))

whitespace = regex.compile(r'\s+', regex.U+regex.M)
paragraph_boundary = regex.compile(r'(.*)(?=\r*\n){2,}', regex.M)

sntpat = regex.compile(r"\s*(?P<snt>[^\s].*?"
                       "(?P<prefix>[^\s]*?)"
                       "(?P<punct>[.?!]+)['\")\]\p{Pf}]*)(?:\s+|$)"
                       "(?=(['\"(?P<inipunct>\[¿¡\r\n\p{Pi}]*)[\s]*\p{Lu}|$)",
                       regex.U+regex.S+regex.M)

def psplit(text):
    if type(text) == str:
        for p in paragraph_boundary.split(text):
            yield p
            pass
    elif text == sys.stdin:
        buffer = []
        for line in text:
            line = line.strip()
            if len(line.strip()) == 0:
                if len(buffer): yield ' '.join(buffer)
                buffer = []
                continue
            buffer.append(line)
            pass
        if len(buffer): yield ' '.join(buffer)
        pass
    else:
        raise "Don't now how to handle objects of type %s"%type(text)
    return

def ssplit(text,language):
    pt = prefix_types.get(language,{})
    buffer = ''
    for m in sntpat.finditer(text):
        p = pt.get(m.group('prefix'),0) # 1: general prefix, 2: numbers only
        print(m.groups(),p)
        #
        # if p ==




if __name__ == "__main__":
    text = """Dies is ein Test. Dies ist ein
    anderer text. Müllerstr. 7. Er wohnt in der Müllerstr. Und noch einer."""

    ssplit(text,"de")

    # buffer = ""
    # for line in sys.stdin:
    #     if len(line.strip()) == 0:
    #         buffer += line
    #     else:
    #         for s in ssplit(buffer,"de"):
    #             print s
    #             pass
    #         buffer = ''
    #         pass
    #     pass
    # pass
