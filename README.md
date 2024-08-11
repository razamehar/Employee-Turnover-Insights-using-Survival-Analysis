# Employee Turnover Insights: Using Survival Analysis

## Project Overview
Conducted a detailed analysis of my former organization's employee turnover for the period 1st Jan, 2022 tp 15th March, 2023, examining historical trends, departmental and band-wise attrition, and tenure-related insights. Utilized predictive analytics from the Employee Engagement Survey 2022, gathered firsthand feedback from former employees, and performed bivariate analyses. Recently incorporated Survival Analysis using Kaplan Meier estimator and COX proportional hazards model to uncover temporal patterns and predictors. The findings informed strategic decisions for improving employee retention.

**Survival Analysis:** A statistical method for analyzing and interpreting the time until an event of interest occurs, such as the duration an employee remains with a company before leaving.

**Kaplan-Meier Estimator:** A non-parametric statistic used in survival analysis to estimate the survival function. It helps visualize the probability of employees remaining with the company over time, often depicted as a survival curve.

**Cox Proportional Hazards Model:** A regression model used in survival analysis to explore the relationship between the time until an event occurs (such as an employee leaving) and one or more predictor variables. It assumes that the effect of these predictors is multiplicative and proportional over time.

## Analysis Steps
1. **Pre-Insights Primer:**
   - Analyzing natue of attrition and looked at attrition through the years.

2. **Core Observations:**
   - Analyzing the attrition with respect to department, band, tenure and reason for turover. Identifying regretable losses.

3. **Predictive Analysis:**
   - Using the insights from the employee engagement survey to predict the vulnerable groups.

4. **Reconnecting with  Former Employees:**
   - Finding out the reaons of turnover from the employee who left the organization before the start of this analysis.

5. **Bivariate Analysis:**
   - Identifying the band group and departments at the higest risk of turnover.

## Survival Analysis
Utilizing  Kaplan-Meier estimator and Cox proportional hazards method.

### Statistical Probability of Employees leaving the Organization
<div>
   <img src="docs/Kaplan_Meier_Survival_Curve.png" alt="Statistical Probability of Employee leaving" style="max-width: 100%";>
</div>

## Usage
### Prerequisites
- Python 3.10.12
- Required Python packages:
  - lifelines 0.27.8

## License
This project is licensed under the Raza Mehar License. See the [LICENSE.md](LICENSE.md) file for details.

## Contact
For any questions or clarifications, please contact Raza Mehar at [raza.mehar@gmail.com].
