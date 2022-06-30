# __author__ = 'lty'
# -*- coding: utf-8 -*-
import logging
import logging.config
import xmlrpclib
import threading


def div_list(ls, n):
    """
    list 等分函数
    :param ls:
    :param n:
    :return:
    """
    if not isinstance(ls, list) or not isinstance(n, int):
        return []
    ls_len = len(ls)
    if n <= 0 or 0 == ls_len:
        return []
    if n > ls_len:
        return []
    elif n == ls_len:
        return [[i] for i in ls]
    else:
        j = ls_len / n
        k = ls_len % n
        # 步长j,次数n-1
        ls_return = []
        for i in xrange(0, (n - 1) * j, j):
            ls_return.append(ls[i:i + j])
            # 算上末尾的j+k
        ls_return.append(ls[(n - 1) * j:])
        return ls_return


class TestScript:
    def __init__(self):
        self.user_id = []
        self.user_id_list = [[]]
        self.server = xmlrpclib.ServerProxy('http://localhost:5557')

    def get_userid(self):
        """
        获取user_id
        :return:
        """
        for line in open('user_id.txt', 'r'):
            line_one = line.split()
            self.user_id.append(line_one[0])
            # self.user_id = ['0001B9A0-5F48-4824-BB0E-AD42050C332E', '1111']

    def test(self, user_id_array):
        """
        测试
        :param user_id_array:
        :return:
        """
        # self.user_id = ['0001B9A0-5F48-4824-BB0E-AD42050C332E', '1111']  # test
        logging.config.fileConfig('logger.conf')
        logger = logging.getLogger('test.test')
        logger.info("test")
        for user_id in user_id_array:
            # self.server.user_recom_trigger(user_id)
            logger.info(user_id)


if __name__ == '__main__':
    test = TestScript()
    test.get_userid()
    threads = []
    test.user_id_list = div_list(test.user_id, 10)
    for user_id_array in test.user_id_list:
        th = threading.Thread(target=test.test, args=(user_id_array,))
        th.start()
        threads.append(th)
    # 等待线程运行完毕
    for th in threads:
        th.join()
    print len(threads)
