# Scrapy settings for work_spider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "work_spider"

SPIDER_MODULES = ["work_spider.spiders"]
NEWSPIDER_MODULE = "work_spider.spiders"


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = "work_spider (+http://www.yourdomain.com)"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = True

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#    "Accept-Language": "en",
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    "work_spider.middlewares.WorkSpiderSpiderMiddleware": 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    "work_spider.middlewares.WorkSpiderDownloaderMiddleware": 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    "work_spider.pipelines.WorkSpiderPipeline": 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"

FEED_FORMAT = 'json'
FEED_URI = 'output.json'


COOKIE = "x-zp-client-id=8110c334-fd03-4451-8539-e5433abf8437; sajssdk_2015_cross_new_user=1; acw_tc=2760829f17028983631445394e65df5e8284cad102d8dc9a791e55d627a653; zp_passport_deepknow_sessionId=cebc2917s16e734a82b4b8a02d4a521bf13e; at=25538ad33b904b0c981cd6356e8bcd31; rt=c34d986f490b4a6cb557256eb257243f; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221185557911%22%2C%22first_id%22%3A%2218c7ca6deeabdd-03c9d9a715b3ba2-17525634-1484784-18c7ca6deebcdd%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.google.com%2F%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMThjN2NhNmRlZWFiZGQtMDNjOWQ5YTcxNWIzYmEyLTE3NTI1NjM0LTE0ODQ3ODQtMThjN2NhNmRlZWJjZGQiLCIkaWRlbnRpdHlfbG9naW5faWQiOiIxMTg1NTU3OTExIn0%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%221185557911%22%7D%2C%22%24device_id%22%3A%2218c7ca6deeabdd-03c9d9a715b3ba2-17525634-1484784-18c7ca6deebcdd%22%7D; sts_deviceid=18c7ca7d5991d3-0eb043e8ff2fcb-17525634-1484784-18c7ca7d59ab20; ZP_OLD_FLAG=false; sts_sg=1; sts_sid=18c7ca7dea3a39-00127813e025ef-17525634-1484784-18c7ca7dea41109; sts_chnlsid=Unknown; zp_src_url=https%3A%2F%2Fpassport.zhaopin.com%2F; ZL_REPORT_GLOBAL={%22/resume/new%22:{%22actionid%22:%2261496cdd-1b77-456e-a61d-8fb22d8a568a%22%2C%22funczone%22:%22addrsm_ok_rcm%22}}; sts_evtseq=4; campusOperateJobUserInfo=8ca07c7f-b661-4259-9e76-e8349d7ed410; JSsUserInfo=24342E6955715A7945320B754C6A5E71016A5E68486B487403334E79266B3F345769597153794C3201754B6A5E71026A5A68456B497401334E793F6B3F34576964250D224F3272752D6A5671056A5B685C6B48740A3355795B6B483450695A7159794F327275356A5671046A52688; JSpUserInfo=24342E6955715A7945320B754C6A5E71016A5E68486B487403334E79266B3F345769597153794C3201754B6A5E71026A5A68456B497401334E793F6B3F34576964250D224F3272752D6A5671056A5B685C6B48740A3355795B6B483450695A7159794F327275356A5671046A52688; LastCity=%E5%A4%A9%E6%B4%A5; LastCity%5Fid=531"
USER_AGENT = [
    # Firefox
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0",
    "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10",
    # Safari
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2",
    # chrome
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 "
    "(KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16",
    # 360
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
    # 猎豹浏览器
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) "
    "Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; "
    ".NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
    # QQ浏览器
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; "
    ".NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; "
    ".NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)"
]

