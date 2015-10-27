#__author__ = 'litongyang'
# -*- coding: utf-8 -*-

"""
统计训练LR模型过程中使用的特征权重大小
@author:    jiayitian
@date:      2014/01/13
"""

import sys
import operator

def calFeatureWeight(argv):
    featureMap = {}
    modelMap = {}

    with open(argv[1]) as featureMapFile:
        for line in featureMapFile.readlines():
            content = line.replace("\n", "").split("\t")
            if (len(content) < 2):
                break
            featureMap[content[1]] = content[0]
        print "featureMap size: " + str(len(featureMap))
    with open(argv[2]) as modelFile:
        for line in modelFile.readlines():
            content = line.replace("\n", "").split(":")
            if (len(content) < 2):
                break
            modelMap[content[0]] = float(content[1])
        featureMap['-1'] = 'intercept'
        print "featureMap size: " + str(len(modelMap))

    sortedModel = sorted(modelMap.items(), key=operator.itemgetter(1))
    top10negative = sortedModel[0:10]
    top10positive = sortedModel[len(sortedModel)-10:len(sortedModel)]
    print "top10positive features:"
    for x in reversed(top10positive):
        print str(featureMap[x[0]]) + " " + str(x[1])
    print "\ntop10negative features:"
    for x in top10negative:
        print str(featureMap[x[0]]) + " " + str(x[1])

if __name__ == '__main__':
    calFeatureWeight(sys.argv)