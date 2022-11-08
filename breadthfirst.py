import collections


class Breadthfirst:
    @staticmethod
    def breadthfirstsearch(nodelist, goal):
        newNodes = []
        for node in nodelist:
            res = [x for x in nodelist + goal if x not in nodelist or x not in goal]
            if len(res) == 0:
                print('goal reached')
                return node

    def goalreached(self):
        pass
