# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import sys
reload(sys)
sys.setdefaultencoding('UTF-8')

from matplotlib.font_manager import _rebuild
_rebuild()

# 设置中文字体和负号正常显示
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False

name_list = ['cython', 'ctypes', 'cffi', 'python']
num_list = [0.49, 0.59, 0.56, 54.10]
plt.bar(range(len(num_list)), num_list, color='rgb', tick_label=name_list)
plt.show()
