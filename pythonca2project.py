import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
df=pd.read_excel("C:\\Users\\HP\\Downloads\\employee_data.xlsx")

print(df)
print(df.head())
print(df.tail())
print(df.describe())
print(df.info())
print(df.columns)
print(df.isnull().sum())
print(df.isnull().sum().sum())
df.dropna()

# creating a bar chart
# Analyze Department-wise Employee Count
plt.figure(figsize=(8, 6))
sns.countplot(data=df, x='Department', hue='Department', dodge=False, order=df['Department'].value_counts().index, palette='Set2')
plt.legend([],[], frameon=False) # hides the redundant legend
plt.title('Employee Count per Department')
plt.xlabel('Department')
plt.ylabel('Number of Employees')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# creating a Boxplot
# Location-wise Salary Comparison
plt.figure(figsize=(8, 6))
sns.boxplot(data=df, x='Location', y='Salary', hue='Location', palette='pastel', legend=False)
plt.title('Location-wise Salary Comparison')
plt.xlabel('Location')
plt.ylabel('Salary')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# creating a pie chart
department_counts = df['Department'].value_counts()
# Plot the pie chart
plt.figure(figsize=(8, 6))
colors = plt.cm.Pastel1(range(len(department_counts)))
plt.pie(department_counts, labels=department_counts.index, autopct='%1.1f%%', colors=colors, startangle=140)
plt.title(label="Pie Chart - Distribution of Employees Across Departments", fontsize=14)
plt.axis('equal')  # Keeps pie chart as a circle
plt.tight_layout()
plt.show()

# creating a line graph
df['Joining Date'] = pd.to_datetime(df['Joining Date'])
# Extract year from 'Joining Date'
df['Joining Year'] = df['Joining Date'].dt.year
# Calculate average salary by year
avg_salary_by_year = df.groupby('Joining Year')['Salary'].mean().reset_index()
# Plotting the line chart
plt.figure(figsize=(10, 6))
plt.plot(avg_salary_by_year['Joining Year'], avg_salary_by_year['Salary'],
         marker='o', linestyle='-', color='royalblue', linewidth=2)
plt.title(label='Average Salary per Year', fontsize=16, fontweight='bold')
plt.xlabel('Joining Year', fontsize=12)
plt.ylabel('Average Salary', fontsize=12)
plt.grid(visible=True, linestyle='--', alpha=0.5)
plt.xticks(avg_salary_by_year['Joining Year'],rotation=45)
plt.show()


# creating a heat map
df['Joining Date'] = pd.to_datetime(df['Joining Date'], errors='coerce')
# Extract year as a separate numeric feature
df['Joining Year'] = df['Joining Date'].dt.year
# Filter numeric columns only
numeric_df = df.select_dtypes(include='number')
# Compute correlation matrix
correlation_matrix = numeric_df.corr()
# Plot the heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap="coolwarm", linewidths=0.5)
plt.title(label="Correlation Heatmap of Numeric Features", fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()
