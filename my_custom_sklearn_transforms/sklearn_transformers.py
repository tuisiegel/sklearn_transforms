from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd
class DropColumns(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        data = X.copy()
        # Retornamos um novo dataframe sem as colunas indesejadas
        return data.drop(labels=self.columns, axis='columns')

    
class Imput(BaseEstimator, TransformerMixin):
    def __init__(self, subject):
        self.subject = subject

    def fit(self, X, y=None):
        return self 
    
    def transform(self, X):
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        data = X.copy() 
          
        nota = "NOTA_" + self.subject
        
        reprovacoes = "REPROVACOES_" + self.subject
        ap_null = data.loc[data[reprovacoes] == 0].loc[pd.isnull(data[nota])]
        
        rp_null = data.loc[data[reprovacoes] != 0].loc[pd.isnull(data[nota])] 
        
        not_null = data.loc[pd.notnull(data[nota])]
                
        ap_null[nota] = data[nota].mean()
        
        rp_null[nota] = 0
        
        data2 = pd.concat([ap_null, rp_null, not_null])
        return data2
