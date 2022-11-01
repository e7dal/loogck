import random
import time

ri=random.randint

class Direction():
    def __init__(i,size,name,characters=['+','-']):
        i.size=size
        i.name=name
        i.direction=random.choice(["+","-"])
        i.choice={'+':characters[0],
                  '-':characters[1]}
        i.pos=ri(0,size)
    def __str__(i):
        return f"D:{i.name} p:{i.pos} d:{i.direction} c:{i.choice[i.direction]}"
    def flip(i):
        if i.direction=="+":
            i.direction="-"
        else:
            i.direction="+"
    def move(i):
        flipped=[False,False]
        if i.direction=="+": 
            if i.pos+1==i.size:
                i.flip()
                flipped[1]=True
            else:
                i.pos+=1
        if i.direction=="-": 
            if i.pos-1==-1:
                i.flip()
                flipped[0]=True
            else:
                i.pos-=1
        return i.pos,flipped
    def back(i):
        i.flip()
        i.move()
        i.flip()




class BoxMoves():
    def __init__(i, height=10, width=30,trail_size=100,show=False):
        i.t=0.1
        i.h=height
        i.w=width
        i._show=show
        i.trail_size=trail_size
        i.trail=[]
        i.DV=Direction(size=i.h,
                       name='Vertical',
                       characters=['Y','y'])

        i.DH=Direction(size=i.w,
                       name='Horizontal',
                       characters=['X','x'])

        i.empty()

    def empty(i):
        i.grid=[]
        for y in range(i.h):
            i.grid.append([])
            for x in range(i.w):
                i.grid[y].append(f" ")

    def show(i,before=None,after=None):
        if not i._show:return
        print("\n"*50)
        if before:print(f"*before: {before} *")
        if after: print(f"*after:  {after} *")
        print((2+i.w)*'*')
        for r in i.grid:print('|'+''.join(r)+'|')
        print((2+i.w)*'*')
        time.sleep(i.t)


    def add_trail(i):
        i.trail.append((i.DV.pos,i.DH.pos))
        if len(i.trail) > i.trail_size:
            #i.trail=i.trail[-i.trail_size:]
            del i.trail[0]
        
        for ty,tx in i.trail:
            #print("trail",ty,ty)
            i.surround(ty,tx,"XX")
        for ty,tx in i.trail:
            i.grid[ty][tx]="o"
            i.set(ty,tx,".")

    def surround(i,y,x,chars='12'):
        #"""
        # . .
        #. o .
        # . .
        #"""
        #points=((-1,-1),
        #        (-1, 1),
        #        ( 0,-2),
        #        ( 0, 2),
        #        ( 1,-1),
        #        ( 1, 1)
        #        )
        #
        """
         ...
        ..o..
         ...
        """
        points=((-1,-1),
                (-1, 0),
                (-1, 1),
                ( 0,-2),
                ( 0,-1),
                ( 0, 1),
                ( 0, 2),
                ( 1,-1),
                ( 1, 0),
                ( 1, 1)
                )
        for dy,dx in points:
            if len(chars)>1:
                i.surround(y+dy,x+dx,chars[1:])
            i.set(y+dy,x+dx,chars[0])

    def set(i,y,x,char='?', overflow=False):
        assert len(char)==1
        if overflow:
            y=y%i.DV.size
            x=x%i.DH.size
        else:
            if y>=i.DV.size:y=i.DV.size-1
            if x>=i.DH.size:x=i.DH.size-1
            if y<0:y=0
            if x<0:x=0

        i.grid[y][x]=char

    def move(i):
        i.empty()
        i.add_trail()
        mb=f"DV={i.DV} DH={i.DH}"
        i.grid[i.DV.pos][i.DH.pos]="O"
        y,yf=i.DV.move()
        x=i.DH.pos
        if not yf[0]:
            x,xf=i.DH.move()
            if xf[0]:
                i.DV.back()

        #i.grid[y][x]="x"
        i.set(i.DV.pos,i.DH.pos,"x")
        ma=f"DV={i.DV} DH={i.DH}"
        i.show(before=mb, after=ma)
        return i.grid

def get_bouncer(width,height):
    bm=BoxMoves(height=width, width=height,trail_size=300,show=False)
    def bouncer():
        return bm.move()
    return bouncer

if __name__=="__main__":
    bm=BoxMoves(height=20, width=80,trail_size=300,show=True)
    while True:bm.move()
