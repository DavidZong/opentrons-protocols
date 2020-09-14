from opentrons import protocol_api

# metadata
metadata = {
    'protocolName': 'My Protocol',
    'author': 'Name <email@address.com>',
    'description': 'Simple protocol to get started using OT2',
    'apiLevel': '2.2'
}

# protocol run function. the part after the colon lets your editor know
# where to look for autocomplete suggestions
def run(protocol: protocol_api.ProtocolContext):

    # labware
    tubes = protocol.load_labware('opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap', '1')
    tiprack = protocol.load_labware('opentrons_96_tiprack_1000ul', '2')

    # pipettes
    left_pipette = protocol.load_instrument(
         'p1000_single_gen2', 'left', tip_racks=[tiprack])

    # commands
    left_pipette.pick_up_tip()
    left_pipette.aspirate(200, tubes['A1'].bottom())
    left_pipette.dispense(200, tubes['B2'].bottom())
    left_pipette.drop_tip()
