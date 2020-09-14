from opentrons import protocol_api
# metadata
metadata = {
    'protocolName': 'MagAttract PowerMicrobiome',
    'author': 'David Zong <davidzong1@gmail.com>',
    'description': 'Executes the Qiagen MagAttract Powermicrobiome kit using OT2',
    'apiLevel': '2.2'
}

def run(protocol_context):

    # define labware
    mag_deck = protocol_context.load_module('magdeck', '1')
    mag_plate = mag_deck.load_labware(
        'usascientific_96_wellplate_2.4ml_deep', 'mag_plate')
    output_plate = protocol_context.load_labware(
        'biorad_96_wellplate_200ul_pcr', '2', 'output plate')
    input_plate = protocol_context.load_labware(
        'usascientific_96_wellplate_2.4ml_deep', '3', 'input_plate')
    reagent_res = protocol_context.load_labware(
        'usascientific_12_reservoir_22ml', '4', 'reagent reservoir')
    wash_buffer_res = protocol_context.load_labware(
        'agilent_1_reservoir_290ml', '5', 'wash reservoir')
    liquid_waste = protocol_context.load_labware(
        'agilent_1_reservoir_290ml', '11', 'waste reservoir')

    slots = ['6', '8', '9', '10']
    tipracks = [
        protocol_context.load_labware('opentrons_96_tiprack_1000ul', slot, 'p1000 tiprack')
        for slot in slots]

    # load pipettes
    left_pipette = protocol_context.load_instrument(
         'p300_single', 'left', tipracks)

    # Disengage MagDeck
    mag_deck.disengage()
