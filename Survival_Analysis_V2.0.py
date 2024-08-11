''' title: "Pre-process the merged dataset"
    author: "Raza Mehar"
    date: "2024-03-02"
    description: Handling missing and duplicate values. Bivariate analyses. Survival analysis'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from lifelines import KaplanMeierFitter, CoxPHFitter

data = pd.read_csv("Manning.csv")

#data.set_index("Person ID", inplace=True)

print("The initial rows of the data are:\n", data.head())
print(data.shape)

# Converting data features to Pandas data type and creating Survival Time feature
data["Start Date"] = pd.to_datetime(data["Start Date"], infer_datetime_format=True, errors="coerce")
data["End Date"] = pd.to_datetime(data["End Date"], infer_datetime_format=True, errors="coerce")
data["Survival Time"] = (data["End Date"] - data["Start Date"]).dt.days
data["Survival Time"] = data["Survival Time"] / 30

# Checking and handling duplicate and missing values
print("\nThe duplicate values are:", data.duplicated().sum())
print("\nThe missing values are:\n", data.isna().sum())

print("The data types of the features are:\n", data.dtypes)

kp = KaplanMeierFitter()
kp.fit(durations=data["Survival Time"], event_observed=data["Left"], label="Kaplan-Meier Survival Curve")

kp.plot_survival_function(linewidth=2, figsize=(12, 6))
plt.xlabel("Time (months)")
plt.xticks(np.arange(0, max(data["Survival Time"]), 30))
plt.ylabel("Survival Probability")
#plt.show()

tenure_3 = data[data["Survival Time"] < 36]
tenure_5 = data[(data["Survival Time"] >= 36) & (data["Survival Time"] < 60)]
tenure_10 = data[(data["Survival Time"] >= 60) & (data["Survival Time"] < 120)]
tenure_10above = data[data["Survival Time"] >= 120]
m1_m2 = data[(data["Band"] == "M1") | (data["Band"] == "M2")]
m3 = data[(data["Band"] == "M3")]
p3_p5 = data[(data["Band"] == "P3") | (data["Band"] == "P4") | (data["Band"] == "P5")]
p6_p7 = data[(data["Band"] == "P6") | (data["Band"] == "P7") | (data["Band"] == "T3")]

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12, 8), sharey=True, gridspec_kw={'hspace': 0.5})
tenure_3.groupby("Left")["Survival Time"].plot(kind="hist", ax=ax1, title="0 - 3")
tenure_5.groupby("Left")["Survival Time"].plot(kind="hist", ax=ax2, title="3 - 5")
tenure_10.groupby("Left")["Survival Time"].plot(kind="hist", ax=ax3, title="5 - 10")
tenure_10above.groupby("Left")["Survival Time"].plot(kind="hist", ax=ax4, title="10+")
plt.xticks(np.arange(0, max(data["Survival Time"]), 30))
ax1.set_xlabel("Time (months)")
ax2.set_xlabel("Time (months)")
ax3.set_xlabel("Time (months)")
ax4.set_xlabel("Time (months)")
#plt.show()

ax = plt.axes()
kp.fit(durations=tenure_3["Survival Time"], event_observed=tenure_3["Left"], label="0 - 3")
kp.plot_survival_function(linewidth=2, figsize=(12, 6), ax=ax)
kp.fit(durations=tenure_5["Survival Time"], event_observed=tenure_5["Left"], label="3 - 5")
kp.plot_survival_function(linewidth=2, figsize=(12, 6), ax=ax)
kp.fit(durations=tenure_10["Survival Time"], event_observed=tenure_10["Left"], label="5 - 10")
kp.plot_survival_function(linewidth=2, figsize=(12, 6), ax=ax)
kp.fit(durations=tenure_10above["Survival Time"], event_observed=tenure_10above["Left"], label="10+")
kp.plot_survival_function(linewidth=2, figsize=(12, 6), ax=ax)
plt.xlabel("Time (months)")
plt.xticks(np.arange(0, max(data["Survival Time"]), 30))
plt.ylabel("Survival Probability")
#plt.show()

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12, 8), sharey=True, gridspec_kw={'hspace': 0.5})
m1_m2.groupby("Left")["Survival Time"].plot(kind="hist", ax=ax1, title="M1-M2")
m3.groupby("Left")["Survival Time"].plot(kind="hist", ax=ax2, title="M3")
p3_p5.groupby("Left")["Survival Time"].plot(kind="hist", ax=ax3, title="P3-P5")
p6_p7.groupby("Left")["Survival Time"].plot(kind="hist", ax=ax4, title="P6-P7")
plt.xticks(np.arange(0, max(data["Survival Time"]), 30))
ax1.legend(labels=["Not churned", "Churned"])
ax1.set_xlabel("Time (months)")
ax2.set_xlabel("Time (months)")
#plt.show()

ax = plt.axes()
kp.fit(durations=m1_m2["Survival Time"], event_observed=m1_m2["Left"], label="M1-M2")
kp.plot_survival_function(linewidth=2, figsize=(12, 6), ax=ax)
kp.fit(durations=m3["Survival Time"], event_observed=m3["Left"], label="M3")
kp.plot_survival_function(linewidth=2, figsize=(12, 6), ax=ax)
kp.fit(durations=p3_p5["Survival Time"], event_observed=p3_p5["Left"], label="P3-P5")
kp.plot_survival_function(linewidth=2, figsize=(12, 6), ax=ax)
kp.fit(durations=p6_p7["Survival Time"], event_observed=p6_p7["Left"], label="P6-P7")
kp.plot_survival_function(linewidth=2, figsize=(12, 6), ax=ax)
plt.xlabel("Time (months)")
plt.xticks(np.arange(0, max(data["Survival Time"]), 30))
plt.ylabel("Survival Probability")
#plt.show()

categorical_columns = ['Gender', 'Grade']
non_categorical_columns = ['Survival Time', 'Left']

# Create a DataFrame with just categorical columns
data_categorical = data[categorical_columns]

# Create a DataFrame with the remaining columns
data_non_categorical = data[non_categorical_columns]

# Perform one-hot encoding on categorical columns
data_categorical_encoded = pd.get_dummies(data_categorical, drop_first=True)

# Check the result
print(data_categorical_encoded.head())

# Concatenate the encoded categorical columns with the non-categorical columns
data_encoded = pd.concat([data_non_categorical, data_categorical_encoded], axis=1)

# Check the result
print(data_encoded.head())

# Initialize the Cox Proportional Hazards model
cph = CoxPHFitter()

# Fit the model with the encoded data
cph.fit(data_encoded, duration_col='Survival Time', event_col='Left')

# Print the summary of the model
cph.print_summary()



data1 = data[data["Left"] == 1]
fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, figsize=(14, 8))
sns.boxplot(data=data1, x="Band", y="Survival Time", ax=ax1)
ax1.set_ylabel("")
ax1.set_title("Tenure Distribution by Band for Employees Who Have Left")

sns.boxplot(data=data1, x="Department", y="Survival Time", ax=ax2)
ax2.set_ylabel("")  # Set y-axis label
ax2.set_title("Tenure Distribution by Department for Employees Who Have Left")
plt.xticks(rotation=45)
plt.ylabel("")
plt.tight_layout()
#plt.show()



