# Workflow Documentation for Supersonic Non-Premixed Reactive Flows

## Overview

This documentation details a Snakemake workflow developed to process and visualize data from direct numerical simulations of supersonic non-premixed reactive flows. The key objective of this workflow is to generate analytical visualizations that aid in comprehending complex high-speed phenomena, which are pivotal in the advancement of technologies like scramjets and propulsion systems. The workflow consists of several rules, each designed to handle specific aspects of the data processing and visualization.

## Rule Descriptions

### Rule `plot_tke` - Plotting Turbulent Kinetic Energy (TKE)

The `plot_tke` rule automates the visualization of Turbulent Kinetic Energy data, crucial for understanding the dynamics of high-speed flows.

#### Input Files
- `infile1="data/tke1.dat"` and `infile2="data/tke2.dat"`: Contain TKE data essential for analyzing flow characteristics.

#### Output File
- `outfile="figures/tke_plot.png"`: A PNG image visualizing the TKE data, highlighting key aspects of the flow's kinetic energy.

#### Shell Command
- Executes `plot_tke.py` script: Processes the TKE data to generate a plot that provides insights into the kinetic energy distribution in the flow.

### Rule `plot_contour` - Plotting Temperature Contours

The `plot_contour` rule focuses on generating temperature contour plots, essential for visualizing thermal characteristics in reactive and non-reactive cases.

#### Input Files
- `infile1="data/temp150.dat1"`: Temperature data for the non-reactive case.
- `infile2="data/temp175.dat1"`: Temperature data for the reactive case.

#### Output Files
- `outfile1="figures/non_reactive.png"`: Contour plot for the non-reactive case.
- `outfile2="figures/reactive.png"`: Contour plot for the reactive case.

#### Shell Command
- Executes `contour.py` script: Creates detailed contour plots that illustrate temperature variations, crucial for understanding thermal behaviors in supersonic flows.

## Connecting to the Main Objective

Each rule in this workflow, including `plot_tke` and `plot_contour`, plays a vital role in dissecting the complex data from simulations. The TKE plots and temperature contours are instrumental in providing a deeper understanding of the flow dynamics and thermal properties in supersonic non-premixed reactive flows. These visualizations not only aid in fundamental research but also have significant implications for the development of high-speed applications like scramjets and advanced propulsion systems.

By analyzing this data, we gain insights into the intricate behaviors of supersonic flows, paving the way for innovations in high-speed flight technologies.
