# __author__ = 'tongyang.li'
# -*- coding: utf-8 -*-

from urllib import urlencode
import urllib2
import random
import base64
from settings import PROXIES
import sys
sys.setdefaultencoding('gbk')


class RandomUserAgent(object):
    """Randomly rotate user agents based on a list of predefined ones"""

    def __init__(self, agents):
        self.agents = agents

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings.getlist('USER_AGENTS'))

    def process_request(self, request, spider):
        print "**************************" + random.choice(self.agents)
        request.headers.setdefault('User-Agent', random.choice(self.agents))


class ProxyMiddleware(object):

    def process_request(self, request, spider):
        proxy = random.choice(PROXIES)
        # if proxy['user_pass'] is not None:
        #     x = "http://%s" % proxy['ip_port']
        #     request.meta['proxy'] = "http://%s:%s" % (proxy['ip_port'], proxy['port'])
        #     # request.meta['proxy'] = urllib2.ProxyHandler({'http': '122.96.59.104:80'})
        #     y = request.meta['proxy']
        #     encoded_user_pass = base64.encodestring(proxy['user_pass'])
        #     # request.headers.setdefault('proxy', x)
        #     request.headers['Proxy-Authorization'] = 'Basic ' + encoded_user_pass
        #     print "**************ProxyMiddleware have pass************" + proxy['ip_port']
        # else:
        print "**************ProxyMiddleware no pass************" + proxy['ip']
        x = 'http://%s:%d' % (proxy['ip'], proxy['port'])
        request.meta['proxy'] = x

    """
    def process_request(self, request, spider):
            # Don't overwrite with a random one (server-side state for IP)
            if 'proxy' in request.meta:
                return
            if 'no_proxy' in request.meta:
                return
            if '192.168.' in request.url:
                return
            proxy = random.choice(PROXIES)
            request.meta['proxy'] = 'http://%s:%d' % (proxy['host'], proxy['port'])
            request.meta['proxy_id'] = proxy['id']
            print request.meta['proxy']

            if proxy and 'host' in proxy:
                uname = proxy.get('username', '')
                pwd = proxy.get('password', '')

                if uname and pwd:
                    import base64
                    http_proxy = 'http://{uname}:{pwd}@{host}:{port}'.format(
                        uname=uname, pwd=pwd, host=proxy['host'], port=proxy['port']
                    )
                    request.meta['proxy'] = http_proxy
                    user_pass_encode = base64.encodestring(uname + ':' + pwd)
                    request.headers['Proxy-Authorization'] = 'Basic ' + user_pass_encode
                else:
                    request.meta['proxy'] = 'http://%s:%d' % (proxy['host'], proxy['port'])
                    print request.meta['proxy']
                request.meta['proxy_id'] = proxy['id']
            # logger.debug('selected proxy %d:%s' % (request.meta['proxy_id'], request.meta['proxy']))
    """

