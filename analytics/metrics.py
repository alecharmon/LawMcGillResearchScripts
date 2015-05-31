from xlsParse import *
import math, datetime
import statistics
from collections import Counter
__author__ = 'Alec'


# takes dictonary files of years and produces articles published
def productivityPerYear(entries):
    for key, values in entries.items():
        print(key, ":", len(values.entries))
        pass
    pass


#takes dictonary files of years and produces articles published
def productivityPerYearProRated(entries):
    for key, values in entries.items():
        authors = getAuthors(values.entries)
        print("productivity Per Year (ProRated)", key, ":", len(values.entries) / len(authors))
        pass
    pass


#percent if lang per ear
def percentLangPerYear(entries):
    toRet = ""
    for key, values in entries.items():
        langs = getLangs(values.entries)
        toRet += key + ": "
        for lang, result in langs.items():
            percent = str("%.2f" % ((len(result.entries) / len(values.entries)) * 100))
            toRet += result.lang + " " + str(percent) + "% ,"
        pass
        toRet += '\n'
    print(toRet)
    pass


#perccent co authored peryear
def percentCoAuthoredperYear(entries):
    toRet = ""

    for key, values in entries.items():
        toRet += key + ": "
        Y = 0
        N = 0
        for entry in values.entries:
            if (entry.coAuthor):
                Y += 1
            else:
                N += 1
        Y = str("%.2f" % ((Y / len(values.entries)) * 100) + "%")
        N = str("%.2f" % ((N / len(values.entries)) * 100) + "%")

        print("{0}: Y {1}   N {2}".format(key, Y, N))
    pass


def CoAuthoredTypePerYear(entries):
    toRet = ""

    for key, values in entries.items():
        toRet += key + ": "
        Y = 0
        F = 0
        NF = 0
        S = 0
        for entry in values.entries:
            if (entry.coAuthor):
                Y += 1
                if entry.coAuthorRelation == "F":
                    F += 1
                if entry.coAuthorRelation == "NF":
                    NF += 1
                if entry.coAuthorRelation == "S":
                    S += 1

        if Y > 0:
            F = str("%.2f" % ((F / Y) * 100) + "%")
            NF = str("%.2f" % ((NF / Y) * 100) + "%")
            S = str("%.2f" % ((S / Y) * 100) + "%")

            print("{0}: F {1}  NF {2}  S {3}".format(key, F, NF, S))
    pass


def hindex(references):
    h = 0
    while True:
        h = h + 1
        n = 0
        for r in references:
            if r.citations >= h: n = n + 1
        if n < h:
            h = h - 1
            break
    # citations = statistics.Statistics([r.citations for r in references])
    # if years:
    #     Yrange = statistics.Statistics(years).range
    # else:
    #     Yrange = 0
    # try:
    #     a = citations.sum / math.pow(h, 2)
    # except ZeroDivisionError:
    #     a = float("inf")
    # try:
    #     m = float(h) / Yrange
    # except ZeroDivisionError:
    #     m = float("inf")
    print(h)


def collectiveHIndexByYear(entries):
    for key, values in entries.items():
        hindex(values.entries)

    pass

def mostUsedPublishers(entries):
    publishers =[]
    for x in entries:
        publishers.append(x.outlet)
        pass
    publishers = Counter(publishers).most_common(6)
    for publisher, count in publishers:
        print('%s : %d'%(publisher, count))

#perccent per region peryear

def percentRegionPerYear(entries):
    toRet = ""
    for key, values in entries.items():
        regions = getRegions(values.entries)
        toRet += key + ": "
        for reg, result in regions.items():
            percent = str("%.2f" % ((len(result.entries) / len(values.entries)) * 100))
            toRet += reg + " " + str(percent) + "% ,"
        pass
        toRet += '\n'
    print(toRet)
    pass
#perccent co authored peryear

def percentPerOutlettypePertime(entries):
    toRet = ""
    for key, values in entries.items():
        journalTypes = getJournalTypes(values.entries)
        toRet += key + ": "
        for type, result in journalTypes.items():
            percent = str("%.2f" % ((len(result.entries) / len(values.entries)) * 100))
            toRet += type + " " + str(percent) + "% ,"
        pass
        toRet += '\n'
    print(toRet)
    pass