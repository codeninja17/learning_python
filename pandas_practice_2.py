import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('NTPC.csv', index_col="Date", parse_dates=True, usecols=["Date", "Close"], na_values=['nan'])

#print(df.head(5))
#print(len(df))
#df.dropna()
#df['Close'].plot()
#plt.show()


import numpy as np
import matplotlib.pyplot as plt

# Sample 2D array
data = np.array([[1, 2, 3, 4, 5],
                 [6, 7, 8, 9, 10],
                 [11, 12, 13, 14, 15]])

# Create a figure and axis object
fig, ax = plt.subplots()

# Plot each row as a separate line using the transposed array
lines = ax.plot(data.T)

# Set labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Plot of 2D Array')

# Add legend
legend_labels = [f'Row {i}' for i in range(data.shape[0])]
ax.legend(lines, legend_labels)

# Show the plot
plt.show()