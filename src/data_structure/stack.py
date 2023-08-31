"""
栈的应用
一般应用的题目是用来匹配两个元素，如果两个元素匹配上了就删除，删除后还有匹配上的，就需要再删除
典型题目是括号的匹配

这里写法先写 如果st不为空并且满足什么条件, 就入栈, 否则出栈

st = []
for item in 要遍历的容器:
    if st and 满足的条件:       #也可能写成while, 需要看抵消几次
        st.append(item)
    else:
        st.pop(item)
"""

