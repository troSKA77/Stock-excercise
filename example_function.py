import pandas as pd

def update_value(data):
    result = data[0]
    df = pd.DataFrame(data[1:], columns=["index 0", "index 1", "index 2", "index 3", "index 4", "index 5", "index 6", "index 7"])
    df = df.drop(df[df["index 2"] != result[2]].index)
    result[5] = df['index 5'].iloc[0]
    return result
