import pandas as pd
from matplotlib import pyplot as plt

# Import data
sheet_title = 'Renland d18O' # set outside for use in plotting
data = pd.read_excel('../../data/vinther2008renland-agassiz.xlsx', \
                      sheetname=sheet_title, header=72)
# Note that they also include a % sign in front of all header lines.
# How might you re-code this to dynamically learn how long the header is
# and skip over it?

# Give headers better names
data.columns = ['years [b2k]', 'depth [m]', 'del18O [permil]']

# And plot
plt.plot(data['years [b2k]'], data['del18O [permil]'])
#plt.gca().invert_yaxis() # Grabs current axes and inverts x-axis
                          # uncomment if you prefer to see time this way.
# Automatically use column labels in the plot
plt.title(sheet_title, fontsize=16, fontweight='bold')
plt.xlabel(data.columns[0], fontsize=16)
plt.ylabel(data.columns[-1], fontsize=16)
plt.show()

# If we want better axis labels, we can use the LaTeX formatting:
plt.figure(figsize=(12,5)) # make figure extra-wide (width, height)
plt.plot(data['years [b2k]'], data['del18O [permil]'])
plt.title('Greenland Ice Core: Renland', fontsize=16, fontweight='bold')
plt.xlabel('Years b2k', fontsize=16)
# Below, I use LaTeX formatting to write the Greek "delta" and the superscript
plt.ylabel('$\delta^{18}$O', fontsize=16)
plt.tight_layout()
plt.show()
