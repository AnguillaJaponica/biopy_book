from Bio import Entrez, SeqID
Entrez.email = 'terumasa.taka@gmail.com'

handle = Entrez.esearch(
    db='nucleotide',
    term='CRT[Gene Name] AND "Plasmodium faruciparum"[Organism]')
rec_list = Entrez.read(handle)

if rec_list['RetMax'] < rec_list['Count']:
    handle = Entrez.esearch(
        db='nucleotide',
        term='CRT[Gene Name] AND "Plasmodium faruciparum"[Organism]',
        retmax=rec_list['Count'])
    rec_list = Entrez.read(handle)
