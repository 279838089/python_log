# python_log
0. 用途：服务器运维
1. 功能：自动读取日志文件，如果文件有新增内容，自动发送内容到指定邮箱
2. 用例：ci日志文件，laravel日志文件，apache日志文件，php日志文件
3. 语言：python3.5
4. 安装：
		
		git clone git@github.com:279838089/python_log.git

		crontab -e

		* * * * * python3 /path/log_main.py

