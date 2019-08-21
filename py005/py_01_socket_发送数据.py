# -*- coding:utf-8 -*-
import socket

def main():
    # 创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 绑定端口
    localaddr = ('', 7788)
    udp_socket.bind(localaddr)

    while True:
        # 使用套接子收发数据
        send_data = input("请输入内容：")
        if send_data == "exit":
            break

        udp_socket.sendto(send_data.encode("gbk"), ("192.168.1.98", 8080))

    # 关闭套接字
    udp_socket.close()



if __name__ == '__main__':
    main()