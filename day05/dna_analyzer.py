def read_fasta(file_path):
    """קריאת רצף ה-DNA מתוך קובץ ה-FASTA תוך התעלמות משורת הכותרת"""
    sequence = ""
    with open(file_path, 'r') as file:
        for line in file:
            if not line.startswith('>'):
                sequence += line.strip()
    return sequence

def calculate_gc_content(sequence):
    """חישוב אחוז ה-G וה-C ברצף"""
    if not sequence:
        return 0.0
    gc_count = sequence.upper().count('G') + sequence.upper().count('C')
    return (gc_count / len(sequence)) * 100

def main():
    input_file = "sample.fasta"
    try:
        dna_seq = read_fasta(input_file)
        gc_percentage = calculate_gc_content(dna_seq)
        
        print(f"--- DNA Analysis Results for {input_file} ---")
        print(f"Total Length: {len(dna_seq)} base pairs")
        print(f"GC Content: {gc_percentage:.2f}%")
        
    except FileNotFoundError:
        print(f"Error: The file {input_file} was not found.")

if __name__ == "__main__":
    main()