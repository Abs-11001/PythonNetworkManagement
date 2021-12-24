# 服务器
import socket
from multiprocessing import Process
import os,struct,json


# 创建服务器socket函数，返回一个监听socket
def create_server_socket(address, listen_n=10):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 创建socket
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # 设置地址重用选项
    s.bind(address)  # 绑定到地址
    s.listen(listen_n)  # 开始监听
    print('Listening at {}'.format(address))
    return s


# 处理链接请求函数
def accept_connections_forever(s):
    # s 是一个监听socket
    while True:
        conn, address = s.accept()
        print('Accepted connection from ', address)  # 显示客户端地址
        p = Process(target=handle_connection, args=(conn,))  # 创建一个新的进程来提供服务
        p.start()

# 从缓冲区读取数据
def handle_connection(conn):
    while True:
        # print("开始从缓冲区读取此次json的长度")
        header_json_len = conn.recv(4)
        json_len = struct.unpack("i",header_json_len)[0]
        # print(json_len)
        # print("开始读json")
        header_json = conn.recv(json_len)
        header_json = json.loads(header_json)
        msg_len = header_json['size']
        # print("开始读取消息")
        msg = conn.recv(msg_len)
        # print(msg)
        data = msg.decode("utf-8")
        # print(data)




if __name__ == '__main__':
    address = ('127.0.0.1', 8000)
    s = create_server_socket((address))
    accept_connections_forever(s)
