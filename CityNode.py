class CityNode(XMLExportable):
    def __init__(self, name, population):
        self.name = name
        self.population = population

    def to_xml(self):
        return f"<City><Name>{self.name}</Name><Population>{self.population}</Population></City>"

