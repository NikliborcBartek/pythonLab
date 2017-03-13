# Bartlomiej Nikliborc dda
import random


class PlaneSimulator:

    const_maxTiltCorrectionDegree = 10
    NofStep = 1

    def __init__(self, plane_orientation = 0, turbulationGaussMean = 0, turbulationGaussSigma = 20 ):
        self.plane_orientation = plane_orientation
        self.turbulationGaussMean = turbulationGaussMean
        self.turbulationGaussSigma = turbulationGaussSigma

    def process(self):
        while True:
            print "----Step Number %s " % self.NofStep
            turbulations = random.gauss(self.turbulationGaussMean, self.turbulationGaussSigma)
            print  "turbulations %s" % turbulations
            self.plane_orientation += turbulations
            print "plane_orientation %s" % self.plane_orientation
            correction = self.getCorrection(self.plane_orientation)
            print "correction %s" % correction
            self.plane_orientation += correction
            print "corrected_Plane_orietnation %s" % self.plane_orientation
            self.NofStep +=1
    def getCorrection(self, orientation):
        if orientation > self.const_maxTiltCorrectionDegree:
            return -self.const_maxTiltCorrectionDegree
        elif orientation < -self.const_maxTiltCorrectionDegree:
            return self.const_maxTiltCorrectionDegree
        else:
            return -orientation

firstPanel = PlaneSimulator()
firstPanel.process()
