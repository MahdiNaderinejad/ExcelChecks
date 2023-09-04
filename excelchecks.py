import pandas as pd

def excelchecks():
    
    # Change file names and headers
    experiments_xlsx = 'experiment.xlsx'
    real_xlsx = 'real.xlsx'
    header_exp = 'Value'
    header_real = 'Value'

    # Open .xlsx files
    df_exp = pd.read_excel(experiments_xlsx)
    df_real = pd.read_excel(real_xlsx)

    # Create a new DataFrame to store the result
    result_df = pd.DataFrame(columns=[header_exp, 'Exists'])

    # Iterate through each value in 'a.xlsx'
    for _, row_exp in df_exp.iterrows():
        print(row_exp)
        value_exp = row_exp[header_exp]

        # Check if the value exists in 'b.xlsx'
        if value_exp in df_real[header_real].values:
            result = 1
        else:
            result = 0

        # Append the result to the result DataFrame
        result_df = result_df._append({header_exp: value_exp, 'Exists': result}, ignore_index=True)

    # Save the result to a new Excel file
    result_df.to_excel(experiments_xlsx, index=False)

if __name__ == '__main__':
    excelchecks()
