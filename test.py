from opentrons import protocol_api

# metadata
metadata = {
    'protocolName': 'test',
    'author': 'Name <email@address.com>',
    'description': 'Test',
    'apiLevel': '2.6'
}

# protocol run function. the part after the colon lets your editor know
# where to look for autocomplete suggestions
def run(protocol: protocol_api.ProtocolContext):

    # labware
    tubes1 = protocol.load_labware('opentrons_96_aluminumblock_generic_pcr_strip_200ul', '1')
    plate = protocol.load_labware('opentrons_96_aluminumblock_generic_pcr_strip_200ul', '2')
    tiprack = protocol.load_labware('opentrons_96_tiprack_20ul', '3')

    # pipettes
    pipette = protocol.load_instrument(
         'p20_single_gen2', 'right', tip_racks=[tiprack])

    locations = ['A3','C3','E3','G3']
    pipette.flow_rate.aspirate = 5
    pipette.well_bottom_clearance.aspirate = 1
    # commands
    # process first tube rack
    for i in range(4):
        pipette.pick_up_tip()
        pipette.aspirate(15, plate.wells()[i+4].bottom())
        pipette.dispense(15, tubes1[locations[i]].bottom())
        pipette.drop_tip()
