from opentrons import protocol_api

# metadata
metadata = {
    'protocolName': 'tube2plate',
    'author': 'David Zong <davidzong1@gmail.com>',
    'description': 'Transfers up to 24 samples from tubes to a plate while keeping samples at 4C',
    'apiLevel': '2.6'
}

# protocol run function. the part after the colon lets your editor know
# where to look for autocomplete suggestions
def run(protocol: protocol_api.ProtocolContext):
# ---------------------edit things here as needed-----------------------

    numtubes = 24 # leave at 24 until last round
    round = 3 # increase to access further wells (starts at 0)

# ----------------------------------------------------------------------

    adjustment = round * 24

    # temperature modules
    module1 = protocol.load_module('Temperature Module', '1')
    module1.set_temperature(4)
    module2 = protocol.load_module('Temperature Module', '4')
    module2.set_temperature(4)
    # labware
    tubes1 = module1.load_labware('opentrons_24_aluminumblock_generic_2ml_screwcap')
    plate = module2.load_labware('opentrons_96_aluminumblock_generic_pcr_strip_200ul')
    tiprack = protocol.load_labware('opentrons_96_tiprack_20ul', '2')

    # pipettes
    pipette = protocol.load_instrument('p20_single_gen2', 'right', tip_racks=[tiprack])
    pipette.flow_rate.aspirate = 3
    pipette.well_bottom_clearance.aspirate = 1.5

    # commands
    # process first tube rack
    for i in range(numtubes):
        pipette.pick_up_tip()
        pipette.aspirate(20, tubes1.wells()[i])
        pipette.dispense(20, plate.wells()[i+adjustment].bottom())
        # pipette.touch_tip(v_offset=-5)
        pipette.aspirate(10, tubes1.wells()[i])
        pipette.dispense(10, plate.wells()[i+adjustment].bottom())
        # pipette.touch_tip(v_offset=-5)
        pipette.drop_tip()
