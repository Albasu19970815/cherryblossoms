import turtle as t

def draw_fractaltree(tree_length,tree_angle):
    
    if tree_length >= 2:

        t.forward(tree_length) #向前画树枝的长度
        t.right(tree_angle)  #右转角度
        draw_fractaltree(tree_length - 10,tree_angle)#画下一级树枝，直到树枝长度小于2

        t.left(2 * tree_angle)  #画左边的树枝
        draw_fractaltree(tree_length -10,tree_angle) #直到树枝长度小于2

        t.rt(tree_angle) #转到正上方向
        if tree_length <= 30:  #树枝长小于等于30时的部分为粉色
            t.pencolor('pink')
        if tree_length > 30:
            t.pencolor('brown')  #树枝大于30的部分为综色
        t.backward(tree_length)  #往回画到上一层

 

def main():
    t.penup()
    t.speed(30)
    #t.pencolor('brown')
    t.left(90)  #方向转左90度
    t.backward(350) 
    t.pendown()
    tree_length = 130  #树枝初始长度为130
    tree_angle = 20  
    draw_fractaltree(tree_length,tree_angle)
    t.exitonclick()  

if __name__ == '__main__':
    main()
