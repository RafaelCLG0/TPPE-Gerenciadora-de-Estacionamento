from src.models.converter_tempo import ConverterTempo

def test_converter_tempo():
    ct = ConverterTempo()
    assert ct.converter(10, 11) == 60
    assert ct.converter(9, 12) == 180
