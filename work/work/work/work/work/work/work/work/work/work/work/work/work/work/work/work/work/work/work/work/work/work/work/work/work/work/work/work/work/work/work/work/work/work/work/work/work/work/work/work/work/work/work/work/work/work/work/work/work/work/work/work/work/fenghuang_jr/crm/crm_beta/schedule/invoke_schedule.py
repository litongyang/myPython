# __author__ = 'tongyang.li'
# -*- coding: utf-8 -*-

import schedule


class InvokeSchedule:
    schedule_class = [schedule.ScheduleClass(0, -1, 'null', 'null')] * 10

    def __init__(self):
        pass

    @staticmethod
    def invoke_first_fun(schedule_id,name, content):
        # self.schedule_class[0] = schedule.ScheduleClass(schedule_id,0,name,content)
        # self.schedule_class[0].add_init()
        InvokeSchedule.schedule_class[0] = schedule.ScheduleClass(schedule_id, 0, name, content)
        InvokeSchedule.schedule_class[0].add_init()

    @staticmethod
    def invoke_level_fun(level, name, content):
        # self.schedule_class[level] = self.schedule_class[level - 1].addSon(level, name, content)
        InvokeSchedule.schedule_class[level] = InvokeSchedule.schedule_class[level - 1].addSon(level, name, content)
        # for level in range(1, len(self.schedule_class)):
        #     self.schedule_class[level] = self.schedule_class[level - 1].addSon(level, "fund_parallel_class(all)")

    @staticmethod
    def invoke_update_fun(level, status, content, num):
        InvokeSchedule.schedule_class[level].update(status, content, num)

if __name__ == '__main__':
    test = InvokeSchedule()
