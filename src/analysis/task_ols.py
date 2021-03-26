import sys

import numpy as np
import statsmodels.api as sm

# import matplotlib.pyplot as plt

sys.path.append("src/data_management")
from data_management import incidence_means
from data_management import mean_series
from data_management import average_month


# OLS wave 1
y = incidence_means.iloc[1:2, 1:2].values
x = [
    [1],
    [mean_series.values[0]],
    [mean_series.values[1]],
    [mean_series.values[2]],
    [mean_series.values[3]],
    [mean_series.values[4]],
    [mean_series.values[5]],
    [mean_series.values[6]],
    [mean_series.values[7]],
    [mean_series.values[8]],
]
x = np.array(x).T
results = sm.OLS(endog=y, exog=x).fit()
print(results.summary())

print(results.summary())

# plt.rc("figure", figsize=(12, 7))
# plt.text(
#     0.01, 0.05, str(results.summary()), {"fontsize": 10}, fontproperties="monospace"
# )
# plt.axis("off")
# plt.tight_layout()
# plt.savefig("bld/analysis/model.png")


# OLS wave 2
y = incidence_means.iloc[2:3, 1:2].values
x = [[1], [mean_series.values[11]], [mean_series.values[12]]]
x = np.array(x).T
results2 = sm.OLS(endog=y, exog=x).fit()
print(results2.summary())

# plt.rc("figure", figsize=(12, 7))
# plt.text(
#     0.01, 0.05, str(results2.summary()), {"fontsize": 10}, fontproperties="monospace"
# )
# plt.tight_layout()
# plt.savefig("bld/analysis/model2.png")


# OLS wave 3
y = incidence_means.iloc[3:4, 1:2].values
x = [
    [1],
    [mean_series.values[18]],
    [mean_series.values[14]],
    [mean_series.values[15]],
    [mean_series.values[19]],
    [mean_series.values[13]],
    [mean_series.values[17]],
    [mean_series.values[16]],
]
x = np.array(x).T
results = sm.OLS(endog=y, exog=x).fit()
print(results.summary())


# OLS wave 4
y = incidence_means.iloc[4:5, 1:2].values
x = [
    [1],
    [float(average_month.iloc[3:4, 18:19].values)],
    [float(average_month.iloc[3:4, 19:20].values)],
    [float(average_month.iloc[3:4, 20:21].values)],
    [float(average_month.iloc[3:4, 21:22].values)],
]
x = np.array(x).T
results = sm.OLS(endog=y, exog=x).fit()
print(results.summary())


# OLS wave 5
y = incidence_means.iloc[7:8, 1:2].values
x = [
    [1],
    [float(average_month.iloc[4:5, 18:19].values)],
    [float(average_month.iloc[4:5, 19:20].values)],
    [float(average_month.iloc[4:5, 20:21].values)],
]
x = np.array(x).T
results = sm.OLS(endog=y, exog=x).fit()
print(results.summary())


# OLS with log base 10


# OLS wave 1
y = incidence_means.iloc[1:2, 6].values
x = [
    [1],
    [mean_series.values[0]],
    [mean_series.values[1]],
    [mean_series.values[2]],
    [mean_series.values[3]],
    [mean_series.values[4]],
    [mean_series.values[5]],
    [mean_series.values[6]],
    [mean_series.values[7]],
    [mean_series.values[8]],
]
x = np.array(x).T
results = sm.OLS(endog=y, exog=x).fit()
print(results.summary())


# OLS wave 2
y = incidence_means.iloc[2:3, 6].values
x = [[1], [mean_series.values[11]], [mean_series.values[12]]]
x = np.array(x).T
results = sm.OLS(endog=y, exog=x).fit()
print(results.summary())


# OLS wave 3 with log base 10
y = incidence_means.iloc[3:4, 6].values
x = [
    [1],
    [mean_series.values[18]],
    [mean_series.values[14]],
    [mean_series.values[15]],
    [mean_series.values[19]],
    [mean_series.values[13]],
    [mean_series.values[17]],
    [mean_series.values[16]],
]
x = np.array(x).T
# x = sm.add_constant(x)
results = sm.OLS(endog=y, exog=x).fit()
print(results.summary())


# OLS wave 4 with log base 10
y = incidence_means.iloc[4:5, 6].values
x = [
    [1],
    [float(average_month.iloc[3:4, 18:19].values)],
    [float(average_month.iloc[3:4, 19:20].values)],
    [float(average_month.iloc[3:4, 20:21].values)],
    [float(average_month.iloc[3:4, 21:22].values)],
]
x = np.array(x).T
# x = sm.add_constant(x)
results = sm.OLS(endog=y, exog=x).fit()
print(results.summary())


# OLS wave 5 with log base 10
y = incidence_means.iloc[7:8, 6].values
x = [
    [1],
    [float(average_month.iloc[4:5, 18:19].values)],
    [float(average_month.iloc[4:5, 19:20].values)],
    [float(average_month.iloc[4:5, 20:21].values)],
]
x = np.array(x).T
# x = sm.add_constant(x)
results = sm.OLS(endog=y, exog=x).fit()
print(results.summary())


# OLS average across all waves without log
y = [
    incidence_means.iloc[1:2, 1:2].values,
    incidence_means.iloc[2:3, 1:2].values,
    incidence_means.iloc[3:4, 1:2].values,
    incidence_means.iloc[4:5, 1:2].values,
    incidence_means.iloc[7:8, 1:2].values,
]
y = np.array(y)
x = [
    [float(average_month.iloc[0:1, 22:23].values)],
    [float(average_month.iloc[1:2, 22:23].values)],
    [float(average_month.iloc[2:3, 22:23].values)],
    [float(average_month.iloc[3:4, 22:23].values)],
    [float(average_month.iloc[4:5, 22:23].values)],
]
x = np.array(x)
results = sm.OLS(endog=y, exog=x).fit()
print(results.summary())


# OLS Average across all the five waves with log base 10

y = [
    incidence_means.iloc[1:2, 6].values,
    incidence_means.iloc[2:3, 6].values,
    incidence_means.iloc[3:4, 6].values,
    incidence_means.iloc[4:5, 6].values,
    incidence_means.iloc[7:8, 6].values,
]
y = np.array(y)
x = [
    [float(average_month.iloc[0:1, 22:23].values)],
    [float(average_month.iloc[1:2, 22:23].values)],
    [float(average_month.iloc[2:3, 22:23].values)],
    [float(average_month.iloc[3:4, 22:23].values)],
    [float(average_month.iloc[4:5, 22:23].values)],
]
x = np.array(x)
results = sm.OLS(endog=y, exog=x).fit()
print(results.summary())
