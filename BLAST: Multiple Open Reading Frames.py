DNA = input("Insert DNA Sequence 3' to 5': ").upper()
list_DNA = (list(DNA))
#transcribes DNA ( 3' to 5') to RNA (5' to 3')
def transcribe(list_DNA):
    list_RNA = []
    for n in range(0,len(list_DNA)):
        if ("A") in list_DNA[n]:
            list_RNA += "U"
        elif ("T") in list_DNA[n]:
            list_RNA += "A"
        elif ("G") in list_DNA[n]:
            list_RNA += "C"
        elif ("C") in list_DNA[n]:
            list_RNA += "G"
        else:
            list_RNA += "?"
    return list_RNA
list_RNA = (transcribe(list_DNA))
RNA = ("").join(list_RNA)
# prints out puts
print ("DNA 3' to 5': " + DNA)
print ("RNA 5' to 3': " + RNA)
# protein translation only initiates if there is a start codon (AUG)
if RNA.find("AUG")== -1:
    print (("Protein: ") + ("No Start Codon"))
#this finds multiple start codons
start = -1
#finds multiple start codons, splices the sequence after a stop codon, translates each string
while True:
    start = RNA.find("AUG", start + 1)
    # if no start, don't translate
    if start == -1: break
    # groups three RNA monomers into a single list item after a start codon
    n = 3
    codon = [RNA[i:i + n] for i in range(int(start), len(RNA), n)]
    #joins each item together with a space to be easily translated
    codons = " ".join(codon)
    # finds stop codon and splices off string after stop codon
    def find_frame(codons):
        stop = codons.find("UAG" or "UGA" or "UAA")
        if int(stop) == -1:
            frame = codons[0:len(codons)]
            return frame
        else:
            frame = codons[0:int(stop+4)]
            return frame
    frame = find_frame(codons)
    # converts string to list
    list_frame = frame.split()
    # translates each open reading frame to a new AA sequence
    def translate(list_frame):
        list_protein = []
        for n in range(0, len(list_frame)):
            if "GCU" in list_frame[n] or "GCC" in list_frame[n] or "GCA" in list_frame[n] or "GCG" in list_frame[n]:
                list_protein.append("Ala")
            elif "UUA" in list_frame[n] or "UUG" in list_frame[n] or "CUU" in list_frame[n] or "CUC" in list_frame[n] or "CUA" in list_frame[n] or "CUG" in list_frame[n]:
                list_protein.append("Leu")
            elif "CGU" in list_frame[n] or "CGC" in list_frame[n] or "CGA" in list_frame[n] or "CGG" in list_frame[n] or "AGA" in list_frame[n] or "AGG" in list_frame[n]:
                list_protein.append("Arg")
            elif "AAA" in list_frame[n] or "AAG" in list_frame[n]:
                list_protein.append("Lys")
            elif "AAU" in list_frame[n] or "AAC" in list_frame[n]:
                list_protein.append("Asn")
            elif "AUG" in list_frame[n] in list_frame[n]:
                list_protein.append("Met")
            elif "GAU" in list_frame[n] or "GAC" in list_frame[n]:
                list_protein.append("Asp")
            elif "UUU" in list_frame[n] or "UUC" in list_frame[n]:
                list_protein.append("Phe")
            elif "UGU" in list_frame[n] or "UGC" in list_frame[n]:
                list_protein.append("Cys")
            elif "CCU" in list_frame[n] or "CCC" in list_frame[n] or "CCA" in list_frame[n] or "CCG" in list_frame[n]:
                list_protein.append("Pro")
            elif "CAA" in list_frame[n] or "CAG" in list_frame[n]:
                list_protein.append("Gln")
            elif "UCU" in list_frame[n] or "UCC" in list_frame[n] or "UCA" in list_frame[n] or "UCG" in list_frame[n] or "AGU" in list_frame[n] or "AGC" in list_frame[n]:
                list_protein.append("Ser")
            elif "GAA" in list_frame[n] or "GAG" in list_frame[n]:
                list_protein.append("Glu")
            elif "ACU" in list_frame[n] or "ACC" in list_frame[n] or "ACA" in list_frame[n] or "ACG" in list_frame[n]:
                list_protein.append("Thr")
            elif "GGU" in list_frame[n] or "GGC" in list_frame[n] or "GGA" in list_frame[n] or "GGG" in list_frame[n]:
                list_protein.append("Gly")
            elif "UGG" in list_frame[n]:
                list_protein.append("Trp")
            elif "CAU"  in list_frame[n]or "CAC" in list_frame[n]:
                list_protein.append("His")
            elif "UAU" in list_frame[n] or "UAC" in list_frame[n]:
                list_protein.append("Tyr")
            elif "AUU" in list_frame[n] or "AUC" in list_frame[n] or "AUA" in list_frame[n]:
                list_protein.append("Ile")
            elif "GUU" in list_frame[n] or "GUC" in list_frame[n] or "GUA" in list_frame[n] or "GUG" in list_frame[n]:
                list_protein.append("Val")
            elif "UAG" in list_frame[n] or "UGA" in list_frame[n] or "UAA" in list_frame[n]:
                list_protein.append("STOP")
            else:
                list_protein.append("???")
        return list_protein
    list_protein = translate(list_frame)
    protein = (" ").join(list_protein)
    print ("Protein: " + (protein))


