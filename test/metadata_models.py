basicMetadataModel = {
    "floors": {
        "has_parent": None,
        "single": True,
        "groundFloor": {
            "aliases": ["ground_floor", "groundfloor"],
            "areas": ["livingroom", "kitchen", "hallway", "bathroom1"]
        },
        "firstFloor": {
            "aliases": ["first_floor", "firstfloor"],
            "areas": ["suite", "bedroom2", "bedroom3", "bathroom2"]
        },
        "garden": {
            "aliases": [],
            "areas": ["garage", "sittingArea"]
        }
    },
    "areas": {
        "has_parent": ["floors"],
        "single": True,
        "bathroom": {
            "aliases": [],
        },
        "kitchen": {
            "aliases": [],
            "measurement": [],
            "binary_measurement": ["smoke"],
            "device": ["tempDevice2", "humidityDevice1"]
        },
        "livingroom": {
            "aliases": ["living_room"],
            "measurement": ["light"],
            "binary_measurement": [],
            "device": ["tempDevice1"]
        },
        "hallway": {
            "aliases": [],
            "measurement": ["light"],
            "binary_measurement": [],
            "device": ["lightDevice1"]
        },
        # first floor
        "suite": {
            "aliases": ["bedroom1"],
            "measurement": ["temperature"],
            "binary_measurement": []
        },
        "bedroom2": {
            "aliases": ["bedroom2"],
            "measurement": [],
            "binary_measurement": ["motion"],
            "sensor": ["motionSensor1"]
        },
        "bedroom3": {
            "aliases": ["bedroom3"],
            "measurement": [],
            "binary_measurement": ["motion"],
            "sensor": ["motionSensor2"]
        },
        "bathroom2": {
            "aliases": []
        },
        # garden
        "garage": {
            "aliases": [],
            "measurement": [],
            "binary_measurement": [],
            "device": ["garageContactDevice"]
        },
        "sittingArea": {
            "aliases": [],
            "measurement": [],
            "binary_measurement": ["motion"]
        }
    },
    "measurement": {
        "has_parent": ["areas"],
        "single": True,
        "apparent_power": {
            "aliases": []
        },
        "aqi": {
            "aliases": []
        },
        "area": {
            "aliases": []
        },
        "atmospheric_pressure": {
            "aliases": []
        },
        "battery": {
            "aliases": []
        },
        "blood_glucose_concentration": {
            "aliases": []
        },
        "co": {
            "aliases": []
        },
        "co2": {
            "aliases": []
        },
        "conductivity": {
            "aliases": []
        },
        "current": {
            "aliases": []
        },
        "data_rate": {
            "aliases": []
        },
        "data_size": {
            "aliases": []
        },
        "distance": {
            "aliases": []
        },
        "duration": {
            "aliases": []
        },
        "energy": {
            "aliases": []
        },
        "energy_distance": {
            "aliases": []
        },
        "energy_storage": {
            "aliases": []
        },
        "frequency": {
            "aliases": []
        },
        "gas": {
            "aliases": []
        },
        "humidity": {
            "aliases": []
        },
        "illuminance": {
            "aliases": []
        },
        "irradiance": {
            "aliases": []
        },
        "moisture": {
            "aliases": []
        },
        "nitrogen_dioxide": {
            "aliases": []
        },
        "nitrogen_monoxide": {
            "aliases": []
        },
        "nitrous_oxide": {
            "aliases": []
        },
        "ozone": {
            "aliases": []
        },
        "ph": {
            "aliases": []
        },
        "pm1": {
            "aliases": []
        },
        "pm10": {
            "aliases": []
        },
        "pm25": {
            "aliases": []
        },
        "power_factor": {
            "aliases": []
        },
        "power": {
            "aliases": []
        },
        "precipitation": {
            "aliases": []
        },
        "precipitation_intensity": {
            "aliases": []
        },
        "pressure": {
            "aliases": []
        },
        "reactive_power": {
            "aliases": []
        },
        "signal_strength": {
            "aliases": []
        },
        "sound_pressure": {
            "aliases": []
        },
        "speed": {
            "aliases": []
        },
        "sulphur_dioxide": {
            "aliases": []
        },
        "temperature": {
            "aliases": []
        },
        "volatile_organic_compounds": {
            "aliases": []
        },
        "volatile_organic_compounds_parts": {
            "aliases": []
        },
        "voltage": {
            "aliases": []
        },
        "volume": {
            "aliases": []
        },
        "volume_flow_rate": {
            "aliases": []
        },
        "volume_storage": {
            "aliases": []
        },
        "water": {
            "aliases": []
        },
        "weight": {
            "aliases": []
        },
        "wind_direction": {
            "aliases": []
        },
        "wind_speed": {
            "aliases": []
        }
    },
    "binary_measurement": {
        "has_parent": ["areas"],
        "single": True,
        "battery_charging": {
            "aliases": []
        },
        "cold": {
            "aliases": []
        },
        "connectivity": {
            "aliases": []
        },
        "door": {
            "aliases": []
        },
        "garage_door": {
            "aliases": []
        },
        "heat": {
            "aliases": []
        },
        "light": {
            "aliases": []
        },
        "lock": {
            "aliases": []
        },
        "motion": {
            "aliases": []
        },
        "moving": {
            "aliases": []
        },
        "occupancy": {
            "aliases": []
        },
        "opening": {
            "aliases": []
        },
        "plug": {
            "aliases": []
        },
        "presence": {
            "aliases": []
        },
        "problem": {
            "aliases": []
        },
        "running": {
            "aliases": []
        },
        "safety": {
            "aliases": []
        },
        "smoke": {
            "aliases": []
        },
        "sound": {
            "aliases": []
        },
        "tamper": {
            "aliases": []
        },
        "update": {
            "aliases": []
        },
        "vibration": {
            "aliases": []
        },
        "window": {
            "aliases": []
        }
    }
}

