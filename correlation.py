import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ENEM - correlation

%precision %.2f

pd.options.display.float_format = '{:,.2f}'.format

uri = 'https://github.com/guilhermesilveira/enem-2018/blob/master/MICRODADOS_ENEM_2018_SAMPLE_43278.csv?raw=true'

data = pd.read_csv(uri)

grade_columns = ['NU_NOTA_CN', 'NU_NOTA_CH', 'NU_NOTA_LC', 'NU_NOTA_MT', 'NU_NOTA_REDACAO']
grade_data = data[grade_columns].dropna()
grade_data.columns = ['ciencias_naturais', 'ciencias_humanas', 'linguagem_codigo', 'matematica', 'redacao']

# It generates a table
corr = grade_data.corr()
corr

# It generates a heatmap

sns.set(font_scale=1.2)

labels = ['Ciências da Natureza', 'Ciências Humanas', 'Linguagens e Códigos', 'Matemática', 'Redação']

plt.figure(figsize=(6, 6))
ax = sns.heatmap(
    corr,
    annot=True,
    cmap="YlGnBu",
    cbar=False,
    xticklabels=labels,
    yticklabels=labels,
    # mask=np.triu(np.ones_like(corr, dtype=np.bool))
)

plt.show()

# Reset configuration to default
sns.set()