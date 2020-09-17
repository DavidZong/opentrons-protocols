from opentrons import protocol_api

# metadata
metadata = {
    'protocolName': 'tube2plate',
    'author': 'Name <email@address.com>',
    'description': 'Transfers up to 48 samples from tubes to a plate',
    'apiLevel': '2.6'
}

# protocol run function. the part after the colon lets your editor know
# where to look for autocomplete suggestions
def run(protocol: protocol_api.ProtocolContext):

    numtubes = 24 # leave at 24 until last round
    round = 1 # increase to access further wells


    adjustment = round * 24
    # labware
    tubes = protocol.load_labware('opentrons_96_aluminumblock_generic_pcr_strip_200ul', '1')
    plate = protocol.load_labware('opentrons_96_aluminumblock_generic_pcr_strip_200ul', '2')
    tiprack = protocol.load_labware('opentrons_96_tiprack_20ul', '3')

    # pipettes
    pipette = protocol.load_instrument(
         'p20_single_gen2', 'right', tip_racks=[tiprack])

     locations = ['A1','C1','E1','G1',
                'A3','C3','E3','G3',
                'A5','C5','E5','G5',
                'A7','C7','E7','G7',
                'A9','C9','E9','G9',
                'A11','C11','E11','G11'
    ]
    pipette.flow_rate.aspirate = 3
    pipette.well_bottom_clearance.aspirate = 1.5
    # commands
    # process first tube rack
    for i in range(numtubes):
        pipette.pick_up_tip()
        pipette.aspirate(20, tubes1[locations[i]])
        pipette.dispense(20, plate.wells()[i+adjustment].bottom())
        pipette.touch_tip(v_offset=-5)
        pipette.aspirate(10, tubes1[locations[i]])
        pipette.dispense(10, plate.wells()[i+adjustment].bottom())
        pipette.touch_tip(v_offset=-5)
        pipette.drop_tip()
