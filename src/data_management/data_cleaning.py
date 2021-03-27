# Importing libraries and packages
# import datetime as dt
# import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# import seaborn as sns

# load the data sets

covid_d1 = pd.read_stata(
    "src/original_data/covid_data_2020_03.dta", convert_categoricals=True
)
covid_d2 = pd.read_stata(
    "src/original_data/covid_data_2020_04.dta", convert_categoricals=True
)
covid_d3 = pd.read_stata(
    "src/original_data/covid_data_2020_05.dta", convert_categoricals=True
)
covid_d4 = pd.read_stata(
    "src/original_data/covid_data_2020_06.dta", convert_categoricals=True
)
covid_d5 = pd.read_stata(
    "src/original_data/covid_data_2020_09.dta", convert_categoricals=True
)

# Extract data from existing data sets (extract variables related to "contact
# reduction") according to their respective waves.

covid_wave_1 = covid_d1[
    [
        "personal_id",
        "month",
        "avoid_busy_places",
        "avoid_public_places",
        "maintain_distance",
        "adjust_school_work",
        "quarantine_symptoms",
        "quarantine_no_symptoms",
        "no_avoidance_behaviors",
        "contact_older_people",
        "contact_young_people",
    ]
]


covid_wave_2 = covid_d2[
    ["personal_id", "month", "change_contacts_personal", "change_contacts_distanced"]
]

covid_wave_3 = covid_d3[
    [
        "personal_id",
        "month",
        "outside_no",
        "outside_contacts",
        "outside_garden",
        "outside_shopping",
        "outside_purchases",
        "outside_care",
        "outside_medical",
    ]
]


covid_wave_4 = covid_d4[
    [
        "personal_id",
        "month",
        "avoid_cafe",
        "avoid_theater",
        "avoid_public_transport",
        "avoid_gym",
    ]
]

covid_wave_5 = covid_d5[
    ["personal_id", "month", "avoid_cafe", "avoid_theater", "avoid_public_transport"]
]


# Append the covid data sets
covid_w1_w2 = covid_wave_1.append(covid_wave_2, ignore_index=False)
covid_w1_w3 = covid_w1_w2.append(covid_wave_3, ignore_index=False)
covid_w1_w4 = covid_w1_w3.append(covid_wave_4, ignore_index=False)

# Final dataframe for all relevant covid waves
covid_data = covid_w1_w4.append(covid_wave_5, ignore_index=False)

# identify string values to be replaced
for col in list(covid_data):
    print(col)
    print(covid_data[col].unique())


# Replace string variables with boolean data type and convert pre-existing boolean
# data type values according to contact reduction rules/assumptions.
# wave 1 variables
covid_data["no_avoidance_behaviors"] = covid_data["no_avoidance_behaviors"].map(
    {0.0: 1.0, 1.0: 0.0}
)

# consider wave 2 variables
covid_data["change_contacts_personal"] = covid_data["change_contacts_personal"].map(
    {"less": 1.0, "much less": 1.0, "roughly equal": 0.0, "more": 0.0, "much more": 0.0}
)

covid_data["change_contacts_distanced"] = covid_data["change_contacts_distanced"].map(
    {"less": 0.0, "much less": 0.0, "roughly equal": 1.0, "more": 1.0, "much more": 1.0}
)

# wave 3 -- w/o "outside_detour" "outside_volunteering"
covid_data["outside_shopping"] = covid_data["outside_shopping"].map(
    {0.0: 1.0, 1.0: 0.0}
)
covid_data["outside_contacts"] = covid_data["outside_shopping"].map(
    {0.0: 1.0, 1.0: 0.0}
)
covid_data["outside_medical"] = covid_data["outside_medical"].map({0.0: 1.0, 1.0: 0.0})
covid_data["outside_purchases"] = covid_data["outside_purchases"].map(
    {0.0: 1.0, 1.0: 0.0}
)
covid_data["outside_care"] = covid_data["outside_care"].map({0.0: 1.0, 1.0: 0.0})

dictionary_map = {
    "none at all": 1.0,
    "hardly any": 1.0,
    "some": 0.0,
    "a lot": 0.0,
    "a whole lot": 0.0,
    "once a week": 0.0,
    "never": 1.0,
    "daily": 0.0,
    "several times a week": 0.0,
    "before the outbreak, but not now": 1.0,
    "not before the outbreak and not now": 1.0,
    "as often as before the outbreak": 0.0,
    "much less often than before the outbreak": 0.0,
    "a little less often than before the outbreak": 0.0,
    "more often than before the outbreak": 0.0,
}

covid_data = covid_data.replace(dictionary_map)


# create multiindex
# convert personal id to integer
covid_data_update = covid_data.copy()

# check for covid_data data type
print(covid_data_update.dtypes)
covid_data_update["personal_id"] = covid_data["personal_id"].astype(int)
covid_data_update = covid_data_update.reset_index(drop=True)
covid_data_update = covid_data_update.set_index(["personal_id", "month"])
covid_data_update.sort_index(inplace=True)

# calculate the mean of each "scale" in the "covid_data_update" data frame to find the average
# reduction in contact in each wave

# list relevant columns (i.e subcales)
scales = covid_data_update.columns.values[::]
print(scales)

mean_series = covid_data_update.loc[:, scales].mean(axis=0)
average_month = covid_data_update.groupby(
    level=1
).mean()  # average reduction in each wave

average_month["mean_w1_w5"] = average_month.mean(axis=1)


# Import covid19 incidence rate information from "Our World in Data"

confirmed_cases = pd.read_csv("src/original_data/owid-covid-data.csv")

# set index to "iso_code"
confirmed_cases.set_index("iso_code")

# restrict sample

confirmed_cases = confirmed_cases[confirmed_cases["iso_code"] == "NLD"]

# convert variable "new_cases_per_million"
# incidence rate to new cases per hundred thousand variable.

confirmed_cases["new_cases_per_hundred_thousand"] = confirmed_cases[
    "new_cases_per_million"
].apply(lambda x: x * 10)
confirmed_cases["total_cases_per_hundred_thousand"] = confirmed_cases[
    "total_cases_per_million"
].apply(lambda x: x * 10)

confirmed_cases = confirmed_cases.rename(
    columns={
        "new_cases_per_hundred_thousand": "nc_incidence",
        "total_cases_per_hundred_thousand": "tc_incidence",
    }
)

cols_to_keep = [
    "iso_code",
    "continent",
    "location",
    "date",
    "nc_incidence",
    "tc_incidence",
    "total_cases",
    "new_cases",
]
inc = confirmed_cases.reindex(cols_to_keep, axis=1)
inc_update = inc.set_index("iso_code")

# find the monthly average incidence rate

inc["month_year"] = pd.to_datetime(inc["date"]).dt.to_period("M")
incidence_means = inc.groupby(["month_year"], as_index=False).mean()

# Calculate natural logarithm and logarithm with base 10 on nc_incidence' columnn "nc_incidence"
incidence_means["natural_log_nc_incidence"] = np.log(incidence_means["nc_incidence"])
incidence_means["logarithm_base10"] = np.log10(incidence_means["nc_incidence"])
print(incidence_means)


inc["Date"] = pd.to_datetime(inc["date"]).dt.to_period("D")
inc_plt = inc.set_index("Date")
inc_plt_time_series = inc_plt.drop(
    columns=[
        "iso_code",
        "new_cases",
        "total_cases",
        "location",
        "continent",
        "month_year",
        "date",
    ]
)

inc_plt_time_series_2 = inc_plt.drop(
    columns=["iso_code", "location", "continent", "month_year", "date"]
)
