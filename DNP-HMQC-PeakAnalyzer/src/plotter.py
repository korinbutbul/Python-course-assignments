import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot_hmqc_spectrum(df, output_image_path='data/hmqc_spectrum.png'):
    """
    Generates a publication-ready 2D scatter plot mimicking an HMQC spectrum.
    Handles dynamic axis limits and prevents crashes if no peaks survived filtering.
    """
    fig, ax = plt.subplots(figsize=(11, 8)) # הגדלנו מעט את הרוחב של הנייר
    sns.set_theme(style="ticks")
    
    # הגדרת פלטת צבעים לפי האזורים הכימיים שסיווגנו
    palette = {'Methyl/Aliphatic': '#1f77b4', 'Aromatic/Amide': '#ff7f0e', 'Other': '#7f7f7f'}
    
    # ציור הפיקים - רק אם הטבלה אינה ריקה
    if not df.empty:
        sns.scatterplot(
            data=df, 
            x='1H (ppm)', 
            y='13C (ppm)', 
            hue='Region', 
            palette=palette, 
            size='Intensity', 
            sizes=(40, 200), 
            alpha=0.8,
            ax=ax
        )
        
        # הוספת תוויות טקסט לכל פיק (Assignment)
        for _, row in df.iterrows():
            if pd.notna(row['Assignment']):
                ax.text(
                    row['1H (ppm)'] + 0.02, # הזזה קלה ב-X שלא יעלה על הנקודה
                    row['13C (ppm)'] + 0.2,  # הזזה קלה ב-Y
                    str(row['Assignment']), 
                    fontsize=8, 
                    alpha=0.8,
                    verticalalignment='bottom'
                )

    # הגנה: אם הסינון השאיר טבלה ריקה, נקבע טווח ברירת מחדל של NMR
    if df.empty:
        print("⚠️ Warning: No peaks survived the filter! Plotting default NMR range.")
        x_max, x_min = 10.0, 0.0
        y_max, y_min = 140.0, 10.0
    else:
        x_max = df['1H (ppm)'].max() + 0.5
        x_min = df['1H (ppm)'].min() - 0.5
        y_max = df['13C (ppm)'].max() + 5.0
        y_min = df['13C (ppm)'].min() - 5.0

    # הגדרת הגבולות והיפוך הצירים
    ax.set_xlim(x_max, x_min)
    ax.set_ylim(y_max, y_min)
    
    # עיצוב מסביב (סטנדרט של מאמרים)
    ax.set_title('DNP-Enhanced 2D HMQC Spectrum (Filtered)', fontsize=14, fontweight='bold', pad=15)
    ax.set_xlabel(r'$^1$H Chemical Shift (ppm)', fontsize=12)
    ax.set_ylabel(r'$^{13}$C Chemical Shift (ppm)', fontsize=12)
    ax.grid(True, linestyle='--', alpha=0.5)
    
    # מיקום המקרא מחוץ לגרף בצורה מוחלטת
    ax.legend(title='Chemical Region', bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0)
    
    # דחיפת הגרף שמאלה כדי לפנות מקום למקרא הצידי
    plt.subplots_adjust(right=0.78)
    
    # שמירה והצגה
    plt.savefig(output_image_path, dpi=300)
    plt.show()
    print(f"Spectrum plot saved successfully to {output_image_path}")