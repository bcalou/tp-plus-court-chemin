from pathfinder.city import City


graph = {
  City.BORDEAUX: {
    City.NANTES: 19,
    City.ORLEANS: 24,
    City.LYON: 31,
    City.TOULOUSE: 14
  },
  City.DIJON: {
    City.STRASBOURG: 20,
    City.PARIS: 16,
    City.ORLEANS: 15,
    City.LYON: 11
  },
  City.LILLE: {
    City.ROUEN: 12,
    City.PARIS: 13,
    City.STRASBOURG: 29
  },
  City.LYON: {
    City.DIJON: 11,
    City.ORLEANS: 20,
    City.BORDEAUX: 31,
    City.TOULOUSE: 28,
    City.MARSEILLE: 18
  },
  City.MARSEILLE: {
    City.LYON: 18,
    City.TOULOUSE: 22
  },
  City.NANTES: {
    City.RENNES: 6,
    City.ROUEN: 19,
    City.ORLEANS: 16,
    City.BORDEAUX: 19
  },
  City.ORLEANS: {
    City.NANTES: 16,
    City.ROUEN: 11,
    City.PARIS: 7,
    City.DIJON: 15,
    City.LYON: 20,
    City.BORDEAUX: 24
  },
  City.PARIS: {
    City.LILLE: 13,
    City.STRASBOURG: 26,
    City.DIJON: 16,
    City.ORLEANS: 7,
    City.ROUEN: 7
  },
  City.RENNES: {
    City.ROUEN: 17,
    City.NANTES: 6
  },
  City.ROUEN: {
    City.LILLE: 12,
    City.PARIS: 7,
    City.ORLEANS: 11,
    City.NANTES: 19,
    City.RENNES: 17
  },
  City.STRASBOURG: {
    City.LILLE: 29,
    City.PARIS: 26,
    City.DIJON: 20
  },
  City.TOULOUSE: {
    City.BORDEAUX: 14,
    City.LYON: 28,
    City.MARSEILLE: 22
  }
}

spfa_graph = {
  City.BORDEAUX: {
    City.NANTES: 50,
    City.TOULOUSE: 50
  },
  City.DIJON: {
    City.STRASBOURG: 30,
  },
  City.LILLE: {
  },
  City.LYON: {
    City.DIJON: 20,
  },
  City.MARSEILLE: {
    City.LYON: 30
  },
  City.NANTES: {
    City.RENNES: 20,
    City.ORLEANS: 10
  },
  City.ORLEANS: {
    City.PARIS: 40,
    City.STRASBOURG: 15
  },
  City.PARIS: {
    City.LILLE: 50,
    City.STRASBOURG: -10,
    City.ORLEANS: -30
  },
  City.RENNES: {
    City.ROUEN: -50,
    City.PARIS: 20
  },
  City.ROUEN: {
    City.PARIS: 10
  },
  City.STRASBOURG: {
    City.LILLE: 50,
  },
  City.TOULOUSE: {
    City.LYON: -75,
    City.MARSEILLE: 40
  }
}