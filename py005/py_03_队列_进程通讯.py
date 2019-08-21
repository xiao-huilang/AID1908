import multiprocessing



def download_from_web(q):
    """下载数据"""
    # 模拟从网上下载数据
    data = [11, 22, 33, 44]

    # 向队列中写入数据
    for temp in data:
        q.put(temp)

    print("---下载完毕---")


def analysis_data(q):
    """数据处理"""
    waitting_analysis_data = list()

    # 从队列中获取数据 写入列表
    while True:
        data = q.get()
        waitting_analysis_data.append(data)

        if q.empty():
            break
    # 模拟数据处理完毕
    print("处理数据完毕")
    print(waitting_analysis_data)



def main():
    # 创建一个队列
    q = multiprocessing.Queue(5)
    # 创建进程
    p1 = multiprocessing.Process(target=download_from_web, args=(q,))
    p2 = multiprocessing.Process(target=analysis_data, args=(q,))
    p1.start()
    p2.start()




if __name__ == '__main__':
    main()