from sklearn.base import BaseEstimator, TransformerMixin


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
    
class NoNull (data1): 
    def imput(subject):
        #subject = "GO"
        nota = "NOTA_" + subject
        nota
        reprovacoes = "REPROVACOES_" + subject
        ap_null = data1.loc[data1[reprovacoes] == 0].loc[pd.isnull(data1[nota])]
        
        rp_null = data1.loc[data1[reprovacoes] != 0].loc[pd.isnull(data1[nota])] 
        
        not_null = data1.loc[pd.notnull(data1[nota])]
                
        ap_null[nota] = data1[nota].mean()
        
        rp_null[nota] = 0
        
        data2 = pd.concat([ap_null, rp_null, not_null])
        return data2
