from __future__ import division
import urllib.request
import json
from math import log


def hits(word1,word2=""):
    query = "http://ajax.googleapis.com/ajax/services/search/web?v=1.0&q="
    if word2 == "":
        print(query+word1)
        results = urllib.request.urlopen(query + word1)
    else:
        print(query + word1+" "+"AROUND(10)"+" "+word2)
        results = urllib.request.urlopen(query + word1+"%20"+"AROUND(10)"+"%20"+word2)
    encoding = results.headers.get_content_charset()
    json_res = json.loads(results.read().decode(encoding))
    google_hits=int(json_res['responseData']['cursor']['estimatedResultCount'])
    return google_hits


def so(phrase):
    num = hits(phrase,"")
    print(num)
    den = hits(phrase,"poor")
    print(den)
    ratio = num / den
    print(ratio)
    sop = log(ratio)
    return sop

print(so("ugly"))
