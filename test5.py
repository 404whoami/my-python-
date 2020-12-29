# import turtle as t
# list1=['blue','purple','red','green','orange']
# for i in range(100):
#     t.color(list1[i%5])
#     t.pensize(i/10+1)
#     t.forward(i)
#     t.left(60)
# t.done()
piece1=[[(-40, 120), (-70, 260), (-130, 230), (-170, 200), (-170, 100), (-160, 40), (-170, 10), (-150, -10), (-140, 10), (-40, -20), (0, -20)],[(0, -20), (40, -20), (140, 10), (150, -10), (170, 10), (160, 40), (170, 100), (170, 200), (130, 230), (70, 260), (40, 120), (0, 120)]]

print(len(piece1[0]) )
for i in range(len(piece1[0])):
    x,y=piece1[0][i]
    print("x>>>",x, "i am y",y)