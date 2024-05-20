# attractorAnim
Processing / Python scripts for animating 2D/3D attractors.

## preview :

![1](https://github.com/xxxxxxxxxmr/attractorAnim/assets/110829015/0389724b-0a2d-4954-b8d1-a1be42c8af6a)

![2](https://github.com/xxxxxxxxxmr/attractorAnim/assets/110829015/2a2f15a1-c9a7-4ec4-9f94-4a4a32e2e9ca)

## files :
#### CliffordAnim.pde :
runs the Clifford attractor with a = 4, b = 1.2, c = -1.5, d = 1.

#### DeJong.pde :
runs the de Jong attractor with , and is adaptable to 3D attractors with PeasyCam 3D visualisation.

#### CliffordAnimQT.py :
GUI that let's you choose nb of steps, opacity of dots, delta + which coeffs to apply delta to


## Install :

#### Processing scripts :
you'll need [Processing](https://processing.org/download). 
Just open the .pde files after install

#### python GUI :
- you'll need python3
- just git clone the repo `git clone git:github.com:xxxxxxxxxmr/attractorAnim.git`
- then `cd attractorAnim && pip install -r requirements`
- and `python CliffordAnimQT.py`
