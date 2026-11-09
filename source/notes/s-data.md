@spec Edexcel 9MA0 Statistics topic 2: 2.1 diagrams (histograms, box plots, cumulative frequency, scatter diagrams and regression); 2.2 correlation; 2.3 measures of location and spread; 2.4 outliers and cleaning data
@intro Once data has been collected, we summarise it with diagrams and statistics. This topic covers histograms, box plots, cumulative frequency, measures of location and spread, outliers, correlation and regression.
# Measures of location and spread
- **Location:** the mean $\bar x=\frac{\sum x}{n}$ (or $\frac{\sum fx}{\sum f}$ for a frequency table), the median and the mode.
- **Spread:** the range, the interquartile range (IQR $=Q_3-Q_1$), interpercentile ranges, the variance and the standard deviation.
:::eq
$$\sigma^2=\frac{\sum x^2}{n}-\bar x^2=\frac{S_{xx}}{n}\qquad\sigma=\sqrt{\sigma^2}$$
:::
- For grouped data, use the class midpoints, and estimate the median by **linear interpolation**.
- **Coding:** if $y=\frac{x-a}{b}$, then $\bar y=\frac{\bar x-a}{b}$ and $\sigma_y=\frac{\sigma_x}{b}$. Adding or subtracting a constant does not change the spread.
:::ex Mean and standard deviation
Q: For the data $n=10$, $\sum x=52$ and $\sum x^2=310$, find the mean and the standard deviation.
1. $\bar x=5.2$.
2. $\sigma^2=\frac{310}{10}-5.2^2=31-27.04=3.96$.
A: $\bar x=5.2$ and $\sigma=1.99$
:::
:::ex Interpolation
Q: In a grouped frequency table, 20 values are below 30, and the class $30\le x<40$ contains 16 values. There are 60 values in total. Estimate the median.
1. The median is the 30th value, which is 10 values into the class of 16.
2. Median $\approx30+\frac{10}{16}\times10=36.25$.
A: About 36.3
:::
# Diagrams
- **Histograms:** frequency density = frequency ÷ class width, and **area is proportional to frequency**.
!fig s-boxplot Box plot showing quartiles, whiskers and an outlier
- **Box plots** show the minimum, $Q_1$, the median, $Q_3$ and the maximum, with outliers marked as crosses. They make comparing distributions easy.
- **Cumulative frequency** graphs are plotted at the **upper class boundaries**. Read off the median at $\frac n2$ and the quartiles at $\frac n4$ and $\frac{3n}{4}$.
- **Outliers:** a common rule is any value more than $1.5\times$IQR below $Q_1$ or above $Q_3$. Alternatively, use the mean $\pm\,2$ or $3$ standard deviations.
- **Cleaning data:** remove values that are errors, such as impossible readings, but keep genuine extreme values. Justify each decision in context.
:::ex Histogram reading
Q: A histogram bar for the class 10–15 has a frequency density of 4.8. Find its frequency.
1. Frequency = frequency density × class width = 4.8 × 5.
A: 24
:::
# Correlation and regression
- **Scatter diagrams** show positive, negative or no correlation. **Correlation does not imply causation.**
- **Regression line** $y=a+bx$: interpret $b$ as the change in $y$ per unit increase in $x$. Use the line only within the range of the data (**interpolation**); **extrapolation** is unreliable.
- The **explanatory** (independent) variable goes on the $x$-axis, and the **response** (dependent) variable on the $y$-axis.
- **PMCC** (A level), written $r$: $-1\le r\le1$. It measures the strength of **linear** correlation. Values close to $\pm1$ indicate strong correlation.
- **Exponential models** (A level): if $\log y$ against $x$ is linear, then $y=kb^x$.
:::ex Interpreting regression
Q: The regression line of daily ice-cream sales $y$ on temperature $x$ (in °C) is $y=12+3.5x$, for $10\le x\le25$. Interpret 3.5, and comment on using the line to predict sales at 35 °C.
1. 3.5 means that sales rise by about 3.5 for each 1 °C rise in temperature.
2. 35 °C is outside the data range, so this would be extrapolation.
A: The prediction is unreliable, because the relationship may not hold outside $10$–$25$ °C.
:::
:::warn
- Plotting frequency (instead of frequency density) on a histogram with unequal class widths.
- Saying that a strong correlation proves one variable causes the other.
- Forgetting to take the square root of the variance to get the standard deviation.
:::
:::tip
- When you compare two distributions, compare a measure of **location** and a measure of **spread**, and say what each means in context.
:::
:::sum
- Mean, median and mode; variance $\frac{\sum x^2}{n}-\bar x^2$; coding.
- Histograms (area ∝ frequency), box plots, cumulative frequency.
- Outliers via $1.5\times$IQR; clean data with justification.
- Correlation ≠ causation; use regression lines only for interpolation; PMCC.
:::
