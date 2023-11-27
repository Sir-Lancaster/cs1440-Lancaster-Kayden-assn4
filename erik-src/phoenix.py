#              Copyright © 2023 DuckieCorp. All Rights Reserved.
#
#                       __      Redistribution and use of this code, with or
#                     /` ,\__   without modification, are permitted provided
#                    |    ).-'  that the following conditions are met:
#                   / .--'
#                  / /          0. Redistributions of this code must retain
#    ,      _.==''`  \             the above copyright notice, this list of
#  .'(  _.='         |             conditions and the following disclaimer.
# {   ``  _.='       |          1. The name of the author may not be used to
#  {    \`     ;    /              endorse or promote products derived from
#   `.   `'=..'  .='               this software without specific prior written
#     `=._    .='                  permission.
#  jgs  '-`\\`__                2. Neither the name of the University nor the
#           `-._{                  names of its contributors may be used to
#                                  endorse or promote products derived from
#                                  this software without specific prior written
#                                  permission.

def count(z, end):
    """
    Return the iteration count for a point on the complex plane `c`
    to guess whether it is in the Phoenix set (bounded by `end`)
    """

    # Julia Constant
    c = complex(0.5667, 0.0)

    # Phoenix Constant
    p = complex(-0.5, 0.0)

    # The first thing we do to the complex number Z is reflect its components,
    # so the imaginary part becomes the real part, and vice versa.
    # If we don't do this, the image comes out SIDEWAYS!!!
    z = complex(z.imag, z.real)

    # zPrevious is the PREVIOUS Z value, except the 1st time through the
    # function, when it starts out as Complex Zero (which is actually the
    # same thing as REAL Zero 0)  MATH IS BEAUTIFUL!
    zPrev = 0+0j

    for i in range(end):
        zSave = z
        z = z * z + c + (p * zPrev)
        if abs(z) > 2:
            return i
        zPrev = zSave  # Set the prevZ value for the next iteration
    return end
