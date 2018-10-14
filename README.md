# 东北大学宣讲会信息 Scrapy 爬虫

> 顺便吐槽东大的网站(沈阳的那个)是真的难用

### Resource
1. [Scrapy中文网](http://www.scrapyd.cn/doc/)
2. [Unicode 编码转换](http://tool.chinaz.com/tools/unicode.aspx)
3. [Python List append](http://www.runoob.com/python/att-list-append.html)
4. [Python 正则表达式](https://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/001386832260566c26442c671fa489ebc6fe85badda25cd000)

### Run

ps: virtalenv is awesome
pps: use python 2.7

```bash
git clone https://github.com/Raoul1996/scrapy_neu_job.git scrapy
source ./venv/bin/active
pip install -r requirement.list
scrapy crawl job -o job.json
```

### Note 

这是我第一个爬虫，花了大概三个小时鼓捣出来的。很 low 逼，大佬勿喷

数据只是放到了一个 json 文件中，暂时凑合用，后边会落 DB

考虑使用 MySQL 或者 PG 也还不错

凑合用用，帮女朋友聚合一下宣讲会信息，基本也够用了

数据都拿到了，随便写个前端基本也够用了，就不把前端放 Github 了
