import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('Analiza_danych_8/Task-8_result.csv')

# Create a histogram for each year
for year in df['year'].unique():
    # Filter the data for the current year
    year_data = df[df['year'] == year]

    # Create a histogram of the base scores
    x = [i / 10.0 for i in range(0, 101)]
    y = [0] * 101
    for index, row in year_data.iterrows():
        if row['baseScore31'] > 0:
            x_index = int(row['baseScore31'] * 10)
            y[x_index] += row['vectorString31']

    fig, ax = plt.subplots(figsize=(12, 5))
    ax.bar(x, y, width=0.1, edgecolor='white', linewidth=0.5)

    # Set the title and axis labels
    ax.set_title(f'Liczba kombinacji flag dla danego base score dla roku {year} (CVSS 3.1)')
    ax.set_xlabel('Wartość Base Score')
    ax.set_ylabel('Liczba wystąpień')

    # set the x-axis limits
    ax.set_xlim(0, 10.1)
    # Set x-axis tick locations and labels
    tick_locs = [i * 0.2 for i in range(51)]
    tick_labels = ['{:.1f}'.format(loc) if i % 2 == 0 else '' for i, loc in enumerate(tick_locs)]
    plt.xticks(tick_locs, tick_labels)

    # Add a white line between adjacent bars
    for i in range(len(x)-1):
        if y[i] > 0 and y[i+1] > 0:
            linewidth = min(y[i], y[i+1]) * 0.01
            ax.plot([x[i], x[i+1]], [y[i], y[i+1]], color='white', linewidth=linewidth)

    # Add grid
    ax.grid(color='gray', linestyle=':', linewidth=0.5, zorder=-1)

    # Save the histogram as an image file
    plt.savefig(f'Analiza_danych_8/wykresy/CVSSv31_{year}.png')

    # Clear the plot for the next iteration
    plt.clf()
