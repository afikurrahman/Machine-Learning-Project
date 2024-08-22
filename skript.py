import os
import csv

parent_folder = r'C:\Users\User\Desktop\A python\BAutomation\Afik ML task\dataset\data\data'
output_csv = 'categorized_resumes.csv'
pdf_files = []

for subfolder in ['ACCOUNTANT', 'ADVOCATE', 'AGRICULTURE','APPAREL', 'ARTS', 'AUTOMOBILE','AVIATION', 'BANKING', 'BPO', 'BUSINESS-DEVELOPMENT', 'CHEF', 'CONSTRUCTION', 'CONSULTANT', 'DESIGNER', 'DIGITAL-MEDIA', 'ENGINEERING', 'FINANCE', 'FITNESS', 'HEALTHCARE', 'HR', 'INFORMATION-TECHNOLOGY','PUBLIC-RELATIONS','SALES','TEACHER']:
    folder_path = os.path.join(parent_folder, subfolder)    
  
    if os.path.exists(folder_path):
      
        for file_name in os.listdir(folder_path):

            if file_name.endswith('.pdf'):
                
                pdf_files.append(os.path.splitext(file_name)[0])
    else:
        print(f"Folder {folder_path} does not exist")


with open(output_csv, 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['PDF File Name'])  
    for file_name in pdf_files:
        writer.writerow([file_name])

print(f"CSV file '{output_csv}' created with {len(pdf_files)} PDF file names (without .pdf extension).")

df2 = pd.read_csv("resumes_directory.csv")
df2

resume_numbers = []
resume_categories = []

for i in range(len(df2)): 
    ID_to_find = df2.iloc[i]['PDF File Name']  
    resume_str_value = df.loc[df['ID'] == ID_to_find, 'Resume_str'].values[0]
    cleaned_resume = clean_text(resume_str_value)   
    input_features = tfidf.transform([cleaned_resume])   
    prediction_id = clf.predict(input_features)[0]
    resume_numbers.append(ID_to_find)
    resume_categories.append(prediction_id)
results_df = pd.DataFrame({
    'Filename': resume_numbers,
    'Category': resume_categories
})

results_df.to_csv('categorized_resumes.csv', index=False)

print("File saved as resume_predictions.csv")