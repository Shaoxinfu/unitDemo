#!/usr/bin/env python
# coding:utf-8
import grpc
import time
from concurrent import futures

# 导入编译好的proto文件。
from example import data_pb2_grpc, data_pb2

# 定义端口
_ONE_DAY_IN_SECONDS = 60 * 60 * 24
_HOST = 'localhost'
_PORT = '6060'


class model(data_pb2_grpc.modelServicer):
    # 定义-封装好的函数
    def serch_student_class(self, index):
        if index == '201801':
            student_class = '6'
            return student_class

    def serch_student_grade(self, name, age):
        if name == 'test' and age == 12:
            student_grade = 100
            return student_grade

    # 输出函数
    def test_show(self, request, context):
        index = request.index
        name = request.name
        age = request.age

        student_class = self.serch_student_class(index)
        student_grade = self.serch_student_grade(name, age)
        print("success！")
        return data_pb2.test_Response(stu_class=student_class, grade=student_grade)


def serve():
    grpcServer = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    data_pb2_grpc.add_modelServicer_to_server(model(), grpcServer)
    grpcServer.add_insecure_port(_HOST + ':' + _PORT)
    grpcServer.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        grpcServer.stop(0)


if __name__ == '__main__':
    serve()
