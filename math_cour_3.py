from collections import Counter
import math
import bisect
a = [52, 40, 47, 54, 40, 54, 41, 74, 45, 45, 51, 76, 58, 37, 40, 42, 53, 54, 65, 46, 65, 61, 55, 38, 66, 42, 56, 54, 40, 60]
b = [43, 49, 77, 64, 53, 64, 58, 54, 56, 53, 43, 35, 56, 34, 59, 58, 66, 49, 49, 57, 48, 42, 46, 52, 59, 50, 62, 50, 55, 55]
c = [46, 53, 51, 50, 60, 30, 48, 56, 29, 74, 52, 60, 44, 62, 23, 54, 40, 33, 20, 55, 42, 61, 54, 41, 45, 75, 59, 41, 51, 45]
d = [54, 32, 62, 69, 65, 49, 48, 63, 52, 46, 44, 55, 60, 54, 39, 82, 67, 68, 34, 56, 51, 56, 48, 53, 47, 59, 51, 59, 66, 48]
e = [61, 42, 54, 33, 39, 47, 46, 47, 73, 63, 34, 44, 51, 46, 40, 43, 30, 60, 61, 53, 47, 42, 56, 70, 48, 45, 65, 48, 48, 51]
f = [40, 57, 56, 33, 44, 43, 45, 35, 35, 56, 59, 66, 56, 52, 44, 53, 49, 55, 25, 53, 48, 73, 38, 58, 72, 57, 46, 54, 55, 59]
g = [38, 53, 48, 68, 36, 53, 41, 55, 51, 50, 45, 50, 29, 60, 39, 50, 59, 33, 56, 49, 31, 70, 56, 56]

inter_start = 17 # начало интервала
inter_pitch = 7 # шаг интервала
inter_pitch_const = 7 #сюда вписать то же число, что и inter_pitch

all = a + b + c + d + e + f + g
all = sorted(all)
maslen = len(all)
sredn = (sum(all) / (maslen))

print("Отсортированная выборка:")
print (all) # выводит сортированный список
print("\n")
print("Количество чисел в выборке:")
print (maslen) # выводит число элементов списка
print("\n")
print("Среднее арифметическое выборки:")
print(sredn) # выводит среднее
print("\n")

ccc = Counter(all) # получаем список[] с кортежами() по 2 числа - само число и сколько раз оно встретилось
sortedd = (sorted(ccc.items(), key=lambda x: x[0]))

i = 0
array_otn = []
while i < len(sortedd):
    numm = sortedd[i][1] / maslen
    numm = round(numm, 6) # 6 в этой строке - число знаков после запятой, можно изменить
    array_otn.append(numm)
    i += 1

sortedd_list = []
i = 0
while i < len(sortedd):
    s_list = list(sortedd[i])
    sortedd_list.append(s_list)
    i += 1

print("Проверка, что сумма относительных частот равна одному - на строчке ниже должна быть ровно единица: ")
print(round(sum(array_otn), 4))
print("\n")

for i in range(len(sortedd_list)):
    sortedd_list[i].append(array_otn[i])

print("[Само число, количество его повторений в выборке, относительная частота]:")
print(sortedd_list) # Двумерный список
print("\n")

i = 0
vib_sr = []
while i < len(sortedd_list):
    mply = sortedd_list[i][0] * sortedd_list[i][1]
    vib_sr.append(mply)
    i += 1
sumo = sum(vib_sr)
vib_sr_res = sumo / maslen

print("Выборочное среднее:")
print(vib_sr_res)
print("\n")

i = 0
vib_dis = []
while i < len(sortedd_list):
    disnum = sortedd_list[i][1] * ((sortedd_list[i][0] - vib_sr_res) ** 2)
    vib_dis.append(disnum)
    i += 1
sumo2 = sum(vib_dis)
vib_dis_res = sumo2 /  maslen

print("Выборочная дисперсия:")
print(vib_dis_res)
print("\n")

ispr_dis = maslen / (maslen - 1) * vib_dis_res
print("Исправленная дисперсия:")
print(ispr_dis)
print("\n")

ispr_sr_kv_otkl = math.sqrt(ispr_dis)
print("Исправленное среднее квадратическое отклонение:")
print(ispr_sr_kv_otkl)
print("\n")

i = 0
count_all = []
while i < (all[-1] / inter_pitch_const):
    leftIndex = bisect.bisect_left(all, inter_start)
    rightIndex = bisect.bisect_left(all, inter_pitch_const + inter_start)
    count_amount = rightIndex - leftIndex
    count_all.append(count_amount)
    inter_pitch = inter_pitch + inter_pitch_const
    inter_start = inter_start + inter_pitch_const
    i += 1
print("Наконец то я сделал это: (уже забыл, зачем делал)")
print(count_all)
print("\n")
print(f"На строчке ниже должно быть написано {maslen}:")
print(sum(count_all))
print("\n")

otn_ch = [i / maslen for i in count_all]
otn_ch = [round(i, 4) for i in otn_ch]
otn_ch_sum = sum(otn_ch)
print("Относительные частоты для интервалов - через строчку ниже должна быть ровно единица:")
print(otn_ch)
print(round(otn_ch_sum, 2))
print("\n")
gisto_height = [i / inter_pitch_const for i in otn_ch]
print("Относительные частоты, деленные на 7 для гистограммы (координата y гистограммы по порядку)")
print(gisto_height)

test_gisto_height = [i * 7 for i in gisto_height]
print(sum(test_gisto_height))
