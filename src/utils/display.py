from IPython.core.display import HTML
from IPython.display import display

def printdf(df):
  display(HTML(df.to_html()))
  

def printsf(sf):
  display(HTML(sf.to_frame().to_html()))
