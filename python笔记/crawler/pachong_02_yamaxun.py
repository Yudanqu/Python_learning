# 当一个网站拒绝request访问时，即防止爬虫，可以通过更改user_agent来避免被其检测到是爬虫
import requests
url = 'https://www.amazon.cn/dp/B01BSKICZA/ref=gwgfloorv1_BMVD_a_1?pf_rd_p=0e393420-91cc-445c-be7c-6f0361fc9c40&pf_rd_s=desktop-8&pf_rd_t=36701&pf_rd_i=desktop&pf_rd_m=A1AJ19PSB66TGU&pf_rd_r=8KH6NQE61WDCX8DBKF52&pf_rd_r=8KH6NQE61WDCX8DBKF52&pf_rd_p=0e393420-91cc-445c-be7c-6f0361fc9c40'

try:
    kw = {'user-agent': 'Mozilla/5.0'}
    r = requests.get(url, headers=kw)  # 更改头信息，因为默认agent中显示requests，表明自己是爬虫
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[1000:2000])
except:
    print("获取失败")
