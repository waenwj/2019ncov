# 2019ncov


## 开发环境

* Python 3.7.5
* Scrapy 1.8.x
* Django 2.2.x

## 数据源 

    * ChinaCDC


### export data to csv

```
cd novel_coronavirus
scrapy  crawl coronavirus -t csv -o ncov.csv
```