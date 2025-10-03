import pandas as pd
import matplotlib.pyplot as plt

# import history
history = pd.read_csv('history.csv')

# rename history columns
columns = {col: col.strip().replace('\"', '') for col in history.columns}
history.rename(columns=columns, inplace=True)

# get time iteration and residuals
inner_iter = history['Inner_Iter']

# plot useful quantities
def plot(field: str, title: str) -> None:
    cols = [col for col in history.columns
            if field.lower() in col.lower()]
    values = history[cols]
    
    # return if no value is found
    if cols == []:
        return

    # plot values
    fig, ax = plt.subplots()
    ax.plot(inner_iter, values, label=cols)
    ax.set_title(title)
    ax.set_xlabel('Iterations')
    ax.legend()
    ax.grid()

plot('rms', 'Residuals')
plot('avg cfl', 'CFL number')
plot('cd', 'Drag Coefficient')
plot('hf', 'Heat Flux')

plt.figure(1)
plt.show(block=True)
