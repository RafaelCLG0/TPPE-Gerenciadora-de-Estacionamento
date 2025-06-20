from src.models.turnos import Turnos

def test_verificar_noturno():
    turnos = Turnos()
    assert turnos.verificar_noturno(22, 2) is True
    assert turnos.verificar_noturno(8, 18) is False