extendedMetadataModel = {
    "floors": {
        "has_parent": None,
        "single": True,
        "groundFloor": {
            "aliases": ["ground_floor", "groundfloor"],
            "areas": ["livingroom", "kitchen", "hallway", "bathroom1"]
        },
        "firstFloor": {
            "aliases": ["first_floor", "firstfloor"],
            "areas": ["suite", "bedroom2", "bedroom3", "bathroom2"]
        },
        "garden": {
            "aliases": [],
            "areas": ["garage", "sittingArea"]
        }
    },
    "areas": {
        "has_parent": ["floors"],
        "single": True,
        "bathroom": {
            "aliases": [],
        },
        "kitchen": {
            "aliases": [],
            "measurement": [],
            "binary_measurement": ["smoke"],
            "device": ["tempDevice2", "humidityDevice1"]
        },
        "livingroom": {
            "aliases": ["living_room"],
            "device": ["tempDevice1"],
            "measurement": ["light"],
            "binary_measurement": []
        },
        "hallway": {
            "aliases": [],
            "measurement": [],
            "binary_measurement": [],
            "device": ["lightDevice1"]
        },
        # first floor
        "suite": {
            "aliases": ["bedroom1"],
            "measurement": ["temperature"],
            "binary_measurement": []
        },
        "bedroom2": {
            "aliases": ["bedroom2"],
            "measurement": [],
            "sensor": ["motionSensor1"]
        },
        "bedroom3": {
            "aliases": ["bedroom3"],
            "measurement": [],
            "sensor": ["motionSensor2"]
        },
        "bathroom2": {
            "aliases": []
        },
        # garden
        "garage": {
            "aliases": [],
            "measurement": [],
            "binary_measurement": [],
            "device": ["garageContactDevice"]
        },
        "sittingArea": {
            "aliases": [],
            "measurement": [],
            "binary_measurement": ["motion"]
        }
    },
    "measurement": {
        "has_parent": ["areas", "sensor", "device"],
        "single": True,
        "apparent_power": {
            "aliases": []
        },
        "aqi": {
            "aliases": []
        },
        "area": {
            "aliases": []
        },
        "atmospheric_pressure": {
            "aliases": []
        },
        "battery": {
            "aliases": []
        },
        "blood_glucose_concentration": {
            "aliases": []
        },
        "co": {
            "aliases": []
        },
        "co2": {
            "aliases": []
        },
        "conductivity": {
            "aliases": []
        },
        "current": {
            "aliases": []
        },
        "data_rate": {
            "aliases": []
        },
        "data_size": {
            "aliases": []
        },
        "distance": {
            "aliases": []
        },
        "duration": {
            "aliases": []
        },
        "energy": {
            "aliases": []
        },
        "energy_distance": {
            "aliases": []
        },
        "energy_storage": {
            "aliases": []
        },
        "frequency": {
            "aliases": []
        },
        "gas": {
            "aliases": []
        },
        "humidity": {
            "aliases": []
        },
        "illuminance": {
            "aliases": []
        },
        "irradiance": {
            "aliases": []
        },
        "moisture": {
            "aliases": []
        },
        "nitrogen_dioxide": {
            "aliases": []
        },
        "nitrogen_monoxide": {
            "aliases": []
        },
        "nitrous_oxide": {
            "aliases": []
        },
        "ozone": {
            "aliases": []
        },
        "ph": {
            "aliases": []
        },
        "pm1": {
            "aliases": []
        },
        "pm10": {
            "aliases": []
        },
        "pm25": {
            "aliases": []
        },
        "power_factor": {
            "aliases": []
        },
        "power": {
            "aliases": []
        },
        "precipitation": {
            "aliases": []
        },
        "precipitation_intensity": {
            "aliases": []
        },
        "pressure": {
            "aliases": []
        },
        "reactive_power": {
            "aliases": []
        },
        "signal_strength": {
            "aliases": []
        },
        "sound_pressure": {
            "aliases": []
        },
        "speed": {
            "aliases": []
        },
        "sulphur_dioxide": {
            "aliases": []
        },
        "temperature": {
            "aliases": []
        },
        "volatile_organic_compounds": {
            "aliases": []
        },
        "volatile_organic_compounds_parts": {
            "aliases": []
        },
        "voltage": {
            "aliases": []
        },
        "volume": {
            "aliases": []
        },
        "volume_flow_rate": {
            "aliases": []
        },
        "volume_storage": {
            "aliases": []
        },
        "water": {
            "aliases": []
        },
        "weight": {
            "aliases": []
        },
        "wind_direction": {
            "aliases": []
        },
        "wind_speed": {
            "aliases": []
        }
    },
    "binary_measurement": {
        "has_parent": ["areas", "sensor", "device"],
        "single": True,
        "battery_charging": {
            "aliases": []
        },
        "cold": {
            "aliases": []
        },
        "connectivity": {
            "aliases": []
        },
        "door": {
            "aliases": []
        },
        "garage_door": {
            "aliases": []
        },
        "heat": {
            "aliases": []
        },
        "light": {
            "aliases": []
        },
        "lock": {
            "aliases": []
        },
        "motion": {
            "aliases": []
        },
        "moving": {
            "aliases": []
        },
        "occupancy": {
            "aliases": []
        },
        "opening": {
            "aliases": []
        },
        "plug": {
            "aliases": []
        },
        "presence": {
            "aliases": []
        },
        "problem": {
            "aliases": []
        },
        "running": {
            "aliases": []
        },
        "safety": {
            "aliases": []
        },
        "smoke": {
            "aliases": []
        },
        "sound": {
            "aliases": []
        },
        "tamper": {
            "aliases": []
        },
        "update": {
            "aliases": []
        },
        "vibration": {
            "aliases": []
        },
        "window": {
            "aliases": []
        }
    },
    "labels": {
        "has_parent": ["floors", "areas", "device"],
        "single": False,
        "area1": {
            "aliases": []
        }, "area2": {
            "aliases": []
        }, "security": {
            "aliases": []
        }, "energy": {
            "aliases": ["energy-saving"]
        }, "binary": {
            "aliases": []
        }, "automations": {
            "aliases": []
        }, "health": {
            "aliases": []
        }, "ambience": {
            "aliases": []
        }
    },
    "device": {
        "has_parent": ["areas"],
        "single": True,
        "tempDevice1": {
            "aliases": [],
            "binary_measurement": [],
            "measurement": ["temperature"]
        },
        "tempDevice2": {
            "aliases": [],
            "binary_measurement": [],
            "measurement": ["temperature"]
        },
        "lightDevice1": {
            "aliases": [],
            "binary_measurement": ["light"],
            "measurement": []
        },
        "humidityDevice1": {
            "aliases": [],
            "binary_measurement": [],
            "measurement": ["humidity"]
        },
        "garageContactDevice1": {
            "aliases": [],
            "sensor": ["garageContactSensor1"],
            "binary_measurement": ["garage_door"],
            "measurement": []
        }
    },
    "sensor": {
        "has_parent": ["device", "areas"],
        "single": True,
        "garageContactSensor1": {
            "aliases": [],
            "label": ["security"],
            "binary_measurement": ["garage_door"],
            "measurement": []
        },
        "motionSensor1": {
            "aliases": [],
            "label": ["security", "energy"],
            "binary_measurement": ["motion"],
            "measurement": []
        },
        "motionSensor2": {
            "aliases": [],
            "label": ["security", "energy"],
            "binary_measurement": ["motion"],
            "measurement": []
        }
    }
}

