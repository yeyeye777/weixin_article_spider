                        **爬虫是一个微信文章爬虫**
                    
数据来源为搜狗微信。

因为搜狗微信上的链接是临时链接所以过一段时间后会失效，所以需要进行转换为永久链接。

目前网上用的方法是临时链接添加uin和key字段，但是这个比较麻烦，而且key比较难以获取。

本项目使用的是西瓜插件来实现。

![image](https://github.com/yeyuzhao/weixin_article_spider/blob/master/sougou_weixin/images/%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20190731123538.png)

使用selenium模拟浏览器，加载插件，应为插件加载信息会需要一定的时间，
所以速度需要放慢，而且搜狗的微信会进行访问限制，所以控制好访问速度。浏览器页面不可隐藏小化，否则插件会出现异常。
![image](https://github.com/yeyuzhao/weixin_article_spider/blob/master/sougou_weixin/images/%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20190731123711.png)
