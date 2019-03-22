import grpc

# 导入编译好的proto文件
from example import data_pb2_grpc , data_pb2

# 跟服务端保持一致
_HOST = 'localhost'
_PORT = '6060'


def run():
    conn = grpc.insecure_channel(_HOST + ':' + _PORT)
    client = data_pb2_grpc.modelStub(channel=conn)
    response = client.test_show(data_pb2.test_Request(index='201801', name='test', age=12))
    print("received: " + response.stu_class)
    print("received: " + str(response.grade))


if __name__ == '__main__':
    run()