largeMetadataModelWithParentLinks = {
    "floors": {
        "has_parent": None,
        "single": True,
        "floor0": {
            "aliases": ["ground_floor", "groundfloor"],
            "areas": ["area0_0", "area0_1", "area0_2", "area0_3", "area0_4"]
        },
        "floor1": {
            "aliases": ["first_floor", "firstfloor"],
            "areas": ["area1_0", "area1_1", "area1_2", "area1_3", "area1_4"]
        },
        "floor2": {
            "aliases": ["second_floor", "secondfloor"],
            "areas": ["area2_0", "area2_1", "area2_2", "area2_3", "area2_4"]
        },
        "floor3": {
            "aliases": ["third_floor", "thirdfloor"],
            "areas": ["area3_0", "area3_1", "area3_2", "area3_3", "area3_4"]
        },
        "floor4": {
            "aliases": ["fourth_floor", "fourthfloor"],
            "areas": ["area4_0", "area4_1", "area4_2", "area4_3", "area4_4"]
        },
        "floor5": {
            "aliases": ["fifth_floor", "fifthfloor"],
            "areas": ["area5_0", "area5_1", "area5_2", "area5_3", "area5_4"]
        },
        "floor6": {
            "aliases": ["sixth_floor", "sixthfloor"],
            "areas": ["area6_0", "area6_1", "area6_2", "area6_3", "area6_4"]
        },
        "floor7": {
            "aliases": ["seventh_floor", "seventhfloor"],
            "areas": ["area7_0", "area7_1", "area7_2", "area7_3", "area7_4"]
        },
        "floor8": {
            "aliases": ["eighth_floor", "eighthfloor"],
            "areas": ["area8_0", "area8_1", "area8_2", "area8_3", "area8_4"]
        },
        "floor9": {
            "aliases": ["ninth_floor", "ninthfloor"],
            "areas": ["area9_0", "area9_1", "area9_2", "area9_3", "area9_4"]
        },
        "groundFloor": {
            "aliases": ["ground_floor", "groundfloor"],
            "areas": ["livingroom", "kitchen", "hallway", "bathroom1"]
        },
        "firstFloor": {
            "aliases": ["first_floor", "firstfloor"],
            "areas": ["suite", "bedroom2", "bedroom3", "bathroom2"]
        },
        "garden": {
            "aliases": [],
            "areas": ["garage", "sittingArea"]
        }
    },
    "areas": {
        "has_parent": ["floors"],
        "single": True,
        "area0_0": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},
        "area0_1": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},
        "area0_2": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},
        "area0_3": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},
        "area0_4": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},

        "area1_0": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},
        "area1_1": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},
        "area1_2": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},
        "area1_3": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},
        "area1_4": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},

        "area2_0": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},
        "area2_1": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},
        "area2_2": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},
        "area2_3": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},
        "area2_4": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},

        "area3_0": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},
        "area3_1": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},
        "area3_2": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},
        "area3_3": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},
        "area3_4": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},

        "area4_0": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},
        "area4_1": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},
        "area4_2": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},
        "area4_3": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},
        "area4_4": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},

        "area5_0": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},
        "area5_1": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},
        "area5_2": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},
        "area5_3": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},
        "area5_4": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},

        "area6_0": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},
        "area6_1": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},
        "area6_2": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},
        "area6_3": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},
        "area6_4": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},

        "area7_0": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},
        "area7_1": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},
        "area7_2": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},
        "area7_3": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},
        "area7_4": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},

        "area8_0": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},
        "area8_1": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},
        "area8_2": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},
        "area8_3": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},
        "area8_4": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},

        "area9_0": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},
        "area9_1": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},
        "area9_2": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},
        "area9_3": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},
        "area9_4": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},
        "bathroom": {
            "aliases": [],
        },
        "kitchen": {
            "aliases": [],
            "measurement": [],
            "binary_measurement": ["smoke"],
            "device": ["tempDevice2", "humidityDevice1"]
        },
        "livingroom": {
            "aliases": ["living_room"],
            "measurement": ["light","temperature"],
            "binary_measurement": [],
            "device": ["tempDevice1"]
        },
        "hallway": {
            "aliases": [],
            "measurement": [],
            "binary_measurement": [],
            "device": ["lightDevice1"]
        },
        # first floor
        "suite": {
            "aliases": ["bedroom1"],
            "measurement": ["temperature"],
            "binary_measurement": []
        },
        "bedroom2": {
            "aliases": ["bedroom2"],
            "measurement": [],
            "sensor": ["motionSensor1"]
        },
        "bedroom3": {
            "aliases": ["bedroom3"],
            "measurement": [],
            "sensor": ["motionSensor2"]
        },
        "bathroom2": {
            "aliases": []
        },
        # garden
        "garage": {
            "aliases": [],
            "measurement": [],
            "binary_measurement": ["garage_door"],
            "device": ["garageContactDevice"]
        },
        "sittingArea": {
            "aliases": [],
            "measurement": [],
            "binary_measurement": ["motion"]
        }
    },
    "measurement": {
        "has_parent": ["areas", "sensor", "device"],
        "single": True,
        "apparent_power": {
            "aliases": []
        },
        "aqi": {
            "aliases": []
        },
        "area": {
            "aliases": []
        },
        "atmospheric_pressure": {
            "aliases": []
        },
        "battery": {
            "aliases": []
        },
        "blood_glucose_concentration": {
            "aliases": []
        },
        "co": {
            "aliases": []
        },
        "co2": {
            "aliases": []
        },
        "conductivity": {
            "aliases": []
        },
        "current": {
            "aliases": []
        },
        "data_rate": {
            "aliases": []
        },
        "data_size": {
            "aliases": []
        },
        "distance": {
            "aliases": []
        },
        "duration": {
            "aliases": []
        },
        "energy": {
            "aliases": []
        },
        "energy_distance": {
            "aliases": []
        },
        "energy_storage": {
            "aliases": []
        },
        "frequency": {
            "aliases": []
        },
        "gas": {
            "aliases": []
        },
        "humidity": {
            "aliases": []
        },
        "illuminance": {
            "aliases": []
        },
        "irradiance": {
            "aliases": []
        },
        "moisture": {
            "aliases": []
        },
        "nitrogen_dioxide": {
            "aliases": []
        },
        "nitrogen_monoxide": {
            "aliases": []
        },
        "nitrous_oxide": {
            "aliases": []
        },
        "ozone": {
            "aliases": []
        },
        "ph": {
            "aliases": []
        },
        "pm1": {
            "aliases": []
        },
        "pm10": {
            "aliases": []
        },
        "pm25": {
            "aliases": []
        },
        "power_factor": {
            "aliases": []
        },
        "power": {
            "aliases": []
        },
        "precipitation": {
            "aliases": []
        },
        "precipitation_intensity": {
            "aliases": []
        },
        "pressure": {
            "aliases": []
        },
        "reactive_power": {
            "aliases": []
        },
        "signal_strength": {
            "aliases": []
        },
        "sound_pressure": {
            "aliases": []
        },
        "speed": {
            "aliases": []
        },
        "sulphur_dioxide": {
            "aliases": []
        },
        "temperature": {
            "aliases": []
        },
        "volatile_organic_compounds": {
            "aliases": []
        },
        "volatile_organic_compounds_parts": {
            "aliases": []
        },
        "voltage": {
            "aliases": []
        },
        "volume": {
            "aliases": []
        },
        "volume_flow_rate": {
            "aliases": []
        },
        "volume_storage": {
            "aliases": []
        },
        "water": {
            "aliases": []
        },
        "weight": {
            "aliases": []
        },
        "wind_direction": {
            "aliases": []
        },
        "wind_speed": {
            "aliases": []
        }
    },
    "binary_measurement": {
        "has_parent": ["areas", "sensor", "device"],
        "single": True,
        "battery_charging": {
            "aliases": []
        },
        "cold": {
            "aliases": []
        },
        "connectivity": {
            "aliases": []
        },
        "door": {
            "aliases": []
        },
        "garage_door": {
            "aliases": []
        },
        "heat": {
            "aliases": []
        },
        "light": {
            "aliases": []
        },
        "lock": {
            "aliases": []
        },
        "motion": {
            "aliases": []
        },
        "moving": {
            "aliases": []
        },
        "occupancy": {
            "aliases": []
        },
        "opening": {
            "aliases": []
        },
        "plug": {
            "aliases": []
        },
        "presence": {
            "aliases": []
        },
        "problem": {
            "aliases": []
        },
        "running": {
            "aliases": []
        },
        "safety": {
            "aliases": []
        },
        "smoke": {
            "aliases": []
        },
        "sound": {
            "aliases": []
        },
        "tamper": {
            "aliases": []
        },
        "update": {
            "aliases": []
        },
        "vibration": {
            "aliases": []
        },
        "window": {
            "aliases": []
        }
    },
    "labels": {
        "has_parent": ["floors", "areas", "device"],
        "single": False,
        "area1": {
            "aliases": []
        }, "area2": {
            "aliases": []
        }, "security": {
            "aliases": []
        }, "energy": {
            "aliases": ["energy-saving"]
        }, "binary": {
            "aliases": []
        }, "automations": {
            "aliases": []
        }, "health": {
            "aliases": []
        }, "ambience": {
            "aliases": []
        }
    },
    "device": {
        "has_parent": ["floors", "areas"],
        "single": True,
        "tempDevice1": {
            "aliases": [],
            "binary_measurement": [],
            "measurement": ["temperature"]
        },
        "tempDevice2": {
            "aliases": [],
            "binary_measurement": [],
            "measurement": ["temperature"]
        },
        "lightDevice1": {
            "aliases": [],
            "binary_measurement": ["light"],
            "measurement": []
        },
        "humidityDevice1": {
            "aliases": [],
            "binary_measurement": [],
            "measurement": ["humidity"]
        },
        "garageContactDevice1": {
            "aliases": [],
            "sensor": ["garageContactSensor1"],
            "binary_measurement": ["garage_door"],
            "measurement": []
        }
    },
    "sensor": {
        "has_parent": ["device", "areas"],
        "single": True,
        "garageContactSensor1": {
            "aliases": [],
            "label": ["security"],
            "binary_measurement": ["garage_door"],
            "measurement": []
        },
        "motionSensor1": {
            "aliases": [],
            "label": ["security", "energy"],
            "binary_measurement": ["motion"],
            "measurement": []
        },
        "motionSensor2": {
            "aliases": [],
            "label": ["security", "energy"],
            "binary_measurement": ["motion"],
            "measurement": []
        }
    }
}

