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

    # labware
    tubes1 = protocol.load_labware('opentrons_24_aluminumblock_nest_1.5ml_snapcap', '1')
    tubes2 = protocol.load_labware('opentrons_24_aluminumblock_nest_1.5ml_snapcap', '2')
    plate = protocol.load_labware('opentrons_96_aluminumblock_generic_pcr_strip_200ul', '3')
    tiprack = protocol.load_labware('opentrons_96_tiprack_20ul', '5')

    # pipettes
    pipette = protocol.load_instrument(
         'p20_single_gen2', 'right', tip_racks=[tiprack])

    # commands
    # process first tube rack
    for i in range(24):
        pipette.pick_up_tip()
        pipette.aspirate(20, tubes1.wells()[i].bottom())
        pipette.dispense(20, plate.wells()[i].bottom())
        pipette.aspirate(20, tubes1.wells()[i].bottom())
        pipette.dispense(20, plate.wells()[i].bottom())
        pipette.drop_tip()

    # process second tube rack
    for i in range(24):
        pipette.pick_up_tip()
        pipette.aspirate(20, tubes2.wells()[i].bottom())
        pipette.dispense(20, plate.wells()[i+24].bottom())
        pipette.aspirate(20, tubes2.wells()[i].bottom())
        pipette.dispense(20, plate.wells()[i+24].bottom())
        pipette.drop_tip()
