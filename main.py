import argparse
from inspection import cmd_console
from inspection import web_console
import sys

def _argparse():
	# argparse用法 https://docs.python.org/3/library/argparse.html
	parser = argparse.ArgumentParser(description='MYSQL巡检报告生成脚本. 最新下载地址: https://github.com/ddcw/inspection')
	parser.add_argument('--web',  action='store_true', dest='web', help='启动控制台')
	parser.add_argument('--web-host',  action='store', dest='web_host',  help='web控制台的监听的地址, 默认 0.0.0.0')
	parser.add_argument('--web-port',  action='store', dest='web_port', type=int, help='web控制台监听的端口')
	#parser.add_argument('--web-user',  action='store', dest='web_user', default="ddcw", help='web控制台用户')
	#parser.add_argument('--web-password',  action='store', dest='web_password', default="123456", help='web控制台密码')
	parser.add_argument('--version', '-v', '-V', action='store_true', dest="VERSION", default=False,  help='VERSION')
	
	parser.add_argument('--host', '-H',  action='store', dest='HOST', help='MYSQL服务器地址(默认localhost)')
	parser.add_argument('--port', '-P' ,  action='store', dest='PORT',type=int, help='MYSQL服务器端口')
	parser.add_argument('--user', '-u' ,  action='store', dest='USER',  help='MYSQL用户')
	parser.add_argument('--password', '-p' ,  action='store', dest='PASSWORD',   help='MYSQL用户的密码')
	parser.add_argument('--socket', '-S' ,  action='store', dest='SOCKET',   help='mysql unix socket')
	parser.add_argument('--ssh-port', '-sP' ,  action='store', dest='SSH_PORT', default=22, type=int , help='MYSQL服务器主机的SSH端口(默认22)')
	parser.add_argument('--ssh-user', '-su' ,  action='store', dest='SSH_USER',  help='MYSQL服务器主机的SSH用户')
	parser.add_argument('--ssh-password', '-sp' ,  action='store', dest='SSH_PASSWORD',   help='MYSQL服务器主机的SSH用户的密码')
	parser.add_argument('--ssh-pkey', '-spk' ,  action='store', dest='SSH_PKEY',   help='MYSQL服务器主机的SSH用户的私钥(支持RSA和DSA)')
	parser.add_argument('--out-file', '-o', '-O' ,  action='store', dest='SAVED_FILE',   help='巡检结果保存文件')
	parser.add_argument('--only-test', '--test' ,  action='store_true', dest='TEST_ONLY',   help='只是测试下mysql或者ssh能不能用')
	parser.add_argument('--file', '-f' ,  action='store', dest='MF',  help='批量巡检(使用这个参数时, 其它参数均无效, --only-test 除外..)')
	parser.add_argument('--config-file', '-c' ,  action='store', default='conf/conf.yaml' , dest='CONF_FILE',  help='指定配置文件, 自动>生成')
	return parser.parse_args()


if __name__ == '__main__':
	parser = _argparse()
	if parser.VERSION:
		print("VERSION: v2.1")
		sys.exit(0)

	if (parser.HOST is not None) or (parser.PORT is not None) or (parser.USER is not None) or (parser.PASSWORD is not None) or (parser.MF is not None) :
		instance = cmd_console.inspection(parser)
		instance.run()
	#elif parser.MF is not None:
	#	instance = cmd_console.multi_inspection(parser)
	#	instance.inspection()
	else:
		instance = web_console.web_inspection(parser)
		instance.run()
		
