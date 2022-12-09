# 导入图形绘制库
import turtle

# 创建画笔
pen = turtle.Turtle()

# 设置画笔颜色为绿色
pen.color("green")

# 循环绘制三棵圣诞树
for i in range(3):
    # 绘制圣诞树的主体
    pen.begin_fill()
    pen.left(120)
    pen.forward(100)
    pen.right(120)
    pen.forward(100)
    pen.right(120)
    pen.forward(100)
    pen.end_fill()

    # 绘制圣诞树的顶部
    pen.left(90)
    pen.forward(50)
    pen.right(90)
    pen.begin_fill()
    pen.circle(25)
    pen.end_fill()

    # 移动画笔到下一棵圣诞树的位置
    pen.left(90)
    pen.forward(150)

# 保持窗口打开
turtle.mainloop()
