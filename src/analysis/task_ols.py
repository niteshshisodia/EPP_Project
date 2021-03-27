import sys
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm
sys.path.append("src/data_management")
from task_data_management import incidence_means
from task_data_management import mean_series
from task_data_management import average_month



def plotmodel(regression_output,title):
    filepath= "bld/analysis/"
    plt.rc("figure", figsize=(12, 7))
    plt.text(
        0.01, 0.05, regression_output, {"fontsize": 10}, fontproperties="monospace"
    )
    plt.axis("off")
    plt.tight_layout()
    plt.savefig(filepath+title+'.png')
    plt.close()

    


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
plotmodel(str(results.summary()),"model_1")



# OLS wave 2
y = incidence_means.iloc[2:3, 1:2].values
x = [[1], [mean_series.values[11]], [mean_series.values[12]]]
x = np.array(x).T
results_2 = sm.OLS(endog=y, exog=x).fit()
print(results_2.summary())
plotmodel(str(results_2.summary()),"model_2")



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
results_3 = sm.OLS(endog=y, exog=x).fit()
print(results_3.summary())
plotmodel(str(results_3.summary()),"model_3")




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
results_4 = sm.OLS(endog=y, exog=x).fit()
print(results_4.summary())
plotmodel(str(results_4.summary()),"model_4")



# OLS wave 5
y = incidence_means.iloc[7:8, 1:2].values
x = [
    [1],
    [float(average_month.iloc[4:5, 18:19].values)],
    [float(average_month.iloc[4:5, 19:20].values)],
    [float(average_month.iloc[4:5, 20:21].values)],
]
x = np.array(x).T
results_5 = sm.OLS(endog=y, exog=x).fit()
print(results_5.summary())
plotmodel(str(results_5.summary()),"model_5")



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
results_6 = sm.OLS(endog=y, exog=x).fit()
print(results_6.summary())
plotmodel(str(results_6.summary()),"model_6")



# OLS wave 2
y = incidence_means.iloc[2:3, 6].values
x = [[1], [mean_series.values[11]], [mean_series.values[12]]]
x = np.array(x).T
results_7 = sm.OLS(endog=y, exog=x).fit()
print(results_7.summary())
plotmodel(str(results_7.summary()),"model_7")



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
results_8 = sm.OLS(endog=y, exog=x).fit()
print(results_8.summary())
plotmodel(str(results_8.summary()),"model_8")



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
results_9 = sm.OLS(endog=y, exog=x).fit()
print(results_9.summary())
plotmodel(str(results_9.summary()),"model_9")


# OLS wave 5 with log base 10
y = incidence_means.iloc[7:8, 6].values
x = [
    [1],
    [float(average_month.iloc[4:5, 18:19].values)],
    [float(average_month.iloc[4:5, 19:20].values)],
    [float(average_month.iloc[4:5, 20:21].values)],
]
x = np.array(x).T
results_10 = sm.OLS(endog=y, exog=x).fit()
print(results_10.summary())
plotmodel(str(results_10.summary()),"model_10")



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
results_11 = sm.OLS(endog=y, exog=x).fit()
print(results_11.summary())
plotmodel(str(results_11.summary()),"model_11")



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
results_12 = sm.OLS(endog=y, exog=x).fit()
print(results_12.summary())
plotmodel(str(results_12.summary()),"model_12")







