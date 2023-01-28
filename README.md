# 官方资料

https://docs.scrapy.org

https://scrapy-cookbook.readthedocs.io/


# scrapy 参考 爬虫核心
https://scrapeops.io/python-scrapy-playbook/

https://scrapeops.io/python-scrapy-playbook/scrapy-beginners-guide/

https://scrapeops.io/python-scrapy-playbook/scrapy-beginners-guide-cleaning-data/

https://scrapeops.io/python-scrapy-playbook/scrapy-beginners-guide-storing-data/

https://scrapeops.io/python-scrapy-playbook/scrapy-beginners-guide-user-agents-proxies/

## 初始化命令

```
#初始化项目
scrapy startproject chocolatescraper
#syntax is --> scrapy genspider <name_of_spider> <website>
scrapy genspider chocolatespider chocolate.co.uk
```

默认目录结构

```
├── scrapy.cfg
└── chocolatescraper
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

fetch('https://www.chocolate.co.uk/collections/all')
response.css('product-item')
```

## 启动爬虫

```
#启动爬虫
scrapy crawl chocolatespider
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