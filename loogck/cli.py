import click
from .mask import import_mask
from .mask import DEFINED_MASKS
from .masking_follower import MaskingFollower


@click.command()
@click.argument('logfile', 
                default='some.log',
                type=click.Path(exists=True))
                # help='the log file you want to follow with loogck')
                #type=click.File('rb'))# filetail accepts filename
@click.option('-m', 
              '--mask',
              help='the mask you wish to apply on the followed file')

def follow(logfile, mask):
    """fancy follow file program, to follow a logfile while dynamically masking some log details/regions.
       like tail -f logfile.log, but you know more fun:)
    """
    click.echo(f"stand back and loogck, will apply: {mask} on {logfile}  while following" )
    if mask not in DEFINED_MASKS: 
        click.echo(f"mask should be one of {DEFINED_MASKS}" )
        return
    masker=import_mask(mask)
    mf=MaskingFollower(logfile,masker)
    mf.follow_and_mask()

if __name__ == '__main__':
    follow()
