import os
from src.analyzer import load_and_filter_peaks, categorize_regions
from src.plotter import plot_hmqc_spectrum

def main():
    # נתיבים לקבצים (נניח שיש קובץ דוגמה בתיקיית data)
    input_file = 'data/raw_peaks.csv'
    output_csv = 'data/filtered_peaks.csv'
    output_plot = 'data/hmqc_spectrum.png'
    
    # יצירת תיקיית דאטה אם היא לא קיימת
    os.makedirs('data', exist_ok=True)
    
    # בדיקה אם קובץ הקלט קיים, אם לא - ניצור אחד פיקטיבי לבדיקה ראשונית
    if not os.path.exists(input_file):
        print(f"[{input_file}] not found. Creating a dummy NMR peak list for testing...")
        create_dummy_data(input_file)

    print("--- Starting DNP-HMQC-PeakAnalyzer ---")
    
    # 1. טעינה וסינון רעשים (Threshold אדפטיבי)
    filtered_peaks = load_and_filter_peaks(input_file, std_multiplier=0.1)
    
    # 2. סיווג לפי אזורים
    processed_peaks = categorize_regions(filtered_peaks)
    
    # 3. שמירת הנתונים הנקיים ל-CSV חדש
    processed_peaks.to_csv(output_csv, index=False)
    print(f"Filtered peak list saved to {output_csv}")
    
    # 4. הפקת הגרף
    plot_hmqc_spectrum(processed_peaks, output_plot)
    
    print("--- Processing Complete! ---")

def create_dummy_data(file_path):
    """ייצור נתונים פיקטיביים רק כדי שאפשר יהיה להריץ ולראות שהכל עובד"""
    import pandas as pd
    dummy_data = {
        'Assignment': ['Ala12', 'Gly15', 'Leu23', 'Val34', 'Phe50', 'Noise1', 'Noise2'],
        '1H (ppm)': [1.2, 3.8, 0.8, 0.9, 7.2, 4.5, 2.1],
        '13C (ppm)': [20.5, 43.2, 22.1, 18.9, 135.4, 60.1, 12.3],
        'Intensity': [500000, 450000, 600000, 550000, 300000, 15000, 8000]
    }
    pd.DataFrame(dummy_data).to_csv(file_path, index=False)

if __name__ == '__main__':
    main()