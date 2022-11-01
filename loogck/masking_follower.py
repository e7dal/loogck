"""Like tail -f for logs, but with some cool hiding tricks..."""
import datetime
import random
import sys
import time
from dataclasses import dataclass

from rich import box
from rich.console import Console
from rich.live import Live
from rich.table import Table
from rich.text import Text


if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

from file_tail import FileTail
from bounce import BoxMoves

@dataclass
class Log:
    lid: int
    line: str
    timestamp: datetime.datetime

class Logs:
    LOGS=[]
    def __init__(i,n,f='data.txt'):
        i.n=n
        i.tail=FileTail(f)
        i.reversed=True
    def keep(i):
        if len(i.LOGS)>i.n:
            i.LOGS=i.LOGS[-i.n:]
            #del i.LOGS[0]  #delete first#i.LOGS=i.LOGS[-i.n:]

    def get_tail(i) -> Log:
        for _ in range(i.n):
            line=next(i.tail)
            if not line:
                continue
            line=line.strip()
            i.LOGS.append(line)
        i.keep()
        for lid,line in enumerate(i.LOGS):
            if i.reversed:
                line=i.LOGS[-lid]
            yield Log(lid=lid,
                      line=line,
                      timestamp=datetime.datetime.now())

class MaskingFollower():
    def __init__(i,logfile,get_mask):
        i.logfile=logfile
        i.get_mask=get_mask
        i.console = Console()
        i.height=i.console.height
        i.width=i.console.width
        i.logs=Logs(i.height,f=i.logfile)
        i.mask=i.get_mask(i.height,i.width)

    def line_mask(i,s,m) -> str:
        #ret=Text(s[:l])+Text('XxXxXxXxX',style="red")+Text(s[l+8:])
        def make_text_overwrite(t):
            org,new=t
            if new==' ': return Text(org,style="green",end='')
            return Text(new,style="bold blue",end='')

        ret=Text(end='')
        res=map(make_text_overwrite, zip(s,m))
        return ret.join(res)

    def create_log_table(i,logs,mask) -> Table:

        """ get this from tail -f or equivalent code, streaming ..."""
        table = Table.grid(padding=0)

        #table.add_row("debug")
        for ln, log in enumerate(logs.get_tail()):
            table.add_row(
                #Text(log.timestamp) +" "+
                i.line_mask(log.line,''.join(mask[ln]))
            )
        return table


    def follow_and_mask(i):
        with Live(console=i.console, screen=True, auto_refresh=False) as live:
            while True:
                live.update(i.create_log_table(i.logs,i.mask()), refresh=True)
                #time.sleep(0.03)
