#! /usr/bin/env python3
#
# Ball Grid Array parts
#

from pcbflow import *


class FTG256(Part):
    family = "U"
    footprint = "FTG256"

    def place(self, dc):
        self.chamfered(dc, 17, 17)
        dc.left(90)
        dc.forward(7.5)
        dc.right(90)
        dc.forward(7.5)
        dc.right(90)
        for j in range(16):
            dc.push()
            for i in range(16):
                dc.left(90)
                self.roundpad(dc, 0.4)
                dc.right(90)
                dc.forward(1)
            dc.pop()
            dc.right(90)
            dc.forward(1)
            dc.left(90)

        return