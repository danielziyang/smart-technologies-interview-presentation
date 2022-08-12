"""
Random classes that might help with analysis.

"""
import pandas as pd
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin

class Helper: 
    """
    Auxiliary functions that aren't estimators or transformers.
    """
    def __init__(self):
        pass 

    @staticmethod
    def usd_to_cad(self, values):
        """
        Converts USD to CAD. Vectorized! 
        Yes, this function is intended as a joke.
        """
        return values * 1.28

class JobTitleTransformer(BaseEstimator,TransformerMixin):

    """
    Custom transformer I've written to create a new feature column that groups job titles more appropriately.
    Vectorized code 

    Args: pd.DataFrame having the "job_title" column.

    Returns: Augmented data matrix with a new column as 'job_group' replacing 'job_title'
    """

    def transform(self, X, y=None):
        job_group = pd.Series(X["job_title"].apply(lambda x: 'Senior' if ('Lead' in x or 'Principal' in x or 'Head' in x or 'Director' in x or 'Manager' in x) else x))
        job_group = job_group.map(lambda x: x.split(' ')[-1])
        job_group = job_group.map(lambda x: 'Other' if ('Architect' in x or 'Consultant' in x or 'Developer' in x or 'Researcher' in x or 'Specialist' in x) else x)
        X = X.drop(columns=["job_title"])
        return X.merge(job_group.rename('job_group'), left_index=True, right_index=True)

    def fit(self, X, y=None):
        return self
    

