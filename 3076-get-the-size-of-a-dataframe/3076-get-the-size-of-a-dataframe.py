import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    
    nrows = len(players)
    ncols = len(players.columns)

    return [nrows, ncols]