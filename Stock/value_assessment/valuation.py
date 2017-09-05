# __author__ = 'lty'
# -*- coding: utf-8 -*-


class Valuation:
    def __init__(self):
        self.profit_pre = 0.35  # 每股收益
        self.bonus_rate = 0.5  # 分红占利润的比值
        self.growth_rate_avg = 1.5  # 平均每年增长率
        self.years_5 = 5  # 持有年限
        self.multiple_5 = 2  # 持有5年收益的倍数
        self.profit_pre_5 = 0  # 5年后公司的每股收益
        self.bonus_sum_5 = 0  # 持有5年分红的总收益

    def compute_value(self):
        self.profit_pre_5 = self.profit_pre
        self.bonus_sum_5 = self.profit_pre * self.bonus_rate
        for i in range(1, self.years_5):
            self.profit_pre_5 *= self.growth_rate_avg
            self.bonus_sum_5 += self.profit_pre_5 * self.bonus_rate
            # print self.profit_pre_5
        print self.bonus_sum_5
        print self.profit_pre_5


if __name__ == '__main__':
    valuation = Valuation()
    valuation.compute_value()
