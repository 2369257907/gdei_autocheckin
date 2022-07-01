# gdei_autocheckin
广东第二师范学院健康系统自动打卡。

## ⚠️免责声明
1. 本程序为免费开源项目，仅供交流学习，遵循GPL v3开源协议，无任何形式的盈利行为。
2. 本程序服务于原系统，旨在让原系统功能更强大。
3. 本程序皆调用官方接口实现，无任何“Hack”行为，无破坏官方接口行为。
4. 本程序仅做数据处理，不拦截、存储、篡改任何用户数据。
5. 严禁使用本程序进行盈利、散播任何违法信息等行为。
6. 本程序不作任何稳定性的承诺，如因使用本程序导致的问题，均与开发者无关。

## 🏠简介
可以任选以下方式其一进行打卡：

1. autocheckin.sh使用了curl进行打卡。只需要安装有curl的环境即可。可以参考https://blog.csdn.net/qq_44214671/article/details/114917964
。可以部署到腾讯云函数或者阿里云函数计算上。
需要注意这里的密码需要填写加密后的密码，这个可以通过抓包获得。在登录界面使用浏览器自带的抓包工具即可。
<img width="1247" alt="image" src="https://user-images.githubusercontent.com/67651900/176877851-60e6f66e-74fe-4a5d-9db0-97ac6567f20e.png">
拷贝为curl后，可以得到这样的内容。其中“password=”后面的一串密文就是加密后的密码。
<img width="1000" alt="image" src="https://user-images.githubusercontent.com/67651900/176878734-e79a60a0-3322-4b2e-8c11-1e8aa59e5313.png">
使用效果：
<img width="571" alt="image" src="https://user-images.githubusercontent.com/67651900/176878581-3a2fcb9b-8ec9-4778-b0f0-5780bb18eec2.png">

2. autocheckin.py使用了selenium自动化工具进行打卡，需要安装有浏览器驱动。对于不同的浏览器需要安装不同的驱动，如chromedrive、edgedriver等。其中包含了打卡后自动邮箱通知的功能
。

## 开始
