# Create calculate_insurance_cost() function below:
def calculate_insurance_cost(age, sex, bmi, num_of_children, smoker, name):
  estimated_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
  return estimated_cost, name

# Initial variables for Maria
age = 28
sex = 0
bmi = 26.2
num_of_children = 3
smoker = 0
name = "Maria"

# Estimate Maria's insurance cost
maria_insurance_cost = calculate_insurance_cost(age, sex, bmi, num_of_children, smoker, name)

print("The estimated insurance cost for " + name + " is " + str(maria_insurance_cost) + " dollars.")

# Initial variables for Omar
age = 35
sex = 1
bmi = 22.2
num_of_children = 0
smoker = 1
name = "Omar"

# Estimate Omar's insurance cost
omar_insurance_cost = calculate_insurance_cost(age, sex, bmi, num_of_children, smoker, name)


print("The estimated insurance cost for " + name + " is " + str(omar_insurance_cost) + " dollars.")
