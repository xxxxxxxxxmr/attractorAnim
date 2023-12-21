# attractorAnim
Processing / Python scripts for animating 2D/3D attractors.


## files:
#### CliffordAnim.pde 
runs the Clifford attractor with a = 4, b = 1.2, c = -1.5, d = 1.

#### DeJong.pde
runs the de Jong attractor with , and is adaptable to 3D attractors with PeasyCam 3D visualisation.

#### CliffordAnimQT.py
GUI that let's you choose nb of steps, opacity of dots, delta + which coeffs to apply delta to


## Install

#### Processing scripts
you'll need [Processing](https://processing.org/download)
just open the .pde files after install

#### python GUI
- you'll need python3
- just git clone the repo `git clone git:github.com:mar1wokeup/attractorAnim.git`
- then `cd attractorAnim && pip install -r requirements`
- and `python CliffordAnimQT.py`