largeMetadataModelWithoutParentLinks = {
    "floors": {
        "has_parent": None,
        "single": True,
        "floor0": {
            "aliases": ["ground_floor", "groundfloor"],
            "areas": ["area0_0", "area0_1", "area0_2", "area0_3", "area0_4"]
        },
        "floor1": {
            "aliases": ["first_floor", "firstfloor"],
            "areas": ["area1_0", "area1_1", "area1_2", "area1_3", "area1_4"]
        },
        "floor2": {
            "aliases": ["second_floor", "secondfloor"],
            "areas": ["area2_0", "area2_1", "area2_2", "area2_3", "area2_4"]
        },
        "floor3": {
            "aliases": ["third_floor", "thirdfloor"],
            "areas": ["area3_0", "area3_1", "area3_2", "area3_3", "area3_4"]
        },
        "floor4": {
            "aliases": ["fourth_floor", "fourthfloor"],
            "areas": ["area4_0", "area4_1", "area4_2", "area4_3", "area4_4"]
        },
        "floor5": {
            "aliases": ["fifth_floor", "fifthfloor"],
            "areas": ["area5_0", "area5_1", "area5_2", "area5_3", "area5_4"]
        },
        "floor6": {
            "aliases": ["sixth_floor", "sixthfloor"],
            "areas": ["area6_0", "area6_1", "area6_2", "area6_3", "area6_4"]
        },
        "floor7": {
            "aliases": ["seventh_floor", "seventhfloor"],
            "areas": ["area7_0", "area7_1", "area7_2", "area7_3", "area7_4"]
        },
        "floor8": {
            "aliases": ["eighth_floor", "eighthfloor"],
            "areas": ["area8_0", "area8_1", "area8_2", "area8_3", "area8_4"]
        },
        "floor9": {
            "aliases": ["ninth_floor", "ninthfloor"],
            "areas": ["area9_0", "area9_1", "area9_2", "area9_3", "area9_4"]
        },
        "groundFloor": {
            "aliases": ["ground_floor", "groundfloor"],
            "areas": ["livingroom", "kitchen", "hallway", "bathroom1"]
        },
        "firstFloor": {
            "aliases": ["first_floor", "firstfloor"],
            "areas": ["suite", "bedroom2", "bedroom3", "bathroom2"]
        },
        "garden": {
            "aliases": [],
            "areas": ["garage", "sittingArea"]
        }
    },
    "areas": {
        "has_parent": None,  # ["floors"],
        "single": True,
        "area0_0": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},
        "area0_1": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},
        "area0_2": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},
        "area0_3": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},
        "area0_4": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},

        "area1_0": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},
        "area1_1": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},
        "area1_2": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},
        "area1_3": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},
        "area1_4": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},

        "area2_0": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},
        "area2_1": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},
        "area2_2": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},
        "area2_3": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},
        "area2_4": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},

        "area3_0": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},
        "area3_1": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},
        "area3_2": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},
        "area3_3": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},
        "area3_4": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},

        "area4_0": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},
        "area4_1": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},
        "area4_2": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},
        "area4_3": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},
        "area4_4": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},

        "area5_0": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},
        "area5_1": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},
        "area5_2": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},
        "area5_3": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},
        "area5_4": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},

        "area6_0": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},
        "area6_1": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},
        "area6_2": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},
        "area6_3": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},
        "area6_4": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},

        "area7_0": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},
        "area7_1": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},
        "area7_2": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},
        "area7_3": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},
        "area7_4": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},

        "area8_0": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},
        "area8_1": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},
        "area8_2": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},
        "area8_3": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},
        "area8_4": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},

        "area9_0": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},
        "area9_1": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},
        "area9_2": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},
        "area9_3": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},
        "area9_4": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},
        "bathroom": {
            "aliases": [],
        },
        "kitchen": {
            "aliases": [],
            "measurement": [],
            "binary_measurement": ["smoke"],
            "device": ["tempDevice2", "humidityDevice1"]
        },
        "livingroom": {
            "aliases": ["living_room"],
            "measurement": ["light"],
            "binary_measurement": [],
            "device": ["tempDevice1"]
        },
        "hallway": {
            "aliases": [],
            "measurement": [],
            "binary_measurement": [],
            "device": ["lightDevice1"]
        },
        # first floor
        "suite": {
            "aliases": ["bedroom1"],
            "measurement": ["temperature"],
            "binary_measurement": []
        },
        "bedroom2": {
            "aliases": ["bedroom2"],
            "measurement": [],
            "sensor": ["motionSensor1"]
        },
        "bedroom3": {
            "aliases": ["bedroom3"],
            "measurement": [],
            "sensor": ["motionSensor2"]
        },
        "bathroom2": {
            "aliases": []
        },
        # garden
        "garage": {
            "aliases": [],
            "measurement": [],
            "binary_measurement": [],
            "device": ["garageContactDevice"]
        },
        "sittingArea": {
            "aliases": [],
            "measurement": [],
            "binary_measurement": ["motion"]
        }
    },
    "measurement": {
        "has_parent": None,  # ["areas","sensor","device"],
        "single": True,
        "apparent_power": {
            "aliases": []
        },
        "aqi": {
            "aliases": []
        },
        "area": {
            "aliases": []
        },
        "atmospheric_pressure": {
            "aliases": []
        },
        "battery": {
            "aliases": []
        },
        "blood_glucose_concentration": {
            "aliases": []
        },
        "co": {
            "aliases": []
        },
        "co2": {
            "aliases": []
        },
        "conductivity": {
            "aliases": []
        },
        "current": {
            "aliases": []
        },
        "data_rate": {
            "aliases": []
        },
        "data_size": {
            "aliases": []
        },
        "distance": {
            "aliases": []
        },
        "duration": {
            "aliases": []
        },
        "energy": {
            "aliases": []
        },
        "energy_distance": {
            "aliases": []
        },
        "energy_storage": {
            "aliases": []
        },
        "frequency": {
            "aliases": []
        },
        "gas": {
            "aliases": []
        },
        "humidity": {
            "aliases": []
        },
        "illuminance": {
            "aliases": []
        },
        "irradiance": {
            "aliases": []
        },
        "moisture": {
            "aliases": []
        },
        "nitrogen_dioxide": {
            "aliases": []
        },
        "nitrogen_monoxide": {
            "aliases": []
        },
        "nitrous_oxide": {
            "aliases": []
        },
        "ozone": {
            "aliases": []
        },
        "ph": {
            "aliases": []
        },
        "pm1": {
            "aliases": []
        },
        "pm10": {
            "aliases": []
        },
        "pm25": {
            "aliases": []
        },
        "power_factor": {
            "aliases": []
        },
        "power": {
            "aliases": []
        },
        "precipitation": {
            "aliases": []
        },
        "precipitation_intensity": {
            "aliases": []
        },
        "pressure": {
            "aliases": []
        },
        "reactive_power": {
            "aliases": []
        },
        "signal_strength": {
            "aliases": []
        },
        "sound_pressure": {
            "aliases": []
        },
        "speed": {
            "aliases": []
        },
        "sulphur_dioxide": {
            "aliases": []
        },
        "temperature": {
            "aliases": []
        },
        "volatile_organic_compounds": {
            "aliases": []
        },
        "volatile_organic_compounds_parts": {
            "aliases": []
        },
        "voltage": {
            "aliases": []
        },
        "volume": {
            "aliases": []
        },
        "volume_flow_rate": {
            "aliases": []
        },
        "volume_storage": {
            "aliases": []
        },
        "water": {
            "aliases": []
        },
        "weight": {
            "aliases": []
        },
        "wind_direction": {
            "aliases": []
        },
        "wind_speed": {
            "aliases": []
        }
    },
    "binary_measurement": {
        "has_parent": None,  # ["areas","sensor","device"],
        "single": True,
        "battery_charging": {
            "aliases": []
        },
        "cold": {
            "aliases": []
        },
        "connectivity": {
            "aliases": []
        },
        "door": {
            "aliases": []
        },
        "garage_door": {
            "aliases": []
        },
        "heat": {
            "aliases": []
        },
        "light": {
            "aliases": []
        },
        "lock": {
            "aliases": []
        },
        "motion": {
            "aliases": []
        },
        "moving": {
            "aliases": []
        },
        "occupancy": {
            "aliases": []
        },
        "opening": {
            "aliases": []
        },
        "plug": {
            "aliases": []
        },
        "presence": {
            "aliases": []
        },
        "problem": {
            "aliases": []
        },
        "running": {
            "aliases": []
        },
        "safety": {
            "aliases": []
        },
        "smoke": {
            "aliases": []
        },
        "sound": {
            "aliases": []
        },
        "tamper": {
            "aliases": []
        },
        "update": {
            "aliases": []
        },
        "vibration": {
            "aliases": []
        },
        "window": {
            "aliases": []
        }
    },
    "labels": {
        "has_parent": None,  # ["floors","areas","device"],
        "single": False,
        "area1": {
            "aliases": []
        }, "area2": {
            "aliases": []
        }, "security": {
            "aliases": []
        }, "energy": {
            "aliases": ["energy-saving"]
        }, "binary": {
            "aliases": []
        }, "automations": {
            "aliases": []
        }, "health": {
            "aliases": []
        }, "ambience": {
            "aliases": []
        }
    },
    "device": {
        "has_parent": None,  # ["floors","areas"],
        "single": True,
        "tempDevice1": {
            "aliases": [],
            "binary_measurement": [],
            "measurement": ["temperature"]
        },
        "tempDevice2": {
            "aliases": [],
            "binary_measurement": [],
            "measurement": ["temperature"]
        },
        "lightDevice1": {
            "aliases": [],
            "binary_measurement": ["light"],
            "measurement": []
        },
        "humidityDevice1": {
            "aliases": [],
            "binary_measurement": [],
            "measurement": ["humidity"]
        },
        "garageContactDevice1": {
            "aliases": [],
            "sensor": ["garageContactSensor1"],
            "binary_measurement": ["garage_door"],
            "measurement": []
        }
    },
    "sensor": {
        "has_parent": None,  # ["device","areas"],
        "single": True,
        "garageContactSensor1": {
            "aliases": [],
            "label": ["security"],
            "binary_measurement": ["garage_door"],
            "measurement": []
        },
        "motionSensor1": {
            "aliases": [],
            "label": ["security", "energy"],
            "binary_measurement": ["motion"],
            "measurement": []
        },
        "motionSensor2": {
            "aliases": [],
            "label": ["security", "energy"],
            "binary_measurement": ["motion"],
            "measurement": []
        }
    }
}

