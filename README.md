# 2019ncov
[![Code Style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Python 3](https://pyup.io/repos/github/edison7500/2019ncov/python-3-shield.svg)](https://pyup.io/repos/github/edison7500/2019ncov/)

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
| province | 省份 | char |
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

### install

```.shell
docker-compose build
docker-compose up -d 
```

### 使用 pygal 绘制 treemap 图

```.shell
cd /path/to/ncov/
python manage.py runserver

chrome http://127.0.0.1:8000/epidemic/20200215/
```

![novel corona virus treemap](img/treemap.png)