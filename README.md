# Employee Turnover Insights: Using Survival Analysis

## Project Overview
The analysis encompassed a review of historical turnover trends, departmental and job band-specific attrition rates, and factors related to employee tenure. I employed predictive analytics derived from the Employee Engagement Survey and integrated direct feedback from former employees. Additionally, the analysis incorporated bivariate analyses and advanced statistical techniques, including Survival Analysis utilizing the Kaplan-Meier estimator and the Cox proportional hazards model.

### Methodologies Used:

- **Predictive Analytics:** Analyzed survey data to forecast turnover trends.
- **Survival Analysis:** Applied Kaplan-Meier estimator and COX proportional hazards model to understand temporal patterns and predictors of turnover.

### Description of Methodolies
- **Survival Analysis:** A statistical method for analyzing and interpreting the time until an event of interest occurs, such as the duration an employee remains with a company before leaving.
- **Kaplan-Meier Estimator:** A non-parametric statistic used in survival analysis to estimate the survival function. It helps visualize the probability of employees remaining with the company over time, often depicted as a survival curve.
- **Cox Proportional Hazards Model:** A regression model used in survival analysis to explore the relationship between the time until an event occurs (such as an employee leaving) and one or more predictor variables. It assumes that the effect of these predictors is multiplicative and proportional over time.

These methodologies can help identify **high-risk groups** by analyzing survival curves. This allows you to determine which employee groups—such as those categorized by department, tenure, or job band—have higher or lower survival rates, indicating their respective risks of turnover.

## Predictive Analysis Steps
1. **Pre-Insights Primer:**
   - Examine the nature of attrition and review attrition trends over the years.

2. **Core Observations:**
   - Analyze attrition with respect to departments, job bands, tenure, and reasons for turnover. Identify regrettable losses.

3. **Predictive Analysis:**
   - Leverage insights from employee engagement surveys to predict vulnerable groups.

4. **Reconnecting with  Former Employees:**
   - Investigate the reasons for turnover from employees who left before the commencement of this analysis.

5. **Bivariate Analysis:**
   - Identify job bands and departments with the highest risk of turnover.

## Survival Analysis
Utilizing  Kaplan-Meier estimator and Cox proportional hazards method.

### Statistical Probability of Employees leaving the Organization
<div>
   <img src="docs/Kaplan_Meier_Survival_Curve.png" alt="Statistical Probability of Employee leaving" style="max-width: 100%";>
</div>

## Conclusion
By anonymizing the data and combining traditional approaches to employee attrition with advanced statistical methods, such as Survival Analysis and predictive analytics, I hope to encourage more HR practitioners to incorporate statistical analysis and machine learning into their retention strategies. This approach can provide deeper, data-driven insights and foster more effective solutions for reducing turnover and improving workplace environments.

## Disclaimer
Please note that all data presented in this analysis has been completely anonymized to ensure the confidentiality of my former organization and its employees. The insights shared are for educational and learning purposes only.

## Usage
### Prerequisites
- Python 3.10.12
- Required Python packages:
  - lifelines 0.27.8

## License
This project is licensed under the Raza Mehar License. See the [LICENSE.md](LICENSE.md) file for details.

## Contact
For any questions or clarifications, please contact Raza Mehar at [raza.mehar@gmail.com].
