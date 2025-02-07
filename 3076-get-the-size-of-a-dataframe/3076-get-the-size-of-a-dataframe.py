import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:

    ## 1    
    # nrows = len(players)
    # ncols = len(players.columns)

    # return [nrows, ncols]

    ## 2
    # players.shape: [nrows, ncols]
    return [players.shape[0], players.shape[1]]