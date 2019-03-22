# -*- coding: utf-8 -*-
import grpc
import unittest
import  math
from mathFunction import *
from example import data_pb2_grpc , data_pb2

_HOST = 'localhost'
_PORT = '6060'


class TestMathTest(unittest.TestCase):

    def setUp(tes):
        tes.conn = grpc.insecure_channel(_HOST + ':' + _PORT)
        tes.client = data_pb2_grpc.modelStub(channel=tes.conn)


    def test_sqrt(self):
        """Test method math.sqrt(x)"""
        response = self.client.test_show(data_pb2.test_Request())
        self.assertEqual(3.0,math.sqrt(9))

    def test_pow(self):
        """Test method math.pow(x,y)"""
        response = self.client.test_show(data_pb2.test_Request())
        self.assertNotAlmostEqual(6561, math.pow(3,4))


    def test_ceil(self):
        """Test method math.ceil(x)"""
        response = self.client.test_show(data_pb2.test_Request())
        self.assertEqual(4, math.ceil(3.4))


    def test_fsum(self):
        """Test method math.fsum([x,y,z])"""
        response = self.client.test_show(data_pb2.test_Request())
        self.assertEqual(2.5, math.fsum([1,2,9,8]))

    def test_add(self):
        """Test method add(a, b)"""
        response = self.client.test_show(data_pb2.test_Request())
        self.assertEqual(6, add(4, 2))

    def test_minus(self):
        """Test method minus(a, b)"""
        response = self.client.test_show(data_pb2.test_Request())
        self.assertNotAlmostEqual(1, minus(3, 3))

    def test_multi(self):
        """Test method multi(a, b)"""
        self.assertEqual(6, multi(2, 3))
        response = self.client.test_show(data_pb2.test_Request())

    def test_divide(self):
        """Test method divide(a, b)"""
        self.assertEqual(2.5, divide(5, 2))
        response = self.client.test_show(data_pb2.test_Request())



