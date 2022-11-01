def get_static_mask(height,width):
    mask=[]
    for y in range(height):
        mask.append([])
        for x in range(width):
            if (x+y)%7==0:
                mask[y].append('X')
            else:
                mask[y].append(' ')
        mask[y]=''.join(mask[y])
    def _mask():
        return mask
    return _mask

if __name__=="__main__":
    for l in get_static_mask(20,30)():
        print(l)
