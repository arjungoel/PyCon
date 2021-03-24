##### **PANDAS**:

Why do we mark something as `NaN` rather than a zero or an empty string or the text unknown?


- `ri.isnull()` is a DataFrame method which returns a DataFrame of true and false values.
- `value_counts()` is a count of values. This function is used to get a Series containing counts of unique values. The resulting object will be in descending order so that the first element is the most frequently-occurring
element. Excludes `NA` values by default.

1. Remove the column that contains missing values:
    - Pay attention to default arguments
    - Check your work
    - There is more than one way to do everything in pandas


2. During a search
    - Use string methods to find partial matches
    - Use the correct denominator when calculating rates
    - pandas calculations ignore missing values
    - Apply the **"smell test"** to your results

- The `stack` method turns column names into index values, and the `unstack` method turns index values into column names. So by shifting the values into the index, we can use `stack` and `unstack` to perform the swap.
- When you take `mean()` of series of 0s and 1s, you get percentage of time it is a one.

**causation** 

- Causation is difficult to conclude, so focus on relationships.
- Include all relevant factors when studying a relationship.

In Data Science if you are talking about relationships are you using statistical tests?


- By default `null(s)` and `NaN(s)` are dropped in pandas methods.
- `mean()` excludes the missing or NaN values.
- You can groupby the things that aren't column names if you just specify them in full.
- The default plot for a pandas series is a `line plot`. If you are in jupyter notebook you need to run `plot()` function else `plt.show()`.

- Series has two methods for sorting, `sort_index()` and `sort_values()` and `value_counts()` does `sort_values()` in descending order by default.

- When you filter a dataframe by multiple conditions you need to use `parantheses ()` around each condition.

- `NaN` is not a string.

`SettingWithCopyWarning` - A value is trying to be set on a copy of a slice from a DataFrame.

What is the appropriate way to handle a `SettingWithCopyWarning` ?



Could we within the loc() effect a second column that doesn't yet exist?

`np.nan`

Exploratory Plots: (Needs to be explored)
