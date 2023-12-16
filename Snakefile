# Snakefile
rule all:
    input:
        "figures/tke_plot.png",
        "figures/non_reactive.png",
        "figures/reactive.png"

rule plot_tke:
    input:
        infile1="data/tke1.dat",
        infile2="data/tke2.dat"
    output:
        outfile="figures/tke_plot.png"
    shell:
        "python scripts/plot_tke.py {input.infile1} {input.infile2} {output.outfile}"

rule plot_contour:
    input:
        infile1="data/temp150.dat1",
        infile2="data/temp175.dat1"
    output:
        outfile1="figures/non_reactive.png",
        outfile2="figures/reactive.png"
    shell:
        "python scripts/contour.py {input.infile1} {input.infile2} {output.outfile1} {output.outfile2}"
