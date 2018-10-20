class Game():
    def __init__(self):
       self.targets = "Time crystals are quantum many body systems that due to interactions between particles are able to spontaneously self organize their motion in a periodic way in time by analogy with the formation of crystalline structures in space in condensed matter physics In solid state physics properties of space crystals are often investigated with the help of external potentials that are spatially periodic and reflect various crystalline structures A similar approach can be applied for time crystals as periodically driven systems constitute counterparts of spatially periodic systems but in the time domain Here we show that condensed matter problems ranging from single particles in potentials of quasicrystal structure to many body systems with exotic long range interactions can be realized in the time domain with an appropriate periodic driving Moreover it is possible to create molecules where atoms are bound together due to destructive interference if the atomic scattering length is modulated in time"
       self.w_index = -1

    def get_next(self):
       self.w_index += 1
       if self.targets[self.w_index] == ' ':
           self.w_index += 1
    #    print(self.targets[self.w_index])
       return {
            'letter': self.targets[self.w_index],
            'display': self.targets[self.w_index+1:self.w_index+25]}
