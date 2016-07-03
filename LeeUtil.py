__author__ = 'Ann'


class LeeUtil:
    @staticmethod
    def toMap(lists, key):
        re = {}
        if lists:
            for a in lists:
                re[getattr(a, key)] = a
        return re

    @staticmethod
    def genPlaceHolders(num):
        return ','.join(['?' for i in range(0, num)])

    # @staticmethod
    # def merge(*c):
    #     res = []
    #     LeeUtil.__merge(res, c)
    #     return res
	#
    # @staticmethod
    # def __merge(result, *c):
    #     for a in c:
    #         if isinstance(a, tuple) or isinstance(a, list):
    #             LeeUtil.__merge(result, a)
    #         else:
    #             result.append(a)

    @staticmethod
    def getFields(a):
        return [attr for attr in dir(a) if not attr.startswith('_')]

    # @staticmethod
    # def myReduce(lambdaMy, mylist):
    #     result = mylist[0]
    #     for i in range(1, len(mylist)):
    #         result = lambdaMy(result, mylist[i])
    #     return result
