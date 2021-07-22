import numpy as np
import pandas as pd


def cut(data, date_num):
    a = data.columns
    test = data[:][a[0:date_num+2]]
    return test


def the_final(data_array, m, n):
    count = [0]*m
    an = ['0']*(n-2)
    temp = []

    for time in range(1, m+1):
        for i in range(2, n):
            temp = []
            if data_array[m][i] == time:  # 看 m 時段所有可以的人

                for person in range(m):
                    if data_array[person][i] == 1:
                        temp.append(person)

                if len(temp) == 0:
                    continue
                if len(temp) == 1:
                    an[i-2] = data_array[temp[0]][0]
                    count[temp[0]] = count[temp[0]] + 1
                    continue

                same_time = []
                # temp[i] = 可以的人的順序 count[k] = 第k個人有幾次班了
                count_min = count[temp[0]]
                for com in temp:
                    if count[com] == count_min:
                        same_time.append(com)
                    elif count[com] < count_min:
                        count_min = count[com]
                        same_time = []
                        same_time.append(com)

                if len(same_time) == 1:
                    count[same_time[0]] += 1
                    an[i-2] = data_array[same_time[0]][0]
                    continue

                lesson_min = data_array[same_time[0]][n]
                teacher = same_time[0]
                for item in same_time:
                    if data_array[item][n] < lesson_min:
                        teacher = item
                        lesson_min = data_array[item][n]
                count[teacher] += 1
                an[i-2] = data_array[teacher][0]
    return an


def able_person_in_time(data_array, m, n):
    for i in range(2, n):
        temp = 0
        for j in range(m):
            if data_array[j][i] == 1:
                temp = temp + 1
        data_array[m][i] = temp


def add_rightanddown(data_array, m, n):
    temp = np.zeros((m, 1))
    data_array = np.hstack((data_array, temp))
    temp = np.zeros((1, n+1))
    data_array = np.vstack((data_array, temp))
    return data_array


def tranfer(data_array, key_word, m, n):
    for i in range(m):
        temp = 0
        for j in range(2, n):
            if data_array[i][j] == key_word:
                data_array[i][j] = 1
                temp = temp + 1
            else:
                data_array[i][j] = 0
        data_array[i][n] = temp
    return data_array
