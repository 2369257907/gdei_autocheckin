# gdei_autocheckin
广东第二师范学院健康系统自动打卡。

##⚠️免责声明
1.本项目仅供学术交流，请勿用于任何商业或其它目的。
2.开发者不对脚本的效果做任何形式的保证，也不对该脚本的使用造成的影响负任何责任。


##🏠简介
可以任选以下方式其一进行打卡：

1.autocheckin.sh使用了curl进行打卡。只需要安装有curl的环境即可。可以参考https://blog.csdn.net/qq_44214671/article/details/114917964
。可以部署到腾讯云函数或者阿里云函数计算上。
需要注意这里的密码需要填写加密后的密码，这个可以通过抓包获得。在登录界面使用浏览器自带的抓包工具即可。
<img width="1440" alt="image" src="https://user-images.githubusercontent.com/67651900/176857703-58b4d657-2e3e-4122-9fbe-848215b9da03.png">
拷贝为curl后，可以得到这样的内容。其中“password=”后面的一串密文就是加密后的密码。
<img width="985" alt="image" src="https://user-images.githubusercontent.com/67651900/176858197-f915bcca-21ac-4f22-ac54-e614fa527470.png">


2.autocheckin.py使用了selenium自动化工具进行打卡，需要安装有浏览器驱动。对于不同的浏览器需要安装不同的驱动，如chromedrive、edgedriver等。其中包含了打卡后自动邮箱通知的功能
。