# compliment strand is the inverse of the original strand, and DNA is read 3' to 5'
compliment = list(DNA[::-1])
# creates the compliment strand as a list
def complimentary_strand(compliment):
    list_compliment_DNA = []
    for n in range(0, len(compliment)):
        if ("A") in compliment[n]:
            list_compliment_DNA += "T"
        elif ("T") in compliment[n]:
            list_compliment_DNA += "A"
        elif ("G") in compliment[n]:
            list_compliment_DNA += "C"
        elif ("C") in compliment[n]:
            list_compliment_DNA += "G"
        else:
            list_compliment_DNA += "?"
    return list_compliment_DNA
list_compliment_DNA = (complimentary_strand(compliment))
# transcription is the same process for both strings of DNA
list_compliment_RNA = (transcribe(list_compliment_DNA))
# returns DNA and RNA to string format
compliment_RNA = ("").join(list_compliment_RNA)
compliment_DNA = ("").join(list_compliment_DNA)
# prints strings
print ("DNA Compliment Strand (3' to 5'): " + compliment_DNA)
print ("RNA of Compliment Strand (5' to 3'): " + compliment_RNA)
if compliment_RNA.find("AUG")== -1:
    print ("Protein of Complimentary Strand: " + "No Start Codon")

# I rewrote my code from above for the compliment strand because the compliment RNA has different positions for start codons and end codons
while True:
    compliment_start = compliment_RNA.find("AUG", start + 1)
    if compliment_start == -1: break
    n = 3
    compliment_codon = [compliment_RNA[i:i + n] for i in range(int(compliment_start), len(compliment_RNA), n)]
    compliment_codons = " ".join(compliment_codon)
    def compliment_find_frame(compliment_codons):
        compliment_stop = compliment_codons.find("UAG" or "UGA" or "UAA")
        if int(compliment_stop) == -1:
            compliment_frame = compliment_codons[0:len(compliment_codons)]
            return compliment_frame
        else:
            compliment_frame = compliment_codons[0:int(compliment_stop+4)]
            return compliment_frame
    compliment_frame = compliment_find_frame(compliment_codons)
    compliment_list_frame = compliment_frame.split()
    def compliment_translate(list_frame):
        list_protein = []
        for n in range(0, len(list_frame)):
            if "GCU" in list_frame[n] or "GCC" in list_frame[n] or "GCA" in list_frame[n] or "GCG" in list_frame[n]:
                list_protein.append("Ala")
            elif "UUA" in list_frame[n] or "UUG" in list_frame[n] or "CUU" in list_frame[n] or "CUC" in list_frame[n] or "CUA" in list_frame[n] or "CUG" in list_frame[n]:
                list_protein.append("Leu")
            elif "CGU" in list_frame[n] or "CGC" in list_frame[n] or "CGA" in list_frame[n] or "CGG" in list_frame[n] or "AGA" in list_frame[n] or "AGG" in list_frame[n]:
                list_protein.append("Arg")
            elif "AAA" in list_frame[n] or "AAG" in list_frame[n]:
                list_protein.append("Lys")
            elif "AAU" in list_frame[n] or "AAC" in list_frame[n]:
                list_protein.append("Asn")
            elif "AUG" in list_frame[n] in list_frame[n]:
                list_protein.append("Met")
            elif "GAU" in list_frame[n] or "GAC" in list_frame[n]:
                list_protein.append("Asp")
            elif "UUU" in list_frame[n] or "UUC" in list_frame[n]:
                list_protein.append("Phe")
            elif "UGU" in list_frame[n] or "UGC" in list_frame[n]:
                list_protein.append("Cys")
            elif "CCU" in list_frame[n] or "CCC" in list_frame[n] or "CCA" in list_frame[n] or "CCG" in list_frame[n]:
                list_protein.append("Pro")
            elif "CAA" in list_frame[n] or "CAG" in list_frame[n]:
                list_protein.append("Gln")
            elif "UCU" in list_frame[n] or "UCC" in list_frame[n] or "UCA" in list_frame[n] or "UCG" in list_frame[n] or "AGU" in list_frame[n] or "AGC" in list_frame[n]:
                list_protein.append("Ser")
            elif "GAA" in list_frame[n] or "GAG" in list_frame[n]:
                list_protein.append("Glu")
            elif "ACU" in list_frame[n] or "ACC" in list_frame[n] or "ACA" in list_frame[n] or "ACG" in list_frame[n]:
                list_protein.append("Thr")
            elif "GGU" in list_frame[n] or "GGC" in list_frame[n] or "GGA" in list_frame[n] or "GGG" in list_frame[n]:
                list_protein.append("Gly")
            elif "UGG" in list_frame[n]:
                list_protein.append("Trp")
            elif "CAU"  in list_frame[n]or "CAC" in list_frame[n]:
                list_protein.append("His")
            elif "UAU" in list_frame[n] or "UAC" in list_frame[n]:
                list_protein.append("Tyr")
            elif "AUU" in list_frame[n] or "AUC" in list_frame[n] or "AUA" in list_frame[n]:
                list_protein.append("Ile")
            elif "GUU" in list_frame[n] or "GUC" in list_frame[n] or "GUA" in list_frame[n] or "GUG" in list_frame[n]:
                list_protein.append("Val")
            elif "UAG" in list_frame[n] or "UGA" in list_frame[n] or "UAA" in list_frame[n]:
                list_protein.append("STOP")
            else:
                list_protein.append("???")
        return list_protein
    compliment_list_protein = compliment_translate(compliment_list_frame)
    compliment_protein = " ".join(compliment_list_protein)
    print ("Protein of Complimentary Strand: " + compliment_protein)
