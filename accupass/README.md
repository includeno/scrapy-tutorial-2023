# 官方资料

https://docs.scrapy.org

https://scrapy-cookbook.readthedocs.io/


# scrapy 参考 爬虫核心
https://scrapeops.io/python-scrapy-playbook/

https://scrapeops.io/python-scrapy-playbook/scrapy-beginners-guide/

https://scrapeops.io/python-scrapy-playbook/scrapy-beginners-guide-cleaning-data/

https://scrapeops.io/python-scrapy-playbook/scrapy-beginners-guide-storing-data/

https://scrapeops.io/python-scrapy-playbook/scrapy-beginners-guide-user-agents-proxies/


# Selenium 参考

目标网站
https://www.accupass.com/?area=north

参考教程

https://www.learncodewithmike.com/2021/11/scrapy-integrate-with-selenium.html



settings.py配置

```
DOWNLOADER_MIDDLEWARES = {
    'scrapy_selenium.SeleniumMiddleware': 800
}
SELENIUM_DRIVER_NAME = 'chrome'
SELENIUM_DRIVER_EXECUTABLE_PATH = 'chromedriver.exe' #驱动路径
SELENIUM_DRIVER_ARGUMENTS = ['-headless']

#WARNING: Disabled SeleniumMiddleware: SELENIUM_DRIVER_NAME and SELENIUM_DRIVER_EXECUTABLE_PATH must be set
```



## 初始化命令

```
#初始化项目
scrapy startproject accupass
#syntax is --> scrapy genspider <name_of_spider> <website>
cd accupass
scrapy genspider accupass_spider accupass.com
```

默认目录结构

```
├── scrapy.cfg
└── accupass
    ├── __init__.py
    ├── items.py
    ├── middlewares.py
    ├── pipelines.py
    ├── settings.py
    └── spiders
        └── __init__.py
```



## 运行shell命令
```
#shell
scrapy shell

fetch('https://www.accupass.com/?area=north')
response.css('style-f13be39c-event-name')
```

## 启动爬虫

```
#启动爬虫
scrapy crawl accupass_spider
```



# scrapyd 参考 服务管理

doc
https://scrapyd.readthedocs.io/en/latest/overview.html

https://scrapeops.io/python-scrapy-playbook/extensions/scrapy-scrapyd-guide/



# Errors 错误和解决方法

M1 mac系列 执行scrapy shell 时出现  MemoryError: Cannot allocate write+execute memory for ffi.callback() 

```
pip install --force-reinstall 'cffi>=1.15.1'
```