# LoginWifi

### 功能

原理：基于python，配置系统计划任务实现每次连接上校园网时都自动登录

 

### 配置方法

1. 配置python环境
2. 验证是否安装完成

在windows任务栏处搜索cmd，打开命令提示符

 ![image-1](https://raw.githubusercontent.com/SuperXingKong/LoginWifi/main/tutorial/1.png)

输入python并回车，若返回值为python版本号等内容（如下图所示）即为安装成功（笔者使用的是3.8.10版本的python）

 ![image-2](https://raw.githubusercontent.com/SuperXingKong/LoginWifi/main/tutorial/2.png)

3. 安装requests库

打开命令提示符，在命令行内输入pip install requests，等待安装完成即可

 ![image-3](https://raw.githubusercontent.com/SuperXingKong/LoginWifi/main/tutorial/3.png)

4. 配置账号密码

1)将LoginWifi,py与LoginWifi.bat放在同一文件夹下（建议放在桌面上,点LoginWifi.bat的时候更方便）

2)双击LoginWifi.bat，根据提示进行第一次配置

 ![image-4](https://raw.githubusercontent.com/SuperXingKong/LoginWifi/main/tutorial/4.png)

3)完成配置，下次只需要在连接上苏大wifi后双击LoginWifi.bat就可以自动登录了！

 

 

 

下期更新：如何实现每次连接WiFi时都自动执行脚本

 