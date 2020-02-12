# 2019ncov


## 开发环境

* Python 3.7.5
* Scrapy 1.8.x
* Django 2.2.x

## 数据源 

* ChinaCDC

### 疫情数据表

| 字段        | 对应中文           | 类型  |
| ------------- |:-------------:| -----:|
| name      | 名称 | char |
| province | 省份 | cahr |
| add_suspect      | 新增疑似     |  int |
| cumulative_suspect | 累计疑似      |   int |
| new_diagnosis | 新增确诊 | int |
| cumulative_diagnosis | 累计确诊 | int |
| added_death | 新增死亡 | int |
| cumulative_death | 累计死亡 | int |
| published_at | 发布日期 | date |


### export data to csv

```
cd novel_coronavirus
scrapy  crawl coronavirus -t csv -o ncov.csv
```