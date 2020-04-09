class ImpactCalculator:
    impactRate = 10
    severeImpactRate = 50

    def __init__(self, region, periodType, timeToElapse, reportedCases, population, totalHospitalBeds):
        self.region = region
        self.periodType = periodType
        self.timeToElapse = timeToElapse
        self.reportedCases = reportedCases
        self.population = population
        self.totalHospitalBeds = totalHospitalBeds

    def impact(self):
        currentlyInfected = self.reportedCases * self.impactRate
        return currentlyInfected

    def severeImpact(self):
        currentlyInfected = self.reportedCases * self.severeImpactRate
        return currentlyInfected
