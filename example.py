import pandas as pd
from iot_leontief_python.multipliers import *

# Read in example data
df = pd.read_csv('data/iot_example.csv')

# Split datasets
output, sectors, disposable_income, hh_demand, io_matrix = get_components(
        df,
        "Total intermediate use",
        "Total output at basic prices",
        "Industry Purchases ↓  Industry Sales →",
        "Households final consumption expenditure",
        "Compensation of employees"
    )

# Get Type 1 and Type 2 Multipliers
mults_t1, mults_mat_t1 = t1_multipliers(io_matrix, output)
mults_t2, mults_mat_t2 = t2_multipliers(io_matrix, output, hh_demand, disposable_income)

# Model a new scenario
new_scenario_t1 = model_scenario(mults_mat_t1, pd.Series([0, 1, 0, 0]))
new_scenario_t2 = model_scenario(mults_mat_t2, pd.Series([0, 1, 0, 0]))

print('Type 1 Scenario')
print(new_scenario_t1)

print('Type 2 Scenario')
print(new_scenario_t2)