
from dataclasses import dataclass

@dataclass
class Deliverable:
    clean: float
    ai0: float
    ai_T: float
    cf: float

def net_basis(F:float, cf:float, dirty0:float, ai_T:float) -> float:
    return F*cf + ai_T - dirty0


