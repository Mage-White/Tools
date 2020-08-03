import requests

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1)'
headers = {'User-Agent':user_agent}

# http://img.ivsky.com/img/bizhi/pre/201802/04/slender_west_lake-001.jpg
url_0 = 'https://lns.hywly.com/a/1/5386/'
num_list = range(1,38) # 生成列表[1,2,3,4,5,6,7,8]，赋值给变量 num_list

for num in num_list: # for 循环，把列表 num_list 里的每个值分别赋值给 num
    # 当 num 为 1时，str(num)把它转换为'1'，然后用加号把 url_0、'1'、'.jpg'拼接起来，结果为'http://img.ivsky.com/img/bizhi/pre/201802/04/slender_west_lake-001.jpg'
    url = url_0 + str(num) + '.jpg'
    # 以下和爬单个图片基本相同
    data = requests.get(url, headers=headers).content
    filename = str(num) + '.jpg'
    f = open(filename, 'wb')
    f.write(data)
    f.close()
    print (url)

print('OK')