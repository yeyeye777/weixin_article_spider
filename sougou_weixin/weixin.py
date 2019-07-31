import requests
from lxml import etree
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

"""
搜狗微信文章爬虫
"""

class weixin():

    chrome_options = Options()
    prefs = {'profile.default_content_setting_values': {'images': 2, }}
    chrome_options.add_experimental_option('prefs', prefs)
    chrome_options.add_extension('./西瓜插件_v1.9.8.0_lowst.crx')
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get("https://weixin.sogou.com/")
    time.sleep(3)
    handles = driver.window_handles
    driver.switch_to_window(handles[0])

    # 获取页面源码
    def get_list(self,url):
        response=requests.get(url,timeout=10)
        response.encoding='utf-8'
        html=response.text
        return html

    # 获取文章的具体信息
    def get_info(self,html):
        tree = etree.HTML(html)
        info_list=tree.xpath('//ul[@class="news-list"]/li')
        if not info_list:
            info_list = tree.xpath('//li')
        for info in info_list:
            article={}
            try:
                article['title']=info.xpath('./div[@class="txt-box"]/h3/a/text()')[0]    #标题信息
                article['source_url']=info.xpath('./div[@class="txt-box"]/h3/a/@data-share')[0]    #临时的文章url
                article['img_url']="http:"+info.xpath('./div[@class="img-box"]/a/img/@src')[0]    #文章标题url
                article['brief']= info.xpath('./div[@class="txt-box"]/p/text()')[0]    #文章摘要信息
                article['author']=info.xpath('./div[@class="txt-box"]/div/a/text()')[0]    #作者信息
                article['avatar_url']="http:"+info.xpath('./div[@class="txt-box"]/div/a/@data-headimage')[0]    #作者的主页
                article['published_time'] =time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(int(info.xpath('./div[@class="txt-box"]/div/@t')[0])))    #文章的发布时间
                article['tags']=tags    #类别标签
                self.get_article(article)
            except Exception as e:
                print(e)


    # 通过插件转换为永久链接，并获取阅读量信息
    def get_article(self,article):
        url=article['source_url']
        self.driver.get(url)
        time.sleep(1)
        html=self.driver.page_source
        tree = etree.HTML(html)
        article['source_url']=tree.xpath('//div[@class="artical-details"]/@data-link')[0]
        article['read_num']=tree.xpath('//p[@class="artical-data-num"]/text()')[1].replace('        10W+\n','100000')
        print(article)




if __name__ == '__main__':
    weixin=weixin()
    cc = [
          {'热门': '0'},
          {'搞笑': '1'},
          {'养生堂': '2'},
          {'私房话': '3'},
          {'八卦精': '4'},
          {'科技咖': '5'},
          {'财金迷': '6'},
          {'汽车控': '7'},
          {'生活家': '8'},
          {'时尚圈': '9'},
          {'育儿': '10'},
          {'旅游': '11'},
          {'职场': '12'},
          {'美食': '13'},
          {'历史': '14'},
          {'教育': '15'},
          {'星座': '16'},
          {'体育': '17'},
          {'军事': '18'},
          {'游戏': '19'},
          {'萌宠': '20'},
          ]
    for i in cc:
        tags = list(i.keys())[0]
        num = list(i.values())[0]
        # 这里设置你要爬取的页数
        for j in range(100):
            print('当前爬取的是{}的第{}页。'.format(tags,j))
            if j==0:
                url='https://weixin.sogou.com/pcindex/pc/pc_{}/pc_{}.html'.format(num,num)
            else:
                url='https://weixin.sogou.com/pcindex/pc/pc_{}/{}.html'.format(num,j)
            html=weixin.get_list(url)
            weixin.get_info(html)

