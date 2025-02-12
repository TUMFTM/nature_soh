import enum


class VehicleConfig(enum.Enum):
    """
    Holds the parameter values for the examined vehicles
    """


    tesla_dict = {"min_cell_volt": 3.2, # V
               "max_cell_volt": 3.6,    # V
               "nom_cell_cap": 161,     # Ah
               "n_s": 106,              # serially connected cells
               "n_p": 1,                # parallel connected cells
               "max_pack_volt": 390,    # V, from data
               "min_pack_volt": 340,    # V, from data
               "nom_pack_cap": 161      # Ah
               }

    vw_dict = { "min_cell_volt": 2.8,   # V
                "max_cell_volt": 4.2,   # V
                "nom_cell_cap": 78,     # Ah
                "n_s": 108,             # serially connected cells
                "n_p": 2,               # parallel connected cells
                "max_pack_volt" : 450,  # V, from data
                "min_pack_volt" : 360,  # V, from data
                "nom_pack_cap" : 2*78   # Ah
                }

    cupra_dict = vw_dict