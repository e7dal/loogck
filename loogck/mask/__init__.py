DEFINED_MASKS=['static',
               'bounce',
               'hexify']

def import_mask(mask_name):
    if mask_name=="static":
        from .static import get_static_mask as get_mask
    if mask_name=="hexify":
        from .hexify import get_hexy as get_mask
    if mask_name=="bounce":
        from .bounce import  get_bouncer as get_mask
    return get_mask

#test this...
#if __name__=="__main__":
#    for m in DEFINED_MASKS:
#        mask=import_mask(m)
#        print(mask)
