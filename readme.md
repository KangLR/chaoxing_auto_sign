## 功能描述

- 登录方式：

支持手机号码登录，支持学号登录

- 签到功能：

支持普通签到，手势签到，二维码签到，位置签到，拍照签到

- 微信推送：

配置server酱key后，签到消息可以推送至您的个人微信

- 接口部署：

使用FastApi框架 和 MongoDB数据库，可以将此项目部署到服务器，通过接口实现多用户多任务签到



## 项目目录


|--api							// 【部署api使用】
    |--- cloud_sign.py			// 整体逻辑
    |--- config.py				// 配置信息
    |--- db_handler.py			// 数据库操作
    |--- main.py				// fastapi运行
    |--- sign_in_script.py		// 负责签到
|--local						// 【本地运行使用】
	|--- cloud_sign.py			// 运行此文件
	|--- config.py 				// 个人信息配置


如果你需要**部署api**，供自己和其他人使用，可以选择`api`下的脚本

如果你只是**自己**使用，本地运行，可以选择`local`的脚本



## 不想折腾？

每次需要签到的时候，就在浏览器内访问这个链接

`{}`替换成自己的账号密码

`http://101.89.182.58:9090/sign?username={}&password={}&schoolid=&sckey=`



## 接口使用

```
http://101.89.182.58:9090/sign
```

请求代码示例：
```python
import requests

# POST
params = {
    'username': 'xxxxx',
    'password': 'xxxxx',
    'schoolid': '',
    'sckey': ''
}
requests.post('http://101.89.182.58:9090/sign', params=params)

# GET
username = 'xxx'
password = 'xxx'
requests.get('http://101.89.182.58:9090/sign?username={}&password={}'.format(username, password))
```

在线接口调试：

<http://101.89.182.58:9090/docs#/default/sign_sign_get>


| 请求方式 |   参数   |  说明  | 是否必须 |
| :------: | :------: | :----: | :------: |
|          | username |  账号  |    是    |
|   **POST/GET**   | password |  密码  |    是    |
|          | schoolid | 学校ID |    否    |
| | sckey | server酱key | 否 |


**如果是学号登录，fid参数必填**

### 如何获取FID
关于学号登录方式，有一个额外参数`schoolid`

http://passport2.chaoxing.com/login

动图演示：

![2020/04/15/cdf5a0415014614.gif](http://cdn.z2blog.com/2020/04/15/cdf5a0415014614.gif)


## 其他签到脚本推荐


| 项目地址                                                | 开发语言   | 备注                                           |
| ------------------------------------------------------- | ---------- | ---------------------------------------------- |
| https://github.com/Wzb3422/auto-sign-chaoxing           | TypeScript | 超星学习通自动签到，梦中刷网课       |
| https://github.com/Huangyan0804/AutoCheckin             | Python     | 学习通自动签到，支持手势，二维码，位置，拍照等 |
| https://github.com/aihuahua-522/chaoxing-testforAndroid | Java       | 学习通（超星）自动签到               |
| https://github.com/yuban10703/chaoxingsign              | Python     | 超星学习通自动签到                   |
