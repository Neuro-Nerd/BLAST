import re

def replace(DNA, substitutions):
    substrings = sorted(substitutions, key=len, reverse=True)
    regex = re.compile('|'.join(map(re.escape, substrings)))
    return regex.sub(lambda match: substitutions[match.group(0)], DNA)

DNA = input("Insert DNA Sequence 3' to 5': ")
if not (("A") or ("T") or ("G") or ("C") in DNA):
    print ("Not DNA")

def transcription(DNA):
    substitutions = {"A": "U", "T": "A", "G": "C", "C": "G"}
    RNA = replace(DNA, substitutions)
    return (RNA)
RNA = transcription(DNA)

start = RNA.find("AUG")
n = 3
codon = [RNA[i:i + n] for i in range(int(start), len(RNA), n)]
codons = " ".join(codon)

def find_frame(codons):
    stop = codons.find("UAG" or "UGA" or "UAA")
    if int(stop) == -1:
        frame = codons[0:len(codons)]
        return frame
    else:
        frame = codons[0:int(stop + 4)]
        return frame
frame = find_frame(codons)

def translation(frame):
    substitutions = {"GCU": "Ala", "GCC": "Ala", "GCA": "Ala","GCG": "Ala", "UUA": "Leu", "UUG": "Leu", "CUU": "Leu", "CUC": "Leu", "CUA": "Leu", "CUG": "Leu", "CGU": "Arg", "CGC": "Arg", "CGA": "Arg", "CGG": "Arg", "AGA": "Arg", "AGG": "Arg", "AAA": "Lys", "AAG": "Lys", "AAU": "Asn", "AAC": "Asn", "AUG": "Met", "GAU": "Asp", "GAC": "Asp", "UUU": "Phe", "UUC": "Phe", "UGU": "Cys", "UGC": "Cys", "CCU": "Pro", "CCC": "Pro", "CCA": "Pro", "CCG": "Pro", "CAA": "Gln", "CAG": "Gln", "UCU": "Ser", "UCC": "Ser", "UCA": "Ser", "UCG": "Ser", "AGU" : "Ser", "AGC": "Ser", "GAA": "Glu", "GAG": "Glu", "ACU": "Thr", "ACC" : "Thr", "ACA" : "Thr", "ACG": "Thr", "GGU": "Gly", "GGC": "Gly", "GGA": "Gly", "GGG": "Gly", "UGG": "Trp", "CAU": "His", "CAC": "His", "UAU": "Tyr", "UAC": "Tyr", "AUU": "Ile", "AUC": "Ile", "AUA": "Ile", "GUU": "Val", "GUC": "Val", "GUA": "Val", "GUG": "Val", "UAG": "STOP", "UGA": "STOP", "UAA": "STOP"}
    protein = replace(frame, substitutions)
    return (protein)
protein = translation(frame)

def complimentary_strand(DNA):
    substitutions = {"A": "T", "T": "A", "G": "C", "C": "G"}
    compliment = replace(DNA, substitutions)[::-1]
    return (compliment)
compliment = complimentary_strand(DNA)
compliment_RNA = transcription(compliment)

compliment_start = compliment_RNA.find("AUG")
n = 3
compliment_codon = [compliment_RNA[i:i + n] for i in range(int(compliment_start), len(compliment_RNA), n)]
compliment_codons = " ".join(compliment_codon)

def find_compliment_frame(compliment_codons):
    compliment_stop = compliment_codons.find("UAG" or "UGA" or "UAA")
    if int(compliment_stop) == -1:
        compliment_frame = compliment_codons[0:len(compliment_codons)]
        return compliment_frame
    else:
        compliment_frame = codons[0:int(compliment_stop + 4)]
        return compliment_frame
compliment_frame = find_compliment_frame(compliment_codons)

def compliment_translation(compliment_frame):
    substitutions = {"GCU": "Ala", "GCC": "Ala", "GCA": "Ala","GCG": "Ala", "UUA": "Leu", "UUG": "Leu", "CUU": "Leu", "CUC": "Leu", "CUA": "Leu", "CUG": "Leu", "CGU": "Arg", "CGC": "Arg", "CGA": "Arg", "CGG": "Arg", "AGA": "Arg", "AGG": "Arg", "AAA": "Lys", "AAG": "Lys", "AAU": "Asn", "AAC": "Asn", "AUG": "Met", "GAU": "Asp", "GAC": "Asp", "UUU": "Phe", "UUC": "Phe", "UGU": "Cys", "UGC": "Cys", "CCU": "Pro", "CCC": "Pro", "CCA": "Pro", "CCG": "Pro", "CAA": "Gln", "CAG": "Gln", "UCU": "Ser", "UCC": "Ser", "UCA": "Ser", "UCG": "Ser", "AGU" : "Ser", "AGC": "Ser", "GAA": "Glu", "GAG": "Glu", "ACU": "Thr", "ACC" : "Thr", "ACA" : "Thr", "ACG": "Thr", "GGU": "Gly", "GGC": "Gly", "GGA": "Gly", "GGG": "Gly", "UGG": "Trp", "CAU": "His", "CAC": "His", "UAU": "Tyr", "UAC": "Tyr", "AUU": "Ile", "AUC": "Ile", "AUA": "Ile", "GUU": "Val", "GUC": "Val", "GUA": "Val", "GUG": "Val", "UAG": "STOP", "UGA": "STOP", "UAA": "STOP"}
    compliment_protein = replace(compliment_frame, substitutions)
    return (compliment_protein)
compliment_protein = compliment_translation(compliment_frame)

if ("U") in DNA:
    print(("RNA Strand: ") + ("Not DNA"))
elif not (("A") or ("T") or ("G") or ("C") in DNA):
    print (("RNA Strand: ") + ("Not DNA"))
else:
    print (("RNA Strand: ") + (RNA))

if ("U") in DNA:
    print(("Protein: ") + ("Not DNA"))
elif not (("A") or ("T") or ("G") or ("C") in DNA):
    print (("Protein: ") + ("Not DNA"))
elif start == -1:
    print (("Protein: ") + ("No Start Codon"))
else:
    print (("Protein: ") + (protein))

if ("U") in DNA:
    print(("DNA Compliment Strand (3' to 5'): ") + ("Not DNA"))
elif not (("A") or ("T") or ("G") or ("C") in DNA):
    print (("DNA Compliment Strand (3' to 5'): ") + ("Not DNA"))
else:
    print (("DNA Compliment Strand (3' to 5'): ") + (complimentary_strand(DNA)))

if ("U") in DNA:
    print (("RNA of Compliment Strand: ") + ("Not DNA"))
elif not (("A") or ("T") or ("G") or ("C") in DNA):
    print (("RNA of Compliment Strand: ") + ("Not DNA"))
else:
    print (("RNA of Compliment Strand: ") + (transcription(complimentary_strand(DNA))))

if ("U") in DNA:
    print(("Protein of Complimentary Strand: ") + ("Not DNA"))
elif not (("A") or ("T") or ("G") or ("C") in DNA):
    print (("Protein of Complimentary Strand: ") + ("Not DNA"))
elif compliment_start == -1:
    print (("Protein of Complimentary Strand: ") + ("No Start Codon"))
else:
    print (("Protein of Complimentary Strand: ") + (compliment_protein))