limitedMetadataModelWithParentLinks = {
    "floors": {
        "has_parent": None,
        "single": True,
        "groundFloor": {
            "aliases": ["ground_floor", "groundfloor"],
            "areas": ["livingroom", "kitchen", "hallway", "bathroom1"]
        },
        "firstFloor": {
            "aliases": ["first_floor", "firstfloor"],
            "areas": ["suite", "bedroom2", "bedroom3", "bathroom2"]
        },
        "garden": {
            "aliases": [],
            "areas": ["garage", "sittingArea"]
        }
    },
    "areas": {
        "has_parent": ["floors"],
        "single": True,
        "bathroom": {
            "aliases": [],
        },
        "kitchen": {
            "aliases": [],
            "measurement": [],
            "binary_measurement": ["smoke"],
            "device": ["tempDevice2", "humidityDevice1"]
        },
        "livingroom": {
            "aliases": ["living_room"],
            "measurement": ["light"],
            "binary_measurement": [],
            "device": ["tempDevice1"]
        },
        "hallway": {
            "aliases": [],
            "measurement": [],
            "binary_measurement": [],
            "device": ["lightDevice1"]
        },
        # first floor
        "suite": {
            "aliases": ["bedroom1"],
            "measurement": ["temperature"],
            "binary_measurement": []
        },
        "bedroom2": {
            "aliases": ["bedroom2"],
            "measurement": [],
            "sensor": ["motionSensor1"]
        },
        "bedroom3": {
            "aliases": ["bedroom3"],
            "measurement": [],
            "sensor": ["motionSensor2"]
        },
        "bathroom2": {
            "aliases": []
        },
        # garden
        "garage": {
            "aliases": [],
            "measurement": [],
            "binary_measurement": [],
            "device": ["garageContactDevice"]
        },
        "sittingArea": {
            "aliases": [],
            "measurement": [],
            "binary_measurement": ["motion"]
        }
    },
    "measurement": {
        "has_parent": ["areas", "sensor", "device"],
        "single": True,
        "energy": {
            "aliases": []
        },
        "humidity": {
            "aliases": []
        },
        "moisture": {
            "aliases": []
        },
        "temperature": {
            "aliases": []
        }
    },
    "binary_measurement": {
        "has_parent": ["areas", "sensor", "device"],
        "single": True,

        "cold": {
            "aliases": []
        },
        "garage_door": {
            "aliases": []
        },
        "heat": {
            "aliases": []
        },
        "light": {
            "aliases": []
        },
        "motion": {
            "aliases": []
        },
        "smoke": {
            "aliases": []
        }
    }
}

