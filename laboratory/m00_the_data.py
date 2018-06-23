import pandas as pd


def main():
    """Load documents.
    """
    
    df = pd.read_csv('../data/studentsreviews.csv')
    df.head()

    return df['comment'].tolist()


if __name__=='__main__':
    docs = main()
    
    