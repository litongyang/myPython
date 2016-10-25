# -*- coding: utf-8 -*-
#__author__ = 'lie.tian'

import os
import logging
import logging.config
import urllib2
import urllib
import httplib
import json


class PostInfomationClass:

    url = "http://10.10.202.16:18080/lablesystem/quazer/"
    headers = {"Content-type": "application/json",
               "Accept": "application/json"}
    update1 = "updateData"
    add1 = "addData"
    add_url = str(url) + str(add1)
    update_url = str(url) + str(update1)

    def __init__(self):
        pass

    @staticmethod
    def tset():
        # print PostInfomationClass.add_url
        params ={"rootId":24,"parentId":1,"thisId":1,"refId":123456000,"status":-1,"deep":0,"parentName":1,"thisName":"test","thisComment":"ade"}
        conn = urllib2.Request(PostInfomationClass.add_url, data=json.JSONEncoder().encode(params), headers=PostInfomationClass.headers)
        response = urllib2.urlopen(conn)
        data = response.read()
        # print data

    @staticmethod
    def add(son1):
        try:
            params = son1.getPostData()
            conn = urllib2.Request(PostInfomationClass.add_url, data=json.JSONEncoder().encode(params), headers=PostInfomationClass.headers)
            response = urllib2.urlopen(conn)
            data = response.read()
            data = json.loads(data)
            # print data
            son1.id = int(data["id"])
            # print "=========", params
            # print "<<<<<<", son1
        except Exception, e:
            print Exception, e
            pass

    @staticmethod
    def update(son1):
        try:
            params = son1.getPostData()
            print params
            conn = urllib2.Request(PostInfomationClass.update_url, data=json.JSONEncoder().encode(params), headers=PostInfomationClass.headers)
            response = urllib2.urlopen(conn)
            data = response.read()
            # print data
        except Exception, e:
            print Exception, e
            pass


class ScheduleClass:
    # 主键id
    id=1l
    # 跟节点id
    rootId = 26
    # 父类id
    parentId = 0
    # 当前节点id
    thisId = 0
    # 直接关联父类的主键id
    refId=0l
    # -1 表示执行 0表示成功 >0表示失败的状态
    # 执行状态
    status=-1
    # 执行深度
    deep=0
    # 父类名
    parentName =""
    # 当前名
    thisName =""
    # 备注信息
    thisComment=""
    # 内容执行次数
    runCount = 0L
    parentNode=None
    son = {}

    def __init__(self, rootId, thisId, thisName, content):
        self.son = {}
        self.rootId = rootId
        self.thisId = thisId
        self.thisName=thisName
        self.thisComment = content
        self.status = -1
        # 发送新增事件请求

    def add_init(self):
        PostInfomationClass.add(self)

    def addSon(self,thisId, thisName, content):
        # 添加字内容
        try:
            if self.thisId == thisId:
                raise Exception, "id冲突"
            son1 = ScheduleClass(self.rootId, thisId, thisName, content)
            son1.deep = self.deep + 1
            son1.thisId=thisId
            son1.parentName=self.thisName
            son1.parentId=self.thisId
            print "------", self.id
            son1.refId = self.id
            son1.status = -1
            son1.thisComment = content
            self.son[id] = son1
            son1.add_init()
            return son1
        except Exception, e:
            # error_info = Exception, ": ", e
            print Exception, ": ", e

    def update(self, status, thisComment, runCount):
        try:
            # 更新程序使用
            self.status = status
            self.thisComment = thisComment
            self.runCount=runCount
            # 发送更新事件请求
            PostInfomationClass.update(self)
        except Exception, e:
            print Exception, ": ", e
            pass

    def printSons(self):
        # 打印子内容
        print "father:",self.id, self.thisName
        print "sons:"
        print self.son

    def getPostData(self):
        data = {}
        # 主键id
        data["id"]=self.id
        # 跟节点id
        data["rootId"]=self.rootId
        # 父类id
        data["parentId"]=self.parentId
        # 当前节点id
        data["thisId"]=self.thisId
        # 直接关联父类的主键id
        data["refId"]=self.refId
        # 执行状态
        data["status"]=self.status
        # 执行深度
        data["deep"]=self.deep
        # 父类名
        data["parentName"]=self.parentName
        # 当前名
        data["thisName"]=self.thisName
        # 备注信息
        data["thisComment"]=self.thisComment
        # 内容执行次数
        data["runCount"]=self.runCount

        return data

    def __repr__(self):
         var= "{id:" + str(self.id) +",name:" + self.thisName + ",sons:["
         i=0
         for (ids,cla) in self.son.items():
             i+=1
             if(i!=1):
                 var +=","
             var += "{key:" +str(ids) + ",val:" + str(cla) +"}"
         var +="]"
         return var


if __name__ == '__main__':
    # test = PostInfomationClass()
    # test.tset()
    test = ScheduleClass(24,1, "Father", "test")
    test.add_init()
    son1=test.addSon(2, "son1","test1")
    # son2=test.addSon(3, "son2")
    # son3=son1.addSon(4, "孩子4")
    #
    # test.printSons()
    #
    #
    # son1.printSons()