limitedMetadataModelWithoutParentLinks = {
    "floors": {
        "has_parent": None,
        "single": True,
        "groundFloor": {
            "aliases": ["ground_floor", "groundfloor"],
            "areas": ["livingroom", "kitchen", "hallway", "bathroom1"]
        },
        "firstFloor": {
            "aliases": ["first_floor", "firstfloor"],
            "areas": ["suite", "bedroom2", "bedroom3", "bathroom2"]
        },
        "garden": {
            "aliases": [],
            "areas": ["garage", "sittingArea"]
        }
    },
    "areas": {
        "has_parent": None,
        "single": True,
        "bathroom": {
            "aliases": [],
        },
        "kitchen": {
            "aliases": [],
            "measurement": [],
            "binary_measurement": ["smoke"],
            "device": ["tempDevice2", "humidityDevice1"]
        },
        "livingroom": {
            "aliases": ["living_room"],
            "measurement": ["light"],
            "binary_measurement": [],
            "device": ["tempDevice1"]
        },
        "hallway": {
            "aliases": [],
            "measurement": [],
            "binary_measurement": [],
            "device": ["lightDevice1"]
        },
        # first floor
        "suite": {
            "aliases": ["bedroom1"],
            "measurement": ["temperature"],
            "binary_measurement": []
        },
        "bedroom2": {
            "aliases": ["bedroom2"],
            "measurement": [],
            "sensor": ["motionSensor1"]
        },
        "bedroom3": {
            "aliases": ["bedroom3"],
            "measurement": [],
            "sensor": ["motionSensor2"]
        },
        "bathroom2": {
            "aliases": []
        },
        # garden
        "garage": {
            "aliases": [],
            "measurement": [],
            "binary_measurement": [],
            "device": ["garageContactDevice"]
        },
        "sittingArea": {
            "aliases": [],
            "measurement": [],
            "binary_measurement": ["motion"]
        }
    },
    "measurement": {
        "has_parent": None,
        "single": True,
        "energy": {
            "aliases": []
        },
        "humidity": {
            "aliases": []
        },
        "moisture": {
            "aliases": []
        },
        "temperature": {
            "aliases": []
        }
    },
    "binary_measurement": {
        "has_parent": None,
        "single": True,

        "cold": {
            "aliases": []
        },
        "garage_door": {
            "aliases": []
        },
        "heat": {
            "aliases": []
        },
        "light": {
            "aliases": []
        },
        "motion": {
            "aliases": []
        },
        "smoke": {
            "aliases": []
        }
    }
}

