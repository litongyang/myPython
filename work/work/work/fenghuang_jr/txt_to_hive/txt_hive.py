# __author__ = 'tongyang.li'
# -*- coding: utf-8 -*-

import os
import shutil


class InputData:
    def __init__(self):
        self.dt = []
        self.file = []
        self.file_write = []
        self.id_temp = []
        self.ts_temp = []
        self.date_temp = []
        self.item = []

    @staticmethod
    def delete_create_file():
        if os.path.exists('./log_txt'):
            shutil.rmtree("./log_txt")
            os.mkdir("./log_txt")
        else:
            os.mkdir("./log_txt")

    # noinspection PyBroadException
    def get_data(self):
        content_file = raw_input("Please enter the name of the file to be uploaded to hive(split:','):")
        content_dt = raw_input("Please enter 'dt'(split:',')(for instance:2016-01-01,2016-01-02):")
        self.file = content_file.split(',')
        self.dt = content_dt.split(',')
        for i in range(0, len(self.dt)):
            self.file_write.append(str(self.dt[i]) + ".txt")
        for file_name in self.file:
            try:
                for line in open(file_name):
                    lineone = line.split('\t')
                    self.id_temp.append(lineone[0])
                    self.ts_temp.append(lineone[1].replace("\n", ""))
                    self.date_temp.append(lineone[1].split(' ')[0].replace("/", "-"))

                for i in range(0, len(self.date_temp)):
                    temp = self.date_temp[i].split('-')
                    if len(temp[1]) == 2 and len(temp[2]) == 2:
                        continue
                    else:
                        self.date_temp[i] = ""
                        if len(temp[1]) == 1:
                            temp[1] = "0" + temp[1]
                        if len(temp[2]) == 1:
                            temp[2] = "0" + temp[2]
                    for v in temp:
                        self.date_temp[i] += v + "-"
                    self.date_temp[i] = self.date_temp[i][:-1]
                for i in range(0, len(self.date_temp)):
                    for j in range(0, len(self.dt)):
                        if self.date_temp[i] == self.dt[j]:
                            self.item.append(self.id_temp[i])
                            self.item.append(self.ts_temp[i])
                            self.item.append("")
                            self.item.append("&")
                            log_file = str(self.dt[j]) + ".txt"
                            fl = open("./log_txt/%s" % log_file, 'a')
                            flag = 0
                            # print self.item
                            for v in self.item:
                                if v != '&':
                                    if flag != 2:
                                        fl.write(str(v))
                                        fl.write('\t')
                                        flag += 1
                                    else:
                                        fl.write(str(v))
                                        flag = 0
                                else:
                                    fl.write('\n')
                            fl.close()
                            self.item = []
                self.id_temp = []
                self.ts_temp = []
                self.date_temp = []
            except:
                print "%s is not exit" % file_name

    def write_hive(self):
        for i in range(0, len(self.dt)):
            command_str = "$HIVE_HOME/bin/hive -e \"ALTER TABLE tm_outbound.tm_outbound DROP IF EXISTS PARTITION (dt='%s');alter table tm_outbound.tm_outbound add partition(dt='%s');load data local inpath '/data/apps/tm_toupon/log_txt/%s' overwrite into table tm_outbound.tm_outbound partition(dt='%s');\"" % (
                self.dt[i], self.dt[i], self.file_write[i], self.dt[i])
            # print command_str
            os.system(command_str)


if __name__ == '__main__':
    inputData = InputData()
    inputData.delete_create_file()
    try:
        inputData.get_data()
        # inputData.write_data()
        inputData.write_hive()
    except Exception, e:
        print Exception, e
    print "done!"
