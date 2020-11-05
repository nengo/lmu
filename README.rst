Legendre Memory Units: Continuous-Time Representation in Recurrent Neural Networks
----------------------------------------------------------------------------------

.. note::

   This is a metapackage for installing LMU implementations. It does not contain any
   code itself. See the list of implementations below.

`Paper <https://papers.nips.cc/paper/9689-legendre-memory-units-continuous-time-representation-in-recurrent-neural-networks.pdf>`_

The LMU is a novel memory cell for recurrent neural
networks that dynamically maintains information across long windows of time using
relatively few resources. It has been shown to perform as well as standard LSTM or
other RNN-based models in a variety of tasks, generally with fewer internal parameters
(see `this paper
<https://papers.nips.cc/paper/9689-legendre-memory-units-continuous-time-representation-in-recurrent-neural-networks.pdf>`_ for more details). For the Permuted Sequential MNIST (psMNIST) task in particular, it has been demonstrated to outperform the current state-of-the-art results. See the note below for instructions on how to get access to this model.

The LMU is mathematically derived to orthogonalize its continuous-time history – doing
so by solving *d* coupled ordinary differential equations (ODEs), whose phase space
linearly maps onto sliding windows of time via the Legendre polynomials up to degree
*d* − 1 (the example for *d* = 12 is shown below).

.. image:: https://i.imgur.com/Uvl6tj5.png
   :target: https://i.imgur.com/Uvl6tj5.png
   :alt: Legendre polynomials

A single LMU cell expresses the following computational graph, which takes in an input
signal, **x**, and couples a optimal linear memory, **m**, with a nonlinear hidden
state, **h**. By default, this coupling is trained via backpropagation, while the
dynamics of the memory remain fixed.

.. image:: https://i.imgur.com/IJGUVg6.png
   :target: https://i.imgur.com/IJGUVg6.png
   :alt: Computational graph

The discretized **A** and **B** matrices are initialized according to the LMU's
mathematical derivation with respect to some chosen window length, **θ**.
Backpropagation can be used to learn this time-scale, or fine-tune **A** and **B**,
if necessary.

Both the kernels, **W**, and the encoders, **e**, are learned. Intuitively, the kernels
learn to compute nonlinear functions across the memory, while the encoders learn to
project the relevant information into the memory (see `paper
<https://papers.nips.cc/paper/9689-legendre-memory-units-continuous-time-representation-in-recurrent-neural-networks.pdf>`_ for details).

LMU implementations
-------------------

* `KerasLMU <https://www.nengo.ai/keras-lmu>`_: Implementation of LMUs in Keras (this
  is the original LMU implementation, which used to be referred to generically
  as *the* LMU repo).

Examples
--------

* `State of the art performance on psMNIST using KerasLMU
  <https://www.nengo.ai/keras-lmu/examples/psMNIST.html>`_
* `LMUs in Nengo (with online learning)
  <https://www.nengo.ai/nengo/examples/learning/lmu.html>`_
* `Spiking LMUs in Nengo Loihi (with online learning)
  <https://www.nengo.ai/nengo-loihi/examples/lmu.html>`_
* `LMUs in NengoDL (reproducing SotA on psMNIST)
  <https://www.nengo.ai/nengo-dl/examples/lmu.html>`_

Citation
--------

.. code-block::

   @inproceedings{voelker2019lmu,
     title={Legendre Memory Units: Continuous-Time Representation in Recurrent Neural Networks},
     author={Aaron R. Voelker and Ivana Kaji\'c and Chris Eliasmith},
     booktitle={Advances in Neural Information Processing Systems},
     pages={15544--15553},
     year={2019}
   }
