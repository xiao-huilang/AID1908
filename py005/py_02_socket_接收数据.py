import socket

def main():
    # 1 创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 2 绑定一个本地信息
    localaddr = ('', 7890)
    udp_socket.bind(localaddr)
    while True:
        # 3 接收数据
        recv_data = udp_socket.recvfrom(1024)
        recv_msg = recv_data[0]  # 存储接收到的数据
        send_addr = recv_data[1]  # 存储发送方的信息
        # 4 打印接收到的数据
        print("内容：%s 发送方信息： %s" % (recv_msg.decode("gbk"), send_addr))

    # 5 关闭字接套
    udp_socket.close()

if __name__ == '__main__':
    main()