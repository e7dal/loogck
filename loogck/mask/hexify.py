import re
from collections import Counter
from hexy import Hexy
import hexy.grid
hexy.grid.GRIDCHAR=' '

#borrowed from click
_ansi_re = re.compile(r"\033\[[;?0-9]*[a-zA-Z]")
def strip_ansi(value: str) -> str:
    return _ansi_re.sub("", value)

def get_hexy(height,width):
    counter=Counter
    cn=Counter('c')
    def get_hexy_lines(cnt=cn):
        cnt.update('c')
        cnt['c']
        #cn%=100
        #if cnt['c']%100==0:cn+=10
        offset=cnt['c']%65
        offset+=10
        hx=Hexy(width,height)
        hx.circle(0,0,offset,offset+3,"HELLO FROM HEXY")
        hx.draw(int(width/2),10,offset)
        hx.draw(int(width/2),10,offset+1)
        hx.draw(int(width/2),10,offset+2)

        hl=[]
        for gi,gl in enumerate(hx.grid):
            hl.append('')
            for gc in gl:
                hl[gi]+=strip_ansi(gc.get())
        return hl
    return get_hexy_lines


if __name__=="__main__":
    getter=get_hexy(20,30)
    for _ in range(5):
        for line in getter():
            print(line)
        print()

