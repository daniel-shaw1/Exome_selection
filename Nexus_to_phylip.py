from Bio import AlignIO

# Replace 'input.nexus' with the path to your Nexus file
input_nexus = 'Roycroft_etal_murine_exome_alignment.nex'
output_phylip = 'Roycroft.phylip'

alignment = AlignIO.read(input_nexus, "nexus")
AlignIO.write(alignment, output_phylip, "phylip")