basicMetadataModelMultiConnections  = {
    "floors": {
        "has_parent": None,
        "single": True,
        "groundFloor": {
            "aliases": ["ground_floor", "groundfloor"],
            "areas": ["livingroom", "kitchen", "hallway", "bathroom1"]
        },
        "firstFloor": {
            "aliases": ["first_floor", "firstfloor"],
            "areas": ["suite", "bedroom2", "bedroom3", "bathroom2"]
        },
        "garden": {
            "aliases": [],
            "areas": ["garage", "sittingArea"]
        }
    },
    "areas": {
        "has_parent": ["floors"],
        "single": True,
        "bathroom": {
            "aliases": [],
        },
        "kitchen": {
            "aliases": [],
            "measurement": [],
            "binary_measurement": ["smoke"],
            "device": ["tempDevice2", "humidityDevice1"]
        },
        "livingroom": {
            "aliases": ["living_room"],
            "measurement": ["light"],
            "binary_measurement": [],
            "device": ["tempDevice1"]
        },
        "hallway": {
            "aliases": [],
            "measurement": [],
            "binary_measurement": [],
            "device": ["lightDevice1"]
        },
        # first floor
        "suite": {
            "aliases": ["bedroom1"],
            "measurement": ["temperature"],
            "binary_measurement": []
        },
        "bedroom2": {
            "aliases": ["bedroom2"],
            "measurement": [],
            "sensor": ["motionSensor1"]
        },
        "bedroom3": {
            "aliases": ["bedroom3"],
            "measurement": [],
            "sensor": ["motionSensor2"]
        },
        "bathroom2": {
            "aliases": []
        },
        # garden
        "garage": {
            "aliases": [],
            "measurement": [],
            "binary_measurement": [],
            "device": ["garageContactDevice"]
        },
        "sittingArea": {
            "aliases": [],
            "measurement": [],
            "binary_measurement": ["motion"]
        }
    },
    "measurement": {
        "has_parent": ["areas", "sensor", "device"],
        "single": True,
        "apparent_power": {
            "aliases": []
        },
        "aqi": {
            "aliases": []
        },
        "area": {
            "aliases": []
        },
        "atmospheric_pressure": {
            "aliases": []
        },
        "battery": {
            "aliases": []
        },
        "blood_glucose_concentration": {
            "aliases": []
        },
        "co": {
            "aliases": []
        },
        "co2": {
            "aliases": []
        },
        "conductivity": {
            "aliases": []
        },
        "current": {
            "aliases": []
        },
        "data_rate": {
            "aliases": []
        },
        "data_size": {
            "aliases": []
        },
        "distance": {
            "aliases": []
        },
        "duration": {
            "aliases": []
        },
        "energy": {
            "aliases": []
        },
        "energy_distance": {
            "aliases": []
        },
        "energy_storage": {
            "aliases": []
        },
        "frequency": {
            "aliases": []
        },
        "gas": {
            "aliases": []
        },
        "humidity": {
            "aliases": []
        },
        "illuminance": {
            "aliases": []
        },
        "irradiance": {
            "aliases": []
        },
        "moisture": {
            "aliases": []
        },
        "nitrogen_dioxide": {
            "aliases": []
        },
        "nitrogen_monoxide": {
            "aliases": []
        },
        "nitrous_oxide": {
            "aliases": []
        },
        "ozone": {
            "aliases": []
        },
        "ph": {
            "aliases": []
        },
        "pm1": {
            "aliases": []
        },
        "pm10": {
            "aliases": []
        },
        "pm25": {
            "aliases": []
        },
        "power_factor": {
            "aliases": []
        },
        "power": {
            "aliases": []
        },
        "precipitation": {
            "aliases": []
        },
        "precipitation_intensity": {
            "aliases": []
        },
        "pressure": {
            "aliases": []
        },
        "reactive_power": {
            "aliases": []
        },
        "signal_strength": {
            "aliases": []
        },
        "sound_pressure": {
            "aliases": []
        },
        "speed": {
            "aliases": []
        },
        "sulphur_dioxide": {
            "aliases": []
        },
        "temperature": {
            "aliases": []
        },
        "volatile_organic_compounds": {
            "aliases": []
        },
        "volatile_organic_compounds_parts": {
            "aliases": []
        },
        "voltage": {
            "aliases": []
        },
        "volume": {
            "aliases": []
        },
        "volume_flow_rate": {
            "aliases": []
        },
        "volume_storage": {
            "aliases": []
        },
        "water": {
            "aliases": []
        },
        "weight": {
            "aliases": []
        },
        "wind_direction": {
            "aliases": []
        },
        "wind_speed": {
            "aliases": []
        }
    },
    "binary_measurement": {
        "has_parent": ["areas", "sensor", "device"],
        "single": True,
        "battery_charging": {
            "aliases": []
        },
        "cold": {
            "aliases": []
        },
        "connectivity": {
            "aliases": []
        },
        "door": {
            "aliases": []
        },
        "garage_door": {
            "aliases": []
        },
        "heat": {
            "aliases": []
        },
        "light": {
            "aliases": []
        },
        "lock": {
            "aliases": []
        },
        "motion": {
            "aliases": []
        },
        "moving": {
            "aliases": []
        },
        "occupancy": {
            "aliases": []
        },
        "opening": {
            "aliases": []
        },
        "plug": {
            "aliases": []
        },
        "presence": {
            "aliases": []
        },
        "problem": {
            "aliases": []
        },
        "running": {
            "aliases": []
        },
        "safety": {
            "aliases": []
        },
        "smoke": {
            "aliases": []
        },
        "sound": {
            "aliases": []
        },
        "tamper": {
            "aliases": []
        },
        "update": {
            "aliases": []
        },
        "vibration": {
            "aliases": []
        },
        "window": {
            "aliases": []
        }
    }
}


