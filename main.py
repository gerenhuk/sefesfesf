import pandas as pd

data = {
    'Name': ['Анна', 'Борис', 'Вікторія', 'Григорій', 'Олена'],
    'Age': [25, None, 22, 30, None],
    'Score': [85, 90, None, 78, 95]
}

df = pd.DataFrame(data)
print("DataFrame:")
print(data)
