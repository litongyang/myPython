# __author__ = 'lty'
# -*- coding: utf-8 -*-

def GetMiddleStr(content,startStr,endStr):
  startIndex = content.index(startStr)
  if startIndex>=0:
    startIndex += len(startStr)
  endIndex = content.index(endStr)
  return content[startIndex:endIndex]
if __name__=='__main__':
    x = '<p class="p1">　　新浪科技讯 7月29日晚间消息，<span id="usstock_BIDU"><a href="http://stock.finance.sina.com.cn/usstock/quotes/BIDU.html" class="keyword f_st" target="_blank><span id="quote_BIDU"></span>今日早盘股价下跌，截止北京时间21：44分，跌7.45美元至158.18美元，跌幅达4.50%。</p><p class="p1">　　百度2016财年第二季度未经审计财报显示，百度第币24.14亿元（约合3.632亿美元），同比下滑34.1%。</p><p class="p1">　　在主营收入方面，搜索广告和推广为核心的网络营收依旧占据绝对地位，且在5月初经历了“魏则西事件”的影响后，百度015年第二季度网络营收收入是162.27亿元，同比增长4.39%。</p>'

    y = (GetMiddleStr(x,'<span', '</span>'))
    tmp = '<span' + y + '</span>'
    print x.replace(tmp, '')