import matplotlib
import matplotlib.pyplot as plt

plt.rc("xtick", labelsize=10)
plt.rc("ytick", labelsize=80)
import seaborn as sns

sns.set(rc={"figure.figsize": (30,20)})
import sys
sys.path.append("src/data_management")
import pandas as pd
# from task_data_management import incidence_means
from task_data_management import mean_series
from task_data_management import average_month
from task_data_management import scales
from task_data_management import inc_plt_time_series
from task_data_management import inc_plt_time_series_2
from task_data_management import incidence_means


# Plot mean of contact reduction variables 

variables = list(mean_series.index)
mean = list(mean_series.values)

fig = plt.figure(figsize=(30, 20))

# creating the bar plot

plt.bar(scales, mean, color="purple", width=0.9)
plt.xticks(fontsize=10, rotation=45)
plt.xlabel("Variables of contact reduction for all waves", fontsize=15)
plt.ylabel("Average", fontsize=15)
plt.title("Mean of contact reduction variables", fontsize=15)
plt.show()
plt.savefig("bld/figures/contact_reduction_variables.png")

# Plot mean of contact reduction variables with similar contact reduction variables between
# wave four and wave five 

av_month = average_month.drop(columns=["mean_w1_w5"])
av = av_month.rename(index=lambda x: x.strftime('%B'))
sns.set()
av.T.plot(kind='bar', stacked=True)
plt.savefig("bld/figures/contact_reduction_variables_2.png")


# Plot with total monthwise mean
df1 = (
    av.stack()
    .reset_index()
    .set_index("month")
    .rename(columns={"level_1": "Contact reduction variables", 0: "Mean of contact reduction variables"})
)

plt.figure(figsize=(20, 10))
ax = sns.barplot(x=df1.index, y="Mean of contact reduction variables", data=df1)

# format the x-axis tick labels uses df, not df1
# ax.xaxis.set_major_formatter(
#     plt.FixedFormatter(av.index.to_series().dt.strftime("%Y-%m-%d"))
# )

plt.xticks(fontsize=10)
plt.show()
plt.savefig("bld/figures/monthwise_mean_variables.png")


# Comparable variables wave 4 to wave 5
X_AXIS = ("June-wave 4", "September-wave 5")

index = pd.Index(X_AXIS, name="Covid19 waves in Netherlands")

data = {
    "avoid_cafe": (
        float(average_month.iloc[3:4, 18:19].values),
        float(average_month.iloc[4:5, 18:19].values),
    ),
    "avoid_theater": (
        float(average_month.iloc[3:4, 19:20].values),
        float(average_month.iloc[4:5, 19:20].values),
    ),
    "avoid_public_transport": (
        float(average_month.iloc[3:4, 20:21].values),
        float(average_month.iloc[4:5, 20:21].values),
    ),
}

df = pd.DataFrame(data, index=index)
plt.figure()
ax = df.plot(kind="bar", stacked=True, figsize=(25, 20))
ax.set_ylabel("Mean of contact reduction variables")
plt.xticks(fontsize=10, rotation=0.0)
plt.legend(title="labels", bbox_to_anchor=(1.0, 1), loc="upper left")
# plt.savefig('stacked.png')  # if needed
plt.show()
plt.savefig("bld/figures/transition_wave4-_wave5.png")


# Plotting new cases and total cases incidence rate
plt.figure()
inc_plt_time_series.plot()
plt.legend(loc="best")
plt.show()
plt.savefig("bld/figures/time_series.png")

# create subplots for total cases, new cases, total and new cases incidence rate


fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(35, 27))
inc_plt_time_series_2["nc_incidence"].plot(ax=axes[0, 0])
axes[0, 0].set_title("New cases incidence rate")
inc_plt_time_series_2["tc_incidence"].plot(ax=axes[0, 1])
axes[0, 1].set_title("Total cases incidence rate")
inc_plt_time_series_2["new_cases"].plot(ax=axes[1, 0])
axes[1, 0].set_title("New cases")
inc_plt_time_series_2["total_cases"].plot(ax=axes[1, 1])
axes[1, 1].set_title("Total cases")
plt.xticks(fontsize=10, rotation=0.0)
plt.savefig("bld/figures/subplots.png")


# create a stacked bar plot of contact reduction variables with the waves

df = pd.DataFrame(data, index=index)
ax = av.plot(kind="bar", stacked=True, figsize=(30, 20))
ax.set_ylabel("Mean of contact reduction variables")
plt.xticks(fontsize=10, rotation=0.0)
plt.legend(title="labels", bbox_to_anchor=(1.0, 1), loc="upper left")
# plt.savefig('stacked.png')  # if needed
plt.show()
plt.savefig("bld/figures/stackedbar.png")

# create a bar plot with mean of contact reduction variables for each wave and a line plot 
# with the new cases incidence rate

inc_plot = incidence_means.drop(
    columns=[
        "new_cases",
        "total_cases",
        "logarithm_base10",
        "natural_log_nc_incidence",
        "tc_incidence",
    ]
)
inc_plot = inc_plot.drop(inc_plot.index[[0, 5, 6, 8, 9, 10, 11, 12]])
inc_plot.reset_index(drop=True, inplace=True)
av = average_month.rename(index=lambda x: x.strftime("%B"))

matplotlib.rc_file_defaults()
ax1 = sns.set_style(style=None, rc=None)

fig, ax1 = plt.subplots(figsize=(12, 6))
sns.lineplot(data=inc_plot, marker="o", sort=True, ax=ax1)
ax2 = ax1.twinx()

sns.barplot(data=av.T, alpha=0.5, ax=ax2)
plt.savefig("bld/figures/incidence_contact_reduction.png")
