import pandas as pd
import numpy as np

def load_and_filter_peaks(file_path, std_multiplier=2.0):
    """
    Loads NMR peak list and filters out baseline noise using an adaptive threshold.
    """
    # טעינת הנתונים (תומך בפסיק או בטאב בהתאם לייצוא של הטופספין)
    try:
        df = pd.read_csv(file_path)
    except Exception:
        df = pd.read_csv(file_path, sep=r'\s+') # במקרה שהקובץ מופרד ברווחים/טאבים
        
    # ניקוי שמות העמודות מרווחים מיותרים
    df.columns = df.columns.str.strip()
    
    # חישוב סף סינון אדפטיבי המבוסס על עוצמת הסיגנל (Intensity)
    mean_intensity = df['Intensity'].mean()
    std_intensity = df['Intensity'].std()
    threshold = mean_intensity + (std_multiplier * std_intensity)
    
    # סינון הפיקים שמעל הסף
    filtered_df = df[df['Intensity'] >= threshold].copy()
    
    print(self_report := f"Loaded {len(df)} peaks. Retained {len(filtered_df)} peaks above threshold ({threshold:.2e}).")
    return filtered_df

def categorize_regions(df, h_col='1H (ppm)'):
    """
    Categorizes peaks into chemical shift regions (e.g., Methyl/Aliphatic vs Aromatic).
    """
    def assign_region(h_ppm):
        if h_ppm < 3.0:
            return 'Methyl/Aliphatic'
        elif 6.0 <= h_ppm <= 9.5:
            return 'Aromatic/Amide'
        else:
            return 'Other'
            
    df['Region'] = df[h_col].apply(assign_region)
    return df