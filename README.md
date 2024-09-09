# MMoM_project - Molecular Modeling of Materials

This repository contains the code and data for the project "Molecular Modeling of Materials" (MMoM) at the Politecnico di Milano. The <b>chosen topic</b> is the study of absorption of hydrogen molecules in gas phase by graphene nanofibers (GNFs). Both DFT and MD analyses are performed to investigate the phenomenon.

![dynamics](https://github.com/ApprehensiveKnee/MMoM_project/blob/main/imgs/movie.gif)

## Project structure

The repository is structured as follows:


- `DFT_absorption`: contains the code and data for the DFT analysis, it further contains the following subfolders:
  - `potentials`: contains the pseudopotentials used for the DFT calculations.
  - `results`: contains the results of the DFT calculations.
  - `scripts`: contains the scripts used to perform the DFT calculations.

  Both `results` and `scripts` contain 2 subfolders:
    - `remote`: contains the files used for the calculations on a remote pc, with <i>lower</i> computational resources.
    - `local`: contains the files used for the calculations on a local pc, with <i>higher</i> computational resources.

- `MD`: contains the code and data for the MD analysis, it further contains the following subfolders:
  - `addingHydrogen`: contains the scripts and final results for the simulations.
  - `geometry`: contains the scripts, templates and molecular data used to define the final systems on which the GCMC simulations where later performed.

- `imgs`: contains some images used in visual.ipynb

- `visual.ipynb`: the notebook where hosting the general idea and logic thread followed in the making of this project