metadataModelExtendedInstances = {
    "floors": {
        "has_parent": None,
        "single": True,
        "floor0": {
            "aliases": ["ground_floor", "groundfloor"],
            "areas": ["area0_0", "area0_1", "area0_2", "area0_3", "area0_4"]
        },
        "floor1": {
            "aliases": ["first_floor", "firstfloor"],
            "areas": ["area1_0", "area1_1", "area1_2", "area1_3", "area1_4"]
        },
        "floor2": {
            "aliases": ["second_floor", "secondfloor"],
            "areas": ["area2_0", "area2_1", "area2_2", "area2_3", "area2_4"]
        },
        "floor3": {
            "aliases": ["third_floor", "thirdfloor"],
            "areas": ["area3_0", "area3_1", "area3_2", "area3_3", "area3_4"]
        },
        "floor4": {
            "aliases": ["fourth_floor", "fourthfloor"],
            "areas": ["area4_0", "area4_1", "area4_2", "area4_3", "area4_4"]
        },
        "floor5": {
            "aliases": ["fifth_floor", "fifthfloor"],
            "areas": ["area5_0", "area5_1", "area5_2", "area5_3", "area5_4"]
        },
        "floor6": {
            "aliases": ["sixth_floor", "sixthfloor"],
            "areas": ["area6_0", "area6_1", "area6_2", "area6_3", "area6_4"]
        },
        "floor7": {
            "aliases": ["seventh_floor", "seventhfloor"],
            "areas": ["area7_0", "area7_1", "area7_2", "area7_3", "area7_4"]
        },
        "floor8": {
            "aliases": ["eighth_floor", "eighthfloor"],
            "areas": ["area8_0", "area8_1", "area8_2", "area8_3", "area8_4"]
        },
        "floor9": {
            "aliases": ["ninth_floor", "ninthfloor"],
            "areas": ["area9_0", "area9_1", "area9_2", "area9_3", "area9_4"]
        },
        "groundFloor": {
            "aliases": ["ground_floor", "groundfloor"],
            "areas": ["livingroom", "kitchen", "hallway", "bathroom1"]
        },
        "firstFloor": {
            "aliases": ["first_floor", "firstfloor"],
            "areas": ["suite", "bedroom2", "bedroom3", "bathroom2"]
        },
        "garden": {
            "aliases": [],
            "areas": ["garage", "sittingArea"]
        }
    },
    "areas": {
        "has_parent": None,  # ["floors"],
        "single": True,
        "area0_0": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},
        "area0_1": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},
        "area0_2": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},
        "area0_3": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},
        "area0_4": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},

        "area1_0": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},
        "area1_1": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},
        "area1_2": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},
        "area1_3": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},
        "area1_4": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},

        "area2_0": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},
        "area2_1": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},
        "area2_2": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},
        "area2_3": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},
        "area2_4": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},

        "area3_0": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},
        "area3_1": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},
        "area3_2": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},
        "area3_3": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},
        "area3_4": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},

        "area4_0": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},
        "area4_1": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},
        "area4_2": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},
        "area4_3": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},
        "area4_4": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},

        "area5_0": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},
        "area5_1": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},
        "area5_2": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},
        "area5_3": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},
        "area5_4": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},

        "area6_0": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},
        "area6_1": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},
        "area6_2": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},
        "area6_3": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},
        "area6_4": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},

        "area7_0": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},
        "area7_1": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},
        "area7_2": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},
        "area7_3": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},
        "area7_4": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},

        "area8_0": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},
        "area8_1": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},
        "area8_2": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},
        "area8_3": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},
        "area8_4": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},

        "area9_0": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},
        "area9_1": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},
        "area9_2": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},
        "area9_3": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},
        "area9_4": {"aliases": [], "measurement": [], "binary_measurement": [], "device": [], "sensor": []},
        "bathroom": {
            "aliases": [],
        },
        "kitchen": {
            "aliases": [],
            "measurement": [],
            "binary_measurement": ["smoke"],
            "device": ["tempDevice2", "humidityDevice1"]
        },
        "livingroom": {
            "aliases": ["living_room"],
            "measurement": ["light"],
            "binary_measurement": [],
            "device": ["tempDevice1"]
        },
        "hallway": {
            "aliases": [],
            "measurement": [],
            "binary_measurement": [],
            "device": ["lightDevice1"]
        },
        # first floor
        "suite": {
            "aliases": ["bedroom1"],
            "measurement": ["temperature"],
            "binary_measurement": []
        },
        "bedroom2": {
            "aliases": ["bedroom2"],
            "measurement": [],
            "sensor": ["motionSensor1"]
        },
        "bedroom3": {
            "aliases": ["bedroom3"],
            "measurement": [],
            "sensor": ["motionSensor2"]
        },
        "bathroom2": {
            "aliases": []
        },
        # garden
        "garage": {
            "aliases": [],
            "measurement": [],
            "binary_measurement": [],
            "device": ["garageContactDevice"]
        },
        "sittingArea": {
            "aliases": [],
            "measurement": [],
            "binary_measurement": ["motion"]
        }
    },
    "measurement": {
        "has_parent": None,  # ["areas","sensor","device"],
        "single": True,
        "apparent_power": {
            "aliases": []
        },
        "aqi": {
            "aliases": []
        },
        "area": {
            "aliases": []
        },
        "atmospheric_pressure": {
            "aliases": []
        },
        "battery": {
            "aliases": []
        },
        "blood_glucose_concentration": {
            "aliases": []
        },
        "co": {
            "aliases": []
        },
        "co2": {
            "aliases": []
        },
        "conductivity": {
            "aliases": []
        },
        "current": {
            "aliases": []
        },
        "data_rate": {
            "aliases": []
        },
        "data_size": {
            "aliases": []
        },
        "distance": {
            "aliases": []
        },
        "duration": {
            "aliases": []
        },
        "energy": {
            "aliases": []
        },
        "energy_distance": {
            "aliases": []
        },
        "energy_storage": {
            "aliases": []
        },
        "frequency": {
            "aliases": []
        },
        "gas": {
            "aliases": []
        },
        "humidity": {
            "aliases": []
        },
        "illuminance": {
            "aliases": []
        },
        "irradiance": {
            "aliases": []
        },
        "moisture": {
            "aliases": []
        },
        "nitrogen_dioxide": {
            "aliases": []
        },
        "nitrogen_monoxide": {
            "aliases": []
        },
        "nitrous_oxide": {
            "aliases": []
        },
        "ozone": {
            "aliases": []
        },
        "ph": {
            "aliases": []
        },
        "pm1": {
            "aliases": []
        },
        "pm10": {
            "aliases": []
        },
        "pm25": {
            "aliases": []
        },
        "power_factor": {
            "aliases": []
        },
        "power": {
            "aliases": []
        },
        "precipitation": {
            "aliases": []
        },
        "precipitation_intensity": {
            "aliases": []
        },
        "pressure": {
            "aliases": []
        },
        "reactive_power": {
            "aliases": []
        },
        "signal_strength": {
            "aliases": []
        },
        "sound_pressure": {
            "aliases": []
        },
        "speed": {
            "aliases": []
        },
        "sulphur_dioxide": {
            "aliases": []
        },
        "temperature": {
            "aliases": []
        },
        "volatile_organic_compounds": {
            "aliases": []
        },
        "volatile_organic_compounds_parts": {
            "aliases": []
        },
        "voltage": {
            "aliases": []
        },
        "volume": {
            "aliases": []
        },
        "volume_flow_rate": {
            "aliases": []
        },
        "volume_storage": {
            "aliases": []
        },
        "water": {
            "aliases": []
        },
        "weight": {
            "aliases": []
        },
        "wind_direction": {
            "aliases": []
        },
        "wind_speed": {
            "aliases": []
        }
    },
    "binary_measurement": {
        "has_parent": None,  # ["areas","sensor","device"],
        "single": True,
        "battery_charging": {
            "aliases": []
        },
        "cold": {
            "aliases": []
        },
        "connectivity": {
            "aliases": []
        },
        "door": {
            "aliases": []
        },
        "garage_door": {
            "aliases": []
        },
        "heat": {
            "aliases": []
        },
        "light": {
            "aliases": []
        },
        "lock": {
            "aliases": []
        },
        "motion": {
            "aliases": []
        },
        "moving": {
            "aliases": []
        },
        "occupancy": {
            "aliases": []
        },
        "opening": {
            "aliases": []
        },
        "plug": {
            "aliases": []
        },
        "presence": {
            "aliases": []
        },
        "problem": {
            "aliases": []
        },
        "running": {
            "aliases": []
        },
        "safety": {
            "aliases": []
        },
        "smoke": {
            "aliases": []
        },
        "sound": {
            "aliases": []
        },
        "tamper": {
            "aliases": []
        },
        "update": {
            "aliases": []
        },
        "vibration": {
            "aliases": []
        },
        "window": {
            "aliases": []
        }
    },
    "labels": {
        "has_parent": ["floors", "areas", "device"],
        "single": False,
        "area1": {
            "aliases": []
        }, "area2": {
            "aliases": []
        }, "security": {
            "aliases": []
        }, "energy": {
            "aliases": ["energy-saving"]
        }, "binary": {
            "aliases": []
        }, "automations": {
            "aliases": []
        }, "health": {
            "aliases": []
        }, "ambience": {
            "aliases": []
        }
    },
    "device": {
        "has_parent": ["floors", "areas"],
        "single": True,
        "tempDevice1": {
            "aliases": [],
            "binary_measurement": [],
            "measurement": ["temperature"]
        },
        "tempDevice2": {
            "aliases": [],
            "binary_measurement": [],
            "measurement": ["temperature"]
        },
        "lightDevice1": {
            "aliases": [],
            "binary_measurement": ["light"],
            "measurement": []
        },
        "humidityDevice1": {
            "aliases": [],
            "binary_measurement": [],
            "measurement": ["humidity"]
        },
        "garageContactDevice1": {
            "aliases": [],
            "sensor": ["garageContactSensor1"],
            "binary_measurement": ["garage_door"],
            "measurement": []
        }
    },
    "sensor": {
        "has_parent": ["device", "areas"],
        "single": True,
        "garageContactSensor1": {
            "aliases": [],
            "label": ["security"],
            "binary_measurement": ["garage_door"],
            "measurement": []
        },
        "motionSensor1": {
            "aliases": [],
            "label": ["security", "energy"],
            "binary_measurement": ["motion"],
            "measurement": []
        },
        "motionSensor2": {
            "aliases": [],
            "label": ["security", "energy"],
            "binary_measurement": ["motion"],
            "measurement": []
        }
    }
}
# Predefined Message Structure:
binary_yes = ("false")
binary_no = ("true")
temperature_raw = ("27")
temperature_json = ("{\"value\":\"27\",\"unit\":\"C\"}")
temperature_json_extended = "{\"value\":\"27\",\"unit\":\"C\",\"measurement\":\"temperature\"}"
humidity_raw = ("10%")
humidity_json = ("{\"value\":\"10\",\"unit\":\"%\"}")
humidity_json_extended = ("{\"value\":\"10\",\"unit\":\"%\",\"measurement\":\"humidity\"}")
