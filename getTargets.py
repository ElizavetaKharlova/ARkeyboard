text = 'Spontaneous symmetry breaking is a fundamental concept in many areas of physics, including cosmology, particle physics and condensed matter1. An example is the breaking of spatial translational symmetry, which underlies the formation of crystals and the phase transition from liquid to solid. Using the analogy of crystals in space, the breaking of translational symmetry in time and the emergence of a ‘time crystal’ was recently proposed2,3, but was later shown to be forbidden in thermal equilibrium4,5,6. However, non-equilibrium Floquet systems, which are subject to a periodic drive, can exhibit persistent time correlations at an emergent subharmonic frequency7,8,9,10. This new phase of matter has been dubbed a ‘discrete time crystal’10. Here we present the experimental observation of a discrete time crystal, in an interacting spin chain of trapped atomic ions. We apply a periodic Hamiltonian to the system under many-body localization conditions, and observe a subharmonic temporal response that is robust to external perturbations. The observation of such a time crystal opens the door to the study of systems with long-range spatio-temporal correlations and novel phases of matter that emerge under intrinsically non-equilibrium conditions7.'
words = []
buffer =
for index in range(len(text)):
    if text[index] == ' ':

    else:
        buffer = buffer + text[index]